MASK = (1 << 64) - 1          
A, B, C = 221, 5, 0x123456   

def boring_challenge(n: int, m: int) -> int:
    return (((n + A) * m + m + B) * C - m) & MASK
expectedVal = 458138870735950
param1 = 12000019
param2 = 32
result = boring_challenge(param1,param2)
print(result==expectedVal)
