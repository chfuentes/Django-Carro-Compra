from django import forms


ELECCIONES_CANTIDAD_PRODUCTO = [(i, str(i)) for i in range(1, 21)]


class FormAgregarProductoCarro(forms.Form):
    cantidad = forms.TypedChoiceField(
        choices=ELECCIONES_CANTIDAD_PRODUCTO,
        coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
