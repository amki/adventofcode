def out_of_range(x):
    if(x > MATRIX_UPPER_LIMIT or x < MATRIX_LOWER_LIMIT):
        return True
    return False

def chars_between(word, line_start, char_start, line_end, char_end):
    print(f"Search limits {line_start}/{char_start} - {line_end}/{char_end}")
    if(out_of_range(line_start) or out_of_range(char_start) or out_of_range(line_end) or out_of_range(char_end)):
        print(f"Index out of range")
        return ""
    # swap start and end if they are wrong order
    is_swap = False
    if(line_start > line_end):
        is_swap = True
        line_end, line_start = line_start, line_end
    if(char_start > char_end):
        is_swap = True
        char_end, char_start = char_start, char_end
    chars = ""
    if(char_start == char_end):
        for i in range(line_start,line_end):
            chars += lines[i][char_start]
        if(is_swap):
            return chars[::-1]
        return chars
    if(line_start == line_end):
        for i in range(char_start, char_end):
            chars += lines[line_start][i]
        if(is_swap):
            return chars[::-1]
        return chars


def search_for_word(word, idx_line, idx_char):
    #print(f"Searching for {word} @ {idx_line}/{idx_char}")
    ## look up
    #chars = chars_between(word, idx_line, idx_char, idx_line-len(word)+1, idx_char)
    #if(len(chars) > 0):
    #    print(f"UP Found {chars}")
    ## look down
    #chars = chars_between(word, idx_line+1, idx_char, idx_line+len(word), idx_char)
    #if(len(chars) > 0):
    #    print(f"DOWN Found {chars}")
    ##look left
    #chars = chars_between(word, idx_line, idx_char, idx_line, idx_char-len(word)+1)
    #if(len(chars) > 0):
    #    print(f"LEFT Found {chars}")
    ##look right
    #chars = chars_between(word, idx_line, idx_char+1, idx_line, idx_char+len(word))
    #if(len(chars) > 0):
    #    print(f"RIGHT Found {chars}")
    #look top/right
    chars = chars_between(word, idx_line-1, idx_char+1, idx_line-len(word), idx_char+len(word))


searchword = "XMAS"

MATRIX_LOWER_LIMIT = 0
MATRIX_UPPER_LIMIT = 140

f = open("input04.txt", "r")
input = f.read()
lines = input.split("\n")
print(f"Looking for {searchword[0]}")
for idx_line,line in enumerate(lines):
    for idx_char,char in enumerate(line):
        if(char == searchword[0]):
            search_for_word(searchword,idx_line,idx_char)