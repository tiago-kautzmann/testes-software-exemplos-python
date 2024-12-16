import math
import pytest

# Função para calcular a soma de uma lista de valores
def soma(valores):
    return sum(valores)

# Função para calcular a média de uma lista de valores
def media(valores):
    if not valores:
        raise ValueError("A lista não pode estar vazia")
    return soma(valores) / len(valores)

# Função para calcular o desvio padrão de uma lista de valores
def desvio_padrao(valores):
    if len(valores) < 2:
        raise ValueError("A lista deve conter pelo menos dois valores")
    m = media(valores)
    variancia = soma([(x - m) ** 2 for x in valores]) / len(valores)
    return math.sqrt(variancia)

# Testes unitários usando pytest
def test_soma():
    assert soma([1, 2, 3, 4, 5]) == 15
    assert soma([0, 0, 0]) == 0
    assert soma([-1, -2, -3]) == -6
    assert soma([]) == 0

def test_media():
    assert media([2, 4, 6, 8]) == 5
    assert media([1]) == 1
    assert media([-1, -2, -3, -4]) == -2.5
    with pytest.raises(ValueError):
        media([])  # Deve lançar uma exceção se a lista estiver vazia

def test_desvio_padrao():
    assert desvio_padrao([2, 4, 4, 4, 5, 5, 7, 9]) == pytest.approx(2.0, rel=1e-3)
    assert desvio_padrao([1, 2, 3, 4, 5]) == pytest.approx(1.414, rel=1e-3)
    with pytest.raises(ValueError):
        desvio_padrao([1])  # Deve lançar uma exceção se houver menos de dois valores
