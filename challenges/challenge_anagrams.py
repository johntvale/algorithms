def is_anagram(first_string, second_string):
    n = len(first_string)
    if ((not first_string) or (not second_string)): return False
    if (len(first_string) != len(second_string)): return False

    first_word = first_string.lower()
    second_word = second_string.lower()
    new_word = ""

    for index in range(0,n):
        for index_second_word in range(0,n):
            if second_word[index_second_word] == first_word[index]:
                new_word += second_word[index_second_word]
                second_word.replace(second_word[index_second_word], "")
    
    return first_word == new_word