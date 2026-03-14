import random 
import sys

iterations = int(sys.argv[1])

revived = False
died = False
stabilized = False
def deathsaves(iterations):
    revives = 0
    stables = 0
    deaths = 0
    for _ in range(iterations):
        failures = 0
        successes = 0
        for _ in range(100):
            r = random.randint(1,20)
            print(r)
            if r == 1: failures += 2
            elif r < 10: failures += 1
            elif r == 20:
                revives += 1
                print('Revived!')
                break
            else: successes += 1
            if failures >= 3:
                deaths += 1
                print('Dead!')
                break
            if successes >= 3:
                stables += 1
                print('Stable!')
                break
    print('REVIVES:', revives / iterations)
    print('DEATHS:', deaths / iterations)
    print('STABLES:', stables / iterations)
    return(':]')

print(deathsaves(iterations))