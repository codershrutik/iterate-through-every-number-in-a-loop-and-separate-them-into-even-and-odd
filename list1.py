mylist = [1,23,5,12,34,56,7,45,56,28,36,59,46,57,36,39,8]

even = []
noteven = []

for i in mylist:
    if(i%2 == 0):
        even.append(i)
    else:
        noteven.append(i)

    print("Even numbers are: ",even)
    print("odd numbers are: ",noteven)