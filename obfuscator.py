import random, base64, string, names, math
from tqdm import tqdm

recursion = 5 # get's exponentially laggier, the higher this number, but more "encrypted"
base = 512 # Must be a whole number, 2 - inf
indent = 0 # How many indents should be used to space out the actual code and the pass. Used to hide the code from a IDE
bytes_allowed = True # If disabled then base cannot be above 93
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
    global highest
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
enc3 = ' '.join([ str(encode(ord(chr), base)) for chr in 'compile'])

for n in tqdm(range(recursion)):
    enc = '`'.join([ str(encode(ord(chr), base)) for chr in code])
    
    if n+1 == recursion:
        message = f"pass{'  '*indent};"
    else:
        message = ''
    src = f"""{message}k='{''.join(key)}';(eval(eval(''.join([chr(sum([k.index(str(ch))*({base}**c) for c, ch in enumerate(str(x)[::-1])]))for x in('{enc3}'.split(' '))]))(''.join([chr(sum([k.index(str(ch))*({base}**c) for c, ch in enumerate(str(x)[::-1])]))for x in('{enc2}'.split(' '))]), "", "eval")))(eval(''.join([chr(sum([k.index(str(ch))*({base}**c) for c, ch in enumerate(str(x)[::-1])]))for x in('{enc3}'.split(' '))]))(''.join([chr(sum([k.index(str(ch))*({base}**c) for c, ch in enumerate(str(x)[::-1])]))for x in('{enc}'.split('`'))]), "", "exec"))"""
    code = src.replace('-.', '-1')

with open('output.py', 'wb') as file:
    file.write(src.encode())

print(src)
