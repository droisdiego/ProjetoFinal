from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = { 
        'nome': forms.TextInput(attrs={'class':'form-control'}), 
        'marca': forms.TextInput(attrs={'class':'form-control'}), 
        'preco': forms.TextInput(attrs={'class':'form-control'}),  
        'imagem': forms.FileInput(attrs={'class': 'form-control' }), 
        'detalhes': forms.TextInput(attrs={'class':'form-control'}), 
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagem'].widget.attrs.update({'enctype': 'multipart/form-data'})