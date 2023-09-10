from functions import *

#assert sprawdza poprawnosc kodu

def test_dodawania():
    assert add(2, 2) == 4

#zeby uruchomic taki test w terminalu trzeba napisac 'pytest' i wtedy nazwa pliku
# np. pytest tests.py

def test_dlugosc_zdania():
    assert number_of_letters("Ala ma kota") == 11


def test_1():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) =='FizzBuzz'
    assert fizzbuzz(30) == 'FizzBuzz'
    assert fizzbuzz(3000) == 'FizzBuzz'
def test_advanced():
    assert fizzbuzz(0) == None
    assert fizzbuzz(5.2) == 'Buzz'
    assert fizzbuzz(3.2) == 'Fizz'
    assert fizzbuzz(3.9) == 'Fizz'
    assert fizzbuzz('Mama') == None