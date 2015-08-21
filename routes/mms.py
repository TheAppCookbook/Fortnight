from commons import twilio_client
import twilio


class MMS:
    def route(self, request):
        if request.method == 'GET':
            return self.GET(request) 
        elif request.method == 'POST':
            return self.POST(request)
         
    def GET(self, request):
        message = twilio_client.messages.create(
            to="+12402912158",
            from_="+12403294422",
            body="fuck u"
        )
        
        return str(message)
        
    def POST(self, request):
        resp = twilio.twiml.Response()
        resp.message = str(request.values)
        
        return str(resp)