from nicegui import ui
import OrbitFinder as of
import re
import ast

data = {'orbit':'The orbit will show up here.', 'rot num':'', 'dep seq':''}

with ui.column():
    with ui.card().tight():
        with ui.row().classes('items-center'):
            #ui.label('Degree:')
            #degree = ui.input('degree', validation={'Not a Positive Integer': lambda v: v.isdigit()}).without_auto_validation()
            #degree.on('blur', degree.validate)
            
            ui.label('Rotation Number:')
            rot_num = ui.input('Ex: 2/5', validation={'Invalid Rotation Number': lambda v: re.search('^\\d+/\\d+$', v)}).without_auto_validation().bind_value(data, 'rot num')
            rot_num.on('blur', rot_num.validate)
            #with ui.column():
                #numerator = ui.input('numerator', validation={'Not a Positive Integer': lambda v: v.isdigit()}).without_auto_validation()
                #numerator.on('blur', numerator.validate)
                #denominator = ui.input('denominator', validation={'Not a Positive Integer': lambda v: v.isdigit()}).without_auto_validation()
                #denominator.on('blur', denominator.validate)
                
            ui.label('Deployment Sequence:')
            dep_seq = ui.input('Ex: (1,3)', validation={'Invalid Deployment Sequence': lambda v: re.search('^\\(\\d+(,\\s*\\d+)*\\)$', v)}).without_auto_validation().bind_value(data, 'dep seq')
            dep_seq.on('blur', dep_seq.validate)
        ui.button('Calculate', on_click=lambda: do_calculation(data['rot num'], data['dep seq']) if(rot_num.value != '' and dep_seq.value != '') else ui.notify('Blank Input Field Detected.'))
    with ui.card().style('width: 900px; height: 100px'):
        ui.label('Orbit:')
        ui.label().bind_text_from(data, 'orbit')
        
def do_calculation(r, s):
    print(r)
    print(s)
    #in_degree = int(d)
    in_rot_num = r.split('/')
    in_rot_num = [int(n) for n in in_rot_num]
    in_dep_seq = ast.literal_eval(s)
    in_dep_seq = list(in_dep_seq)
    raw_orbit = of.getOrbit(in_dep_seq, in_rot_num)
    raw_orbit = raw_orbit[0]
    print(in_dep_seq)
    print(in_rot_num)
    print(raw_orbit)
    
    orbit_list = ["".join(str(i) for i in raw_orbit)]
    for i in range(in_rot_num[1]-1):
        orbit_list.append(orbit_list[i][1:]+orbit_list[i][0])
    for i in range(len(orbit_list)):
        orbit_list[i] = "_"+orbit_list[i]
    print(orbit_list)
    data.update(orbit = ", ".join(orbit_list))
    
    
    return
        
ui.run()