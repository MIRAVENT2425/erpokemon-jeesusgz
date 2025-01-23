from PokemonType import PokemonType


class Pokemon:
    def __init__(self, id, name, type, height, weight, abilities):
        self.id = id
        self.name = name
        self.type = type
        self.height = height
        self.weight = weight
        self.abilities = abilities

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Type: {self.type.value}\n"
                f"Height: {self.height}\n"
                f"Weight: {self.weight}\n"
                f"Abilities: {', '.join(self.abilities)}\n")

    pokemonList = []

def addPokemon():
    print("Introduce los detalles del Pokémon")
    id = input("ID: ")
    name = input("Nombre: ")

    print("Elige el tipo de Pokémon")
    # Muestra los tipos de Pokémon disponibles
    for typeOption in PokemonType:
        print(f"{typeOption.value}")

    # Valida que el tipo sea válido
    typeInput = input("Tipo: ")
    while typeInput not in PokemonType._value2member_map_:
        print("Tipo inválido. Por favor elige una de los opciones válidas")
        typeInput = input("Tipo: ")
    # asigna el tipo al Pokémon
    type = PokemonType(typeInput)

    height = float(input("Altura (metros): "))
    weight = float(input("Peso (Kilos): "))

    # Ingresa las habilidades y la divide en una lista cuando está separadas por ","
    abilities = input("Abilidades (separadas por comas): ").split(",")

    # elimina los espacios entre las abilidades
    abilities = [ability.strip() for ability in abilities]

    # crea un objeto de Pokémon
    pokemon = Pokemon(id, name, type, height, weight, abilities)
    # se añade a la lista
    Pokemon.pokemonList.append(pokemon)


def showPokemonList():
    if not Pokemon.pokemonList:
        print("\nNo hay pokemon en la lista")
    else:
        print("\nLista de pokemon")
        for pokemon in Pokemon.pokemonList:
            print(pokemon)
            # Imprime 20 guiones
            print("-" * 20)
