import prompt


def welcome_user():

    print("Welcome to the Brain Games!")  # solo da un mensaje de bienvenida

    name = prompt.string("May I have your name? ")  # preguntar el nombre

    print(f"Hello, {name}!")  # saludar

    return name

