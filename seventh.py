# read/write file examples

# open or read function

f=open("hello.txt")
content = f.read()
# for line in f :
#     print(line)
print(content)
f.close()

# write function

f= open("hello.txt", "w")
f.write("Farheen is too much inteligent...")
f.write("Yes...I am")
f.close()
