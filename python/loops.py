planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print(product)

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
product

for i in range(5):
    print("Doing important work. i =", i)

i = 0
while i < 10:
    print(i, end=' ')
    i += 1

squares = [n**2 for n in range(10)]
squares

squares = []
for n in range(10):
    squares.append(n**2)
squares

short_planets = [planet for planet in planets if len(planet) < 6]
short_planets

# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
loud_short_planets

[
    planet.upper() + '!' 
    for planet in planets 
    if len(planet) < 6
]

[32 for planet in planets]

def count_negatives(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])