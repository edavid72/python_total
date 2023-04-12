import os
from os import system
from pathlib import Path
from termcolor import colored, cprint

directory_path = Path(Path.home(), 'Recetas')


def count_recipes(route):
    counter = 0

    for recipe in Path(directory_path).glob('**/*.txt'):
        counter += 1
    return counter


# Show Start Menu
def start_menu():
    system('clear')
    # Welcome Message
    print('\n')
    print(colored('*' * 50, 'light_yellow', attrs=['reverse']))
    print(
        colored(
            f'***Dino Bio Administrador De Recetas De Cocina ***',
            'light_yellow',
            attrs=['reverse', ]
        )
    )
    print(colored('*' * 50, 'light_yellow', attrs=['reverse']))
    print('\n')

    # Info about Recipes in location
    print(colored(
        f'Las recetas estan alojadas en "{directory_path}"',
        'light_blue',
        attrs=['reverse']
    ))
    print(colored(
        f'Total Recetas: {count_recipes(directory_path)}',
        'light_cyan',
        attrs=['blink']
    ))

    user_menu_select = 'x'

    while not user_menu_select.isnumeric() or int(user_menu_select) not in range(1, 7):
        print(colored('\nElige una opcion', 'light_blue'))
        print(colored(
            '''
            [1] - Leer receta
            [2] - Crear receta nueva
            [3] - Crear categoria nueva
            [4] - Eliminar receta
            [5] - Eliminar categoria
            [6] - Salir
            ''',
            'light_yellow'
        ))
        user_menu_select = input(colored('Aqui: ', 'light_blue'))

    return int(user_menu_select)


def show_categories(route):
    system('clear')
    # Welcome Message
    print('\n')
    print(colored('*' * 50, 'light_yellow', attrs=['reverse']))
    print(
        colored(
            f'***Dino Bio Administrador De Recetas De Cocina ***',
            'light_yellow',
            attrs=['reverse', ]
        )
    )
    print(colored('*' * 50, 'light_yellow', attrs=['reverse']))
    print('\n')

    print(colored('\nCategorias\n', 'light_blue', attrs=['blink']))
    category_route = Path(route)
    category_list = []
    category_container = 1

    for category in category_route.iterdir():
        category_folder = str(category.name)
        print(colored(f'[{category_container}] - {category_folder}', 'light_yellow'))
        category_list.append(category)
        category_container += 1

    return category_list


def choose_category(list):
    correct_choice = 'x'

    while not correct_choice.isnumeric() or int(correct_choice) not in range(1, len(list) + 1):
        correct_choice = input(colored('\nElije una categoria: ', 'light_blue'))

    return list[int(correct_choice) - 1]


def show_recipes(route):
    system('clear')
    # Welcome Message
    print('\n')
    print(colored('*' * 50, 'light_yellow', attrs=['reverse']))
    print(
        colored(
            f'***Dino Bio Administrador De Recetas De Cocina ***',
            'light_yellow',
            attrs=['reverse', ]
        )
    )
    print(colored('*' * 50, 'light_yellow', attrs=['reverse']))
    print('\n')

    print(colored('\nRecetas \n', 'light_blue', attrs=['blink']))
    recipe_route = Path(route)
    recipe_list = []
    recipe_container = 1

    for recipe in recipe_route.glob('*.txt'):
        recipe_str = str(recipe.name)
        print(colored(f'[{recipe_container}] - {recipe_str}', 'light_yellow'))
        recipe_list.append(recipe)
        recipe_container += 1

    return recipe_list


def choose_recipe(list):
    correct_choice = 'x'

    while not correct_choice.isnumeric() or int(correct_choice) not in range(1, len(list) + 1):
        correct_choice = input(colored('\nElige una receta: ', 'light_blue'))

    return list[int(correct_choice) - 1]


def read_recipe(recipe):
    system('clear')
    # Welcome Message
    print('\n')
    print(colored('*' * 50, 'light_yellow', attrs=['reverse']))
    print(
        colored(
            f'***Dino Bio Administrador De Recetas De Cocina ***',
            'light_yellow',
            attrs=['reverse', ]
        )
    )
    print(colored('*' * 50, 'light_yellow', attrs=['reverse']))
    print('\n')

    print(colored(
        f'Contenido de {recipe.name}:\n',
        'light_green'
    ))
    print(colored('Inicio', 'light_yellow'))
    print(Path.read_text(recipe))
    print(colored('Fin', 'light_yellow'))


def create_new_recipe(route):
    system('clear')
    # Welcome Message
    print('\n')
    print(colored('*' * 50, 'light_yellow', attrs=['reverse']))
    print(
        colored(
            f'***Dino Bio Administrador De Recetas De Cocina ***',
            'light_yellow',
            attrs=['reverse', ]
        )
    )
    print(colored('*' * 50, 'light_yellow', attrs=['reverse']))
    print('\n')
    already_exists = False

    while not already_exists:
        print(colored(
            '\nEscribe el nombre de tu nueva receta ',
            'light_blue'
        ))
        recipe_name = input(
            colored('\nAqui: ', 'light_yellow')
        ) + '.txt'
        print(f'Escribe el contenido de {recipe_name}: ')
        recipe_content = input(colored(
            '\nAqui: ',
            'light_yellow'
        ))
        new_recipe_created = Path(route, recipe_name)

        if not os.path.exists(new_recipe_created):
            Path.write_text(new_recipe_created, recipe_content)
            system('clear')
            print(colored(
                f'\n \nTu receta "{recipe_name}" ha sido creada con exito',
                'cyan'
            ))
            pass
            already_exists = True
        else:
            print(colored(
                'Lo siento, esta receta ya existe, intenta con otro nombre.',
                'light_red'
            ))


def create_new_category(route):
    system('clear')
    # Welcome Message
    print('\n')
    print(colored('*' * 50, 'light_yellow', attrs=['reverse']))
    print(
        colored(
            f'***Dino Bio Administrador De Recetas De Cocina ***',
            'light_yellow',
            attrs=['reverse', ]
        )
    )
    print(colored('*' * 50, 'light_yellow', attrs=['reverse']))
    print('\n')

    already_exists = False

    while not already_exists:
        print(colored(
            f'\nEscribe el nombre de tu nueva categoria\n',
            'light_blue'
        ))
        category_name = input(colored(
            'Aqui:',
            'light_yellow'
        ))
        new_category_created = Path(route, category_name)

        if not os.path.exists(new_category_created):
            Path.mkdir(new_category_created)
            system('clear')
            print(colored(
                f'\n \nTu categoria "{category_name}" ha sido creada con exito',
                'light_cyan'
            ))
            pass
            already_exists = True
        else:
            print(colored(
                'Lo siento, esta categoria ya existe, intenta con otro nombre.',
                'light_red'
            ))


def delete_recipe(recipe):
    sure = 'n'

    sure = input('Estas seguro de eliminar esta receta ? ( y/n ): ').lower()

    if sure == 'y':
        Path(recipe).unlink()
        print(colored(
            f'La receta {recipe.name} fue eliminada con exito',
            'light_red'
        ))
    else:
        pass


def delete_category(category):
    sure = 'n'

    sure = input('Estas seguro de eliminar esta categoria ? ( y/n ): ').lower()

    if sure == 'y':
        Path(category).rmdir()
        print(colored(
            f'La receta {category.name} fue eliminada con exito',
            'light_red'
        ))
    else:
        pass


def back_to_home():
    choice_return = 'x'

    while choice_return.lower() != 'v':
        choice_return = input(colored(
            f'\nPresione "V" para volver al menu inicio: ',
            'light_blue'
        ))


close_app = False

while not close_app:

    menu = start_menu()

    match menu:
        case 1:
            my_categories = show_categories(directory_path)
            my_category = choose_category(my_categories)
            my_recipes = show_recipes(my_category)
            if len(my_recipes) == 0:
                print('aqui no hay nada')
            else:
                my_recipe = choose_recipe(my_recipes)
                read_recipe(my_recipe)
            back_to_home()
        case 2:
            my_categories = show_categories(directory_path)
            my_category = choose_category(my_categories)
            new_recipe = create_new_recipe(my_category)
            back_to_home()
        case 3:
            new_category = create_new_category(directory_path)
            back_to_home()
        case 4:
            my_categories = show_categories(directory_path)
            my_category = choose_category(my_categories)
            my_recipes = show_recipes(my_category)
            my_recipe = choose_recipe(my_recipes)
            delete_my_recipe = delete_recipe(my_recipe)
            back_to_home()
        case 5:
            my_categories = show_categories(directory_path)
            my_category = choose_category(my_categories)
            delete_my_category = delete_category(my_category)
            back_to_home()
        case 6:
            close_app = True
