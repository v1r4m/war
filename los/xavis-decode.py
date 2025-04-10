import struct

d = 0xc6b00000c6550000ad730000000000000000000000000000000000000000

def is_valid_utf16(bytes_chunk):
    try:
        return bytes_chunk.decode('utf-16-le')
    except UnicodeDecodeError:
        return "[non-utf16]"

def parse_hex_advanced(data):
    hex_str = hex(data)[2:].rjust(64, '0')
    chunks_4b = [hex_str[i:i+8] for i in range(0, len(hex_str), 8)]

    print("==== 4-Byte UTF-16/ASCII/Float/Int Analysis ====")
    for i, chunk in enumerate(chunks_4b):
        b = bytes.fromhex(chunk)
        b_le = b[::-1]

        print(f"\nChunk {i+1}: 0x{chunk}")

        # UTF-16 해석 (Little Endian)
        utf16_try = is_valid_utf16(b)
        utf16_try_le = is_valid_utf16(b_le)

        # 기존 해석
        try: ascii_text = b.decode('ascii')
        except: ascii_text = "[non-ascii]"

        float_val = struct.unpack(">f", b)[0]
        float_val_le = struct.unpack("<f", b_le)[0]

        print(f"  ASCII           : {ascii_text}")
        print(f"  UTF-16          : {utf16_try}")
        print(f"  UTF-16 (LE)     : {utf16_try_le}")
        print(f"  Float (BE)      : {float_val}")
        print(f"  Float (LE)      : {float_val_le}")
        print(f"  Int (BE, signed): {struct.unpack('>i', b)[0]}")
        print(f"  Int (LE, signed): {struct.unpack('<i', b)[0]}")
        
parse_hex_advanced(d)
