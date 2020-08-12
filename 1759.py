import sys
import itertools

'''MACROS'''
VOWELS = ['a', 'e', 'i', 'o', 'u']
MIN_LEN_VOWELS = 1
MIN_LEN_CONSONANTS = 2

'''VARIABLES'''
# (3 ≤ L ≤ C ≤ 15)
L, C = 0, 0 
letters = []
consonants = []
vowels = []
LEN_VOWELS = 0
LEN_CONSONANT = 0
count = 0
result = []
'''UTILS'''

def is_vowels(letter):
    return letter in VOWELS

def is_consonants(letter):
    return not is_vowels(letter)

'''INPUT'''

line = sys.stdin.readline().split()
L, C = list(map(int, line))

letters = sys.stdin.readline().split()
vowels = list(filter(is_vowels, letters))
consonants = list(filter(is_consonants, letters))

'''COMPUTE'''

vowels.sort()
consonants.sort()

LEN_VOWELS = len(vowels)
LEN_CONSONANT = len(consonants)

'''OUTPUT'''

LEN_EXTRA = L - MIN_LEN_CONSONANTS - MIN_LEN_VOWELS

for e in range(LEN_EXTRA+1):
    num_of_vowels = MIN_LEN_VOWELS + e
    num_of_consonants = MIN_LEN_CONSONANTS + LEN_EXTRA - e

    # Combination Process
    for vowel_comb in itertools.combinations(vowels, num_of_vowels):
        for consonant_comb in itertools.combinations(consonants, num_of_consonants):
            comb = [*vowel_comb, *consonant_comb]
            comb.sort()
            result.append(comb)
            count += 1

result.sort()

for i in result:
    print("".join(i))


'''
CONDITION: 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
vowels : [] consonants: [] extras: []

CASE 1. Normal Case -> 
                4 6
                a t c i s w

CASE 2. Scarce vowels ->
                4 6
                t c s w b d

CASE 3. Scarce consonants -> 
                4 5
                a e i o u

                4 5
                a e i o c
'''