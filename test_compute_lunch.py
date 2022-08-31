from compute_lunch import days_until_lunch


def test_days_until_lunch():
    assert (days_until_lunch(24, 31) == 7)


def test_days_until_lunch_4():
    assert (days_until_lunch(22, 26) == 4)


def test_days_until_lunch_0():
    assert (days_until_lunch(253, 253) == 0)


def test_days_until_lunch_0_negative():
    assert (days_until_lunch(83, 64) == 0)


def test_days_until_lunch_1():
    assert (days_until_lunch(9, 10) == 1)
