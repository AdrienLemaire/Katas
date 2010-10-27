from wrap import wrap_line


def test_basic():
    """First test, we send a text and receive the same one"""
    line = "test"
    assert wrap_line(line) == "test"


def test_wrap_word():
    """One word is longer than the max column, we have to
    break the word"""
    line = "n" * 81
    assert wrap_line(line) == "n" * 80 + "\nn"


def test_wrap_2_words():
    """We have 2 words longer than the max of column,
    we should replace the space by a \n"""
    w1, w2 = "n" * 75, "n" * 5
    line = "%s %s" % (w1, w2)
    assert wrap_line(line) == "%s\n%s" % (w1, w2)


def test_space_at_the_end():
    """ If the last character of the line is a space, remove it"""
    line = "n" * 79 + " "
    print "--%s--" % wrap_line(line)
    assert wrap_line(line) == "n" * 79


def test_with_2_lines():
    """If we have a \n in the text, we replace it with a space, then
    we wrap the new lines"""
    line = "n" * 15 + "\n" + "n" * 60 + " " + "n" * 10
    assert wrap_line(line) == "n" * 15 + " " + "n" * 60 + "\n" + "n" * 10
