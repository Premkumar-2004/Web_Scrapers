# cook your dish here
t=input()
test=[]


result=beautifulsubstring(t,test)

for i in range(t):
    n,q=map(int,input().split())
    s=input().strip()
    query=[]
    for j in range(q):
       query.append(input().strip())
    
    test.append([n,q,s]+query)



def longestsubstring(s):
    maxl=0
    clen=1
    
    for i in range(len(s)):
        if s[i]==s[i-1]:
            clen+=1 
        
        else:
            maxl=max(maxl,clen)
            clen=1 
        
    return max(maxl,clen)


def beautifulsubstring(t,test):
    results=[]   
    for t in test:
        n,q=t[0],t[1]
        s=t[2] 
        ilen=longestsubstring(s)
        results.append(ilen)

        for i in range(q):
            c=test[i+3]
            s=s+c
            z=longestsubstring(s)
            results.append(z)
    return results



for i in result:
    print(i,end=" ")
        



     
    
        
    
    














