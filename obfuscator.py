import random
import base64
import zlib
import math
from tqdm import tqdm

class Obfuscator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.recursion = 1
        self.base = 2
        self.indent = 0
        self.bytes_allowed = False
        self.invisible_characters = False
        self.compress = False
        self.code = self.read_file()
        self.key = self.generate_key()
        self.highest = 0

    def read_file(self):
        with open(self.file_path, "rb") as f:
            return f.read().decode()

    def generate_key(self):
        if self.bytes_allowed:
            key = list(map(chr, range(94, 94+self.base)))
        else:
            key = list(map(chr, range(33, 34+self.base)))

        for item in ["'", "`", "\\"]:
            if item in key:
                key.remove(item)
                self.base -= 1

        random.shuffle(key)
        return key

    def encode(self, x):
        if not x:
            return self.key[0]
        
        log = math.floor(math.log(x, self.base))

        st = [0]*(log+1)
        st[-1] = 1
        if log:
            x -= self.base**log

        while True:
            if x >= self.base:
                log = math.floor(math.log(x, self.base))
                x -= self.base**log
                st[log] += 1 
                if st[log] > self.highest: 
                    self.highest = st[log]
            else:
                st[0] = x
                if st[0] > self.highest: 
                    self.highest = x
                return ''.join([str(self.key[char]) for char in st[::-1]])

    def obfuscate(self):
        for n in tqdm(range(self.recursion)):
            if n+1 == self.recursion:
                message = f"pass{'  '*self.indent};"
                if self.invisible_characters:
                    self.base = 2
                    self.key = ['​', '‍', '‎']
            else:
                message = ''
                random.shuffle(self.key)

            enc = '‌'.join([ (str(self.encode(ord(chr)))) for chr in self.code])
            enc2 = ' '.join([ (str(self.encode(ord(chr)))) for chr in 'exec'])
            enc3 = ' '.join([ (str(self.encode(ord(chr)))) for chr in 'compile'])
            src = f"""{message}lf1=lambda m: ''.join([ch[m**--++++0x0-1] for ch in '{''.join(self.key)}']);(eval(eval(''.join([chr(sum([lf1(++{self.base}**2).index(str(ch))*({hex(self.base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc3}'.split(' '))]))(''.join([chr(sum([lf1(++{self.base}**2).index(str(ch))*({hex(self.base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc2}'.split(' '))]), "", dir(__builtins__)[0x69-1])))(eval(''.join([chr(sum([lf1(++{self.base}**2).index(str(ch))*({hex(self.base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc3}'.split(' '))]))(''.join([chr(sum([lf1(++{self.base}**2).index(str(ch))*({hex(self.base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc}'.split('‌'))]), "", dir(__builtins__)[0x6a-1]))"""
            if self.compress:
                src = f'''eval(dir(__builtins__)[0x6a-1])(__import__('zlib').decompress(__import__('base64').b64decode(b'{base64.b64encode(zlib.compress(src.encode())).decode()}')).decode())'''
            print(len(enc), len(self.code), len(enc), len(src))

        with open(f'{self.file_path} (output).py', 'wb') as file:
            file.write(src.encode())

if __name__ == "__main__":
    obfuscator = Obfuscator("C:\\Users\\Username\\Desktop\\file.py")
    obfuscator.obfuscate()
