import os
import sys
from os import system
from pathlib import Path
from termcolor import colored, cprint


def start_app():
    system('clear')

    name = input(
        colored('\nHola cual es tu nombre ? ',
                'green',
                attrs=['bold'])
    )

    system('clear')

    greeting_welcome = colored(
        f'\n** Hola {name}, Bienvenido a **"Dine Bio"** un asistente de recetas de cocina ***',
        'yellow',
        attrs=['reverse', 'bold', 'dark']
    )

    print('\n')

    print(greeting_welcome)


start_app()


def main_board():
    home = Path.home()
    recipes = []
    recipes_qty = 0
    recipes_directory = Path(home, 'Recetas')
    user_option = 3
    options = {
        '1': 'Ir al menu de recetas',
        '2': 'Finalizar programa'
    }
    option_selected = True

    for recipe in Path(recipes_directory).glob('**/*.txt'):
        recipes.append(recipe)

    recipes_qty = len(recipes)

    print(colored(
        f'\tEn este recetario encontraras recetas de variadas comidas y bebidas, actualmente '
        f'cuenta con {recipes_qty} recetas listas.\n', 'blue', attrs=['reverse', 'bold']))

    for value, option in options.items():
        print(colored(f'[{value}] {option}', 'yellow'))

    while user_option > 2 or user_option < 0:
        user_option = int(
            input(colored('\nElige una opcion: ', 'blue', attrs=['bold'])))
        if user_option == 1:
            option_selected = True
        elif user_option == 2:
            option_selected = False
            print(colored('\nMuy bien, Bye!', 'red', attrs=['reverse']))
            break
        else:
            print(colored('Esa no es una opcion correcta', 'red', attrs=['reverse']))

    return option_selected


resultado = main_board()


def options_board(option):
    interactive_option = {
        '1': 'Leer Receta',
        '2': 'Crear Receta',
        '3': 'Crear Categoria',
        '4': 'Eliminar Receta',
        '5': 'Eliminar Categoria',
        '6': 'Finalizar Programa'
    }

    user_option = 7

    system('clear')
    if option == True:
        print(colored(
            '\n** Dino Bio **', 'yellow', attrs=['bold', 'reverse']
        ))
        print(colored('Selecciona una opcion del menu: \n', 'blue', attrs=['reverse']))
        for key, recipe in interactive_option.items():
            print(f'[{key}] {recipe}')

        while user_option not in range(1, 7):
            user_option = int(input(colored(
                f'\nQue deseas hacer con "Dino Bio": ',
                'green',
            )))

            match user_option:
                case 1:
                    return 'leer_receta'
                case 2:
                    return 'crear_receta'
                case 3:
                    return 'crear_categoria'
                case 4:
                    return 'eliminar_receta'
                case 5:
                    return 'eliminar_categoria'
                case 6:
                    return 'finalizar_programa'
                case default:
                    print('noe es una opcion')
    else:
        print('Adios')


result_tablero = options_board(resultado)


def read_recipe():
    home = Path.home()
    recipes_directory = Path(home, 'Recetas')
    print(recipes_directory)
    cateories = []
    menu = {}

    for category in Path.iterdir(recipes_directory):
        if category.is_dir():
            cateories.append(str(category).replace('/', ' ').split().pop())

    midic = {+= 1:x for x in cateories}

    print(midic)


    print(cateories)


def create_recipe():
    print('Crear receta')


def create_category():
    print('Crear categoria')


def delete_recipe():
    print('Eliminar Receta')


def delete_category():
    print('Eliminar Categoria')


match result_tablero:
    case 'leer_receta':
        read_recipe()
    case 'crear_receta':
        create_recipe()
    case 'crear_categoria':
        create_category()
    case 'eliminar_receta':
        delete_recipe()
    case 'eliminar_categoria':
        delete_category()
    case 'finalizar_programa':
        print('adios perrito')
