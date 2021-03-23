def write(word):
    return "print('{}')".format(word)

def add_var(name,value):
    return "{} = {}".format(name,value)

def show_var(name):
    return "print({})".format(name)






program = []
running = True
while running:
    command = input("Command: ")

    if command == "Write":
        word = input("What do you want to write? ")
        program.append("write('{}')".format(word))
    
    elif command == "add_var":
        name = input("Name of the Variable: ")
        value = input("Value of the variable: ")
        program.append("add_var('{}',{})".format(name,value))
    
    elif command == "show_var":
        name = input("What variable do you want? ")
        program.append("show_var('{}')".format(name))
    
    

    elif command == "exit":
        name = input("Name your program: ")
        with open(name + '.py','w') as f:
                for c in program:
                    f.write(eval(c))
                    f.write('\n')
        running = False