
import marshal
import zlib
import lzma
import random
import binascii
import os
import pystyle
from pystyle import *

__Creator__ = 'Brigade Anti-420 ??#7274'


def sun7(banner):
    os.system("")
    faded = ""
    red = 255
    green = 125
    blue = 0
    for line in banner.splitlines():
        faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
        if not green == 255:
            green += 8
            if green > 255:
                green = 255
        if not blue == 0:
            blue -= 8
            if blue < 0:
                blue = 0
        if not red == 255:
            red -= 8
            if red < 245:
                red = 245
    return faded

banner = r"""

 .S    S.     sSSs_sSSs     .S_sSSs     .S       S.     sSSs  
.SS    SS.   d%%SP~YS%%b   .SS~YS%%b   .SS       SS.   d%%SP  
S%S    S%S  d%S'     `S%b  S%S   `S%b  S%S       S%S  d%S'    
S%S    S%S  S%S       S%S  S%S    S%S  S%S       S%S  S%|     
S%S SSSS%S  S&S       S&S  S%S    d*S  S&S       S&S  S&S     
S&S  SSS&S  S&S       S&S  S&S   .S*S  S&S       S&S  Y&Ss    
S&S    S&S  S&S       S&S  S&S_sdSSS   S&S       S&S  `S&&S   
S&S    S&S  S&S       S&S  S&S~YSY%b   S&S       S&S    `S*S  
S*S    S*S  S*b       d*S  S*S   `S%b  S*b       d*S     l*S  
S*S    S*S  S*S.     .S*S  S*S    S%S  S*S.     .S*S    .S*P  
S*S    S*S   SSSbs_sdSSS   S*S    S&S   SSSbs_sdSSS   sSS*S   
SSS    S*S    YSSP~YSSY    S*S    SSS    YSSP~YSSY    YSS'    
       SP                  SP                                 
       Y                   Y                                  
                                                              

"""

banner2 = '''
⠀⠀⠀⠀⣀⣤⣶⠾⠿⠿⠿⠿⢶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣤⠾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⠷⣶⣤⣤⣤⣀⣀⣀⣀⣀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠀⠀
⠀⠀⠀⠀⣠⡾⢛⣽⣿⣿⣏⠙⠛⠻⠷⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀
⠀⠀⢠⣾⣋⡀⢸⣿⣿⣿⣿⠀⠀⢀⣀⣤⣽⡿⠿⠛⠿⠿⠷⠾⠿⠿⠛⠋⠀⠀
⠀⠀⠻⠛⠛⠻⣶⣽⣿⣿⣿⡶⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣿⡏⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⠶⢶⣤⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢹⣯⠁⠀⠈⠛⢷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠸⠧⠀⠀⢹⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠉⠻⠷⣦⣤⣤⣀⣀⣀⣀⣠⣤⡶⠟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀
'''


def encode_hex(data):
    return ''.join(['\\x' + format(b, '02x') for b in data])

def obfuscate():
    print(Center.XCenter(sun7(banner)))
    filename = Write.Input(
    "[+] Drag the file you want to obfuscate -> ", Colors.red_to_yellow, interval=0.005)

    with open(filename, 'r') as f:
        source = f.read()

    code = compile(source, "<string>", "exec")

    data = marshal.dumps(code)

    compressed_data1 = zlib.compress(data)

    compressed_data2 = lzma.compress(compressed_data1)

    compressed_data2_hexa = encode_hex(compressed_data2)




    random_fix = ''.join([random.choice('Il') for _ in range(12)])
    random_prefix = ''.join([random.choice('Il') for _ in range(12)])
    random_suffix = ''.join([random.choice('Il') for _ in range(12)])
    keyvarenc = ''.join([random.choice('Il') for _ in range(12)])
    output_filename = os.path.splitext(os.path.basename(filename))[0] + "-hess.py"

    rdmkey = random.randint(10000, 100000)  
    rdmkey2 = random.randint(10000, 100000) 
    key = rdmkey * rdmkey2  
    rdmkey = str(rdmkey)
    rdmkey2 = str(rdmkey2)
    key = str(key)

    random_fix_var = [ord(c) for c in random_fix]
    random_prefix_var = [ord(c) for c in random_prefix]
    random_suffix_var = [ord(c) for c in random_suffix]

    rdmkeyvar = [ord(c) for c in rdmkey]
    rdmkeyvar2 = [ord(c) for c in rdmkey2]
    keyvar = [ord(c) for c in key]
    keyencrypt = [ord(c) for c in keyvarenc]


    with open(output_filename, 'w') as f:
        f.write(
            f"{random_fix} = eval(bytes({keyvar}).decode())\n{random_prefix} = eval(bytes({rdmkeyvar}).decode())\n{random_suffix}=eval(bytes({rdmkeyvar2}).decode())\nif eval(bytes({random_fix_var}).decode()) == eval(bytes({random_prefix_var}).decode()) * eval(bytes({random_suffix_var}).decode()): \n   {keyvarenc} = eval(bytes([95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115]).decode())(eval(bytes([95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 122, 108, 105, 98, 39, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115]).decode())(eval(bytes([95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 108, 122, 109, 97, 39, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115]).decode())(b'{compressed_data2_hexa}')))\n   eval(bytes([101, 120, 101, 99]).decode())(eval(bytes({keyencrypt}).decode()))#exec")

if __name__ == "__main__":
    obfuscate()
