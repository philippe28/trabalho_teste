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


def test_add_trabalho():
    sprint = Sprint()
    sprint.add_trabalho(0)

    assert 1 == len(sprint.trabalho)
    assert 0 == sprint.trabalho[0]


def test_mock_trabalho():
		sprint = Sprint()		
		sprint.trabalho = MagicMock()
		sprint.trabalho.__len__.return_value = 1
		sprint.trabalho.__iter__.return_value = iter([1])

		assert len(sprint.trabalho) == 1
		assert list(sprint.trabalho) == [1]


def test_mock_simetria_lenght():
	sprint = Sprint()
	sprint.add_trabalho = MagicMock()
	sprint.add_trabalho.__len__.return_value = 1
	sprint.add_meta = MagicMock()
	sprint.add_meta.__len__.return_value = 1

	assert len(sprint.trabalho) == len(sprint.meta)


