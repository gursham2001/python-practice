def odd_or_even(sequence):

    num_of_odd = 0
    num_of_even = 0

    for i in sequence:
        if i == True:
            num_of_even += 1
        elif i == False:
            num_of_odd += 1

    if num_of_even > num_of_odd:
        print(num_of_even - num_of_odd)
    elif num_of_odd > num_of_even:
        print(num_of_odd - num_of_even)

sequence = True, True, True, False, False, True
odd_or_even(sequence)
