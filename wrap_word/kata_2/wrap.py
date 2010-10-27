def wrap_line(text, col=80):
    # First we change all the \n by spaces
    text = text.replace("\n", " ")
    new_text, line = "", ""
    for char in text:
        line += char
        if len(line) == col:
            line, next_line = verify_line(line, col)
            new_text += line + '\n'
            line = next_line
    new_text += line
    if new_text[-1] == "\n":
        return new_text[:-1]
    return new_text


def verify_line(line, col):
    """We have a line :
        - if there is a space before, we split there
        - Else it's a unique word, we return it"""
    col -= 1
    next_line = ""

    while col >= 0:
        if line[col] == " ":
            # We return the wrapped line, and the beginning of the next one
            return line[:col], next_line
        else:
            next_line = line[col] + next_line
            line = line[:col]
            col -= 1
    # this line is a unique word, we return it
    return next_line, line
