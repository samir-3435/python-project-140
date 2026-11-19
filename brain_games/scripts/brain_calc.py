import random
from brain_games.cli import welcome_user

def calcul(name):
    operaciones = ["suma", "resta", "multiplicación"]  # lista para guardar las expresiones aleatorias

    contador_correctas = 0  # contador para saber la cantidad de respuestas correctas del usuario

    while contador_correctas < 3:
        operacion_elegida = random.choice(operaciones)  # elegir una operación de manera aleatoria

        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)  # elegir dos numeros aleatorios para la operación

        if operacion_elegida == "suma":
            print("What is the result of the expression?")

            question = int(input(f"Question: {number_1} + {number_2} "))

            print(f"Your answer: {question}")

            if question == (number_1 + number_2):
                print("Correct!")  # exito
                contador_correctas = contador_correctas + 1
            else:
                print(f"'{question}' is wrong answer ;(. Correct answer was '{number_1 + number_2}'")  # fracaso
                print(f"Let's try again, {name}")
                return

        if operacion_elegida == "resta":
                    print("What is the result of the expression?")
        
                    question = int(input(f"Question: {number_1} - {number_2} "))
        
                    print(f"Your answer: {question}")
        
                    if question == (number_1 - number_2):
                        print("Correct!")  # exito
                        contador_correctas = contador_correctas + 1
                    else:
                        print(f"'{question}' is wrong answer ;(. Correct answer was '{number_1 - number_2}'")  # fracaso
                        print(f"Let's try again, {name}")
                        return

        if operacion_elegida == "multiplicación":
                    print("What is the result of the expression?")
        
                    question = int(input(f"Question: {number_1} * {number_2} "))
        
                    print(f"Your answer: {question}")
        
                    if question == (number_1 * number_2):
                        print("Correct!")  # exito
                        contador_correctas = contador_correctas + 1
                    else:
                        print(f"'{question}' is wrong answer ;(. Correct answer was '{number_1 * number_2}'")  # fracaso
                        print(f"Let's try again, {name}")
                        return

def main():
     name = welcome_user()
     calcul(name)

if __name__ == "__main__":
     main()