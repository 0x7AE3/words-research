from decimal import Decimal
import math
a, a_prime = [None] * 20, [None] * 20
b, b_prime = [None] * 20, [None] * 20
q, q_prime = [None] * 20, [None] * 20

q[0] = q_prime[0] = 1
q[1] = 3
a_prime[1] = q_prime[1] = 28
b_prime[1] = 9
a[1] = q[1] = 3
a[2] = 3**8 + 3**5
q[2] = 3**9 + 3**6 + 1
b[2] = 3**6

for n in range(3, 8):
    for i in range(2, n + 1):
        b_prime[i] = q_prime[i - 1]**6 + q_prime[i - 2] - 1
        b[i] = q[i - 1]**6 + q[i - 2] - 1
        q[i] = b[i] * q_prime[i - 1] + 1
        q_prime[i] = b_prime[i] * q[i] + 1
        a[i] = (q[i - 1]**6 + q[i - 2] - 1) * b_prime[i - 1] + q[i - 1]**5
        a_prime[i] = (q_prime[i - 1]**6 + q_prime[i - 2] - 1) * b[i] + q_prime[i - 1]**5
        # print(f"{n}:")
        # print(f"log of q[{i}]: {math.log(q[i])}")
        # print(f"log of q_prime[{i}]: {math.log(q_prime[i])}")
        # print(f"a[{i}]: {a[i]}")
        # print(f"a_prime[{i}]: {a_prime[i]}")
        # print(f"b[{i}]: {b[i]}")
        # print(f"b_prime[{i}]: {b_prime[i]}")
    print()

    alpha = Decimal(1.0) / Decimal(a[n - 1])
    beta = Decimal(1.0) / Decimal(a_prime[n - 1])
    for i in range(n - 2, 0, -1):
        alpha += Decimal(a[i])
        alpha = Decimal(1.0) / alpha
        beta += Decimal(a_prime[i])
        beta = Decimal(1.0) / beta


#   new
    alpha = Decimal(1.0) / Decimal(a[n - 1])
    beta = Decimal(1.0) / Decimal(a_prime[n - 1])
    for i in range(n - 2, 0, -1):
        alpha += Decimal(a[i])
        alpha = Decimal(1.0) / alpha
        beta += Decimal(a_prime[i])
        beta = Decimal(1.0) / beta
    alpha = Decimal(1.0) / Decimal(a[n - 1])
    beta = Decimal(1.0) / Decimal(a_prime[n - 1])
    for i in range(n - 2, 0, -1):
        alpha += Decimal(a[i])
        alpha = Decimal(1.0) / alpha
        beta += Decimal(a_prime[i])
        beta = Decimal(1.0) / beta
    alpha = Decimal(1.0) / Decimal(a[n - 1])
    beta = Decimal(1.0) / Decimal(a_prime[n - 1])
    for i in range(n - 2, 0, -1):
        alpha += Decimal(a[i])
        alpha = Decimal(1.0) / alpha
        beta += Decimal(a_prime[i])
        beta = Decimal(1.0) / beta
#    new
    # print(a[1])
    # print(a[2])
    # print(a_prime[1])

    print(f'alpha: {alpha}')
    print(f'beta: {beta}')

    # for i in range(0, n + 1):
    #     for j in range(1, n + 1):
    #         if(q[j] % q[i] == 1):
    #             print(f'j: {j} i: {i}')


