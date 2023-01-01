# Simple-Obfuscator 🐱‍💻
A simple python obfuscator 

# Explanation

The program starts by creating a list of characters, each character representing a different value, based on it's location in the list. <br> Then the program takes your source code and runs it through a base N convertor, then converts each number inside that str into it's respective character inside the previous list. Then the program puts the list, with all the characters inside the obfuscated source code, as well as the code to deobfuscate it, then the program runs it via exec.

Below is a simple hello world script (Obfuscated 2 extra times)
```py
pass;k='(:uaHFYv.P]^/7&RhXO3jb<x_ofc\ZK"0n#2dSy,Q>-eUMw?Cq=4{6|18%G*)!stN9AT[B@~g;IDim5lk+$}rJWLVzEp';(eval(compile(''.join([chr(sum([k.index(str(ch))*(91**c) for c, ch in enumerate(str(x)[::-1])]))for x in(':] :Z :] :.'.split(' '))]), "", "eval")))(compile(''.join([chr(sum([k.index(str(ch))*(91**c) for c, ch in enumerate(str(x)[::-1])]))for x in(':h`!`,`Q`G`:f`:Y`g`@`z`:c`w`k`:u`:a`?`1`y`$`:7`V`l`4`:R`:v`)`:Z`:H`:j`:^`:.`::`E`D`#`C`:3`2`=`:P`}`:K`U`+`s`M`:]`J`m`:\`t`T`:<`!`{`:0`|`:n`q`8`S`~`-`>`n`:_`:o`5`%`9`r`:(`A`N`:2`:/`*`;`[`:&`:O`6`:X`:h`e`d`:#`:x`I`L`i`W`:"`B`:b`,`*`Q`:]`:c`:Y`:X`Q`:.`:j`:O`:b`:&`:X`:]`Q`,`,`w`:R`:j`:&`:3`Q`:(`:.`:7`:x`Q`:_`:f`:O`Q`:(`:h`w`:&`:3`:P`:]`:Z`Q`:_`:o`:x`Q`:.`:7`>`>`-`Q`%`q`-`-`:.`>`0`:^`:j`:x`0`:.`U`0`:.`:7`0`:&`:3`0`:]`:3`:f`:O`:]`:x`:Y`:o`:]`Q`:_`:o`:x`Q`:Z`>`:(`G`G`M`q`:u`>`:u`>`>`:^`:j`:x`0`:Z`0`:&`:3`Q`,`G`:u`0`G`E`0`G`:u`0`G`w`,`w`:_`:b`:X`:&`:o`Q`,`0`,`>`>`:u`>`U`0`#`#`U`0`#`:]`:c`:Y`:X`#`>`>`>`Q`:.`:j`:O`:b`:&`:X`:]`Q`,`,`w`:R`:j`:&`:3`Q`:(`:.`:7`:x`Q`:_`:f`:O`Q`:(`:h`w`:&`:3`:P`:]`:Z`Q`:_`:o`:x`Q`:.`:7`>`>`-`Q`%`q`-`-`:.`>`0`:^`:j`:x`0`:.`U`0`:.`:7`0`:&`:3`0`:]`:3`:f`:O`:]`:x`:Y`:o`:]`Q`:_`:o`:x`Q`:Z`>`:(`G`G`M`q`:u`>`:u`>`>`:^`:j`:x`0`:Z`0`:&`:3`Q`,`G`:v`:F`G`:Z`:F`G`y`:F`G`4`:F`G`:j`:F`+`:F`2`:F`:/`:F`G`:u`:F`G`V`:F`G`V`:F`G`:R`:F`C`:F`i`:F`G`:R`:F`G`:Z`:F`G`V`:F`G`k`:F`:3`:F`2`:F`s`,`w`:_`:b`:X`:&`:o`Q`,`:F`,`>`>`:u`>`U`0`#`#`U`0`#`:]`:Z`:]`:.`#`>`>'.split('`'))]), "", "exec"))
```

# Usage ⚙
Just input the files name into the `input` variable

 - recursion: How many times to encrypt, keep this below 100 at most, because it will start taking a ridiculous amount of time to encrypt and run
 - base: what Base system to use during encryption, must be a whole number, can go all the way up to infinity, unless you disable `bytes_allowed`. 
   - ⚠ The higher the base the longer it'll take to run, generally keep it below 1024
 - input: filename to obfuscate
 - bytes_allowed: Wether or not the program is allowed to use byte characters
