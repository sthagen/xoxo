import pathlib

from xoxo import xoxo as xo

FIXTURES = pathlib.Path('test', 'fixtures')


def test_main_nothing(capsys):
    assert xo.main([]) == 0
    out, err = capsys.readouterr()
    assert not err
    assert 'usage' in out


def test_main_gone(capsys):
    assert xo.main(['gone-not-present-away.txt']) == 1
    out, err = capsys.readouterr()
    assert not err
    assert 'does not exist or is empty' in out


def test_main_empty(capsys):
    assert xo.main([FIXTURES / 'grid_empty.txt']) == 1
    out, err = capsys.readouterr()
    assert not err
    assert 'does not exist or is empty' in out


def test_main_grid_s_1(capsys):
    assert xo.main([FIXTURES / 'grid_s_1.txt']) == 0
    out, err = capsys.readouterr()
    assert not err
    assert '| O | X | X | O | X | O |  4' in out


def test_main_grid_s_1_space_alien(capsys):
    assert xo.main([FIXTURES / 'grid_s_1_space_alien.txt']) == 0
    out, err = capsys.readouterr()
    assert not err
    assert '| O | X |   |   |   | X |  3' in out
    assert '| X | X | O | X | O | O |  6' in out


def test_main_grid_s_2(capsys):
    assert xo.main([FIXTURES / 'grid_s_2.txt']) == 0
    out, err = capsys.readouterr()
    assert not err
    assert '| O |   |   |   | X | O |  5' in out
    assert '| X | O | O | X | O | X |  1' in out


def test_main_grid_m_1(capsys):
    assert xo.main([FIXTURES / 'grid_m_1.txt']) == 0
    out, err = capsys.readouterr()
    assert not err
    assert '|   |   |   | X | O | X |   |   |  7' in out
    assert '| X | O | X | X | O | X | O | O |  2' in out


def test_main_grid_m_2(capsys):
    assert xo.main([FIXTURES / 'grid_m_2.txt']) == 0
    out, err = capsys.readouterr()
    assert not err
    assert '| O | X | X | O |   |   | X |   |  2' in out
    assert '| O | X | X | O | X | O | X | O |  2' in out


def test_main_grid_x_1(capsys):
    assert xo.main([FIXTURES / 'grid_x_1.txt']) == 0
    out, err = capsys.readouterr()
    assert not err
    assert '|   |   | X |   | X | X | O | O | X | X |  8' in out
    assert '| O | O | X | O | X | X | O | O | X | X |  8' in out


def test_main_grid_x_2(capsys):
    assert xo.main([FIXTURES / 'grid_x_2.txt']) == 0
    out, err = capsys.readouterr()
    assert not err
    assert '|   |   |   | O |   |   |   |   |   |   |  9' in out
    assert '| X | O | X | O | X | O | X | X | O | O |  9' in out


def test_main_grid_x_3(capsys):
    assert xo.main([FIXTURES / 'grid_x_3.txt']) == 0
    out, err = capsys.readouterr()
    assert not err
    assert 'Problem:' in out
    assert '|   |   | O |   |   |   |   | X |   |   | 10' in out
    assert 'Solution:' in out
    assert ',---+---+---+---+---+---+---+---+---+---,' in out
    assert '| O | X | O | O | X | O | X | X | O | X | 10' in out
    assert '*---+---+---+---+---+---+---+---+---+---*' in out
    assert '  1   2   3   4   5   6   7   8   9  10' in out


def test_main_tic_tac_toe_wild_with_overrun(capsys):
    assert xo.main([FIXTURES / 'tic_tac_toe.txt']) == 0
    out, err = capsys.readouterr()
    assert not err
    assert '| X | X | O | X | O | O |  6' in out


def test_rows_equal_yes():
    the_wun_and_only = [xo.X, xo.O]
    assert xo.rows_equal(the_wun_and_only, the_wun_and_only) is True


def test_rows_equal_some():
    for wun in xo.SYMBOLS:
        for other in xo.SYMBOLS:
            assert xo.rows_equal([wun], [other]) is bool(wun == other)
    for wun in xo.TOKENS:
        assert xo.rows_equal([wun], [xo.E]) is False
    assert xo.rows_equal([xo.E], [xo.E]) is False


def test_any_row_equal_yes():
    the_wun_and_only = [xo.X, xo.O]
    grid = [
        the_wun_and_only,
        the_wun_and_only,
    ]
    assert xo.any_row_equal(grid) is True
