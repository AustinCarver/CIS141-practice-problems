'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
'''
input = input("Give me a string.")
def count_vowels(input):
    vowels = 0
    for char in input:
        if char == 'a':
            vowels += 1
        elif char == 'e':
            vowels += 1
        elif char == 'i':
            vowels += 1
        elif char == 'o':
            vowels += 1
        elif char == 'u':
            vowels += 1
        elif char == 'A':
            vowels += 1
        elif char == 'E':
            vowels += 1
        elif char == 'I':
            vowels += 1
        elif char == 'O':
            vowels += 1
        elif char == 'U':
            vowels += 1
    return vowels
print("The number of vowels in", input, "is", count_vowels(input))
'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
'''
def is_palidrome(s):
    lower = s.lower()
    flip = lower[::-1]
    return lower == flip
print(is_palidrome("radar"))
print(is_palidrome("Austin"))
print(is_palidrome("Kayak"))
'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
'''
def type_advantage(attacker, defender):
    if (attacker, defender) == ("Water", "Fire"):
        return "Super Effective"
    elif (attacker, defender) == ("Fire", "Water"):
        return "Not Very Effective"
    elif (attacker, defender) == ("Electric", "Grass"):
        return "Neutral"
print(type_advantage("Electric", "Grass"))
print(type_advantage("Fire", "Water"))
print(type_advantage("Water", "Fire"))
'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
'''
def ferry_fare(age, vehicle):
    if age >= 65:
       if  vehicle == "yes":
           fare = "$15"
       elif vehicle == "no":
           fare = "$5"
    elif age <= 18:
        fare = "Free"
    else:
        if  vehicle == "yes":
           fare = "$20"
        elif vehicle == "no":
            fare = "$10"
    return fare
print(ferry_fare(31, "no"))
print(ferry_fare(68, "no"))
print(ferry_fare(26, "yes"))
print(ferry_fare(70, "yes"))
print(ferry_fare(14, "no"))
'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''
def level_up(experience):
    if experience >= 200:
        return "Level 3"
    elif experience <= 99:
        return "Level 1"
    else:
        return "Level 2"
print(level_up(25))
print(level_up(151))
print(level_up(204))
