def solve (count, seq):
    n = count[0]
    k = count[1]
    #print ("solve: ", (seq), "\n")
    #for i in range(n):
        #seq[i] = seq[i]%k
    #print (seq)
    # Store the end index of a base subsequence that starts with i.
    # 
    BaseArray = [0] * n
    for i in range(n):
        cnt = 0
        
        for j in range(i,n):
            cnt += seq[j]
            cnt %= k
            if cnt == 0:
                #BaseArray.append(j)
                BaseArray[i] += 1
                if j<n-1:
                    BaseArray[j+1] = BaseArray[i]
                break
            if j == n-1:
                BaseArray[i] = 0 # reset count back to zero
                #BaseArray.append(-1)
    #print ("\nsubs:", BaseArray, "\n")

    #CountKSeq(BaseArray)

    s = sum (BaseArray)
    print (s)


def CountKSeq(BaseArray):
    count = 0

    #print ("\ncount: ", count)

    for i in range (len(BaseArray)):
        c = 0
        next = i
        
        while (next < len(BaseArray) and BaseArray[next] != -1):
            c += 1
            saved = next
            next = BaseArray[next] + 1
            BaseArray[saved] = -1

        if c > 0:
            count += (int)((c*c + c) / 2)

    print (count)

def GetInput():
    T = int(input())
    counts = []
    seqs = []

    for i in range(T):
        c = list(map(int, input().split()))
        counts.append(c)
        seq = list(map(int, input (). split ()))
        seqs.append(seq)
        
    return [counts, seqs]

def GetInputT():
    return [[[5, 3], [6, 2]], [[1, 2, 3, 4, 1], [1, 2, 1, 2, 1, 2]]]  

def GetInputF():
    f = open ("in1.txt", "r")
    T = int(f.readline())
    counts = []
    seqs = []

    for i in range(T):
        c = list(map(int, f.readline().split()))
        counts.append(c)
        seq = list(map(int, f.readline(). split ()))
        seqs.append(seq)
    f.close()

    return [counts, seqs]

def main():              
     
    InArray = GetInputF()
    #print (InArray)

    for i in range(len(InArray[0])):
        solve (InArray[0][i], InArray[1][i])
    
if __name__ == "__main__":
    main() 