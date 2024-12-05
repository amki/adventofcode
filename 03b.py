import re

pattern = r"mul\((\d{1,3},\d{1,3})\)"

f = open("input03.txt", "r")
input = f.read()

result = 0
dos = input.split("do()")
for do in dos[1:]:
    filtered = do.split("don't()")[0]
    print(filtered)
    match = re.findall(pattern,filtered)
    
    for operands in match:
        ops = operands.split(",")
        mul = int(ops[0]) * int(ops[1])
        result += mul
print(f"Result is {result}")