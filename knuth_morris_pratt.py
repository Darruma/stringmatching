def kmp_table(text):
    text = list(text)
    table = [0 for x in range(len(text) + 1)]
    table[0] = -1;
    pos = 1
    next_char = 0
    
    while pos < len(text):
        if text[pos] == text[next_char]:
            table[pos] = table[next_char]
            pos = pos + 1
            next_char = next_char + 1
        else:
            table[pos] = table[next_char]

            next_char = table[next_char]
            while next_char > 0 and text[pos] != text[next_char]:
                next_char = table[next_char]
            pos = pos + 1
            next_char = next_char + 1
            print(pos)
    table[pos] = next_char
    return table
    
    

def kmp(text,pattern):
    text = list(text)
    pattern = list(pattern)
    t_position = 0
    p_position = 0
    positions = [0 for i in range(len(text))]

    num_positions = 0
    table = kmp_table(pattern)

    while t_position < len(text):
        if(pattern[p_position] == text[t_position]):
           t_position = t_position + 1
           p_position = p_position + 1
           
           if(p_position == len(pattern)):
               positions[num_positions] = t_position - p_position
               p_position = table[len(pattern)]
        else:
           p_position = table[p_position]
           if p_position < 0:
               t_position = t_position + 1
               p_position = p_position + 1

    return positions
           
    
print(kmp("chicken","k"))       
