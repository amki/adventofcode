import math

result = 0

f = open("input05.txt", "r")
input = f.read()
lines = input.split("\n\n")
rules = lines[0].split("\n")
updates = lines[1].split("\n")

ruledict = {}

for r in rules:
    splits = r.split("|")
    if(not splits[1] in ruledict):
        ruledict[splits[1]] = []
    ruledict[splits[1]].append(splits[0])
print(f"Parsed rules {ruledict}")

def make_valid(update):
    while(not check_valid(update)):
        prints = update.split(",")
        changed = False
        for idx,p in enumerate(prints):
            for i in range(idx,len(prints)):
                if(not p in ruledict):
                    continue
                prules = ruledict[p]
                if(prints[i] in prules):
                    #print(f"{prints[i]} is in {p}'s list: {ruledict[p]}")
                    offender = prints[i]
                    prints.remove(offender)
                    changed = True
                    if(idx-1 < 0):
                        prints.insert(0,offender)    
                    else:
                        prints.insert(idx-1,offender)
                    update = ",".join(prints)
                    break
            if(changed):
                break
    return update
          

def check_valid(update):
    #print(f"Taking update {update}")
    prints = update.split(",")
    valid = True
    for idx,p in enumerate(prints):
        #print(f"For print {p}")
        for i in range(idx,len(prints)):
            if(not p in ruledict):
                continue
            prules = ruledict[p]
            if(prints[i] in prules):
                #print(f"{prints[i]} is in {p}'s list: {ruledict[p]}")
                valid = False
    if(valid):
        return True
    return False

for u in updates:
    if(len(u) < 1):
        continue
    isvalid = check_valid(u)
    print(f" is {u} valid? {isvalid}")
    if(not isvalid):
        vu = make_valid(u)
        print(f"{u} is now {vu} and valid")
        prints = vu.split(",")
        middle = prints[math.floor(len(prints)/2)]
        print(f"Middle element {middle}")
        result += int(middle)

print(f"Result is {result}")