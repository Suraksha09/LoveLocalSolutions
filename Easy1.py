def last_string(s):
    # if the input string is empty then exit
    if not s:
        return 0
    beg = -1
    end = -1
    # Iterate the string in reverse
    for i in range(len(s)-1, -1, -1):
        if s[i] != ' ':
            # Found the end of the last word
            if end == -1:
                end = i
        elif end != -1:
            # Found the start of the last word
            beg = i + 1
            break
    # Extract the last word from the original string
    if beg != -1:
        return len(s[beg:end + 1])
    else:
        return 0
s1 = "Hello World"
s2 = "fly me to the moon"
s3 = "luffy is still joyboy"
print(last_string(s1))
print(last_string(s2))
print(last_string(s3))
