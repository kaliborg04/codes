import hashlib

f = open("password.txt")
pwd = f.read()
f.close()
print(pwd)

sha = hashlib.sha256()
sha.update(pwd.encode())
digest = sha.hexdigest()
print(digest)

f = open("password.sha256", "w")
f.write(digest)
f.close()