import math
import random

import prompt

from brain_games.cli import welcome_user


def prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    contador_correctas = 0

    while contador_correctas < 3:
        number = random.randint(1, 100)

        if number < 2:
            correct_answer = "no"
        else:
            correct_answer = "yes"
            for i in range(2, math.isqrt(number) + 1):
                if number % i == 0:
                    correct_answer = "no"
                    break

        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")

        if correct_answer == answer:
            print("Correct!")
            contador_correctas = contador_correctas + 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    name = welcome_user()
    prime(name)


if __name__ == "__main__":
    main()
