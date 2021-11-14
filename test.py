pre = 128
hour = (0b1111000000 & pre) >> 4
minute = 0b0000111111 & pre
print(hour, minute)