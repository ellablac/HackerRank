def solve (n, k, NumArray):
# The sums divisible by k can exist only between the identical
# mod k remainders of running totals., e.g. if the running
# total list has a number x appearing anywhere in the list
# multiple times, the sum of numbers  between each pair of
# x must equal to k. In addition, all such subsequences must
# be adjoining. 

    RunningSumArr = []
    RunningSumArr.append(NumArray[0] % k) # An array of running sums

    for i in range(1, n):
        RunningSumArr.append((NumArray[i] + RunningSumArr[i-1]) % k)
    RunningSumArr.sort()

    NumSubSeq = 0
    if RunningSumArr[0] == 0: #special condition
        cnt = 1
    else:
        cnt = 0

    for i in range(1, n):
        # count the number of times each element appears in the list
        
        if RunningSumArr[i] == RunningSumArr[i-1]:
            cnt += 1
            if i == n - 1:
                NumSubSeq += (int)((cnt*cnt + cnt) / 2)
        
        else:
            if cnt > 0:
                NumSubSeq += (int)((cnt*cnt + cnt) / 2)
                cnt = 0


    return (NumSubSeq)

def GetInput(inmode):

    if inmode == "t": # test mode
        return [[[5, 3], [6, 2]], [[1, 2, 3, 4, 1], [1, 2, 1, 2, 1, 2]]] 
    
    if inmode == "f": # input from file
        f = open ("in8.txt", "r")

    if inmode == "s":  # input from stdin
        import sys
        f = sys.stdin

    T = int(f.readline())
    counts = []
    seqs = []

    for i in range(T):
        c = list(map(int, f.readline().split()))
        counts.append(c)
        seq = list(map(int, f.readline(). split ()))
        seqs.append(seq)
        
    if inmode == "f":  # input from a file
        f.close()

    return [counts, seqs]


def main():              
     
    InArray = GetInput("f")
    #print (InArray)

    for i in range(len(InArray[0])):
        print (solve (InArray[0][i][0], InArray[0][i][1], InArray[1][i]))

    
if __name__ == "__main__":
    main() 