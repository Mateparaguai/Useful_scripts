#Select_all_obj_which_names_start_whith
import bpy

scene = bpy.context.scene

for ob in scene.objects:
    if ob.name.startswith("Obj"):
        ob.select = True
    else: 
        ob.select = False


#all objects to current z position 
import bpy
sel_objs = bpy.context.selected_objects
for i in sel_objs:
    i.location.z = 0

#delete all materials in scene
all_m = bpy.data.materials
for i in all_m:
    i.user_clear()

#remane_some_text_in_all_materials
import bpy
import string
all_mat = bpy.data.materials
keep_wd = '.002'
for mat in all_mat:
    if keep_wd in mat.name:
        mat.name = mat.name.replace('.002','')
    else:
        pass
    
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

