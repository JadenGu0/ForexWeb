from models import Strategy
from django.forms import ModelForm

class StrategyForm(ModelForm):

    class Meta:
        model=Strategy
        fields = ['user','title','description','code','status']