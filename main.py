def boring_challenge(n: int, m: int) -> int:
    return ((n + 221) * m + m + 5) * 0x123456 - m
expectedVal = 458138870735950
param1 = 12000019
param2 = 32
result = boring_challenge(param1,param2)
print(result==expectedVal)
