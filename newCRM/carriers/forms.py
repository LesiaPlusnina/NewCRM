from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Carrier, Customer, Category, FollowUp

User = get_user_model()


class CarrierModelForm(forms.ModelForm):
    class Meta:
        model = Carrier
        fields = (
            'first_name',
            'last_name',
            'age',
            'customer',
            'description',
            'phone_number',
            'email',
            'profile_picture'
        )

    def clean_first_name(self):
        data = self.cleaned_data["first_name"]
        # if data != "Alesia":
        #     raise ValidationError("Your name is not Alesia")
        return data

    def clean(self):
        pass
        # first_name = self.cleaned_data["first_name"]
        # last_name = self.cleaned_data["last_name"]
        # if first_name + last_name != "Alesia Plusnina":
        #     raise ValidationError("Your name is not Alesia Plusnina")


class CarrierForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class AssignCustomerForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        customers = Customer.objects.filter(organisation=request.user.userprofile)
        super(AssignCustomerForm, self).__init__(*args, **kwargs)
        self.fields["customer"].queryset = customers


class CarrierCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Carrier
        fields = (
            'category',
        )


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
        )


class FollowUpModelForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        fields = (
            'notes',
            'file'
        )