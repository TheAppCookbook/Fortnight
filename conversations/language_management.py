# -*- coding: utf-8 -*-

from commons import twilio_sender
from commons import twilio_client

import twilio.twiml


def message(recipient_phone, languages):
    message = "🛂 Ok. Fortnight now knows you speak these languages: "
    message += ','.join(languages)
        
    resp = twilio.twiml.Response()
    resp.message(message)
    
    return str(resp)
