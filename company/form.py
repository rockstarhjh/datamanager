from django import forms
from company.models import Company


class ComForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        labels = {
            'name': '상호', 'comnum': '사업자번호', 'ceo': '대표자',
            'tel': '전화번호', 'fax': '팩스', 'address': '주소',
            'type': '업태', 'item': '종목', 'delivery': '배달정보',
            'cellphone': '휴대폰', 'post': '우편번호', 'email': '이메일',
            'division': '매입/매출', 'remark': '비고'
        }

    def __init__(self, *args, **kwargs):
        super(ComForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
