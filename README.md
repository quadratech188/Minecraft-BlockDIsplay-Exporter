# Minecraft-BlockDIsplay-Exporter
This is a simple project that I worked on for a couple of days, that allows you to export cubes in Blender to a Minecraft datapack containing block display summon commands.

# Requirements
- All cubes must have matching scale and dimensions (Scale by 0.5 in edit mode)
- negative scales will not work (unless you are planning on using the resulting backface culling)
- All cubes must have a material with the name of the corresponding minecraft block

# How To Use
- Paste / open the .py file
- Create a datapack in your minecraft world file
- Paste the .mcfunction filepath to the FILEPATH variable
- Run the script
- Execute the .mcfunction file the normal way (don't forget to reload)
