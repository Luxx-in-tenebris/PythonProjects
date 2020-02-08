str1=input().split()
sumx1,sumx2,sum1,sum2=0,0,0,0
itstime=False
delta=1
#step1
for x in str1:
    if x=='=':
        itstime=True
        delta=1
    elif x=='-':
        delta=-1;    
    elif x=='+':
        delta=1
    if(itstime):
        if 'x' in x:
            if x[0]=='x':
                sumx2+=1*delta
            else:      
                temp=x[0:-1]
                sumx2+=int(temp)*delta
        elif ('=' not in x) and ('+' not in x) and ('-' not in x):
            sum2+=int(x)*delta
    
    else:
        if 'x' in x:
            if x[0]=='x':
                sumx1+=1*delta
            else:      
                temp=x[0:-1]
                sumx1+=int(temp)*delta
        elif ('=' not in x) and ('+' not in x) and ('-' not in x):
            sum1+=int(x)*delta
   
print(str(sumx1)+'x',str(sum1) if str(sum1)[0]== '-' else '+'+ str(sum1),'=',str(sumx2)+'x',str(sum1) if str(sum2)[0]== '-' else '+'+ str(sum2))
#
# print(str(sumx1)+'x','+',sum1,'=',str(sumx2)+'x','+',sum2)   

#step2 
sumx2*=-1
sum1*=-1
print(str(sumx1)+'x',str(sumx2)+'x' if str(sumx2)[0]== '-' else '+'+ str(sumx2)+'x','=', str(sum2), str(sum1) if str(sum1)[0]== '-' else '+'+ str(sum1))

sumx=sumx1+sumx2
sum_=sum1+sum2
print(str(sumx)+'x','=',sum_)
answer=sum_/sumx
print('x','=',answer)