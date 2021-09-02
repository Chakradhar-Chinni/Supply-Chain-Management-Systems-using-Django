from django import forms
from .models import AdminRegistration,SupplierRegistration,UserRegistration,UserOrder,tud,tmd

class AdminRegistrationForm(forms.ModelForm):   
    class Meta:
        model = AdminRegistration
        fields = "__all__"

class SupplierRegistrationForm(forms.ModelForm): 
    class Meta:
        model = SupplierRegistration
        fields = "__all__"

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = "__all__"

class OrderForm(forms.ModelForm):
    class Meta:
        model = UserOrder
        fields = ('ProductName','Quantity','State')

class tudForm(forms.ModelForm):
    class Meta:
        model = tud
        fields = ('UserName','Number')

class tmdForm(forms.ModelForm):
    class Meta:
        model = tmd
        fields = "__all__"

