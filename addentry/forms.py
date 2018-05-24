from django.forms import ModelForm, IntegerField, Textarea
from .models import Physician, Rule

class PhysicianForm(ModelForm):
    npi = IntegerField(max_value=1999999999, min_value=1000000000, label='NPI', help_text='A number between 100000000 and 199999999')
    rating = IntegerField(max_value=5, min_value=1, label='Rating', help_text='A number between 1 and 5')
    class Meta:
        model = Physician
        fields = ['npi', 'board_cert', 'age', 'location', 'language', 'rating']

class RuleForm(ModelForm):
    class Meta:
        model = Rule
        fields = '__all__'
        widgets = {
            'content': Textarea(attrs={'disabled': 'disabled'})
        }
