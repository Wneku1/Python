
def scalar_multiple(v1, v2):

    while len(v1) != len(v2):
        l1 = len(v1)
        l2 = len(v2)
        if l1 > l2:
            v2.append(0)
        elif l2 < l1:
            v1.append(0)
    result = []
    for i in range(0, len(v1)):
        result.append(v1[i] * v2[i])
    return result


a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

print(scalar_multiple(a, b))
