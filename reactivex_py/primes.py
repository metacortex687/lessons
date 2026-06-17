import reactivex
from reactivex import operators as ops

source = reactivex.from_iterable(range(1,100))
# source = reactivex.from_iterable([2,3,5,6])

def validate_sequential(prev_number, number):
    if number - prev_number != 1:
        raise ValueError(f"Числа должны увеличиватся на единицу. За числом {prev_number} не может следовать {number}")
    return number

def sieve_step(state, number):
    _, prime_multiples = state 
    for prime, next_multiple_of_prime in prime_multiples:
        while next_multiple_of_prime < number:
            next_multiple_of_prime += prime
        if next_multiple_of_prime == number:
            return (None, prime_multiples)
        
    return (number, [*prime_multiples, (number, number*2)])    


composed = source.pipe(
    ops.filter(lambda i: i >= 2), 
    ops.scan(validate_sequential, seed=1),
    ops.scan(sieve_step, seed=(None,[])),
    ops.map(lambda sieve_result: sieve_result[0]),
    ops.filter(lambda i: i is not None), 
)

composed.subscribe(
    on_next=lambda value: print(f"Простое число: {value}"), 
    on_error=lambda e: print(f"Ошибка: {e}"))


