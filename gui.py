import PySimpleGUI as gui
import functions as f

label = gui.Text("type in a name: ")
inputBox = gui.InputText(tooltip = "enter a name", key ='name')
button1 = gui.Button("add")
window = gui.Window("Name Program", 
                    layout=[[label], [inputBox, button1]],
                    font = ('helvetica', 15))


while True:
    event, values = window.read()
    print(event)
    print(values)
    if 'add':
        mylist = f.getNames()
        name = values["name"] + "\n"
        mylist.append(name)
        f.storeNames(mylist)
    if gui.WINDOW_CLOSED:
        break
        
        
        
    
    
window.close()