from parse_rest.datatypes import Object as ParseObject
from parse_rest.user import User as ParseUser

from conversations.language_management import language_map

import phonenumbers
import re

from phonenumbers.phonenumberutil import NumberParseException


class User(ParseUser):
    @classmethod
    def credentials(cls, phone_number):
        return (
            phone_number.replace('+', 'u'),
            phone_number.replace('+', 'p')
        )
        
    @classmethod
    def valid_number(cls, phone_number):
        parse_type = None if phone_number.startswith('+') else 'US'
        
        try:
            return phonenumbers.format_number(
                phonenumbers.parse(phone_number, parse_type),
                phonenumbers.PhoneNumberFormat.E164
            )
        except:
            return None
            
    @classmethod
    def languages(cls, language_str):
        language_str = re.sub(r'(\w+)', '', language_str)
        languages = [lang for lang in re.split(r'\s+', language_str) if lang]
        
        languages += [
            language_map[lang] for lang in languages
            if lang in language_map
        ]
        
        languages = list(set(languages))
        return languages


class Palship(ParseObject):
    pass