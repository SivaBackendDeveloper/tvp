from django import forms
from j.models import Member,Activity


class MemberForm(forms.ModelForm):
 class Meta:
    model=Member
    fields='__all__'

class ActivityForm(forms.ModelForm):
 class Meta:
    model=Activity
    fields='__all__'

