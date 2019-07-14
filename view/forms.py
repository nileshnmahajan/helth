from django import forms  
from view.models import Users  
from view.models import Hospital  
from view.models import Disease  
from view.models import Users
class ViewForm(forms.ModelForm):  
	class Meta:  
		model = Users  
		fields = "__all__"  