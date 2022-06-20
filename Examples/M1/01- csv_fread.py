"""
TODO _summary_ of this module/file CSV_FREAD
"""
# lib imports
import csv
import sys
import config as cf
import os

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

print("\n--- Joining filepath ---")
# subfolder name
file_folder = "Samples"
pokemon_fn = "Pokemon-utf8-sample.csv"
# join pokemon file path
pokemon_path = os.path.join(cf.data_dir,
                            file_folder,
                            pokemon_fn)
print("Pokemon filepath:", pokemon_path)

# reading pokemon file
print("+++++++ Reading Pokemon file with csv.DictReader +++++++")
pokemon_file = open(pokemon_path, "r", encoding="utf-8")
# dict reader
pokemons = csv.DictReader(pokemon_file, delimiter=",")
# row counter
i = 0
N = 200

# looping through pokemon file
for mon in pokemons:
    if i % N == 0.0:
        # printing each N th row
        print("i:", i,
              "type:", type(mon), "\n"
              "data:", mon)
    i = i + 1

# pokemon file details
print("\n--- Pokemon csv details ---")
print("Pokemon file size:", i)
print("Pokemon fieldnames:\n", pokemons.fieldnames)

# close pokemon file
pokemon_file.close()

# reading pokemon file
print("+++++++ Reading Pokemon file with csv.DictReader +++++++")
pokemon_file = open(pokemon_path, "r", encoding="utf-8")
# reader
pokemons = csv.reader(pokemon_file, delimiter=",")
# row counter
i = 0
pocket_cols = list()

# looping through pokemon file
for mon in pokemons:
    if i == 0:
        # getting pokemon columns
        pocket_cols = mon
    elif i % N == 0.0:
        # printing each N th row
        print("i:", i,
              "type:", type(mon), "\n"
              "data:", mon)
    i = i + 1

# pokemon file details
print("\n--- Pokemon csv details ---")
print("Pokemon file size:", i)
print("Pokemon columns:\n", pocket_cols)

# close pokemon file
pokemon_file.close()
