from django import forms
from stocks.models import Stocks


class StocksForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = '__all__'
        # exclude = ['idproducts']
        widgets = {'idproducts': forms.HiddenInput}
        labels = {
            'date': '날짜', 'category': '카테고리', 'p_name': '제품명',
            'company': '거래처', 'in_field': '입고', 'out_field': '출고',
            'return_field': '반품', 'lost_field': '망실', 'location': '장소',
            'remark': '비고'
        }

    def __init__(self, *args, **kwargs):
        super(StocksForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
