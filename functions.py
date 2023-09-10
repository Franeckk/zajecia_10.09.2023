def add (x, y):
    return x + y

def number_of_letters(x):
    return(len(x))

def fizzbuzz(liczba):
    if isinstance(liczba, str) is True:
        return None
    else:
        liczba = int(liczba)
        if liczba<= 0:
            return None
        elif liczba % 3 == 0 and liczba % 5 == 0:
            return 'FizzBuzz'
        elif  liczba % 3 == 0:
            return 'Fizz'
        elif liczba % 5 == 0:
            return 'Buzz'

        return liczba

# inna opcja tego co wyżej
def fizzbuzz(liczba):
    if not isinstance(liczba, str) and liczba > 0:
        liczba = int(liczba)
        if liczba % 3 == 0 and liczba % 5 == 0:
            return 'FizzBuzz'
        elif  liczba % 3 == 0:
            return 'Fizz'
        elif liczba % 5 == 0:
            return 'Buzz'
        else:
            return liczba

#inna opcja
def fizzbuzz(liczba):
    if isinstance(liczba, (int, float)) and liczba > 0:
        # i jak wyzej juz reszta