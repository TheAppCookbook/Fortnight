import twilio

client = twilio.rest.TwilioRestClient(
    "AC8785a0ab24a08edcf4e7427c3ee42dd3",
    "fb838481285047827014f94fd493a6d4"
)

message = client.messages.create(
    to="+12402912158",
    from_="+12403294422",
    body="fuck u"
)