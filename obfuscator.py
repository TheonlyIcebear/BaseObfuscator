import random
import base64
import zlib
import math
from tqdm import tqdm
import customtkinter as ctk
from tkinter import filedialog

class Obfuscator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.recursion = 1
        self.base = 26
        self.indent = 0
        self.bytes_allowed = False
        self.invisible_characters = False
        self.compress = False
        self.code = self.read_file()

    def read_file(self):
        with open(self.file_path, "rb") as f:
            return f.read().decode()

    def generate_key(self):
        if self.bytes_allowed:
            key = list(map(chr, range(94, 94+50000)))
        else:
            key = list(map(chr, range(33, 95)))

        key = ''.join(key)

        blacklist = ["'", "`", '"', "\\", "\x00", "\n", "\r"]
        for item in blacklist:
            if item in key:
                key = key.replace(item, "")


        key = list(key)
        key = ''.join(random.sample(key, self.base))

        return key

    def encode(self, x, key, base):
        result = [(x // (base ** i)) % base for i in range(int(math.log(x, base)) + 1)]
        return ''.join([str(key[char]) for char in result[::-1]])
        

    def obfuscate(self):
        base = self.base
        for n in tqdm(range(self.recursion)):
            key = self.generate_key()
            if n+1 == self.recursion:
                message = f"pass{'  '*self.indent};"
                if self.invisible_characters:
                    base = 2
                    key = ['​', '‍', '‎']
            else:
                message = ''
                random.shuffle(key)

            enc = '‌'.join([ (str(self.encode(ord(chr), key, base))) for chr in self.code])
            enc2 = ' '.join([ (str(self.encode(ord(chr), key, base))) for chr in 'exec'])
            enc3 = ' '.join([ (str(self.encode(ord(chr), key, base))) for chr in 'compile'])
            src = f"""{message}lf1=lambda m: ''.join([ch[m**--++++0x0-1] for ch in r'{''.join(key)}']);(eval(eval(''.join([chr(sum([lf1(++{base}**2).index(str(ch))*({hex(self.base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc3}'.split(' '))]))(''.join([chr(sum([lf1(++{self.base}**2).index(str(ch))*({hex(self.base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in(r'{enc2}'.split(' '))]), "", dir(__builtins__)[0x69-1])))(eval(''.join([chr(sum([lf1(++{self.base}**2).index(str(ch))*({hex(self.base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in(r'{enc3}'.split(' '))]))(''.join([chr(sum([lf1(++{self.base}**2).index(str(ch))*({hex(self.base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in(r'{enc}'.split('‌'))]), "", dir(__builtins__)[0x6a-1]))"""
            if self.compress:
                src = f'''eval(dir(__builtins__)[0x6a-1])(__import__('zlib').decompress(__import__('base64').b64decode(b'{base64.b64encode(zlib.compress(src.encode())).decode()}')).decode())'''

        output_file = f'{self.file_path} (output).py'
        with open(output_file, 'wb') as file:
            file.write(src.encode())

        print(f"Obfuscated code written to {output_file}")

def browse_file():
    input_file = filedialog.askopenfilename(title="Select File to Obfuscate")
    obfuscator = Obfuscator(input_file)
    obfuscator.obfuscate()

if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("400x200")
    app.title("Python Obfuscator || UI Made By Lunar/Associable") # Obfuscator logic is mine but the GUI code is from https://github.com/Associable/obfuscator

    ctk.set_default_color_theme("dark-blue")

    file_label = ctk.CTkLabel(app, text="")
    file_label.pack(pady=20)

    browse_button = ctk.CTkButton(app, text="Browse", command=browse_file)
    browse_button.pack(pady=10)

    app.mainloop()
    
    
    
