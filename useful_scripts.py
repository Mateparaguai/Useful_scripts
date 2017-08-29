#Select_all_obj_which_names_start_whith
import bpy

scene = bpy.context.scene

for ob in scene.objects:
    if ob.name.startswith("Obj"):
        ob.select = True
    else: 
        ob.select = False

        
#create new armature in position every selected obj
import bpy

sel_objs = bpy.context.selected_objects
pos = (0.0, 0.0, 0.0)
#arm = ob.data

for m in sel_objs:
    pos = m.location
    bpy.ops.object.armature_add()
    ob = bpy.context.scene.objects.active
    ob.name = "AR" + m.name
    ob.location = pos

#all objects to current z position 
import bpy
sel_objs = bpy.context.selected_objects
for i in sel_objs:
    i.location.z = 0

#delete all materials in scene
all_m = bpy.data.materials
for i in all_m:
    i.user_clear()

#rename_selected_bones
import bpy

mode = bpy.context.object.mode

if mode == "POSE":
    sel = bpy.context.selected_pose_bones
else:
    sel = bpy.context.selected_bones

num = 0
name = 'pose_brow_'
R = '.R'
L = '.L'
for i in sel:
    i.name = str(name) + str(num) + str(R)
    num += 1
    print(i.name) 

#del_all_constraints_from_selected_bones
import bpy

sel_bones = bpy.context.selected_pose_bones

for i in sel_bones:
    consList = i.constraints
    for n in consList:
        i.constraints.remove(n)
