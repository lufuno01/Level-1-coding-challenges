def triangle(num):
    for i in range(num):
        for j in range(i + 1):
            print("#")
    print()

    while num < 0:
        absolute_number = abs(num)

    for k in range(absolute_number):
        for x in range(absolute_number - k):
            print("#")
    print()


triangle(4)
