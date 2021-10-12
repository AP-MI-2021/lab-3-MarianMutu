"""
6. Toate numerele sunt divizibile cu k (citit).
Funcția de calcul: get_longest_div_k(lst: list[int], k: int) -> list[int]

13. Toate numerele sunt formate din cifre prime.
Funcția de calcul: get_longest_prime_digits(lst: list[int]) -> list[int]
"""


def get_longest_div_k(lst, k):
    """
    Determina subsecventa cu toate numerele divizibile cu k
    :param lst: int
    :param k: int
    :return: lista ceruta -> int
    """
    rez1 = []  # rezultatul cerut
    temp1 = []  # lista temporara
    for x in lst:
        if x % k == 0:
            temp1.append(x)
        else:
            if len(rez1) < len(temp1):
                rez1 = temp1[:]
            temp1.clear()

    return rez1


def test_get_longest_div_k():
    """Testeaza functia "get_longest_div_k" """
    assert get_longest_div_k([10, 20, 30, 10, 10, 25], 10) == [10, 20, 30, 10, 10]
    assert get_longest_div_k([29, 27, 9, 18, 3, 21, 20], 3) == [27, 9, 18, 3, 21]
    assert get_longest_div_k([], 4) == []


def prime_digits(n):
    """
    Determina daca un nr  are toate cifrele prime
    :param n: int
    :return: true daca n respecta cerinta, false altfel
    """
    not_prime = [0, 1, 4, 6, 8, 9]
    while n != 0:
        for x in not_prime:
            if n % 10 == x:
                return False
        n = n // 10

    return True


def get_longest_prime_digits(lst):
    """
    Determina subsecventa cu toate numerele formate din cifre prime.
    :param lst: int
    :return:  lista ceruta
    """
    rez2 = []  # rezultatul cerut
    temp2 = []  # lista temporara
    for x in lst:
        if prime_digits(x):
            temp2.append(x)
        else:
            if len(temp2) > len(rez2):
                rez2 = temp2[:]
            temp2.clear()

    return rez2


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([22, 23, 37, 82, 21]) == [22, 23, 37]
    assert get_longest_prime_digits([23, 25, 72, 89]) == [23, 25, 72]
    assert get_longest_prime_digits([]) == []


def show_menu():
    print('''
    1. Citire date.
    2. Determinare cea mai lungă subsecvență cu proprietatea 6.
    3. Determinare cea mai lungă subsecvență cu proprietatea 13.
    4. Ieșire.
        ''')


def read_list():
    """
    citeste lista
    :return: lista citita
    """
    lst = []
    n = int(input("Introduceti numarul de elemente din lista"))
    for i in range(n):
        x = int(input("lst[{}]".format(i)))
        lst.append(x)
    return lst


def run_ui():  # main
    """
    interfata cu utilizatorul
    :return:
    """
    lst = []
    while True:
        show_menu()
        cmd = input("Comanda")
        if cmd == '1':
            lst = read_list()
        elif cmd == '2':
            k = int(input("k="))
            print(get_longest_div_k(lst,  k))
        elif cmd == '3':
            print(get_longest_prime_digits(lst))
        elif cmd == '4':
            break
        else:
            print("Comanda invalida")


run_ui()
test_get_longest_prime_digits()
test_get_longest_div_k()
