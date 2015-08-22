from commons import twilio_client

from routes.route import Route

from models.user import User
from models.user import Palship
from models.message import Message

from conversations import message_sending
from conversations import language_management

from parse_rest.core import ResourceRequestBadRequest


class MMS(Route):
    methods = ['POST']

    def POST(self, request):
        body = request.values.get('Body')
        if not body:
            body = request.get_json()['Body']
    
        phone = request.values.get('From')
        if not phone:
            phone = request.get_json()['From']
    
        credentials = User.credentials(phone)
        
        try:
            sender = User.login(*credentials)
        except (ResourceRequestBadRequest, KeyError):
            return ('', 401)
        
        # Languages
        if body.startswith('add'):
            return self._add_language(sender, body, request)
        elif body.startswith('remove'):
            return self._remove_language(sender, body, request)
        
        # Pen Pals
        elif body.startswith('report'):
            return self._report_pen_pal(sender, body, request)
        elif body.startswith('swap'):
            return self._swap_pen_pal(sender, body, request)
        
        # Messages
        else:
            return self._queue_message(sender, body, request)    
        
    # Languages
    def _add_language(self, sender, body, request):
        languages = User.languages(body) + sender.languages
        sender.languages = languages
        
        sender.save()
        return language_management.message(sender.phone, languages)
        
    def _remove_language(self, sender, body, request):
        languages = User.languages(body)
        languages = [lang for lang in sender.languages if lang not in languages]
        
        
        sender.languages = languages
        sender.save()
        return language_management.message(sender.phone, languages)
        
    # Pen Pals
    def _report_pen_pal(self, sender, body, request):
        pass
        
    def _swap_pen_pal(self, sender, body, request):
        pass
        
    # Messages
    def _queue_message(self, sender, body, request):
        # Find any existing messages and merge...
        messages = Message.Query.filter(sender=sender)
        if messages:
            message = messages[0]
        
            message.body += '\n--\n' + body
            message.save()
            
            return message_sending.message()
    
        # Otherwise, add a new
        palships = Palship.Query.filter(lhs=sender)
        if palships:
            recipient = palships[0].rhs
        else:
            palships = Palship.Query.filter(rhs=sender)
            if not palships:
                return None
            recipient = palships[0].lhs

        message = Message(
            body=body,
            sender=sender,
            recipient=recipient
        )
        
        message.save()
        return message_sending.message()
