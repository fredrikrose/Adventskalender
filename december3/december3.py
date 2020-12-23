def algorithm(input,down,right):
    length_down=len(input)
    tree_counter=0
    down_location=down
    right_location=right
    while (down_location<length_down):
        if (input[down_location][right_location]=='#'):
            tree_counter+=1
            #print('X')
        #else:
            #print('O')
        down_location+=down
        right_location+=right

    return tree_counter

def Prepare_file():
    f=open(r'december3\december3.txt','r')
    data=f.readlines()
    f.close()
    ext_data=[]
    for line in data:
        line=line.rstrip('\n')
        ext_data.append(line*100)
    return ext_data


def main():
    test_data=Prepare_file()
    right=[1,3,5,7,1]
    down=[1,1,1,1,2]
    answer=1
    for i in range (len(right)):
        tree=algorithm(test_data,down[i],right[i])
        print(tree)
        answer=answer*tree
    return answer
    


        
print(main())