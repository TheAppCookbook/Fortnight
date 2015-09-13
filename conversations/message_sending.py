# -*- coding: utf-8 -*-

from commons import twilio_sender
from commons import twilio_client

import twilio.twiml


def send_received_message(sender_phone):
    message = (
        "🛂 Your messages will be delivered to your "
        "Pen Pal in two weeks' time."
    )
    
    twilio_client.messages.create(
        to=sender_phone,
        from_=twilio_sender,
        body=message
    )

def send_message(message, recipient_phone):
    twilio_client.messages.create(
        to=recipient_phone,
        from_=twilio_sender,
        body=message
    )
