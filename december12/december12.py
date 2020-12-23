
filename=r'Adventskalender\december12\december12.txt'
COMMANDS=[]
with open(filename) as f_in:
    input=list(f_in)
    for line in input:
        COMMANDS.append(line.strip())
#print(COMMANDS)

def task1(commands):
    direction=90 #0=north, 90=east, 180=south, 270=west, 
    east_value=0
    north_value=0
    for c in commands:
        if c[0]=='N':
            north_value+=int(c[1:])
        elif c[0]=='S':
            north_value-=int(c[1:])
        elif c[0]=='E':
            east_value+=int(c[1:])
        elif c[0]=='W':
            east_value-=int(c[1:])
        elif c[0]=='L':
            direction-=int(c[1:])
        elif c[0]=='R':
            direction+=int(c[1:])
        elif c[0]=='F':
            if direction in [0,360,720,-360,-720,-1080]:
                north_value+=int(c[1:])
            elif direction in [90,360+90,720+90,-270,-270-360,-270-720]:
                east_value+=int(c[1:])
            elif direction in [180,360+180,720+180,-180,-180-360,-720-180]:
                north_value-=int(c[1:])
            elif direction in [270,360+270,720+270,-90,-450,-450-360,-450-720]:
                east_value-=int(c[1:])
            else:
                print(direction)
    print('nort_value:', north_value)
    print('east_value:', east_value)    
    return abs(north_value)+abs(east_value)

#print(task1(COMMANDS))

def task2(commands):
    waypoint=[1,10] #north,east
    position=[0,0] #north east
    #direction=90 #0=north, 90=east, 180=south, 270=west, 
    for c in commands:
        if c[0]=='N':
            waypoint[0]+=int(c[1:])
        elif c[0]=='S':
            waypoint[0]-=int(c[1:])
        elif c[0]=='E':
            waypoint[1]+=int(c[1:])
        elif c[0]=='W':
            waypoint[1]-=int(c[1:])
        elif c[0]=='L':
            temp_n=waypoint[0]
            temp_e=waypoint[1]
            if int(c[1:])==90:
                waypoint[0]=temp_e
                waypoint[1]=-temp_n
            elif int(c[1:])==180:
                waypoint[0]=-1*waypoint[0]
                waypoint[1]=-1*waypoint[1]
            elif int(c[1:])==270:
                waypoint[0]=-temp_e
                waypoint[1]=temp_n
        elif c[0]=='R':
            temp_n=waypoint[0]
            temp_e=waypoint[1]
            if int(c[1:])==90:
                waypoint[0]=-temp_e
                waypoint[1]=temp_n
            elif int(c[1:])==180:
                waypoint[0]=-1*waypoint[0]
                waypoint[1]=-1*waypoint[1]
            elif int(c[1:])==270:
                waypoint[0]=temp_e
                waypoint[1]=-temp_n
        elif c[0]=='F':
            position[0]+=int(c[1:])*waypoint[0]
            position[1]+=int(c[1:])*waypoint[1]
    #print('nort_value:', north_value)
    #print('east_value:', east_value)    
    return abs(position[0])+abs(position[1])
print(task2(COMMANDS))