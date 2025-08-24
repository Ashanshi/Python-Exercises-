import random

digit3 = "".join(str(random.randint(0, 9)) for _ in range(3))
digit4 = "".join(str(random.randint(1, 6)) for _ in range(4))

print(f"3-digit code: {digit3}")
print(f"4-digit code: {digit4}")