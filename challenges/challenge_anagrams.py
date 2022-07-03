def is_anagram(first_string, second_string):
    n = len(first_string)
    if ((not first_string) or (not second_string)): return False
    if (len(first_string) != len(second_string)): return False
    result = True

    first_word = first_string.lower()
    second_word_list = list(second_string.lower())
    new_word = ""

    for index in range(0,n):
        if first_word[index] in second_word_list:
            new_word += first_word[index]
            second_word_list.remove(first_word[index])
    
    if (first_word != new_word):
        result = False
    
    return result