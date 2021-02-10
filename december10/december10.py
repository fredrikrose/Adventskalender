import numpy as np
import itertools

filename=r'december10\december10.txt'
numbers=[]
preamble=25
with open(filename) as f_in:
    input=list(f_in)
for line in input:
    numbers.append(int(line))
numbers=np.sort(numbers)

def task1():
    diff_3=1 #last adapter
    diff_1=0
    adapter=0
    for i in range(len(numbers)):
        if numbers[i]-adapter==1:
            diff_1+=1
        elif numbers[i]-adapter==3:
                diff_3+=1
        else:
            print('not 1 or 3')
        adapter=numbers[i]
    #print('diff_1: ',diff_1)
    #print('diff_3: ',diff_3)
    print('task1:',diff_1*diff_3) 
    #print(len(numbers))
    return diff_3*diff_1

task1()


Taken={}
start=0
end=numbers[-1]+3
new_numbers=numbers
new_numbers=np.insert(new_numbers,-1,end)
new_numbers=np.insert(new_numbers,0,start)
new_numbers=np.sort(new_numbers)

def task2(i):
    #task2(i) is the number of ways to complete the adapter chain given that you are at 
    # adapter new_numbers[i]
    ans=0
    if i==len(new_numbers)-1:
        return 1
    if i in Taken:
        return Taken[i]
    for j in range(i+1,len(new_numbers)):
        if new_numbers[j]-new_numbers[i]<=3:
            #One way to get from i to the end is to first step to j
            #The number of paths from i that start by stepping to new_numbers[j] is Target[j]
            #So task2(i)=\sum_{valid j} task2(j)
            ans+=task2(j)
    Taken[i]=ans
    #print(Taken[i])
    return ans

print('task2:',task2(0))

   


         

