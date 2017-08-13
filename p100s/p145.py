def solve():
    limit = 9
    odd_outside = 20
    odd_inside = 30
    even_no_carry = 25
    mid_points = 5
    total = 0
    for i in range(2, limit+1):
        if i % 2 == 0:
            total += odd_outside * odd_inside**((i-2)//2)
        elif i % 4 == 1:
            pass
        elif i % 4 == 3:
            total += mid_points * odd_outside * (even_no_carry * odd_outside) ** (i//4)
    return total
