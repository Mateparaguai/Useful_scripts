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
