import random
#
print("The lotto numbers are:  ")
#input how many sets of number to list
Lotto = 9
#create main function
def main():

    values = [ 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for r in range(Lotto):
        values[r] = random.randint(0, 9)
#print results
    print(values)
#call main function
main()
