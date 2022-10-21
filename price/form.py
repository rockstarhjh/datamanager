from django import forms
from price.models import Price
from products.models import Products


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Products


class PriceForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Products.objects.all(),
                                      to_field_name='category',
                                      empty_label="카테고리")
    p_name = forms.ModelChoiceField(queryset=Products.objects.all(),
                                    to_field_name='p_name',
                                    empty_label="제품명")

    class Meta:
        model = Price
        # exclude = Products
        fields = '__all__'
        # widgets = {'idproducts': forms.HiddenInput}
        labels = {
            'buyprice': '매입단가', 'renew_bp_date': '매입갱신일', 'sellprice': '매출단가',
            'renew_sp_date': '매출갱신일',
            'remark': '비고'
        }

    def __init__(self, *args, **kwargs):
        super(PriceForm, self).__init__(*args, **kwargs)
        # self.fields['product'].queryset = Products.objects.filter(idproducts=Price.product)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
