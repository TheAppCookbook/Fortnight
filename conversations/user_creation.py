# -*- coding: utf-8 -*-

from commons import twilio_sender
from commons import twilio_client


def send_join_message(recipient_phone, has_palship):
    message = "🛂 Greetings! Welcome to Fortnight! \n\n"
    if has_palship:
        message += (
            "You've been paired with a Pen Pal! "
            "Any message you send will be delivered "
            "in two weeks' time."
        )
    else:
        message += (
            "It doesn't look like anyone who's "
            "available is speaking your language. "
            "To add more languages, text 'add 🇧🇹', "
            "or any other flag emoji."
        )

    twilio_client.messages.create(
        to=recipient_phone,
        from_=twilio_sender,
        body=message
    )

def send_pal_message(recipient_phone):
    message = (
        "🛂 Fortnight has found you a Pen Pal! \n\n"
        "Any message you send will be delivered "
        "in two weeks' time."
    )
    
    twilio_client.messages.create(
        to=recipient_phone,
        from_=twilio_sender,
        body=message
    )