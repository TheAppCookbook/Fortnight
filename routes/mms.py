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
            
        print("received message %s" % body)
    
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
        language_management.send_message(sender.phone, languages)
        return ""
        
    def _remove_language(self, sender, body, request):
        languages = User.languages(body)
        languages = [lang for lang in sender.languages if lang not in languages]
        
        
        sender.languages = languages
        sender.save()
        
        language_management.send_message(sender.phone, languages)
        return ""
        
    # Pen Pals
    def _report_pen_pal(self, sender, body, request):
        pass
        
    def _swap_pen_pal(self, sender, body, request):
        pass
        
    # Messages
    def _queue_message(self, sender, body, request):
        # Find any existing messages and merge...
        messages = list(Message.Query.filter(sender=sender.objectId))
        if messages:
            message = messages[0]
        
            message.body += '\n--\n' + body
            message.save()
            
            message_sending.send_received_message(sender.phone)
            return ""
    
        # Otherwise, add a new
        palships = list(Palship.Query.filter(lhs=sender.objectId))
        if palships:
            recipient = User.Query.get(objectId=palships[0].rhs)
        else:
            palships = list(Palship.Query.filter(rhs=sender))
            if not palships:
                return None
            recipient = User.Query.get(objectId=palships[0].lhs)

        message = Message(
            body=body,
            sender=sender.objectId,
            recipient=recipient.objectId
        )
        
        message.save()
        message_sending.send_received_message(sender.phone)
        return ""
