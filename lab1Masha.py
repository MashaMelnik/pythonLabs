# Домашнее задание 1, вариант 2
def seasonDefinition(n):
    mapOfSeasons = {"1": "зима",
                    "2": "зима",
                    "3": "весна",
                    "4": "весна",
                    "5": "весна",
                    "6": "лето",
                    "7": "лето",
                    "8": "лето",
                    "9": "осень",
                    "10": "осень",
                    "11": "осень",
                    "12": "зима"}
    print(mapOfSeasons[n])


seasonDefinition(input())

#Домашнее задание 2
assert (seasonDefinition(1), "зима")
assert (seasonDefinition(2), "зима")
assert (seasonDefinition(9), "осень")
assert (seasonDefinition(6), "лето")
