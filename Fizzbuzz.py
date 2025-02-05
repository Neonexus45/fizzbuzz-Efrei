# Implémentation de FizzBuzz en Python

def fizz_buzz():
    for i in range(1, 101):
        output = ""
        
        # Si le nombre est divisible par 3 ou contient un 3
        if i % 3 == 0 or '3' in str(i):
            output += "Fizz"
        
        # Si le nombre est divisible par 5 ou contient un 5
        if i % 5 == 0 or '5' in str(i):
            output += "Buzz"
        
        # Si la sortie est vide, afficher le nombre, sinon afficher "Fizz", "Buzz", ou "FizzBuzz"
        if output == "":
            print(i)
        else:
            print(output)

# Appel de la fonction
fizz_buzz()
