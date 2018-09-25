#!/usr/bin/env python3

'''
http://www.pythonchallenge.com/pc/def/274877906944.html
'''

cyphered_s = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr "
              "amknsrcpq ypc dmp. bmgle gr gl zw fylb gq "
              "glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. "
              "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu "
              "ynnjw ml rfc spj."
              )

clear_l = []

for c in cyphered_s:
    if " " == c or "." == c or "'" == c or "(" == c or ")" == c:
        t = c
    elif "y" == c:
        t = "a"
    elif "z" == c:
        t = "b"
    else:
        t = chr(ord(c) + 2)
    clear_l.append(t)

clear_s = ''.join(clear_l)

print(clear_s)

intab = "yzabcdefghijklmnopwrstuvwx"
outtab = "abcdefghijklmnopwrstuvwxyz"
trantab = str.maketrans(intab, outtab)

s = "map"
t = "http://www.pythonchallenge.com/pc/def/{}.html".format(s.translate(trantab))
print()
print(t)
print()
