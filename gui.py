import PySimpleGUI as gui
import functions

label = gui.Text("type in a name: ")
inputBox = gui.InputText("enter a name")
button1 = gui.Button("add")
window = gui.Window("Name Program", layout=[[label], [inputBox, button1]])
window.read()
window.close()