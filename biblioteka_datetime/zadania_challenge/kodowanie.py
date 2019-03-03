#tekst = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb \
        #'rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


from string import ascii_lowercase

print(ascii_lowercase)

#abcdefghijklmnopqrstuvwxyz
#yzabcdefghijklmnopqrstuvwx

tekst = 'map'
shift = 2

shifted_ascii = 'yzabcdefghijklmnopqrstuvwx'


out= ''
for i in tekst:
    if i in ascii_lowercase:
        ii = shifted_ascii.index(i)
        out += ascii_lowercase[ii]
    else:
        out += i

print(out)