import math
import sys

word = input()
most_powerful_word = ''
max_value = -sys.maxsize
# ll = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

while word != "End of words":
    word_power = 0
    for letter in word:
        word_power += ord(letter)

    if word[0] in 'aeiouyAEIOUY':
        # if word[0] in ll:
        word_power *= len(word)
    else:
        word_power = math.floor(word_power / len(word))

    if word_power > max_value:
        most_powerful_word = word
        max_value = word_power

    word = input()
print(f"The most powerful word is {most_powerful_word} - {max_value:.0f}")
