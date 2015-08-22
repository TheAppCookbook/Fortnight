# -*- coding: utf-8 -*-

import twilio.twiml


def message():
    message = (
        "🛂 Your messages will be delivered to your "
        "Pen Pal in two weeks' time."
    )
    
    resp = twilio.twiml.Response()
    resp.message(message)
    
    return str(resp)
