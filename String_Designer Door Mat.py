n, m = list(map(int, input().split()))
not_middle = False
reverse_first = True
count = 0
filler = ".|."

for i in range(n):
    count += 1

    if count == (n // 2) + 1:
        print("WELCOME".center(m, "-"))
        not_middle = True
        filler = filler[6:]

    else:
        if not_middle is True:
            print(filler.center(m, "-"))
            filler = filler[6:]
        else:
            print(filler.center(m, "-"))
            filler += ".|..|."
