from django.core.exceptions import ValidationError

def validar_costo(value):
    if value%10 != 0:
        raise ValidationError(
            '%(value)s no es un costo permitido',
            params={'value': value},
        )