from commons import twilio_client
import twilio.twiml


class MMS:
    methods = ['POST']

    def route(self, request):
        if request.method == 'POST':
            return self.POST(request)
        
    def POST(self, request):
        request.values.get('body')
        
        # Languages
        if body.startswith('add'):
            return self._add_language(request)
        elif body.startswith('remove'):
            return self._remove_language(request)
        
        # Pen Pals
        elif body.startswith('report'):
            return self._report_pen_pal(request)
        elif body.startswith('swap'):
            return self._swap_pen_pal(request)
        
        # Messages
        else:
            return self._queue_message(request)    
        
    # Languages
    def _add_language(self, request):
        pass
        
    def _remove_language(self, request):
        pass
        
    # Pen Pals
    def _report_pen_pal(self, request):
        pass
        
    def _swap_pen_pal(self, request):
        pass
        
    # Messages
    def _queue_message(self, request):
        pass
