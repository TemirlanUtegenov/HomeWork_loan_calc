import pytest

from app.loan_calc import calculate_loan

@pytest.mark.parametrize('summ, rate, period, expected', [
    (500000, 8, 12, 43344)
])
def test_calculate_loan(summ, rate, period, expected):
    actual = calculate_loan(summ, rate, period)
    assert expected == actual
