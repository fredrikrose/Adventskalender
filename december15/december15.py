
S=[1,2,16,19,18,0]
last_index={}

for i,n in enumerate(S):
    if i!=len(S)-1:
        last_index[n]=i
#print(last_index)

while len(S)<30000000:
    prev=S[-1]
    prev_prev=last_index.get(prev,-1)
    last_index[prev]=len(S)-1
    if prev_prev==-1:
        next_=0
    else:
        next_=len(S)-1-prev_prev
    S.append(next_)

print(S[-1])

