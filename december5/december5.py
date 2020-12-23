import numpy as np

def test(filename=r'Adventskalender\december5\december5.txt'):
    seat_id=[]
    #lines=['BFFFBBFRRR','FFFBBBFRRR']
    with open(filename) as f_in:
        lines=list(f_in)
        for line in lines:
            row=list([i for i in range(128)])
            column=[i for i in range(8)]
            line=line.strip()
            row_values=line[0:7]
            column_values=line[7:]
            for value in row_values:
                #print(value)
                mid=len(row)/2
                if value=='F':
                    row=row[:int(mid)]
                elif value=='B':
                    row=row[int(mid):]
                else:
                    print('Error')
                    break
                #print(row)
            for cvalue in column_values:
                mid=len(column)/2
                if cvalue=='R':
                    column=column[int(mid):]
                elif cvalue=='L':
                    column=column[:int(mid)]
            #print(row)
            #print(column)
            seat_id_number=int(row[0])*8+int(column[0])
            seat_id.append(seat_id_number)
    return seat_id
        


seat_id=np.array(test())
#print(np.max(seat_id))
max_seat_id=127*8+8
missing=[]
for i in range(max_seat_id):
    if i not in seat_id:
        missing.append(i)
print(missing)


