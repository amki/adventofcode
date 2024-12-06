result = 0

def search_l(word, idx_line, idx_char):
    try:
        chars = ""
        for i in range(1,len(word)):
            if(idx_char-i < 0):
                return ""
            chars += lines[idx_line][idx_char-i]
        return chars
    except:
        return ""

def search_r(word, idx_line, idx_char):
    try:
        chars = ""
        for i in range(1,len(word)):
            chars += lines[idx_line][idx_char+i]
        return chars
    except:
        return ""

def search_u(word, idx_line, idx_char):
    try:
        chars = ""
        for i in range(1,len(word)):
            if(idx_line-i < 0):
                return ""
            chars += lines[idx_line-i][idx_char]
        return chars
    except:
        return ""

def search_d(word, idx_line, idx_char):
    try:
        chars = ""
        for i in range(1,len(word)):
            chars += lines[idx_line+i][idx_char]
        return chars
    except:
        return ""
    
def search_ur(word, idx_line, idx_char):
    try:
        chars = ""
        for i in range(1,len(word)):
            if(idx_line-i < 0):
                return ""
            chars += lines[idx_line-i][idx_char+i]
        return chars
    except:
        return ""

def search_dr(word, idx_line, idx_char):
    try:
        chars = ""
        for i in range(1,len(word)):
            chars += lines[idx_line+i][idx_char+i]
        return chars
    except:
        return ""

def search_dl(word, idx_line, idx_char):
    try:
        chars = ""
        for i in range(1,len(word)):
            if(idx_char-i < 0):
                return ""
            chars += lines[idx_line+i][idx_char-i]
        return chars
    except:
        return ""

def search_ul(word, idx_line, idx_char):
    try:
        chars = ""
        for i in range(1,len(word)):
            if(idx_line-i < 0 or idx_char-i < 0):
                return ""
            chars += lines[idx_line-i][idx_char-i]
        return chars
    except:
        return ""

def handle_chars_found(word, chars):
    global result
    print(f"Check {chars}")
    for chr in chars:
        if chr == word[1:]:
            print(f"Match {chr}")
            result += 1


def search_for_word(word, idx_line, idx_char):
    print(f"Searching for {word} @ {lines[idx_line][idx_char]} {idx_line}/{idx_char}")
    results = []
    results.append(search_u(word, idx_line, idx_char))
    results.append(search_d(word, idx_line, idx_char))
    results.append(search_l(word, idx_line, idx_char))
    results.append(search_ul(word, idx_line, idx_char))
    results.append(search_dl(word, idx_line, idx_char))    
    results.append(search_r(word, idx_line, idx_char))
    results.append(search_ur(word, idx_line, idx_char))
    results.append(search_dr(word, idx_line, idx_char))
    
    handle_chars_found(word, results)



searchword = "XMAS"

f = open("input04.txt", "r")
input = f.read()
lines = input.split("\n")
print(f"Looking for {searchword[0]}")
for idx_line,line in enumerate(lines):
    for idx_char,char in enumerate(line):
        if(char == searchword[0]):
            search_for_word(searchword,idx_line,idx_char)
print(f"Result is {result}")