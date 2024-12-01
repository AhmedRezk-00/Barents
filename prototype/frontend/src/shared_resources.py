# canvas variable to manager the canvas across multiple gui components. 
# this variable allows access to the canvas from all other scripts
canvas = None
editor_mode = 'default'
part_of_set = set()

def set_editor_mode(mode):
    global editor_mode 
    editor_mode = mode
    print('editor is now in mode: ' + editor_mode)