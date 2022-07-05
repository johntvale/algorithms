def is_anagram(first_string, second_string):
    n = len(first_string)
    if ((not first_string) or (not second_string)):
        return False
    if (len(first_string) != len(second_string)):
        return False

    first_word = first_string.upper()
    second_word_list = list(second_string.upper())
    new_word = ""

    for index in range(0, n):
        if first_word[index] in second_word_list:
            new_word += first_word[index]
            second_word_list.remove(first_word[index])

    return first_word == new_word
