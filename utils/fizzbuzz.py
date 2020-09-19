def fizz_or_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'fizzbuzz'
    if number % 3 == 0:
        return 'fizz'
    if number % 5 == 0:
        return 'buzz'
    return number

def fizzbuzz_sequence(limit):
    if limit <= 0:
        raise ValueError(f'Limit must be greater than 0, but {limit} was passed')
    result = []
    for i in range(1, limit + 1):
        result.append(fizz_or_buzz(i)) 
    return result