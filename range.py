"""
range created a range
3 options
range(start,stop,jump)
1- range (stop) - from 0 to stop (not included) - range(0,stop,1)
2- range(start,stop)- from start to stop (not included)- range(start,stop,1)
3 - range(start,stop,jump) - from start to stop with jumping of jump
"""

print(list(range(6)))  # 0,1,2,3,4,5
print(list(range(2, 7)))  # 2,3,4,5,6
print(list(range(2, 11, 2)))  # 2,4,6,8,10
print(list(range(24, 30, 2)))  # 24,26,28 - 30 isn't included in range!!

