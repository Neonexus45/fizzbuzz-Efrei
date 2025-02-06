def fizzbuzz(n=100):
    """
    Renvoie une liste des résultats FizzBuzz jusqu'à n.

    Paramètres:
    n (int): Nombre maximum jusqu'à lequel exécuter FizzBuzz.

    Retourne:
    list: Liste contenant les valeurs de 1 à n avec "Fizz", "Buzz" ou "FizzBuzz".
    """
    results = []
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if "3" in str(i):
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if "5" in str(i):
            output += "Buzz"
        results.append(output or str(i))
    return results


if __name__ == '__main__':
    for value in fizzbuzz():
        print(value)

print("test")