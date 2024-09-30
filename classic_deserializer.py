
from binascii import hexlify
from read_bytes_utils import read_next, read_str,read_short
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
        shift+= len(class_name)+2
        print(class_name)
        uuid = read_next(data,11+shift,19+shift)
        class_handle = read_next(data,19+shift,20+shift)
        nb_of_field = read_short(data,20+shift)
        print(nb_of_field)
        
        
        deserialized_data = ClassicLevelData()
        deserialized_data.magic_number = mc_magic_num
        deserialized_data.version_number = version_number

        return deserialized_data
