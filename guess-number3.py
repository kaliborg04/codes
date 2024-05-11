while True:
    s = input("Enter sentence: ")
    if s == '':
        break
    s = s.strip()
    s = s.rstrip("!.?")
    s = s.replace(",", " ").replace("-", " ")
    s = s.lower()
    words = s.split()
    s = " ".join(words)
    print(len(s), "word(s)", s)
