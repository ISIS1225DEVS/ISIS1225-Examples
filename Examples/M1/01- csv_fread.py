"""
TODO _summary_ of this module/file CSV_FREAD
"""
# lib imports
import csv
import sys
import config as cf
import os

#load pokemon file, reading, looping through the fie
def load_data(N):

        print("\n--- Joining filepath ---")
        # subfolder name
        pokemon_fn = "Pokemon-utf8-sample.csv"
        # join pokemon file path
        pokemon_path = os.path.join(cf.data_dir,
                                pokemon_fn)
        print("Pokemon filepath:", pokemon_path)    
        # reading pokemon file
        print("+++++++ Reading Pokemon file with csv.DictReader +++++++")
        pokemon_file = open(pokemon_path, "r", encoding="utf-8")
        # reader
        pokemons = csv.reader(pokemon_file, delimiter=",")
        # row counter
        i = 0
        pocket_cols = list()
        pokemon_list_values = list()

        # looping through pokemon file
        for mon in pokemons:
            if i == 0:
                # getting pokemon columns
                pocket_cols = mon
            elif i != 0:
                if i%N == 0:
                    pokemon_list_values.append(mon)
            i = i + 1

        # pokemon file details
        print("\n--- Pokemon csv details ---")
        print("Pokemon file size:", i)
        print("Pokemon columns:\n", pocket_cols)
        print("////////////////////////////////////////////////////////////////////////////////////////")
        print("////////////////////////////////////////////////////////////////////////////////////////")

        # close pokemon file
        pokemon_file.close()
        return (pocket_cols,pokemon_list_values)

def print_results(titulos, valores, N):
    i=0
    list_result = list()
    for x in range(0,N):
        pokemon = "" 
        for z in range(0, len(titulos)):
            pokemon +=titulos[z]+ ": "+ valores[x][z]+" "
            list_result.append(pokemon)
        print(pokemon,"\n")

#Method main
if __name__ == "__main__":
    # start main()
    print("==========================================================")
    print("================== csv readfile example ==================")
    print("==========================================================\n")

    print("--- Config ---")
    # OS max field size
    SYS_MAX_SIZE_FIELD = sys.maxsize
    print("OS MAX FIELD SIZE:", SYS_MAX_SIZE_FIELD)

    # current example max field size
    # Higher than OS max field size generates an error!!!
    CUR_MAX_SIZE_FIELD = pow(2, 31) - 1
    print("CURRENT MAX FIELD SIZE:", CUR_MAX_SIZE_FIELD)

    # config field size
    csv.field_size_limit(CUR_MAX_SIZE_FIELD)

    # row counter

    secuencia_a_imprimir = int(input("ingresa la secuencia con la que deseas imprimir los pokemones"))
    pokemon_lists = load_data(secuencia_a_imprimir)
    datos_a_imprimir = int(input("ingresa la cantidad de pokemones que deseas imprimir"))

    print_results(pokemon_lists[0], pokemon_lists[1], datos_a_imprimir)

    
