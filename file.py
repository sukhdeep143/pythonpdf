# file = open("hello.txt", "w+")
# file.write("Hello, world!")  
# file.seek(0)  # Move the cursor to the beginning
# r = file.read()  
# print(r)  
# file.close()


fo = open("write.txt", "w+")

fo.write("This is a simple file")
r=fo.read()
print(r)
fo.close()


