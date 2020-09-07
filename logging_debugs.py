import logging
logging.basicConfig(filename='myprogramlog.txt', level=logging.DEBUG, format='%(asctime)s-%(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)


def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug(f'i is {i} and total is {total} ')
    return total

print(factorial(5))
