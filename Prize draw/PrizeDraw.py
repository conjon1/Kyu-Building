import re


def  rank(st, we, n):
    if not st:
        return "No participants"

    name = re.findall(r'[A-Za-z]+', st)
    
    if len(name) < n:
        return "Not enough participants"

    winning_numbers = {}
    for st, we in zip(name, we):
        som = sum(ord(char.upper()) - ord('A') + 1 for char in st) + len(st)
        winning_numbers[st] = som * we

    sorted_name = sorted(name, key=lambda x: (winning_numbers[x], x))

    return sorted_name[n-1]



    


