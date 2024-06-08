#from functions import get_todos , write_todos
import functions
import time

now = time.strftime("%b %d %Y %I:%M:%S %p")
print("It's", now)

while True:
    user_action = input("Type add , show, edit , complete or exit :")

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        #todo = input("Enter Todo  :") + "\n"
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        newtodo =[]
        for item in todos:
            newitem = item.strip('\n')  
            newtodo.append(newitem)
        for index, item in enumerate(newtodo):
            row = f"{index + 1} :-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number -1 
            todos = functions.get_todos()
            newtodo = input("Enter new todo : ")
            todos[number] = newtodo + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Invalid Input")
            continue

    elif user_action.startswith("complete"):
        try:
            #number = int(input("Enter number to close : "))
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = (number - 1)
            remove_todo = todos[index].strip("\n")
            todos.pop(number -1)
            functions.write_todos(todos)
            message = f"{remove_todo + " Removed succesfully"}"
            print(message)
        except IndexError:
            print("Invalid Index")
            continue

    elif   user_action.startswith("exit"):
        break

    else:
        print("Invalid Function enterd!")
print("BYE!")