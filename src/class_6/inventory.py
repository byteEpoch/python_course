# Mini inventario de tienda en python.
import json
import sys


def dump_inventory(inventory):
    with open('inventory.json', 'w') as f:
        f.write(json.dumps({'items': inventory}))


def load_inventory():
    try:
        with open('inventory.json') as f:
            return json.loads(f.read())['items']
    except FileNotFoundError:
        return []


def create_product(inventory, name=None):
    if name is None:
        name = input('Introduce el nombre del producto: ').lower()
    amount = input('Introduce el número de artículos: ')
    for product in inventory:
        if name == product['name']:
            print('El producto ya existe')
            break
    else:
        inventory.append({'name': name, 'amount': amount})
        print('Producto guardado correctamente.')


def search_product(inventory):
    name = input('Introduce el nombre del producto a buscar: ').lower()
    for product in inventory:
        if name == product['name']:
            print(f'El producto {name} tiene {product["amount"]} unidades.')
            break
    else:
        print('El producto no existe.')
        while True:
            option = input('Desea crear el producto? [s/n]: ')
            if option.lower() == 's':
                create_product(inventory, name=name)
                break
            elif option.lower() == 'n':
                break
            else:
                print('Opción invalida.')


def list_products(inventory):
    for product in inventory:
        print(f'El producto {product["name"]} tiene {product["amount"]} unidades.')


def print_exit_submenu():
    print('+-----------------------+')
    print('| 1. Guardar y salir    |')
    print('| 2. Salir sin guardar  |')
    print('| 3. Cancelar           |')
    print('+-----------------------+')


def exit_submenu(inventory):
    while True:
        print_exit_submenu()
        option = input('Introduce una opción [1-3]: ')
        if option == '1':
            dump_inventory(inventory)
            sys.exit()
        elif option == '2':
            sys.exit()
        elif option == '3':
            break
        else:
            print('Opción no valida.')


def print_menu():
    print('+---------------------+')
    print('| 1. Crear producto   |')
    print('| 2. Buscar producto  |')
    print('| 3. Listar productos |')
    print('| 4. Salir            |')
    print('+---------------------+')


def menu():
    inventory = load_inventory()
    while True:
        print_menu()
        option = input('Introduce una opción [1-4]: ')
        if option == '1':
            create_product(inventory)
        elif option == '2':
            search_product(inventory)
        elif option == '3':
            list_products(inventory)
        elif option == '4':
            exit_submenu(inventory)
        else:
            print('Opción no valida.')


def main():
    menu()


if __name__ == '__main__':
    main()
