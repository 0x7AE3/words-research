from sortedcontainers import SortedList
from collections import Counter
import math


def to_letter(ls):
    unique_spaces = list(SortedList(set(ls)))
    #     print(unique_spaces)
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


def word(alpha, n):
    circle = SortedList()
    for k in range(1, n + 1):
        prod = k * alpha
        circle.add(prod - math.floor(prod))  # fractional part of k * alpha
    # print(circle)
    spacings = [circle[i] - circle[i - 1] for i in range(1, len(circle))]  # differences
    spacings.append(1 + circle[0] - circle[-1])  # looped around spacing
    # print(spacings) # explicit values
    spacings = [round(i, 5) for i in spacings]
    spacings.sort()
    # print(spacings) # rounded values
    letters = to_letter(spacings)
    #
    # eps = 0.001
    #
    # p1, p2, p3 = [], [] ,[]
    # for i in range(1, len(circle)):
    #     curr_space = circle[i] - circle[i - 1]
    #     if abs(curr_space - spacings[0]) <= eps:
    #         p1.append(i)
    #     elif abs(curr_space - spacings[1]) <= eps:
    #         p2.append(i)
    #     elif abs(curr_space - spacings[2]) <= eps:
    #         p3.append(i)

    return ''.join(letters)


def longest_run(alpha, n):
    total = word(alpha, n)
    local_best = 1
    best = 1
    for i in range(len(total) - 1):
        if total[i + 1] == 'a' and total[i] == 'a':
            local_best += 1
            best = max(best, local_best)
            if i == len(total) - 2:
                j = 0
                while total[j] == 'a' and total[i] == 'a':
                    local_best += 1
                    j += 1
            best = max(best, local_best)
        else:
            local_best = 1
    return best


def generate_words(alpha, n):
    circle = SortedList()
    for k in range(-n, n + 1):
        prod = k * alpha
        circle.add(prod - math.floor(prod))  # fractional part of k * alpha
    spacings = [circle[i] - circle[i - 1] for i in range(1, len(circle))]  # differences
    spacings.append(1 - circle[-1])  # looped around spacing
    # print(spacings) # explicit values
    spacings = [round(i, 5) for i in spacings]
    # print(spacings) # rounded values
    letters = to_letter(spacings)
    str = ''
    for i in letters:
        str += i
    # print(str)
    return str
    if len(spacings) != len(letters):
        raise ValueError('spacings and letters have different lengths')
    # print('{} and {}'.format(len(spacings), len(letters))) # precision check
    # print(letters)
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


def generate_partitons(alpha, n):
    circle = SortedList()
    for k in range(1, n + 1):
        prod = k * alpha
        circle.add((prod - math.floor(prod), k))  # fractional part of k * alpha
    # print(circle)
    spacings = [circle[i][0] - circle[i - 1][0] for i in range(1, len(circle))]  # differences
    spacings.append(1 + circle[0][0] - circle[-1][0])  # looped around spacing
    # print(spacings) # explicit values
    spacings = [round(i, 5) for i in spacings]
    # print(spacings) # rounded values
    letters = to_letter(spacings)

    eps = 0.001

    spacings = list(set(spacings))
    spacings = sorted(spacings)

    p1, p2, p3 = [], [], []
    for i in range(1, len(circle)):
        curr_space = circle[i][0] - circle[i - 1][0]
        if abs(curr_space - spacings[0]) <= eps:
            p1.append(circle[i][1])
        elif abs(curr_space - spacings[1]) <= eps:
            p2.append(circle[i][1])
        elif abs(curr_space - spacings[2]) <= eps:
            p3.append(circle[i][1])
    last_space = 1 + circle[0][0] - circle[-1][0]
    # print(last_space)
    # print(spacings)
    if abs(last_space - spacings[0]) <= eps:
        p1.append(circle[0][1])
    elif abs(last_space - spacings[1]) <= eps:
        p2.append(circle[0][1])
    elif abs(last_space - spacings[2]) <= eps:
        p3.append(circle[0][1])

    return ([sorted(p1)[0], sorted(p1)[-1]], [sorted(p2)[0], sorted(p2)[-1]], [sorted(p3)[0], sorted(p3)[-1]])

def generate_partitons_2(alpha, n):
    circle = SortedList()
    for k in range(1, n + 1):
        prod = k * alpha
        circle.add((prod - math.floor(prod), k))  # fractional part of k * alpha
    # print(circle)
    spacings = [circle[i][0] - circle[i - 1][0] for i in range(1, len(circle))]  # differences
    spacings.append(1 + circle[0][0] - circle[-1][0])  # looped around spacing
    # print(spacings) # explicit values
    spacings = [round(i, 5) for i in spacings]
    # print(spacings) # rounded values
    letters = to_letter(spacings)

    eps = 0.001

    spacings = list(set(spacings))
    spacings = sorted(spacings)

    p1, p2, p3 = [], [], []
    for i in range(1, len(circle)):
        curr_space = circle[i][0] - circle[i - 1][0]
        if abs(curr_space - spacings[0]) <= eps:
            p1.append(circle[i - 1][1])
        elif abs(curr_space - spacings[1]) <= eps:
            p2.append(circle[i - 1][1])
        elif abs(curr_space - spacings[2]) <= eps:
            p3.append(circle[i - 1][1])
    last_space = 1 + circle[0][0] - circle[-1][0]
    # print(last_space)
    # print(spacings)
    if abs(last_space - spacings[0]) <= eps:
        p1.append(circle[-1][1])
    elif abs(last_space - spacings[1]) <= eps:
        p2.append(circle[-1][1])
    elif abs(last_space - spacings[2]) <= eps:
        p3.append(circle[-1][1])

    return ([sorted(p1)[0], sorted(p1)[-1]], [sorted(p2)[0], sorted(p2)[-1]], [sorted(p3)[0], sorted(p3)[-1]])