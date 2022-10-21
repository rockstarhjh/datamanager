from django import forms
from v_money.models import VMoney


class VMoneyForm(forms.ModelForm):
    class Meta:
        model = VMoney
        fields = '__all__'
        # widgets = {'idproducts': forms.HiddenInput}
        labels = {
            'date': '날짜', 'deposit': '충전', 'expense': '지출',
            'remark': '내용'
        }

    def __init__(self, *args, **kwargs):
        super(VMoneyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
