def fizzbuzz(i):
    result = ""
    
    # Si le nombre est divisible par 3 et 5
    if i % 3 == 0 and i % 5 == 0:
        result = "FizzBuzz"
    elif i % 3 == 0:
        result = "Fizz"
    elif i % 5 == 0:
        result = "Buzz"
    else:
        result = str(i)

    # Si le nombre contient un 3, ajouter "Fizz"
    if "3" in str(i):
        result += "Fizz"
    
    # Si le nombre contient un 5, ajouter "Buzz"
    if "5" in str(i) and "Buzz" not in result:  # Vérifier que "Buzz" n'est pas déjà dans result
        result += "Buzz"

    print(result)
