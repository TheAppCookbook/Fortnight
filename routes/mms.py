from commons import twilio_client


class MMS:
    def route(self, request):
        if request.method == 'GET':
            return self.GET(request) 
         
    def GET(self, request):
        message = twilio_client.messages.create(
            to="+12402912158",
            from_="+12403294422",
            body="fuck u"
        )
        
        return str(message)