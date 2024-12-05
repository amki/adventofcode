import re

pattern = r"mul\((\d{1,3},\d{1,3})\)"

f = open("input03.txt", "r")
input = f.read()
match = re.findall(pattern,input)
result = 0
for operands in match:
    ops = operands.split(",")
    mul = int(ops[0]) * int(ops[1])
    result += mul
print(f"Result is {result}")
