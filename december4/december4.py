
def inrange(key,low,high):
    return low<=int(key)<=high

def test(filename=r'Adventskalender\december4\december4.txt'):
    counter1=0
    counter2=0
    passport={}
    with open(filename) as f_in:
        lines=list(f_in)
        lines.append('')
        for line in lines:
            line=line.strip()
            print(line)
            if not line: #Blank line
                valid1=True
                for field in ['byr','iyr','eyr','hgt','hcl','ecl','pid']:
                    if field not in passport:
                        valid1=False
                if valid1:
                    counter1+=1
                    valid2=True
                    if not inrange(passport['byr'],1920,2002):
                        valid2=False
                    if not inrange(passport['iyr'],2010,2020):
                        valid2=False
                    if not inrange(passport['eyr'],2020,2030):
                        valid2=False
                    hgt_units=passport['hgt']
                    if hgt_units.endswith('in'):
                        if not inrange(hgt_units[:-2],59,76):
                            valid2=False
                    elif hgt_units.endswith('cm'):
                        if not inrange(hgt_units[:-2],150,193):
                            valid2=False
                    else:
                        valid2=False
                    hcl=passport['hcl']
                    if hcl[0]!='#' or any([c not in '0123456789abcdef' for c in hcl[1:]]):
                        valid2=False
                    ecl=passport['ecl']
                    if ecl not in ['amb','blu','brn','gry','grn','hzl','oth']:
                        valid2=False
                    pid=passport['pid']
                    if len(pid)!=9 or any ([c not in '0123456789' for c in pid]):
                        valid2=False
                    if valid2:
                        counter2+=1

                passport={}
            else:
                words=line.split()
                for word in words:
                    k,v=word.split(':')
                    passport[k]=v
           # print(passport)
    print('task1: ',counter1)
    print('task2: ',counter2)
test()




