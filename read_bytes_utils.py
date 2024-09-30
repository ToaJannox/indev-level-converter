from binascii import hexlify
BYTE_SIZE = 1
SHORT_SIZE = 2
INT_SIZE = 4
LONG_SIZE = 8

def print_hex_value(byte_stream: bytes):
    print(hexlify(byte_stream," ",1).decode())

def read_next(data: bytes,start:int,end:int):
    read_data = data[start:end]
    print_hex_value(read_data)
    return read_data

def read_byte(data:bytes, start):
    return read_next(data,start,start+BYTE_SIZE)

def read_char(data:bytes, start:int):
    return read_byte(data,start).decode("utf-8")

def read_short(data,start):
    return int.from_bytes(read_next(data,start,start+SHORT_SIZE))

def read_int(data,start):
    return int.from_bytes(read_next(data,start,start+INT_SIZE))

def read_long(data,start):
    return int.from_bytes(read_next(data,start,start+LONG_SIZE))

def read_str(data:bytes, start:int):
    length = read_short(data,start)
    str_start = start+SHORT_SIZE
    str_end = str_start+length
    string_bytes = read_next(data,str_start,str_end)
    return string_bytes.decode("utf-8")

def match_type(type_token:str):
    match(type_token):
        case 'I':
            return int
        case 'B':
            return bytes

def read_field(data:bytes,start:int):
    type_char = read_char(data,start)
    field_name = read_str(data,start+BYTE_SIZE)



