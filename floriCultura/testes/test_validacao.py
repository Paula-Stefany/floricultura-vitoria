import os 
import sys 
from floriCultura.forms.form_validators import *
import pytest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


def test_validate_password_equal_valid():
    try:
        validate_password_equal('abcde', 'abcde')
    except ValidationError:
        pytest.fail('validate_password_equal() - ValidationError inesperado')


def test_password_invalid_equal():
    with pytest.raises(ValidationError):
        validate_password_equal('12345', '23456')


def test_valid_password_strength():
    try:
        validate_password_strength('1234qwe(f')
    except ValidationError:
        pytest.fail("validate_password_strength() - ValidationError inesperado")


def test_invalid_password_size():
    with pytest.raises(ValidationError):
        validate_password_strength('wer23$')


def test_password_without_digit():
    with pytest.raises(ValidationError):
        validate_password_strength('rftgyhuj*')


def test_password_without_special_char():
    with pytest.raises(ValidationError):
        validate_password_strength('gggty66668')


def test_valid_cpf():
    try:
        validate_cpf('222.333.444.78')
        validate_cpf('888.666-888-88')
        validate_cpf('66666677755')
    except ValidationError:
        pytest.fail('validate_cpf() - ValidationError inesperado')


def  test_invalid_cpf_length():
    with pytest.raises(ValidationError):
        validate_cpf('222.555.666.7')


def test_cpf_without_digit():
    with pytest.raises(ValidationError):
        validate_cpf('ggg-jjj.nnn.nn')


def test_valid_cep():
    try:
        validate_cep('66677788')
        validate_cep('666.888-99')
        validate_cep('999.99999')
    except ValidationError:
        pytest.fail('validate_cep() - ValidationError inesperado')


def test_invalid_cep_length():
    with pytest.raises(ValidationError):
        validate_cep('777.999.9900')


def test_cep_without_digit():
    with pytest.raises(ValidationError):
        validate_cep('jjj.jjj.kk')
