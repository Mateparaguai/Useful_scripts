#Select_all_obj_which_names_start_whith
import bpy

scene = bpy.context.scene

for ob in scene.objects:
    if ob.name.startswith("Obj"):
        ob.select = True
    else: 
        ob.select = False
