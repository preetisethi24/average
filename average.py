def average(array):
    # your code goes here
    print(len(set(array)))
    return float(sum(set(array)))/len(set(array))

print(average([3,4,4,5,5,6]))
