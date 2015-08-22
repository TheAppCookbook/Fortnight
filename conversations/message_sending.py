# -*- coding: utf-8 -*-

from commons import twilio_sender
from commons import twilio_client

import twilio.twiml


def message():
    message = (
        "🛂 Your messages will be delivered to your "
        "Pen Pal in two weeks' time."
    )
    
    resp = twilio.twiml.Response()
    resp.message(message)
    
    return str(resp)

def send_message(message, recipient_phone):
    twilio_client.messages.create(
        to=recipient_phone,
        from_=twilio_sender,
        body=message
    )
