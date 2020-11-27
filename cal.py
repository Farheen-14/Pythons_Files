
# print("Hey its calculate 2nd, don't be confused", __name__) 
# if we simple run the cal.py then the output will be __main__ , if the import to demo.py then the output will be --cal.

def add():
    print("Adding value")

def sub():
    print("Substtract the value")

def main():
    add()
    sub()
if __name__ == "__main__":
    main()