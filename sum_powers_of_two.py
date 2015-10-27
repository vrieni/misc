

def sum_powers_of_two(n):
        EXPONENT = 2
	if n != 0:
		return power(n, EXPONENT) + sum_powers_of_two(n-1)
	else:
		return n


def power(base, exponent):
    return base ** exponent

print sum_powers_of_two(4)