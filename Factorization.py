coefficient1 = int(input())
coefficient2 = int(input())
constant = int(input())


def find_divisors_pairs(num):

    pairs = []

    for i in range(-(abs(num)+1), abs(num)+1):
        for j in range(-(abs(num)+1), abs(num)+1):
            if i * j == num:
                pairs.append([i, j])
    return pairs


coeffDivPairs = find_divisors_pairs(coefficient1)
constDivPairs = find_divisors_pairs(constant)

for coeffDivPair in coeffDivPairs:
    for constDivPair in constDivPairs:
        a = coeffDivPair[0]
        b = constDivPair[0]
        c = coeffDivPair[1]
        d = constDivPair[1]

        if a*d + b*c == coefficient2:
            print("(" +  str(a) + "x + " + str(b) + ")(" + str(c) + "x + " + str(d) + ")")
