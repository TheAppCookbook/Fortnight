from commons import twilio_client
from commons import parse_client

from routes.route import Route

from models.user import User
from models.user import Palship

from conversations import user_creation

import flask
import json
import uuid
import random

from parse_rest.core import ResourceRequestBadRequest


class Index(Route):
    methods = ['GET', 'PUT']

    def GET(self, request):
        return flask.render_template('index.html')
    
    def PUT(self, request):
        refresh = '<meta http-equiv="refresh" content="0; url=/">'
    
        raw_phone = request.values.get('phone_number')
        if not raw_phone:
            raw_phone = request.get_json()['phone_number']
        
        phone = User.valid_number(raw_phone)
        if not phone:
            return ('', 400)
            
        languages = [request.values.get('base_language')]
        if not languages:
            languages = [request.get_json()['base_language']]
        
        pals = list(User.Query.filter(languages__all=languages, pal=None, phone__ne=phone))
        pal = random.choice(pals) if pals else None
        
        credentials = User.credentials(phone)        
        try:
            user = User.signup(
                credentials[0],
                credentials[1],
                phone=phone,
                languages=languages,
                palship=None
            )
            
            palship = None
            if pal:
                palship = Palship(
                    lhs=user,
                    rhs=pal
                )
                
                palship.save()
                
            # Send Message
            user_creation.send_join_message(phone, palship != None)
            if palship:
                user_creation.send_pal_message(pal.phone)
            
        except ResourceRequestBadRequest as err_obj:
            err_str = err_obj.args[0].decode('utf-8')
            err = json.loads(err_str)
            
            if err['code'] == 202:
                return refresh
            raise err_obj
        
        return refresh
