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

right_dict = {}
for num in list_right:
    if(num in right_dict):
        right_dict[num] += 1
    else:
        right_dict[num] = 1

print(len(right_dict))
result = 0

for num in list_left:
    # It does not appear in the right list, so the similarity score does not increase
    if(not (num in right_dict)):
        continue
    print(f"Checking {num}")
    similarity = int(num) * int(right_dict[num])
    print(f"Similarity is {similarity}")
    result += similarity

print(f"Total similarity is {result}")