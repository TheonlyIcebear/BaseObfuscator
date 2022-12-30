import base64, names, math

recursion = 1 # get's exponentially laggier, the higher this number, but more "encrypted"
base = 7 # only works from base 1 - 10
input = "example.py" # file to obfuscate

code = open(input)

def encode(x, base):
    log = math.floor(math.log(x, base))
    st = [0]*(log+1)
    st[-1] = 1
    x -= base**log
    while True:
        if x >= base:
            log = math.floor(math.log(x, base))
            x -= base**log
            st[log] += 1 
        else:
            st[0] = x
            return int(''.join([str(char )for char in st[::-1]]))


def decode(x, base):
    result = 0
    for count, char in enumerate(str(x)[::-1]):
        result += int(char)*(base**count)

    return result

for n in range(recursion):
    list = [names.get_first_name() for _ in range(4)]
    enc = ' '.join([ str(encode(ord(chr), base)) for chr in code])
    if n+1 == recursion:
        indent = '  '*5000
    else:
        indent = '  '*20
    src = f"""{list[0]}='{enc}'{indent};{list[1]}=exec;{list[1]}(''.join([chr(sum([int(ch)*({base}**c) for c, ch in enumerate(str(x)[::-1])]))for x in({list[0]}.split(' '))]))"""
    code = src

with open('output.py', 'wb') as file:
    file.write(src.encode())

print(src)