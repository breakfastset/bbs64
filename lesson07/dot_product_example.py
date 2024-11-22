
def dot_product(v1, v2):
    """Return the dot product of 2 vectors."""
    total = 0
    for i in range(len(v1)):
        total = total + (v1[i] * v2[i])

    return total

def main():
    v1 = [0.3, 0.0, 0.4]
    v2 = [0.2, 0.5, 0.6]
    result = dot_product(v1, v2)
    print(result)

main()