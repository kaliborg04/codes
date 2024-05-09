words = []
while True:
    s = input("Enter word: ")
    if len(s) == 0:
        break
    words.append(s)
print(words)

numbers = []
for word in words:
    if word.isdigit():
        numbers += [word]
print(numbers)