import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in todo")
input_box = sg.InputText(tooltip="Enter Todo :")
add_button = sg.Button("Add")

window = sg.Window('My todo app', layout=[[label], [input_box , add_button ]])

# while True:
#     event, values = window.read()
#     print(event)
#     print(values)
#     match event:
#         case "Add":
            
window.read()
window.close()