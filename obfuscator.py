import random, base64, string, names, zlib, math
from tqdm import tqdm

recursion = 1 # get's exponentially laggier, the higher this number, but more "encrypted"
base = 15000 # Must be a whole number, 2 - 55000
indent = 0 # How many indents should be used to space out the actual code and the pass. Used to hide the code from a IDE
bytes_allowed = True # If disabled then base cannot be above 93
invisble_characters = True # Use invisible characters
compress = False # compress code
input = "example.py" # file to obfuscate


code = open(input, "rb").read().decode()
if bytes_allowed:
    key = characters = list(map(chr, range(94, 94+base)))
else:
    key = characters = list(map(chr, range(33, 34+base)))

blacklist = ["'", "`", "\\"]

for item in blacklist:
    if item in key:
        key.remove(item)
        base -= 1

random.shuffle(key)
highest = 0

def encode(x, base):
    global highest, key
    if not x:
        return key[0]
    
    log = math.floor(math.log(x, base))

    st = [0]*(log+1)
    st[-1] = 1
    if log:
        x -= base**log

    while True:
        if x >= base:
            log = math.floor(math.log(x, base))
            x -= base**log
            st[log] += 1 
            if st[log] > highest: highest = st[log]
        else:
            st[0] = x
            if st[0] > highest: highest = x
            return ''.join([str(key[char] )for char in st[::-1]])

def decode(x, base):
    result = 0
    for count, char in enumerate(str(x)[::-1]):
        result += int(key.index(str(char)))*(base**count)

    return result

for n in tqdm(range(recursion)):
    
    if n+1 == recursion:
        message = f"pass{'  '*indent};"
        if invisble_characters:
            base = 2
            key = ['​', '‍', '‎']
    else:
        message = ''
        random.shuffle(key)

    enc = '‌'.join([ (str(encode(ord(chr), base))) for chr in code])
    enc2 = ' '.join([ (str(encode(ord(chr), base))) for chr in 'exec'])
    enc3 = ' '.join([ (str(encode(ord(chr), base))) for chr in 'compile'])
    src = f"""{message}k='{''.join(key)}';(eval(eval(''.join([chr(sum([k.index(str(ch))*({hex(base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc3}'.split(' '))]))(''.join([chr(sum([k.index(str(ch))*({hex(base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc2}'.split(' '))]), "", dir(__builtins__)[0x69-1])))(eval(''.join([chr(sum([k.index(str(ch))*({hex(base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc3}'.split(' '))]))(''.join([chr(sum([k.index(str(ch))*({hex(base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc}'.split('‌'))]), "", dir(__builtins__)[0x6a-1]))"""
    if compress:
        src = f'''eval(dir(__builtins__)[0x6a-1])(__import__('zlib').decompress(__import__('base64').b64decode(b'{base64.b64encode(zlib.compress(src.encode())).decode()}')).decode())'''
    print(len(enc), len(code), len(enc), len(src))
    # print(enc)

with open(f'{input} (output).py', 'wb') as file:
    file.write(src.encode())

# print(src)