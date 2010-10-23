def create_line(list_words, col_max):
    line = ""
    if len(list_words[0]) > col_max:
        word = list_words.pop(0)
        new_word = word[:col_max]
        list_words.insert(0, word[col_max:])
        if list_words:
            new_word += "\n"
        return new_word, list_words
    while 1:
        new_list_words = list(list_words)
        new_line = line + new_list_words.pop(0)
        if len(new_line) > col_max:
            return line + "\n", list_words
        elif not new_list_words:
            return new_line, new_list_words
        else:
            line = new_line
            list_words = new_list_words

def wrap_line(text):
    col_max = 7
    list_words = text.split()
    final_text = ""
    while list_words:
        line, list_words = create_line(list_words, col_max)
        final_text += line
    return final_text
