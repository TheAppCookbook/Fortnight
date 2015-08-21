import twilio
import parse_rest.connection


twilio_sender = '+12403294422'
twilio_client = twilio.rest.TwilioRestClient(
    "AC8785a0ab24a08edcf4e7427c3ee42dd3",
    "fb838481285047827014f94fd493a6d4"
)

parse_client = parse_rest.connection.register(
    "ucKFTEG0XQpB7jYgkC1hUsv4zBVcmfzkO1QKA2B8",
    "C8BG9j2dKtCzZPGp3DIHjh4vdGZzaxfhZ6xZCEoT"
)
