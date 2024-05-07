words = []
while True:
    w = input("Enter word: ")
    if len(w) == 0:
        print(len(words), "word(s):")
        print(words)
        exit(0)
    words += [w]