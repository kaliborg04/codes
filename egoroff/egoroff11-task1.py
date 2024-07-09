string = input("Enter string: ")
string = string.upper()
print(string)
words = string.split()
print('Number of words:', len(words))
if len(words) >= 1:
    print('First word:', words[0])
if len(words) >= 2:
    print('Second word:', words[1])
