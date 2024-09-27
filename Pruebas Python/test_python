import pytest
from io import StringIO
import sys

# Suponiendo que tu función está en un archivo llamado `code.py`
from code import code_challenge_one

def test_code_challenge_one(capfd):
    # Datos de prueba
    list_num = [80, 68, 5, 4, 3, 2, 8, 7, 9, 29, 18, 6, 88]
    S = 8

    # Llamar a la función
    code_challenge_one(list_num, S)

    # Capturar la salida
    captured = capfd.readouterr()
    
    # Resultado esperado
    expected_output = "[7, 6, 4, 3, 2]\n"
    
    # Verificar que la salida sea la esperada
    assert captured.out == expected_output
