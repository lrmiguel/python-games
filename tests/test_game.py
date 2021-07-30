def test_soma():
    a = 120
    b = 140
    soma = a + b

    assert soma == 260, "should be 260"


def test_division():
    a = 200
    b = 120

    total = a / b

    assert round(total, 1) == 1.7
