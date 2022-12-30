import base64, string, names, math
from tqdm import tqdm

recursion = 2 # get's exponentially laggier, the higher this number, but more "encrypted"
base = 72 # Must be a whole number, 1 - 72
input = "example.py" # file to obfuscate

code = open(input, "r+").read()
key = ["#", "$", "@", "&", "^", "!", "&", "*", "<", ">", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] + list(string.ascii_lowercase) + list(string.ascii_uppercase)

def encode(x, base):
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
        else:
            st[0] = x
            return ''.join([str(key[char] )for char in st[::-1]])


def decode(x, base):
    result = 0
    for count, char in enumerate(str(x)[::-1]):
        result += int(key.index(str(char)))*(base**count)

    return result

enc2 = ' '.join([ str(encode(ord(chr), base)) for chr in 'exec'])

for n in tqdm(range(recursion)):
    enc = ' '.join([ str(encode(ord(chr), base)) for chr in code])
    
    if n+1 == recursion:
        indent = '  '*20000
        message = 'pass;'
    else:
        indent = ''
        message = ''
    src = f"""{message}{indent}k={str(key).replace(' ', '')};(eval(''.join([chr(sum([k.index(str(ch))*({base}**c) for c, ch in enumerate(str(x)[::-1])]))for x in('{enc2}'.split(' '))])))(''.join([chr(sum([k.index(str(ch))*({base}**c) for c, ch in enumerate(str(x)[::-1])]))for x in('{enc}'.split(' '))]))"""
    code = src.replace('-.', '-1')

with open('output.py', 'wb') as file:
    file.write(src.encode())

print(src)
