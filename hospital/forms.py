from django import forms  
from view.models import Users  
from view.models import Hospital  
from view.models import Disease  
from view.models import Users
def formView(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'loggedin.html', {"username" : username})
   else:
      return render(request, 'login.html', {})