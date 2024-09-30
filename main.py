#### Imports et définition des variables globales
"""f"""
import csv
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r', encoding='utf8') as f:
        r=csv.reader(f, delimiter=';')
        return [ list(map(int ,ligne)) for ligne in r]
def get_list_k(data, k):
    """f"""
    l = data
    return l[k]

def get_first(l):
    """f"""
    if not l:
        raise ValueError("La liste est vide.")
    return l[0]

def get_last(l):
    """f"""
    if not l:
        raise ValueError("La liste est vide.")
    return l[-1]

def get_max(l):
    """f"""
    if not l:
        raise ValueError("La liste est vide.")
    return max(l)

def get_min(l):
    """f"""
    if not l:
        raise ValueError("La liste est vide.")
    return min(l)

def get_sum(l):
    """f"""
    if not l:
        raise ValueError("La liste est vide.")
    return sum(l)


#### Fonction principale


def main():
    """f"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
