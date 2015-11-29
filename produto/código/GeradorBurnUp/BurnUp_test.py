import pytest
from BurnUp import Sprint

def test_inicio_padrao():
    sprint = Sprint()

    assert 0 == len(sprint.meta)
    assert 0 == len(sprint.trabalho)
    assert 0 != sprint.sprint


def test_add_meta():
    sprint = Sprint()
    sprint.add_meta(100)

    assert 1 == len(sprint.meta)
    assert 100 == sprint.meta[0]