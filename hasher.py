import hashlib

while True:
    s = input("Enter string: ")
    if len(s) == 0:
        exit(0)
    h = hashlib.sha512()
    h.update(s.encode())
    digest = h.hexdigest()
    print(digest)