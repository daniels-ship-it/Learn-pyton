
def xtest():
    rows = 25
    for i in range(rows):
        for j in range(rows):
            if i == j or j == rows - 1 - i:
                print("x", end="")
            else:
                print("   ", end="")
        print()

while True:
    kata = input()
    if kata == "x":
        xtest()
        break
    else:
        print(kata)

