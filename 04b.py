result = 0

def search_for_word(word, idx_line, idx_char):
    global result
    print(f"Searching for {word} @ {lines[idx_line][idx_char]} {idx_line}/{idx_char}")
    if(idx_line-1 < 0 or idx_char-1 < 0):
        return
    try:
        chars = ""
        chars += lines[idx_line-1][idx_char-1]
        chars += lines[idx_line+1][idx_char+1]
        chars += lines[idx_line-1][idx_char+1]
        chars += lines[idx_line+1][idx_char-1]
        if(chars == "MSMS" or chars == "SMMS" or chars == "MSSM" or chars == "SMSM"):
            print(f"Found {chars}")
            result += 1
    except:
        return

searchword = "XMAS"

f = open("input04.txt", "r")
input = f.read()
lines = input.split("\n")
print(f"Looking for {searchword[0]}")
for idx_line,line in enumerate(lines):
    for idx_char,char in enumerate(line):
        if(char == searchword[2]):
            search_for_word(searchword,idx_line,idx_char)
print(f"Result is {result}")