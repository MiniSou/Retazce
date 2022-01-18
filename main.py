# Funkcia na zistenie počtu požadovaných súborov
def pocet_suborov():
    while True:
        cislo = input("Zadajte počet súborov: ")
        try:
            return abs(int(cislo))
        except ValueError:
            print("Nezadali ste cele číslo!")


vstup = []
cislo_slova = 0
# Načítanie slov zo súboru basnicka.txt
with open("basnicka.txt", encoding="utf-8") as subor:
    for slovo in subor:
        vstup += slovo.split()
# Vypisovanie slov do súborov
for i in range(pocet_suborov()):
    cislo_slova += 1
    if cislo_slova == len(vstup):
        cislo_slova -= len(vstup)
    with open(f"""slovo{i + 1}""", mode="w") as subor:
        print(vstup[cislo_slova - 1], file=subor)
