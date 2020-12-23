import numpy as np

filename=r'Adventskalender\december13\december13.txt'
with open(filename) as f_in:
    input=list(f_in)
t0=int(input[0].strip())
ids=[int(i) for i in input[1].strip().split(',') if i!='x']
#print(ids)

t_best=100000000
id_best=0
for b in ids:
    t=t0
    while (t%b)!=0:
        t+=1
        first_departure=t%b
        if first_departure==0 and t<t_best:
            t_best=t
            id_best=b
print(t_best,id_best,(t_best-t0)*id_best)
