import squareseqdigit


def test_squareseqdigit_1():
    assert squareseqdigit.square_sequence_digit(1) == 1, " square_sequence_digit(1) == 1 "


def test_squareseqdigit_2():
    assert squareseqdigit.square_sequence_digit(2) == 4, " square_sequence_digit(2) == 4 "


def test_squareseqdigit_3():
    assert squareseqdigit.square_sequence_digit(7) == 5, " square_sequence_digit(7) == 5 "


def test_squareseqdigit_4():
    assert squareseqdigit.square_sequence_digit(12) == 6, " square_sequence_digit(12) == 6 "


def test_squareseqdigit_5():
    assert squareseqdigit.square_sequence_digit(17) == 0, " square_sequence_digit(17) == 0 "


def test_squareseqdigit_6():
    assert squareseqdigit.square_sequence_digit(27) == 9, " square_sequence_digit(27) == 9 "
