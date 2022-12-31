# Simple-Obfuscator 🐱‍💻
A simple python obfuscator 

# Explanation

The program starts by creating a list of characters, each character representing a different value, based on it's location in the list. <br> Then the program takes your source code and runs it through a base N convertor, then converts each number inside that str into it's respective character inside the previous list. Then the program puts the list, with all the characters inside the obfuscated source code, as well as the code to deobfuscate it, then the program runs it via exec.

# Usage ⚙
Just input the files name into the `input` variable

 - recursion: How many times to encrypt, keep this below 5 at most, because it will start taking a ridiculous amount of time to encrypt and run
 - base: what Base system to use during encryption, must be a whole number and below 10
 - input: filename to obfuscate

# Example

Below is a simple hello world script
```py
pass;k=['%','|','H','"','(','M','j','-','s','L','v','c','5','l','~','2','A','V','<','Q','a','b','R','K','f','0','Y','6','e','i','3','#','_','h','7','=','t','>','E','!','4','^','.','C','8','9','x','?','}','W','*','$',',','`','r','[','O','/','q','T','m','o','1','p','N',':','F','U','+','n',')','y','J',']','k','z',';','&','X','B','Z','g','D','d','P','@','{','G','u','S','w','I'];(eval(''.join([chr(sum([k.index(str(ch))*(93**c) for c, ch in enumerate(str(x)[::-1])]))for x in('|s |6 |s |j'.split(' '))])))(''.join([chr(sum([k.index(str(ch))*(93**c) for c, ch in enumerate(str(x)[::-1])]))for x in('|~ o I ! > ! 8 ! |# ! 8 ! J ! 8 ! 7 ! 8 ! 4 ! 8 ! & ! 8 ! |l ! 8 ! 9 ! 8 ! |R ! 8 ! ; ! 8 ! |0 ! 8 ! |j ! 8 ! ` ! 8 ! |2 ! 8 ! |h ! 8 ! * ! 8 ! : ! 8 ! { ! 8 ! m ! 8 ! g ! 8 ! |( ! 8 ! |M ! 8 ! D ! 8 ! z ! 8 ! |L ! 8 ! } ! 8 ! S ! 8 ! r ! 8 ! |s ! 8 ! |5 ! 8 ! $ ! 8 ! = ! 8 ! |H ! 8 ! |c ! 8 ! [ ! 8 ! o ! 8 ! |K ! 8 ! 1 ! 8 ! n ! 8 ! h ! 8 ! , ! 8 ! || ! 8 ! x ! 8 ! U ! 8 ! O ! 8 ! / ! 8 ! |6 ! 8 ! p ! 8 ! |_ ! 8 ! G ! 8 ! . ! 8 ! t ! 8 ! 8 ! 8 ! |" ! 8 ! |b ! 8 ! I ! 8 ! B ! 8 ! ? ! 8 ! |a ! 8 ! P ! 8 ! |A ! 8 ! |< ! 8 ! W ! 8 ! |Q ! 8 ! X ! 8 ! q ! 8 ! ) ! 8 ! @ ! 8 ! C ! 8 ! |V ! 8 ! ^ ! 8 ! |e ! 8 ! k ! 8 ! |% ! 8 ! |~ ! 8 ! |i ! 8 ! T ! 8 ! E ! 8 ! u ! 8 ! F ! 8 ! w ! 8 ! |v ! 8 ! + ! 8 ! |- ! 8 ! Z ! 8 ! N ! 8 ! |3 ! 8 ! y ! 8 ! |f ! 8 ! d ! 8 ! |Y ! 8 ! ] ! |% T 4 |s |0 |( |2 4 ! ! x |l |< |5 |V 4 I |j |c |b 4 |R |f |A 4 I |~ x |5 |V |- |s |6 4 |R |K |b 4 |j |c ^ ^ . 4 / $ . . |j ^ _ |L |< |b _ |j 8 _ |j |c _ |5 |V _ |s |V |f |A |s |b |( |K |s 4 |R |K |b 4 |6 ^ I q q 9 W |% ^ |% ^ ^ |L |< |b _ |6 _ |5 |V 4 ! |# |R _ |# r _ |# |R _ |# |l ! x |R |Q |2 |5 |K 4 ! _ ! ^ ^ |% ^ ^ ^ 4 ! ! x |l |< |5 |V 4 I |j |c |b 4 |R |f |A 4 I |~ x |5 |V |- |s |6 4 |R |K |b 4 |j |c ^ ^ . 4 / $ . . |j ^ _ |L |< |b _ |j 8 _ |j |c _ |5 |V _ |s |V |f |A |s |b |( |K |s 4 |R |K |b 4 |6 ^ I q q 9 W |% ^ |% ^ ^ |L |< |b _ |6 _ |5 |V 4 ! |# g _ |# |M _ |# ` _ |# { _ |# z _ , _ [ _ k _ |# |R _ |# * _ |# * _ |# m _ |H _ y _ |# m _ |# |M _ |# * _ |# 9 _ |c _ [ _ || ! x |R |Q |2 |5 |K 4 ! _ ! ^ ^ |% ^ ^'.split(' '))]))
```
