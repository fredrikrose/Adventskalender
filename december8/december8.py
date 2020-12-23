# #Preparing file format
# # filename=r'Adventskalender\december8\december8.txt'
# # commands=[]
# # with open(filename) as f_in:
# #     for line in f_in:
# #         line=line.strip()
# #         commands.append(line)




def task1():
    #Preparing file format
    filename=r'Adventskalender\december8\december8.txt'
    commands=[]
    with open(filename) as f_in:
        for line in f_in:
            line=line.strip()
            commands.append(line)

    position=0
    acc_counter=0
    previous_positions=[] #Keep track of previous positions to terminate correctly
    while position not in previous_positions:
        previous_positions.append(position)
        if commands[position][0:3]=='nop':
            position+=1
        elif commands[position][0:3]=='jmp':
            if commands[position][4]=='+':
                position+=int(commands[position][5:])
            elif commands[position][4]=='-':
                position-=int(commands[position][5:])
        elif commands[position][0:3]=='acc':
            if commands[position][4]=='+':
                acc_counter+=int(commands[position][5:])
                position+=1
            elif commands[position][4]=='-':
                acc_counter-=int(commands[position][5:])
                position+=1
        else:
            print('Error')
            break
    #print('position: ',position,' acc_counter: ',acc_counter)
    print(acc_counter)            

#task1()

            

def new():
    filename=r'Adventskalender\december8\december8.txt'
    with open(filename) as f_in:
        old_commands=list(f_in)
    #print(commands)
    #commands=list(old_commands)
    for change in range(len(old_commands)): #For every swittch of nop/jmp we check if it solves
        commands=list(old_commands)
        if commands[change].split()[0]=='nop':
            commands[change]='jmp '+commands[change].split()[1]
        elif commands[change].split()[0]=='jmp':
            commands[change]='nop '+commands[change].split()[1]
        else:
            continue
        #print(commands)
        t=0
        ip=0
        acc=0
        while 0<=ip<len(commands) and t<1000:
            #print(t)
            t+=1
            words=commands[ip].split()
            if words[0]=='acc':
                acc+=int(words[1])
                ip+=1
            elif words[0]=='nop':
                ip+=1
            elif words[0]=='jmp':
                ip+=int(words[1])
        if ip==len(commands):
            print(acc)

                      
#new()
print(int('-3\n'))
        






    