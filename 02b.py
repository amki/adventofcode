import copy

def check_line_for_safety(report):
    levels = report.split(" ")
    last_level = -1
    monotonic_rising = True
    monotonic_falling = True
    is_safe = True
    for level in levels:
        if(last_level == -1):
            last_level = int(level)
            continue
        diff = int(last_level) - int(level)
        absdiff = abs(int(last_level) - int(level))
        #print(f"Diff between {last_level} and {level} is  {diff}")
        if diff < 0:
            monotonic_rising = False
        if diff > 0:
            monotonic_falling = False
        if not monotonic_falling and not monotonic_rising:
            is_safe = False
            break
        if absdiff == 0:
            is_safe = False
            break
        if absdiff > 3:
            is_safe = False
            break
        last_level = level
    return is_safe

f = open("input02.txt", "r")
input = f.read()
lines = input.split("\n")
result = 0
for report in lines:
    if(len(report) < 1):
        break
    issafe = check_line_for_safety(report)
    #print(f"Report result: safe? {is_safe} rising? {monotonic_rising} falling? {monotonic_falling}")
    if(issafe):
        result += 1
    else:
        #print(f"Levels {report} is unsafe.")
        levels = report.split(" ")
        newlevels = " "
        for idx,level in enumerate(levels):
            copylevels = copy.deepcopy(levels)
            copylevels.pop(idx)
            newlevels = newlevels.join(copylevels)
            #print(f"{levels} becomes {newlevels}")
            retrysafe = check_line_for_safety(newlevels)
            #print(f"... and is {retrysafe}")
            if(retrysafe):
                #print(f"Subset {newlevels} is safe")
                result += 1
                break
            newlevels = " "
            
print(f"How many are safe? {result}")
