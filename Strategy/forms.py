from models import Strategy
from django.forms import ModelForm
from django.forms.widgets import Textarea
class StrategyForm(ModelForm):

    class Meta:
        model=Strategy
        fields = ['user','title','description','code','status']
        widget={
            'code': Textarea(attrs={'cols': 3000, 'rows': 20}),
        }