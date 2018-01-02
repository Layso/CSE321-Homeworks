def Towers(source, temp, destination, timeArr, n):
    if (n==1):
        print ("Disk " + str(n) + ": " + "Move from " + source + " to " + destination)
        timeArr[n-1] += n*abs(ord(source)-ord(destination))

    else:
        Towers(source, destination, temp, timeArr, n-1)
        print ("Disk " + str(n) + ": " + "Move from " + source + " to " + destination)
        timeArr[n-1] += n*abs(ord(source)-ord(destination))
        Towers(temp, source, destination, timeArr, n-1)



def TowersOfHanoiTime(n):
    print ("Input size is " + str(n))

    timer = [0] * n
    Towers("A", "B", "C", timer, n)

    print ("\nTotal elapsed time for each disk:")
    for i in range(0,n):
        print ("Elapsed time for disk " + str(i+1) + ": " + str(timer[i]))


TowersOfHanoiTime(7)
