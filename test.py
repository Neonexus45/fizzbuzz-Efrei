from fizzbuzz import fizzbuzz 

def test_fizzbuzz():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(31) == "31"
    print("Tout les testes sont passez !")

test_fizzbuzz()