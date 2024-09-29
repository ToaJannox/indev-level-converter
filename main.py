import gzip
from classic_deserializer import ClassicDeserializer


file_path = "test_data/test-c.mine"
level_file = open(file_path,"rb")
raw_data = level_file.read()
level_file.close()

uncompressed_data = gzip.decompress(raw_data)
uncompressed_file= open("test_data/test_uncomp","wb+")
uncompressed_file.write(uncompressed_data)
uncompressed_file.close()

deserialized_data = ClassicDeserializer.deserialize(uncompressed_data)

print(deserialized_data)

