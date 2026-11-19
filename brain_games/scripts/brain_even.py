import random

import prompt

from brain_games.cli import welcome_user  # función para saludar al usuario


def par_o_impar(name):  # función para saber si es par o impar

    contador_correctas = 0  # contador para guardar la cantidad de respuestas correctas

    print('Answer "yes" if the number is even, otherwise answer "no".')  # imprimir las instrucciones del juego

    while contador_correctas < 3:

        question = random.randint(1, 100)  # asignar un numero entero aleatorio
        
        print(f"Question: {question}")  # mostrar el numero aleatorio del 1 al 100 en este caso

        answer = prompt.string("Your answer: ")  # preguntar por la respuesta

        if question % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"  # saber cual es la respuesta correcta para comparar con la del usuario

        if answer == correct_answer:
            print("Correct!")  # acierto
            contador_correctas = contador_correctas + 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    name = welcome_user()
    par_o_impar(name)


if __name__ == "__main__":
    main()