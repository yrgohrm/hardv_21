# http://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm

def create_bmp(height, width):
    bmp_file = bytearray(b'BM')

    file_size = height*width*3 + 54

    # File size 4 bytes, placeholder
    bmp_file += file_size.to_bytes(4, byteorder="little")

    # 4 bytes reserved
    bmp_file += b'\x00\x00\x00\x00'

    # Data offset 4 bytes
    bmp_file += b'\x36\x00\x00\x00'

    # info header size 4 bytes
    bmp_file += b'\x28\x00\x00\x00'

    # width, 4 bytes
    bmp_file += width.to_bytes(4, byteorder="little")

    # height, 4 bytes
    bmp_file += height.to_bytes(4, byteorder="little")

    # planes, 2 byte (always 1)
    bmp_file += b'\x01\x00'

    # bits per pixel, 2 bytes, 0x18 = 24 bits
    bmp_file += b'\x18\x00'

    # compression, 4 bytes, 0 = no compression
    bmp_file += b'\x00\x00\x00\x00'

    # image size, 4 bytes, can be zero if comp = 0
    bmp_file += b'\x00\x00\x00\x00'

    # x pixels per meter, 4 bytes, 0xb13 = 2835 ca. 72 ppi
    bmp_file += b'\x13\x0b\x00\x00'

    # y pixels per meter, 4 bytes
    bmp_file += b'\x13\x0b\x00\x00'

    # colors used, 4 bytes
    bmp_file += b'\xFF\xFF\xFF\x00'

    # important colors, 4 bytes, 0 = all
    bmp_file += b'\x00\x00\x00\x00'

    for y in range(width):
        for x in range(height):
            red = y % 256
            green = x % 256
            blue = (x*y) % 256
            bmp_file += blue.to_bytes(1, byteorder="little")
            bmp_file += green.to_bytes(1, byteorder="little")
            bmp_file += red.to_bytes(1, byteorder="little")

    with open("out.bmp", "wb") as file:
        file.write(bmp_file)

create_bmp(240, 240)
