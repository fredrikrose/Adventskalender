from collections import defaultdict


filename=r'Adventskalender\december7\december7.txt'

def task1(target,counter):
    #target=['shiny gold']
    #bags=[]
    #counter=0
    with open(filename) as f_in:
            lines=list(f_in)
            #lines.append('')
            for line in lines:
                line=line.strip()
                #line=line.strip('bags')
                line=line.split('contain')
                #print(line)
                for i in range (len(target)):
                    temp=line[0].split('bag')
                    #print(temp[0])
                    if target[i] in line[1] and temp[0] not in target:
                        target.append(temp[0])
                        counter+=1
                        #print(target)
            
            #print(target)
            #print(counter)
            return target,counter


#Default values                
counter=0                
target=['shiny gold']
target,counter=task1(target,counter)
for i in range(4):
    target,counter=task1(target,counter)
#print(counter)

# def task2(target,answer):
#     #numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#     #target=['shiny gold']
#     bag_counter=0
    
    
#     with open(filename) as f_in:
#             lines=list(f_in)
#             #lines.append('')
#             for line in lines:
#                 line=line.strip()
#                 #line=line.strip('bags')
#                 line=line.split('contain')
#                 #print(line)
#                 for i in range (len(target)):
#                     temp_left=line[0].split('bag')
#                     encapsulated_bags=line[1].split(',')
#                     holder_bag=temp_left[0]
#                     #print(encapsulated_bags[0])
#                     for bag in encapsulated_bags:
#                         #print(holder_bag)
#                         #print(target[i])
#                         #print(holder_bag)
#                         bag=bag.split()
#                         bag_string=bag[1]+' '+bag[2] #bag
#                         if target[i] in holder_bag and bag_string not in target and bag[0]!='no':
#                             #print('JADDA')
#                             #print(target[i])
#                             #print(bag)
#                             target.append(bag_string)
#                             #print(int(bag[0]))
#                             bag_counter+=int(bag[0])
#                             print(bag_counter)

#             answer.append(bag_counter)
#             bag_counter=0
#                 #print(target)
                        


            
#             #print(target)
            
#             return target,answer



# #Default values
# target=['shiny gold']
# answer=[]
# task2(target,answer)
# for i in range (1):
#     target,answer=task2(target,answer)
# print(target)
# print(answer)

PARENTS=defaultdict(list)
CONTENTS=defaultdict(list)
target='shinygoldbag'
#print(PARENTS)
with open(filename) as f_in:
        lines=list(f_in)
        #lines.append('')
        for line in lines:
            line=line.strip()
            words=line.split()
            #print(words)
            container=words[0]+words[1]+words[2]
            container=container[:-1]
            #print(container)
            if words[-3]=='no': #Dont contain other bags
                continue
            else:
                idx=4
                while idx<len(words):
                    bag=words[idx]+words[idx+1]+words[idx+2]+words[idx+3]
                    if bag.endswith('.'):
                        bag=bag[:-1]
                    if bag.endswith(','):
                        bag=bag[:-1]
                    if bag.endswith('s'):
                        bag=bag[:-1]
                    n=int(bag[0])
                    assert bag[1] not in '0123456789'
                    while any([bag.startswith(d) for d in '0123456789']):
                        bag=bag[1:]
                    PARENTS[bag].append(container)
                    CONTENTS[container].append((n,bag))
                    idx+=4    



#print(PARENTS)
print(CONTENTS)
def size(bag):
    ans=1
    #print(bag)
    for(n,y) in CONTENTS[bag]:
        print(y,n,size(y))
        ans+=n*size(y)
        #print(y,n,size(y),n*size(y))
    return ans

print(size(target)-1)