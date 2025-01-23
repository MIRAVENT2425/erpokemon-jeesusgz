from Pokemon import addPokemon, showPokemonList


def main():
    while True:
        print("Menú Principal")
        print("1. Añadir Pokémon")
        print("4. Ver lista de Pokémon")
        print("5. Salir")

        choice = input("Elige una opción:")

        if choice == "1":
            addPokemon()
        elif choice == "4":
            showPokemonList()
        elif choice == "5":
            print("Hasta luego!!!")
            break
        else:
            print("Opción inválida. Por favor selecciona una opción correcta")

if __name__ == "__main__":
    main()