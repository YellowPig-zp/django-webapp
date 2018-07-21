#!/usr/bin python3
import os

with open("mysite/settings.py", "r") as f:
	data = f.readlines()
my_secret_key = data[1][data[1].index("=")+2:]
print(my_secret_key)
data[1] = "my_secret_key = 'no key'\n"
print(my_secret_key)

with open("mysite/settings.py", "w") as f:
	f.writelines(data)

commit_message = input("Enter commit message:")
if not commit_message:
	raise RuntimeError("Empty commit message as not allowed!")

os.system("git add .")
os.system("git commit -m \"%s\"" % commit_message)
os.system("git push origin master")


with open("mysite/settings.py", "r+") as f:
	data = f.readlines()
	print(my_secret_key)
	data[1] = "my_secret_key = %s\n" % my_secret_key
	f.writelines(data)


