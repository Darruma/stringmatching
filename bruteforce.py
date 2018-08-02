
def brute_force_match(text,pattern):
    text = list(text)
    pattern = list(pattern)
   
    for x in range(0,len(text) - len(pattern) + 1):
        for y in range(0,len(pattern)):
            if( text[x + y] != pattern[y]):
                break
            return x
    return -1

txt = "aabaa"
pattern = "b"

print(brute_force_match(txt,pattern))
