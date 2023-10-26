import PySimpleGUI as gui 

label1 = gui.Text("select a file to Compress")
input1 = gui.InputText()
selectButton1 = gui.FileBrowse("Select")

label2 = gui.Text("select a file to Compress")
input2 = gui.InputText()
selectButton2 = gui.FolderBrowse("Select")
compressButton = gui.Button("Compress")
window = gui.Window("File Zipper", 
                    layout =
                    [[label1, input1, selectButton1],
                     [label2, input2, selectButton2],
                     [compressButton]])
window.read()
window.close()
