import FreeSimpleGUI as sg
from zip_file_func import make_archive

label1 = sg.Text("Select files to compress")
input1 = sg.Input()
choose_btn = sg.FilesBrowse("Choose", key = "files")

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_btn_2 = sg.FolderBrowse("Choose" , key = "folders")

compress_btn = sg.Button("Compress")
txt_box = sg.Input(key = "com_file_name")
label3 = sg.Text("Enter compressed file name")

window = sg.Window("File compress", layout=[[label1, input1 , choose_btn], [label2, input2, choose_btn_2], [label3,txt_box,compress_btn]])

while True:
    event , values = window.read()
    print(event,values)
    filepaths = values["files"].split(";")
    folderpath = values["folders"]
    filename = values["com_file_name"]
    print("check - " ,filepaths , folderpath , filename)
    make_archive(filepaths , folderpath , filename)


window.close()