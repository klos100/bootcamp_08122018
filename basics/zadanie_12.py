i = 0

while i < 101:
    print (i)
    i = i ** 2
    if i % 10 == 0:
        i += 1
        continue
    print(i)
    i += 1
    # if i == 100:
    #     break

