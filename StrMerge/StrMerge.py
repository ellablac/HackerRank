def merge_strings(a, b):
    sz = min(len(a), len (b))
    
    l = ""

    for i in range (sz):
        l+=a[i]
        l+=b[i]

    if len(a) > sz:
        for i in a[sz:len(a)]:
            l+=i
    else:
        for i in b[sz:len(b)]:
            l+=i

    print (l)


merge_strings("abcdef", "xyzwhatever")