import pytest

@pytest.fixture # essa função irá ser executada sempre que inciar o teste
def retorna_valor():
    return 10

@pytest.mark.primarios # marcando testes primários
def test_par(retorna_valor):
    assert retorna_valor % 2 == 0 # assert é para avaliar uma condição quando pytest passar

@pytest.mark.primarios
def test_par2(retorna_valor):
    assert retorna_valor % 3 == 0 # fazendo com que gere erro