from binascii import hexlify
def print_hex_value(byte_stream: bytes):
    print(hexlify(byte_stream," ",1).decode())

def read_next(data: bytes,start:int,end:int):
    read_data = data[start:end]
    print_hex_value(read_data)
    return read_data

def read_str(data:bytes, start:int):
    length_bytes = read_next(data,start,start+2)
    length = int.from_bytes(length_bytes)
    string_bytes = read_next(data,start+2,start+2+length)
    return string_bytes.decode("utf-8")

