''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    T=input()
    for i in range(int(T)):
        calculate()
 # Write code here 
def calculate():
    ReqIng1=[]
    TotIng1=[]
    N=input()
    ReqIng1=input()
    TotIng1=input()
    TotIng=TotIng1.split()
    ReqIng=ReqIng1.split()
    TotIng=[int(x) for x in TotIng]
    ReqIng=[int(x) for x in ReqIng]
    TotIng.sort()
    ReqIng.sort()
    #print(ReqIng)
    #print(TotIng)
    a=0
    c=0
    k=0
    #print(ReqIng)
    #print(TotIng)
    for i in range(int(N)):
        if (len(ReqIng)>int(i+c)):    
            #print('VALUES',int(ReqIng[i+c]),int(TotIng[i]))
            if (int(ReqIng[i+c])>int(TotIng[i-k])):
                a=a+1
                #print('Condition check1',len(ReqIng),'i=',i,'c=',c,i+c,'a=',int(a),int(ReqIng[i+c]),int(TotIng[i-k]))
            else:
                #c=1
                k=k+1
    print(int(a))
main()

