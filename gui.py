import PySimpleGUI as gui
import functions as f

label = gui.Text("type in a name: ")
inputBox = gui.InputText(tooltip="enter a name", key='name')
addButton = gui.Button("add")
editButton = gui.Button("edit")
listBox = gui.Listbox(f.getNames(), key="names", enable_events=True, size=[40, 10])

window = gui.Window("Name Program",
                    layout=[[label], [inputBox, addButton], [listBox, editButton]],
                    font=('helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'add':
            mylist = f.getNames()
            name = values["name"] + "\n"
            mylist.append(name)
            f.storeNames(mylist)
            window['names'].update(values=mylist)
        
        case 'edit':
            nameEdit = values["names"][0]
            newName = values['name']
            mylist = f.getNames()
            index = mylist.index(nameEdit)
            mylist[index] = newName + "\n"
            f.storeNames(mylist)
            window['names'].update(values=mylist)
        
        case gui.WINDOW_CLOSED:
            break

window.close()
