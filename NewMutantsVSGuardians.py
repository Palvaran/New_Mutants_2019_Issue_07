import random
mutants = ['Mirage', 'Smasher', 'Mondo', 'Chamber', 'Wolfsbane', 'Karma']
guardians = ['Manta', 'Earthquake', 'Quasar', 'Starbolt', 'Flashfire', 'Hussar']
round = 1
print('ROUND ONE:')
print('')
print('Mutants:')
print(*mutants, sep =", ")
print('Guardians:')
print(*guardians, sep =", ")
print('')
while len(mutants) > 0 and len(guardians) > 0:
    print('')
    print('Fight ' + str(round))
    print('')
    print(str(len(mutants)) + ' Mutants left!')
    print(*mutants, sep =", ")
    print(str(len(guardians)) + ' Guardians left!')
    print(*guardians, sep =", ")
    print('')
    print('----FIGHT----')
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
    round += 1
    print('')
if len(mutants) > 0:
    print('The Mutants are victorius! Congratulations to ' + ', '.join(mutants) + '!') 
else:
    print('The Guardians are victorius! Congratulations to ' + ', '.join(guardians) + '!')   

