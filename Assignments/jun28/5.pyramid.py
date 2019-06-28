
def pyramid():
    levels = int(input("Levels: "))
    for i in range(levels):
        print(' '*(levels - i -1 ) + '*' *(2 * i + 1))

# pyramid()

print(' '*(2 - 1 -1 ) + '*' *(2 * 1 + 1))