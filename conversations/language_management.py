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

def send_message(recipient_phone, languages):
    message = "🛂 Ok. Fortnight now knows you speak these languages: "
    for language in languages:
        message += language.encode('utf-8') + " "
    message = message.decode('utf-8')
        
    twilio_client.messages.create(
        to=recipient_phone,
        from_=twilio_sender,
        body=message
    )