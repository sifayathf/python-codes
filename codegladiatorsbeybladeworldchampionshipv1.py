ReqIng1=[]
TotIng1=[]
T=input()
N=input()
ReqIng1=input()
TotIng1=input()
TotIng=TotIng1.split()
ReqIng=ReqIng1.split()
TotIng.sort()
ReqIng.sort()
#print(ReqIng)
#print(TotIng)
a=0
c=0
for i in range(int(N)):
    #print('VALUES',int(ReqIng[i+c]),int(TotIng[i]))
    if (int(ReqIng[i+c])>int(TotIng[i])):
        a=a+1
        #print (a,ReqIng[i+c],TotIng[i])
    else:
        c=c+1
    if (len(ReqIng)<=int(i+c)):
        #print('3rd IF',len(ReqIng),i+c,int(a))
        break
    #print ('pass',i)
print(int(a))


