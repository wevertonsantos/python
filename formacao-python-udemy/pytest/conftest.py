#conf test serve para passar função fixture para todos os arquivos como se fosse configuração padrão
import pytest

@pytest.fixture # essa função irá ser executada sempre que inciar o teste
def retorna_valor():
    return 10