#!/usr/bin python3

with open("mysite/settings.py", "r") as f:
	data = f.readlines()
	print(data[1])
my_secret_key = data[1].index("=")
data[1] = "my_secret_key = 'nf922*1)4z4=k4rt!n9smgj6116@a(e3yjjm6d(5jc7b-1&_q4'"