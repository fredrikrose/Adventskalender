import numpy as np
def task1(filename=r'Adventskalender\december6\december6.txt'):
    answers=[]
    char='abcdefghijklmnopqrstuvwxyz'
    counter_list=[]
    with open(filename) as f_in:
            lines=list(f_in)
            lines.append('')
            for line in lines:
                line=line.strip()
                #print(line)
                if not line: #Blank line
                    answers=''.join(answers) #Concatenates list of string to one string
                    #print(answers)
                    counter=0
                    for c in char:
                        if c in answers:
                            counter+=1
                    counter_list.append(counter) 
                    answers=[]
                    
                else:
                    line=line.split()
                    answers+=line
    return counter_list

                    
                    
                
                    

counter_list=task1()
#print(counter_list)
sum_counter=np.sum(counter_list)
print('Answer taks1: ',sum_counter)

def task2(filename=r'Adventskalender\december6\december6.txt'):
    answers=[]
    char='abcdefghijklmnopqrstuvwxyz'
    counter_list=[]
    counter=0
    with open(filename) as f_in:
            lines=list(f_in)
            lines.append('')
            for line in lines:
                line=line.strip()
                #print(line)
                if not line: #Blank line
                    #answers=''.join(answers) #Concatenates list of string to one string
                    #print(answers)

                    for c in char:
                        person_counter=0
                        for person in range(len(answers)):
                            if c in answers[person]:
                                person_counter+=1
                        if person_counter==len(answers): 
                            counter+=1
                    counter_list.append(counter) 
                    answers=[]
                    counter=0
                else:
                    line=line.split()
                    answers+=line
    return counter_list

answer2_list=task2()
#print(answer2_list)
print('Answer task2: ',np.sum(answer2_list))
