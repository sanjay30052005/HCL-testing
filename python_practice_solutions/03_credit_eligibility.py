
def check_eligibility(income, credit_score, existing_debt):
    if income > 50000 and credit_score >= 700 and existing_debt < 20000:
        return "Eligible"
    elif credit_score >= 600:
        return "Review"
    else:
        return "Reject"
