#!/usr/bin/python

def hexdump(src, length = 16):
    result = []
    digits = 2 if isinstance(src, str) else 4
    for i in range(0, len(src), length):
        s = src[i:i+length]
        hexa = ' '.join(['%0*X' % (digits, ord(x)) for x in s])
        text = ''.join([x if 0x20 <= ord(x) < 0x7F else '.' for x in s])
        result.append('%04X  %-*s   %s' % (i, length*(digits + 1), hexa, text))
    print('\n'.join(result))


hexdump('我爱小仙女')

