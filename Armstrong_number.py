Num = list(range(100, 501))      # list of numbers from 100-500
armstrong = []                   # empty list to append the armstrong numbers

def Armstrong(Num):              # armstrong function

    """ This function calculates the armstrong number in the given list. """

    for i in Num:                # for loop to iterate over the list
        n_ = n = i
        sum_ = 0    
        while n != 0:            # run loop until n == 0
            n = n//10            # calculating the quotient
            r = n_ % 10          # calculating the remainder
            sum_ += r**3         # calculating cube of the remainder and adding it to s
            n_ = n               # updating value of n to n_
        if sum_ == i:            # if condition to append the armstrong numbers into the  list
            armstrong.append(i)
    return armstrong             # returning the armstrong list

print(Armstrong(Num))            # calling the armstrong function
print("webhook done successfull")
