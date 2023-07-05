input_message=input("What is the message you want to encode?")

# version 1
encoded=[]
for char in input_message:
    encoded.append(chr(ord(char)+10))
print(f"Version 1: encoded message is {''.join(encoded)}")

# version 2
encoded="".join([chr(ord(char)+10)for char in input_message])
print(f"Version 2: encoded message is {encoded}")