from nbtlib import Byte,Compound,Int,Short,File, List,ByteArray
from block_ids_enum import ClassicIds
import gzip
import os
CLASSIC_WORLDS_PATH = "./classic_worlds/"
INDEV_WORLDS_PATH = "./indev_worlds/"
#Find world 
print("Classic world converter")
try:
    os.chdir(CLASSIC_WORLDS_PATH)
    classic_worlds = [os.path.join(CLASSIC_WORLDS_PATH,f) for f in os.listdir() if f.endswith('.mine')]
    print(f'Found world {classic_worlds}')
    os.chdir("..")

except:
    print('No worlds found! Check that the file extension is .mine and that you have placed something inside the folder.')
    input()
    exit()
indev_worlds = []
clothes = [
    ClassicIds.RED_CLOTH.value,
    ClassicIds.ORANGE_CLOTH.value,
    ClassicIds.YELLOW_CLOTH.value,
    ClassicIds.CHARTREUSE_CLOTH.value,
    ClassicIds.GREEN_CLOTH.value,
    ClassicIds.SPRING_GREEN_CLOTH.value,
    ClassicIds.CYAN_CLOTH.value,
    ClassicIds.CAPRI_CLOTH.value,
    ClassicIds.ULTRAMARINE_CLOTH.value,
    ClassicIds.PURPLE_CLOTH.value,
    ClassicIds.VIOLET_CLOTH.value,
    ClassicIds.MAGENTA_CLOTH.value,
    ClassicIds.ROSE_CLOTH.value,
    ClassicIds.DARK_GRAY_CLOTH.value,
    ClassicIds.LIGHT_GRAY_CLOTH.value,
    ClassicIds.WHITE_CLOTH.value
]
remove_cloth_blocks = False
cloth_replacer = ClassicIds.BRICKS
if remove_cloth_blocks:
    print(f"Removing cloth block. Replacing with {cloth_replacer.name.capitalize()} (ID:{cloth_replacer.value})")
for world in classic_worlds:
    #read world file
    world_name = world.split('.')[1].split("/")[2]
    file = open(world, 'rb')
    raw_data = file.read()
    file.close()
    #Decode level

    print('Decoding level...')

    classic_file = gzip.decompress(raw_data)[20630:4214934]

    blocks = []

    for byte in classic_file:
        if remove_cloth_blocks and byte in clothes:
            byte = cloth_replacer.value
        blocks.append(Byte(byte))

    #Make *.mclevel

    print('Creating indev level file...')

    new_file = File({
        'MinecraftLevel': Compound({
            'Environment': Compound({
                'CloudColor': Int(16777215),
                'CloudHeight': Short(66),
                'FogColor': Int(16777215),
                'SkyBrightness': Byte(100),
                'SkyColor': Int(10079487),
                'SurroundingGroundHeight': Short(23),
                'SurroundingGroundType': Byte(2),
                'SurroundingWaterHeight': Short(32),
                'SurroundingWaterType': Byte(8),
                }),
            'Map': Compound({
                'Spawn': List[Short]([Short(128), Short(36), Short(128)]),
                'Height': Short(64),
                'Length': Short(256),
                'Width': Short(256),
                'Blocks': ByteArray(blocks),
                'Data': ByteArray([Byte(15)] * 4194304)
                })
            })
        })
    new_world_path = os.path.join(INDEV_WORLDS_PATH,f"{world_name}.mclevel")
    indev_worlds.append(new_world_path)
    new_file.save(new_world_path, gzipped=True)

print(f'Converted worlds {classic_worlds} to {indev_worlds} indev  save format')
