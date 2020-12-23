import numpy as np

filename=r'Adventskalender\december9\december9.txt'
numbers=[]
preamble=25
with open(filename) as f_in:
    input=list(f_in)
for line in input:
    numbers.append(int(line))

def task1():
    preamble_numbers=numbers[0:preamble]#First numbers
    not_preamble_numbers=numbers[preamble:]

    for i in range(len(not_preamble_numbers)):
        valid=False
        for j in range(len(preamble_numbers)):
            for k in range(len(preamble_numbers)):
                if preamble_numbers[k]+preamble_numbers[j]==not_preamble_numbers[i] and k!=j:
                    valid=True
        preamble_numbers.append(not_preamble_numbers[i])
        #print(preamble_numbers)
        #preamble_numbers=preamble_numbers[0:]
        del preamble_numbers[0]
        #print(preamble_numbers)
        #print('########################')
        if valid:
            continue
        else:
            #print(preamble_numbers)
            print('task1: ', not_preamble_numbers[i])
            return not_preamble_numbers[i]



def task2(target_sum):
    n=len(numbers)
    
    for idx1 in range(n):
        teller=0
        curr_sum=0
        idx2=idx1
        #print(idx2)
        while idx2<=n-1 and teller<=1200:
            teller+=1
            #print(idx1,idx2)
            if curr_sum==target_sum:
                #print(idx1,idx2)
                return idx1,idx2
            if idx2<n:
                curr_sum+=numbers[idx2]
                idx2+=1
            
            
idx1,idx2=task2(task1())
print('task2: ',np.max(numbers[idx1:idx2])+np.min(numbers[idx1:idx2]))
