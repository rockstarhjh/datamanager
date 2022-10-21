from django import forms
from acount.models import Acount


class AcoForm(forms.ModelForm):
    class Meta:
        model = Acount
        fields = '__all__'
        labels ={
            'date': '거래일자', 'company': '거래처명', 'product': '제품명',
            'count': '수량', 'unit': '단위', 'price': '단가',
            'sumprice': '공급가액', 'tax': '세액', 'totalprice': '총합계금액',
            'inoutcompany': '매입처/매출처', 'incomeprice': '매입금액', 'division': '매입/매출',
            'paymethod': '결제방법', 'remark': '참고내용'
        }

    def __init__(self, *args, **kwargs):
        super(AcoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'