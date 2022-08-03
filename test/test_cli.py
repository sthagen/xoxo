import pathlib

from xoxo.cli import app

FIXTURES = pathlib.Path('test', 'fixtures')


def test_app_nothing(capsys):
    assert app([]) == 0
    out, err = capsys.readouterr()
    assert not err
    assert 'usage' in out


def test_app_gone(capsys):
    assert app(['gone-not-present-away.txt']) == 1
    out, err = capsys.readouterr()
    assert not err
    assert 'does not exist or is empty' in out


def test_app_empty(capsys):
    assert app([FIXTURES / 'grid_empty.txt']) == 1
    out, err = capsys.readouterr()
    assert not err
    assert 'does not exist or is empty' in out


def test_app_grid_s_1(capsys):
    assert app([FIXTURES / 'grid_s_1.txt']) == 0
    out, err = capsys.readouterr()
    assert not err
    assert '| O | X | X | O | X | O |  4' in out
