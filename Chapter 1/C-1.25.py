def no_punctuation(text):
    for i in text:
        if ord(i) in range(33, 48):
            text = text.replace(i, "")
    return text

#beware of : and ;