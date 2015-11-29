import pytest
from mock import patch, MagicMock
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

def test_mock_meta():
	sprint = Sprint()		
	sprint.meta = MagicMock()
	sprint.meta.__len__.return_value = 1
	sprint.meta.__iter__.return_value = iter([1])

	assert len(sprint.meta) == 1
	assert list(sprint.meta) == [1]
