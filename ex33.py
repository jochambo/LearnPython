def print_range(lower_limit, upper_limit):
    i = lower_limit
    numbers = []

    while i < upper_limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

print_range(3, 5)
