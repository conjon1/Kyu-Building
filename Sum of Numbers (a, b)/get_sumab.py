def get_sum(a, b):
    # Note: a and b are not ordered!
    minimum = min(a, b)
    maximum = max(a, b)
    # reeeeturn sum of inbeteen and addong +1
    return sum(range(minimum, maximum + 1))