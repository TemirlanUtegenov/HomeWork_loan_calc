def calculate_loan(summ, rate, period):
    """
     >>> calculate_loan(500000, 8,  12)
     43494

    :param summ:
    :param rate:
    :param period:
    :return:
    """
    # Formula
    # M = L[i(1+i)n] / [(1+i)n-1]

    #   * M = Monthly Payment (what were trying to find out)
    #   * L = Loan Amount (loanAmount)
    #   * I = Interest Rate (for an interest rate of 5%, i = 0.05 (interestCalculation)
    #   * N = Number of Payments (repaymentLength)

    temp = rate / 100.
    monthly_pay = summ * temp * (1 + temp) * period / (
            (1 + temp) * period - 1)

    return round(monthly_pay)
