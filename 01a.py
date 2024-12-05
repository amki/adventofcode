f = open("input01.txt", "r")
input = f.read()
lines = input.split("\n")
list_left = []
list_right = []
for line in lines:
    if(len(line) < 1):
        continue
    nums = line.split("   ")
    list_left.append(nums[0])
    list_right.append(nums[1])

list_right.sort()
list_left.sort()
result = 0
for idx, num in enumerate(list_left):
    diff = abs(int(num) - int(list_right[idx]))
    print(f"{diff}")
    result += diff
print(f"Total diffrence is {result}")