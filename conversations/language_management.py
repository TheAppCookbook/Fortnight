# -*- coding: utf-8 -*-

import twilio.twiml


language_map = {
    # English
    "🇻🇮": "🇺🇸", "🇮🇪": "🇺🇸", "🇦🇺": "🇺🇸", "🇻🇬": "🇺🇸",
    "🇨🇦": "🇺🇸", "🇰🇾": "🇺🇸", "🇫🇯": "🇺🇸", "🇳🇿": "🇺🇸",
    "🇬🇧": "🇺🇸",
    
    # Spanish
    "🇦🇷": "🇪🇸", "🇨🇱": "🇪🇸", "🇨🇴": "🇪🇸", "🇨🇷": "🇪🇸",
    "🇩🇴": "🇪🇸", "🇸🇻": "🇪🇸", "🇲🇽": "🇪🇸", "🇳🇮": "🇪🇸",
    "🇵🇦": "🇪🇸", "🇵🇾": "🇪🇸", "🇵🇪": "🇪🇸", "🇻🇪": "🇪🇸",
    
    # French
    "🇬🇵": "🇫🇷", "🇭🇹": "🇫🇷", "🇲🇶": "🇫🇷", "🇷🇪": "🇫🇷",

    # Portugese
    "🇧🇷": "🇵🇹", "🇵🇷": "🇵🇹",
    
    # Korean
    "🇰🇵": "🇰🇷",

    # German
    "🇨🇭": "🇩🇪"
}

def message(recipient_phone, languages):
    message = "🛂 Ok. Fortnight now knows you speak these languages: "
    for language in languages:
        message += language + " "
        
    resp = twilio.twiml.Response()
    resp.message(message)
    
    return str(resp)