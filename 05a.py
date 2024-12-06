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

for u in updates:
    if(len(u) < 1):
        continue
    print(f"Taking update {u}")
    prints = u.split(",")
    valid = True
    for idx,p in enumerate(prints):
        #print(f"For print {p}")
        for i in range(idx,len(prints)):
            if(not p in ruledict):
                continue
            prules = ruledict[p]
            if(prints[i] in prules):
                print(f"{prints[i]} is in {p}'s list: {ruledict[p]}")
                valid = False
    if(valid):
        middle = prints[math.floor(len(prints)/2)]
        print(f"Middle element {middle}")
        result += int(middle)
print(f"Result is {result}")
