import math
from word_methods import *

pi = math.pi

# for i in range(1, 100):
    #     s = word(math.sqrt(2), i)
    # print(i, s)
    # if 'cabc' in s or 'cbac' in s:
    #     print(i, s)
    # if 'ac'in s:
    #     print(i, s)

    # if 'c' not in s:
        # print('RELABELING')

for n in range(105, 106):
    # print(n, generate_partitons(math.sqrt(2), n))
    # print(generate_partitons_2(math.sqrt(2), n))
    print(n, generate_words(math.sqrt(2), n))

    # print(i, s)
    # c_count = 0
    # for j in s:
    #     if j == 'c':
    #         c_count += 1
    #     if c_count > 1:
    #         break
    # if c_count == 1:
    #     print('RELABEL RELABEL RELABEL')
    # good = True
    # for j in str:
    #     if j == 'c':
    #         good = False
    #         break
    # if good:
    #     print(i, word(pi + 0.9312, i))
    # print(i, longest_run(pi, i))
