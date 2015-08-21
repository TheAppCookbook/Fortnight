from parse_rest.datatypes import Object as ParseObject
from parse_rest.user import User as ParseUser
import phonenumbers

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
            
    __language_map = {}
            
    @classmethod
    def languages(cls, language_str):
        language_str = re.sub(r'(\w+)', '', language_str)
        languages = [lang for lang in re.split(r'\s+', language_str) if lang]
        
        languages += [
            cls.__language_map[lang] for lang in languages
            if lang in cls.__language_map
        ]
        
        return languages


class Palship(ParseObject):
    pass