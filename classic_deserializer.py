
from binascii import hexlify
from read_bytes_utils import read_next, read_str
from classic_level_data import ClassicLevelData
class ClassicDeserializer:
    """Class to deserialize minecraft classic level using 3rd format type. 
       For more information check the wiki page: https://minecraft.wiki/w/Java_Edition_Classic_level_format#Third_Format"""
    @staticmethod
    def deserialize(data: bytes):
        shift = 0 #variable amount of byte shift 
        mc_magic_num = read_next(data,0,4)
        version_number = read_next(data,4,5)
        java_serialization_magic_number = read_next(data,5,9)
        obj_token = read_next(data,9,10)
        class_token = read_next(data,10,11)        
        class_name = read_str(data,11)
        shift+= len(class_name)
        print(class_name)
        
        
        deserialized_data = ClassicLevelData()
        deserialized_data.magic_number = mc_magic_num
        deserialized_data.version_number = version_number

        return deserialized_data
