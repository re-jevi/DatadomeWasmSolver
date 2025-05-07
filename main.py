def boring_challenge(n: int, m: int) -> int:
    return 0x123456 * (n * m + 7109) - m
expectedVal = 458138870735950
param1 = 12000019
param2 = 32
result = boring_challenge(param1,param2)
print(result==expectedVal)
