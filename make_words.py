import math
from sortedcontainers import SortedList
from collections import Counter

pi = math.pi

def to_letter(ls):
    unique_spaces = list(SortedList(set(ls)))
    if len(unique_spaces) == 1:
        return ['a'] * len(ls)
    letters = []
    if len(unique_spaces) == 2:
        for space in ls:
            if space == unique_spaces[0]:
                letters.append('a')
            elif space == unique_spaces[1]:
                letters.append('b')
    if len(unique_spaces) == 3:
        for space in ls:
            if space == unique_spaces[0]:
                letters.append('a')
            elif space == unique_spaces[1]:
                letters.append('b')
            elif space == unique_spaces[2]:
                letters.append('c')
    return letters

def generate_words(alpha, n):
    circle = SortedList()
    for k in range (-n, n + 1):
        prod = k * alpha
        circle.add(prod - math.floor(prod)) # fractional part of k * alpha
    spacings = [circle[i] - circle[i - 1] for i in range(1, len(circle))] # differences
    spacings.append(1 - circle[-1]) # looped around spacing
    # print(spacings) # explicit values
    spacings = [round(i, 10) for i in spacings]
    # print(spacings) # rounded values
    letters = to_letter(spacings)
    if len(spacings) != len(letters):
        raise ValueError('spacings and letters have different lengths')
    # print('{} and {}'.format(len(spacings), len(letters))) # precision check
    print(letters)
    str = ''
    for i in letters:
        str += i
    print(str)
    words = []
    for i in range(len(letters)):
        for j in range(len(letters)):
            if i <= j:
                words.append(''.join(letters[i:(j + 1)]))
            else:
                words.append(''.join(letters[i:]) + ''.join(letters[:(j + 1)]))
    # print(words)
    # words.sort()

    # sorts by length then by alphabet:
    words.sort()
    words = sorted(words, key=len)

    counts = Counter(words)
    # print(words)
    counts = sorted(counts.items())
    # print(counts)

def longest_run(alpha, n):
    circle = SortedList()
    for k in range (-n, n + 1):
        prod = k * alpha
        circle.add(prod - math.floor(prod)) # fractional part of k * alpha
    spacings = [circle[i] - circle[i - 1] for i in range(1, len(circle))] # differences
    spacings.append(1 - circle[-1]) # looped around spacing
    # print(spacings) # explicit values
    spacings = [round(i, 5) for i in spacings]
    # print(spacings) # rounded values
    letters = to_letter(spacings)
    total = ''.join(letters)
    # print(total)
    local_best = 1
    best = 1
    for i in range(len(total) - 1):
        if total[i + 1] == total[i]:
            local_best += 1
            best = max(best, local_best)
            if i == len(total) - 2:
                j = 0
                while total[j] == total[i]:
                    local_best += 1
                    j += 1
            best = max(best, local_best)
        else:
            local_best = 1
    return best
