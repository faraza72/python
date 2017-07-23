N=int(input("Enter a positive integer less than 10:"))
if N >= 10:
    print ('Input out of range')
else:
    for i in range(1,N+1):
        print((10**i//9)**2)