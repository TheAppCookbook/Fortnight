from commons import twilio_sender
from commons import twilio_client


def send_join_message(recipient_phone, has_palship):
    message = u"🛂 Greetings! Welcome to Fortnight! \n\n"
    if has_palship:
        message += (
            u"You've been paired with a Pen Pal! "
            u"Any message you send will be delivered "
            u"in two weeks' time."
        )
    else:
        message += (
            u"It doesn't look like anyone who's "
            u"available is speaking your language. "
            u"To add more languages, text 'add 🇲🇽', "
            u"or any other flag emoji."
        )

    twilio_client.messages.create(
        to=recipient_phone,
        from_=twilio_sender,
        body=message
    )

def send_pal_message(recipient_phone):
    message = (
        u"🛂 Fortnight has found you a Pen Pal! \n\n"
        u"Any message you send will be delivered "
        u"in two weeks' time."
    )
    
    twilio_client.messages.create(
        to=recipient_phone,
        from_=twilio_sender,
        body=message
    )