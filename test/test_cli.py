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
    assert app([str(FIXTURES / 'grid_empty.txt')]) == 1
    out, err = capsys.readouterr()
    assert not err
    assert 'does not exist or is empty' in out


def test_app_grid_s_1(capsys):
    assert app([str(FIXTURES / 'grid_s_1.txt')]) == 0
    out, err = capsys.readouterr()
    assert not err
    assert '| O | X | X | O | X | O |  4' in out


def test_app_empty_1x1(capsys):
    assert app([str(FIXTURES / 'empty_1x1.txt')]) == 1
    out, err = capsys.readouterr()
    assert not err
    assert 'Analysis: You need at least 2 times 2 cells for a valid solution.' in out


def test_app_filled_1x1(capsys):
    assert app([str(FIXTURES / 'filled_1x1.txt')]) == 1
    out, err = capsys.readouterr()
    assert not err
    assert 'Analysis: You need at least 2 times 2 cells for a valid solution.' in out
    assert '-   Note: Received a completely filled (invalid) grid - what is the expectation?' in out


def test_app_empty_2x2(capsys):
    assert app([str(FIXTURES / 'empty_2x2.txt')]) == 0
    out, err = capsys.readouterr()
    assert not err
    assert '| O | X |  2' in out


def test_app_complete_2x2(capsys):
    assert app([str(FIXTURES / 'complete_2x2.txt')]) == 0
    out, err = capsys.readouterr()
    assert not err
    assert '| O | X |  1' in out


def test_app_invalid_cols_eq_4x4(capsys):
    assert app([str(FIXTURES / 'invalid_cols_eq_4x4.txt')]) == 1
    out, err = capsys.readouterr()
    assert not err
    assert 'Analysis: Neighbor rows or columns are identical.' in out


def test_app_invalid_twin_plus_6x6(capsys):
    assert app([str(FIXTURES / 'invalid_twin_plus_6x6.txt')]) == 1
    out, err = capsys.readouterr()
    assert not err
    assert 'Analysis: More than two symbols of a kind together in a row or column.' in out


def test_app_invalid_rows_eq_4x4(capsys):
    assert app([str(FIXTURES / 'invalid_rows_eq_4x4.txt')]) == 1
    out, err = capsys.readouterr()
    assert not err
    assert 'Analysis: Neighbor rows or columns are identical.' in out


def test_app_empty_3x3(capsys):
    assert app([str(FIXTURES / 'empty_3x3.txt')]) == 1
    out, err = capsys.readouterr()
    assert not err
    assert 'Analysis: You need even squares to balance the symbols per row and column.' in out


def test_app_empty_2x4(capsys):
    assert app([str(FIXTURES / 'empty_2x4.txt')]) == 1
    out, err = capsys.readouterr()
    assert not err
    feedback = (
        'Analysis: You need (even) squares to balance the symbols per row and column'
        ' - found a 2 times 4 rectangle instead.'
    )
    assert feedback in out


def test_app_invalid_balance_4x4(capsys):
    assert app([str(FIXTURES / 'invalid_balance_4x4.txt')]) == 1
    out, err = capsys.readouterr()
    assert not err
    assert '| X |   | X | X |  1' in out
    assert 'Analysis: Some symbol has been overused.' in out
