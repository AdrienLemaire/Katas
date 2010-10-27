from wrap import wrap_line


def test_wrap_line():
    text = "bob"
    assert wrap_line(text) == "bob2"


def test_word_gt_colmax():
    text = "c" * 8
    assert wrap_line(text) == "c" * 7 + "\nc"

def test_1_split():
    text = "this iscool"
    assert wrap_line(text) == "this\niscool"


def test_1_split_longer():
    text = "thisisbiggerbutthis iscool"
    print wrap_line(text)
    assert wrap_line(text) == "thisisb\niggerbu\ntthis\niscool"
