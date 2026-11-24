def split_bill(total, people):
    return total / people


def check_people(people):
    if people == 0:
        raise ValueError("people cannot be zero")
