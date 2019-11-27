import hashlib
msg=input("enter the message")
res=hashlib.md5(msg.encode())
print("the hash value through md5 is {} ".format(res.hexdigest()))
