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
    message += ','.join(languages)
        
    resp = twilio.twiml.Response()
    resp.message(message)
    
    return str(resp)