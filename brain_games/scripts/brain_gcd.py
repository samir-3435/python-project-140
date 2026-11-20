import math
import random
import prompt
from brain_games.cli import welcome_user


def find_gcd(name):

    print("Find the greatest common divisor of given numbers.")

    contador_correctas = 0  # contador para correctas

    while contador_correctas < 3:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)  # dos numeros aleatorios de 1 a 100

        maximo_comun_divisor = math.gcd(number_1, number_2)

        print(f"Question: {number_1} {number_2}")
        answer = prompt.string("Your answer: ")

        if answer == str(maximo_comun_divisor):
            print("Correct!")
            contador_correctas = contador_correctas + 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{maximo_comun_divisor}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    name = welcome_user()
    find_gcd(name)


if __name__ == "__main__":
    main()
