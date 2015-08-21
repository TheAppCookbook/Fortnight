class Route:
    methods = ['GET']
    
    def route(self, request):
        if request.method == 'GET':
            return self.GET(request) 
        elif request.method == 'POST':
            return self.POST(request)
        elif request.method == 'PUT':
            return self.PUT(request)
        elif request.method == 'DELETE':
            return self.DELETE(request)
