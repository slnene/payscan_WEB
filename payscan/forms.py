from django import forms
from django.core.exceptions import ValidationError
from .models import Business
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class RegisterForm(forms.Form):
    email = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    first_name =forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
  
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")
        

class DepositForm(forms.Form):
    amount = forms.DecimalField()

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise ValidationError('Amount must be greater than zero')
        return amount

class WithdrawForm(forms.Form):
    amount = forms.DecimalField()

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise ValidationError('Amount must be greater than SZL 0.00')
        if self.balance is not None and amount > self.balance:
            raise ValidationError('Insufficient Funds')
        return amount

class PaymentForm(forms.Form):
    business = forms.ModelChoiceField(queryset=Business.objects.all())
    amount = forms.DecimalField()

    def __init__(self, *args, **kwargs):
        self.balance = kwargs.pop('balance', None)
        super(PaymentForm, self).__init__(*args, **kwargs)

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise ValidationError('Amount must be greater than SZL 0.00')
        if self.balance is not None and amount > self.balance:
            raise ValidationError('Insufficient Funds')
        return amount



#########business########

class BusinessRegistrationForm(UserCreationForm):
    business_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'business_name', 'password1', 'password2']

    def clean_business_name(self):
        business_name = self.cleaned_data.get('business_name')
        if Business.objects.filter(name=business_name).exists():
            raise ValidationError('Business name already exists.')
        return business_name

class BusinessLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class BusinessPaymentForm(forms.Form):
    business = forms.ModelChoiceField(queryset=Business.objects.all())
    amount = forms.DecimalField()

    def __init__(self, *args, **kwargs):
        self.balance = kwargs.pop('balance', None)
        super(BusinessPaymentForm, self).__init__(*args, **kwargs)

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise ValidationError('Amount must be greater than SZL 0.00')
        if self.balance is not None and amount > self.balance:
            raise ValidationError('Insufficient Funds')
        return amount

class BusinessWithdrawForm(forms.Form):
    amount = forms.DecimalField()

    def __init__(self, *args, **kwargs):
        self.balance = kwargs.pop('balance', None)
        super(BusinessWithdrawForm, self).__init__(*args, **kwargs)

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise ValidationError('Amount must be greater than SZL 0.00')
        if self.balance is not None and amount > self.balance:
            raise ValidationError('Insufficient Funds')
        return amount

