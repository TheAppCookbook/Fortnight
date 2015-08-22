# -*- coding: utf-8 -*-

from commons import twilio_sender
from commons import twilio_client


def message(recipient_phone):
    message = (
        "🛂 Your message will be delivered to your "
        "Pen Pal in two weeks' time."
    )
    
    twilio_client.messages.create(
        to=recipient_phone,
        from_=twilio_sender,
        body=message
    )
