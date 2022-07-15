def gleichResult(s1,r):
    gibt={x:1 for x in s1}
    a=1
    result=set()
    for k in range(len(s1)-1):
        if gibt[s1[k]]==1:
            target=r-s1[k]
            if gibt[target] in gibt:
                result.add((min(target,s1[k]),max(target,s1[k])))
                gibt[target]=0

    print(result)
gleichResult([1,3,2,2,4,0,2,2],4)