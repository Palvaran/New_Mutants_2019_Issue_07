import random
mutants = ['Mirage', 'Smasher', 'Mondo', 'Chamber', 'Wolfsbane', 'Karma']
mutant_survivors=len(mutants)
guardians = ['Manta', 'Earthquake', 'Quasar', 'Starbolt', 'Flashfire', 'Hussar']
guardian_survivors=len(guardians)
print('ROUND ONE:')
print('')
print('Mutants:')
print(*mutants, sep =", ")
print('Guardians:')
print(*guardians, sep =", ")
print('')
while mutant_survivors > 0 or guardian_survivors > 0:
    print('')
    mutant_survivors=len(mutants)
    print(str(mutant_survivors) + ' Mutants left!')
    print(*mutants, sep =", ")
    guardian_survivors=len(guardians)
    print(str(guardian_survivors) + ' Guardians left!')
    print(*guardians, sep =", ")
    mutant1 = (random.choice(mutants))
    die1 = random.randint(1,6)
    print(mutant1 + ' rolled a ' + str(die1))
    guardian1 =(random.choice(guardians))
    die2 = random.randint(1,6)
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
