#Exception Handling

#try      -> Instruction from which we are expecting the exceptions
#except   -> exception is raised in try block it will be handled by this block
#else     -> optional(no exceptions)
#finally -> Always it will display

while True:
    a = int(input("a value"))
    b = int(input("b value"))
    try:
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")  #if 'try' works 'else' also runs otherwise 'except' block runs
    finally:
        print("program ends...")
