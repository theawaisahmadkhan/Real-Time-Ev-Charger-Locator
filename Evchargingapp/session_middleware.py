from django.shortcuts import redirect,render

class SessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.session.get('id'):
            response = self.get_response(request)
            return response
            return redirect('loginsignup')  # Replace 'login' with the appropriate URL name for your login page
        else:
            
          return redirect('loginsignup') 
