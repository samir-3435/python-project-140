from brain_games.cli import welcome_user
import random
import prompt

def progression(name):
    print("What number is missing in the progression?")

    contador_correctas = 0

    while contador_correctas < 3:

        start = random.randint(1, 50) # para empezar la progresion
        step = random.randint(1,50) # paso entre numero
        length = 10 # cantidad de numeros de la progresion
        hidden_index = random.randint(0, length - 1) # indice oculto 

        progression = [start + i * step for i in range(length)]

        correct_answer = progression[hidden_index]

        progression[hidden_index] = ".."

        question = " ".join(str(x) for x in progression) # lista a un texto separado por espacios para la pregunta

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == str(correct_answer):
            print("Correct!")
            contador_correctas = contador_correctas + 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

def main():
    name = welcome_user()
    progression(name)

if __name__ == "__main__":
    main()