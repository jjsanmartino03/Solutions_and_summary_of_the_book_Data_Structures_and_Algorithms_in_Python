listing = input(">>>")

words_list = listing.split(" ")
used = []

for i in words_list:
    if i not in used:
        print(f"The word '{i}' appears {words_list.count(i)} times")
        used.append(i)
