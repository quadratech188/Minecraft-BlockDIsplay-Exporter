
import bpy
import mathutils
from os.path import dirname, join

joined_command = ""

for object in bpy.data.objects:
    
    if object.type != 'MESH':
        continue
    
    transform = object.matrix_world.copy()
    
    # change center to -x, +y, -z
    
    position = object.matrix_world.to_translation() + object.matrix_world.to_quaternion() @ -(object.dimensions) / 2
    
    transform[0][3] = position.x
    transform[1][3] = position.y
    transform[2][3] = position.z
    
    transform = mathutils.Matrix([(1, 0, 0, 0), (0, 0, 1, 0), (0, -1, 0, 0), (0, 0, 0, 1)]) @ transform # z-up to y-up
    
    material_slots = object.material_slots
    
    if object.material_slots == []:
        print("no material:" + object.name + ", omitting")
        continue
        
    
    transform_list = list(transform[0]) + list(transform[1]) + list(transform[2]) + list(transform[3])
    
    transform_string = "["
    
    for element in transform_list:
        transform_string = transform_string + str(element) + ", "
        
    transform_string = transform_string[:-2] + "]"
    
    summon_command = 'summon minecraft:block_display ~ ~ ~ {block_state:{Name:"' + material_slots[0].name + '"}, transformation: ' + transform_string + '}'
    
    joined_command = joined_command + summon_command + "\n"
    
    
print(joined_command)

# path to your datapack
    
FILEPATH = '(World Directory)/datapacks/blockdisplayexport/data/blockexport/functions/export.mcfunction'
    
with open(FILEPATH,'w') as file_object:
    file_object.write(joined_command)
