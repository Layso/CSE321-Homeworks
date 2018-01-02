# Well, this algorithm needs to work in O(log(n) + log(m)) or O(log(k))time. But
# I couldn't figure out a decrease and conquer method that does the job in
# limits. This is the only algorithm I came up with and I believe it works in
# O(k) time. Recurence relation should be T(k) = T(k-1) + 5 since it calls itself
# until the k = 0.



def compare(first, second):
    if (first == None):
        if (second == None):
            return None
        else:
            return second

    elif (second == None):
        return first

    else:
        return first if (first < second) else second



def find_kth_book_2(m, n, x):
    lenM = len(m)
    lenN = len(n)
    M = None if (lenM == 0) else m[0]
    N = None if (lenN == 0) else n[0]

    if (x == 1):
        return compare(M, N)

    else:
        if (compare(M, N) == M and M != None):
            return find_kth_book_2(m[1:lenM], n, x-1)
        elif (compare(M, N) == N and N != None):
            return find_kth_book_2(m, n[1:lenN], x-1)




m = ["algorithm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop"]

book = find_kth_book_2(m,n,4)
print(book)
# Expected output: oop

book = find_kth_book_2(m,n,6)
print(book)
# Expected output: systemsprogramming
