import random
mutants = ['Mirage', 'Smasher', 'Mondo', 'Chamber', 'Wolfsbane', 'Karma']
mutant_survivors=len(mutants)
guardians = ['Manta', 'Earthquake', 'Quasar', 'Starbolt', 'Flashfire', 'Hussar']
guardian_survivors=len(guardians)
die1 = random.randint(1,6)
die2 = random.randint(1,6)
print('ROUND ONE:')
print('')
print('Mutants:')
print(*mutants, sep =", ")
print('Guardians:')
print(*guardians, sep =", ")
print('')
mutant1 = (random.choice(mutants))
print(mutant1 + ' rolled a ' + str(die1))
guardian1 =(random.choice(guardians))
print(guardian1 + ' rolled a ' + str(die2))
if (die1 > die2):
    print (mutant1 + ' wins! ' + (guardian1) + ' loses!')
    guardians.remove(guardian1)
elif (die1 < die2):
    print (guardian1 + ' wins! ' + (mutant1) + ' loses!')
    mutants.remove(mutant1)
else:
    print ('Its a double knockout!')
    mutants.remove(mutant1)
    guardians.remove(guardian1)
print('')
mutant_survivors=len(mutants)
print(str(mutant_survivors) + ' Mutants left!')
print(*mutants, sep =", ")
guardian_survivors=len(guardians)
print(str(guardian_survivors) + ' Guardians left!')
print(*guardians, sep =", ")