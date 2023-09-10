def add (x, y):
    return x + y

def number_of_letters(x):
    return(len(x))

def fizzbuzz(i):
    if isinstance(i, str) is True:
        return None
    else:
        i = int(i)
        if i<= 0:
            return None
        elif i % 3 == 0 and i % 5 == 0:
            return 'FizzBuzz'
        elif  i % 3 == 0:
            return 'Fizz'
        elif i % 5 == 0:
            return 'Buzz'

        return i

