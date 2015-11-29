import pytest
from BurnUp import Sprint

def test_inicio_padrao():
    sprint = Sprint()

    assert 0 == len(sprint.meta)
    assert 0 == len(sprint.trabalho)
    assert 0 != sprint.sprint