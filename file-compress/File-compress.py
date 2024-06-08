import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress")
input1 = sg.Input()
choose_btn = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_btn_2 = sg.FolderBrowse("Choose")

compress_btn = sg.Button("Compress")

window = sg.Window("File compress", layout=[[label1, input1 , choose_btn], [label2, input2, choose_btn_2], [compress_btn]])
window.read()
window.close()