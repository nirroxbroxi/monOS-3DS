import sys
import struct

def build_firm(bin_path, firm_path):
    with open(bin_path, 'rb') as f:
        code = f.read()

    # En-tête de 512 octets (0x200) pour format FIRM 3DS
    header = bytearray(0x200)
    
    # Magic 'FIRM'
    header[0:4] = b'FIRM'
    
    # Entrypoint ARM9 & Adresse de chargement (0x08000000)
    struct.pack_into('<I', header, 0x08, 0x08000000) # ARM9 entrypoint
    struct.pack_into('<I', header, 0x40, 0x00000000) # Section 0 offset
    struct.pack_into('<I', header, 0x44, 0x08000000) # Section 0 address
    struct.pack_into('<I', header, 0x48, len(code))   # Section 0 size

    with open(firm_path, 'wb') as f:
        f.write(header)
        f.write(code)

if __name__ == '__main__':
    build_firm(sys.argv[1], sys.argv[2])
