import numpy as np
from copy import deepcopy

filename=r'Adventskalender\december11\december11.txt'
SEATING=[]
with open(filename) as f_in:
    input=list(f_in)
    L=[list(l.strip()) for l in input]
    for line in input:
#         print(line)
        SEATING.append(line.strip())
# #print(SEATING)
print(L)

def adjacent_task1(seating,i,j):
    counter=0
    #Under
    if i!=len(seating)-1: #not bottom row
        if seating[i+1][j]=='#':
            counter+=1
        if j!=len(seating[i])-1:
            if seating[i+1][j+1]=='#':
                counter+=1
        if j!=0:
            if seating[i+1][j-1]=='#':
                counter+=1
    #Side
    if j!=0:
        if seating[i][j-1]=='#':
            counter+=1
    if j!=len(seating[i])-1:
        if seating[i][j+1]=='#':
            counter+=1
    #Over
    if i!=0: #Not top row
        if seating[i-1][j]=='#':
            counter+=1
        if j!=len(seating[i])-1:
            if seating[i-1][j+1]=='#':
                counter+=1
        if j!=0:
            if seating[i-1][j-1]=='#':
                counter+=1
    return counter


def task1(seating):
    #print(SEATING)
    seating_new=[]
    for i in range(len(seating)):
        temp=''
        for j in range(len(seating[0])):
            adj=adjacent_task1(seating,i,j)
            if seating[i][j]=='.':
                temp+='.'
            else:
                if seating[i][j]=='#' and adj>=4:
                    temp+='L'
                elif seating[i][j]=='L' and adj==0:
                    temp+='#'
                else:
                    temp+=seating[i][j]
        seating_new.append(temp)
    return seating_new



def main():
    seating=np.array(SEATING)
    teller=0
    occupied=0
    #prev_seating=[]
    while teller<150:
        #prev_seating=seating
        seating=task1(seating)
        teller+=1
    for i in range(len(seating)):
        for j in range(len(seating[0])):
            if seating[i][j]=='#':
                occupied+=1

    print('Convergence after',teller,'iterations and',occupied,'occupied seats')
    
#main()

R=len(L)
C=len(L[0])
def task2(L):
    while True:
        seating_new=deepcopy(L)
        #seating_new=L
        change=False
        for r in range(R):
            for c in range(C):
                nocc=0
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        if dr==0 and dc==0:
                            continue
                        rr=r+dr
                        cc=c+dc
                        while 0<=rr<R and 0<=cc<C and L[rr][cc]=='.':
                            rr=rr+dr
                            cc=cc+dc
                        if 0<=rr<R and 0<=cc<C and L[rr][cc]=='#':
                            nocc+=1
                if L[r][c]=='L':
                    if nocc==0:
                        seating_new[r][c]='#'
                        change=True
                elif L[r][c]=='#' and nocc>=5:
                    seating_new[r][c]='L'
                    change=True
        if not change:
            break
        L=deepcopy(seating_new)
        #L=seating_new
    ans=0
    for r in range (R):
        for c in range (C):
            if L[r][c]=='#':
                ans+=1
    return ans


print(task2(L))

