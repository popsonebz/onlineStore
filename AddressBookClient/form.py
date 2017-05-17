from AddressBookClient.models import AddressBookTable

from django import forms

from crispy_forms.helper import FormHelper

from crispy_forms.helper import FormHelper

class AddressBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddressBookForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['phone_number'].label = "Mobile Number"
        self.fields['email_address'].label = "Email"
        self.fields['address'].label = "Address"

        helper = FormHelper(self)
        helper.label_class = 'col-lg-2'
        helper.field_class = 'col-lg-8'
    class Meta:
        model = AddressBookTable
        widgets = {
            
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name',}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name',}),
            'phone_name': forms.TextInput(attrs={'placeholder': 'Phone Number',}),
            'email_address':forms.TextInput(attrs={'placeholder': 'Email'}),
            'address': forms.Textarea(attrs={'cols': 50, 'rows': 10, 'placeholder': 'Please give some comments'}),
        }

        fields = ['first_name', 'last_name', 'phone_number', 'email_address', 'address'] 



