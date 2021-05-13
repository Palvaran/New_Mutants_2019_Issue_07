import random

mutants = ['Mirage', 'Smasher', 'Mondo', 'Chamber', 'Wolfsbane', 'Karma']
mutant_reinforcements = ['Cannonball', 'Sunspot', 'Magik']
guardians = ['Manta', 'Earthquake', 'Quasar', 'Starbolt', 'Flashfire', 'Hussar']
guardian_reinforcements = ['Mentor', 'Oracle', 'Gladiator']
wins_mutants = 0
wins_guardians = 0

def roundone():
    print('New Mutants 2019, Issue 07')
    print('')
    print('Normally, this fight would have gone on for seventeen glorious pages. Women and men would have triumphed, male and female aliens would have fallen. Maybe vice versa. Maybe not. But now there is only one way to tell...and all you need is a pair of dice.')
    print('')
    print('LETS GET IT ON!')
    print('')
    print('ROUND ONE:')
    print('Roll one die each to choose a combatant from a side - one mutant, one guardian')
    print('')
    rosters()
    print('')
    print('Then roll for damage for each character. Whoever rolls the highest number wins, and the lower number is eliminated. If both numbers are the same, BOTH characters are eliminated. Play until one team is eliminated.')
    print('')

def roundtwo():
    print('ROUND TWO:')    
    print('The eliminated team is then allowed to introduce their final three players. Play until one team is, again, eliminated. If the winning team lost the first round, then the losing team can use their final three players. Then, again, play until one team is eliminated.')
    print('')
    print('Mutants')
    print(*mutant_reinforcements, sep =", ")
    print('Guardians')
    print(*guardian_reinforcements, sep =", ")
    print('')

def rosters():
    print(str(len(mutants)) + ' Mutants')
    print(*mutants, sep =", ")
    print(str(len(guardians)) + ' Guardians')
    print(*guardians, sep =", ")

roundone()
roundtwo()
while wins_mutants or wins_guardians < 3:
    while len(mutants) > 0 and len(guardians) > 0:
        print(str(len(mutants)) + ' mutants left vs. ' + str(len(guardians)) + ' guardians left.')
        mutant = (random.choice(mutants))
        guardian =(random.choice(guardians))
        dice_mutant = random.randint(2,12)
        dice_guardian = random.randint(2,12)
        if (dice_mutant > dice_guardian):
            print ((mutant) + ' wins! ' + (guardian) + ' loses!')
            guardians.remove(guardian)
        elif (dice_mutant < dice_guardian):
            print ((guardian) + ' wins! ' + (mutant) + ' loses!')
            mutants.remove(mutant)
        else:
            print ('Its a double knockout!')
            mutants.remove(mutant)
            guardians.remove(guardian)
    if len(mutants) > 0 and wins_mutants < 1:
        wins_mutants += 1
        guardians.extend(guardian_reinforcements)
        print('The Mutants are victorius! ' + str(wins_mutants) + ' wins!')
        print('...but Guardian reinforcements have arrived!')
    elif len(guardians) > 0 and wins_guardians < 1:
        wins_guardians += 1
        mutants.extend(mutant_reinforcements)
        print('The Guardians are victorius! ' + str(wins_guardians) + ' wins!')
        print('...but New Mutant reinforcements have arrived!')
    elif len(mutants) > 0 and wins_mutants < 2:
        wins_mutants += 1
    elif len(guardians) > 0 and wins_guardians < 2:
        wins_guardians += 1
    else:
        break
print('')
print('That is ' + str(wins_mutants) + ' wins for the Mutants.')
print('That is ' + str(wins_guardians) + ' wins for the Guardians.')
if wins_mutants > wins_guardians:
    print('Congratulations to the New Mutants for winning the contest with ' + str(wins_mutants) + ' wins!')
else:
    print('Congratulations to the Guardians for winning the content with ' + str(wins_guardians) + ' wins!')
print('')
print('Final rosters')
rosters()
