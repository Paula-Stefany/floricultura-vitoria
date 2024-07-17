from django.core.exceptions import ValidationError


def validate_password_equal(password1, password2):
    if password1 and password2 and password1 != password2:
        raise ValidationError('Senhas não coicidem')
    
    
def validate_password_strength(password):
    if len(password) < 8:
        raise ValidationError('A senha precisa ter no mínimo 8 caracteres')
    
    if not any(char.isdigit() for char in password):
        raise ValidationError('A senha precisa de pelo menos um número')
    
    if not any(char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for char in password):
        raise ValidationError('A senha precisa de pelo menos um caracter especial')


def validate_cpf(value):
    cpf = value.replace('.', '').replace('-', '')

    if not cpf.isdigit() or len(cpf) != 11:
        raise ValidationError('CPF inválido')


def validate_cep(value):
    cep = value.replace('.', '').replace('-', '')

    if not cep.isdigit() or len(cep) > 8:
        raise ValidationError('CEP inválido')
