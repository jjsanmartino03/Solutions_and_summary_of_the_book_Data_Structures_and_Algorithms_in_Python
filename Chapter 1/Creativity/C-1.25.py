"""
C-1.25 
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example,
if given the string "Let s try, Mike.", this function would return
"Lets try Mike".
"""

def no_punctuation(text):
    for i in text:
        if ord(i) in range(33, 48):
            text = text.replace(i, "")
    return text

#beware with : and ;, because this is a lazy approaching to the objective and therefore its working is limited.
