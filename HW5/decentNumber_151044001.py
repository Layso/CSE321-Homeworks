# This algorithm tries to find biggest decent number possible by testing if
# current situation is suitable for the decent number definition. On each step
# i and n-i will check if i*5 and (n-1)*3 makes a decent number starting i from
# 0 to half of digit number (n/2)

# Algorithm has a main loop that checks if current step makes a decent number
# and maximum number finder at the end. Number constructor builds the combination
# desired from current step. It will take linear time since it's loop makes
# amount1 + amount2, which equals n, times. Having a linear loop (numberConstructor)
# inside a linear loop (decentNumber) makes it n^2 for time complexity. Since
# there is no complexity constraint I'll make it stay that way (can be optimized
# to immediately return first number if length is divisable by 3 or 5 which gives
# linear best case). But current algorithm works on O(n^2)



def numberConstructor(number1, amount1, number2, amount2):
    sum = 0
    digitCount = amount1+amount2

    for i in range(0, digitCount):
        digitValue = pow(10,amount1+amount2-1)
        if (amount1 > 0):
            sum += number1*digitValue
            amount1 -= 1

        elif (amount2 > 0):
            sum += number2*digitValue
            amount2 -= 1

    return sum



def decentNumber(n):
    combinations = [-1]

    for i in range(0, int(n/2)+1):
        if (i == 0):
            if ((n-i) % 3 == 0):
                combinations.append(numberConstructor(5, n-i, 3, 0))
            elif ((n-i) % 5 == 0):
                combinations.append(numberConstructor(5, 0, 3, n-i))
        elif (i % 3 == 0):
            if ((n-i) % 5 == 0):
                combinations.append(numberConstructor(5, i, 3, n-i))
        elif (i % 5 == 0):
            if ((n-i) % 3 == 0):
                combinations.append(numberConstructor(5, n-i, 3, i))

    return max(combinations)



dn =  decentNumber(1)
print(dn)
# Expected Output: -1

dn =  decentNumber(3)
print(dn)
# Expected Output: 555

dn =  decentNumber(5)
print(dn)
# Expected Output: 33333

dn =  decentNumber(11)
print(dn)
# Expected Output: 55555533333
