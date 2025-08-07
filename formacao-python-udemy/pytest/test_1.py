import pytest

@pytest.mark.primarios # marcando testes primários
def test_par(retorna_valor):
    assert retorna_valor % 2 == 0 # assert é para avaliar uma condição quando pytest passar

@pytest.mark.primarios
def test_par2(retorna_valor):
    assert retorna_valor % 3 == 0 # fazendo com que gere erro

@pytest.mark.parametrize("num1,num2",[(10,2),(3,2),(3,1),(12,4)]) #parametrizando números para fazer teste
def test_par3(num1,num2):
    assert num1 % num2 == 0