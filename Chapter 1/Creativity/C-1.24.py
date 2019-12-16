def count_vowels(phrase):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in phrase.lower():
        if i in vowels:
            count += 1
    return count


print(count_vowels(input()))
