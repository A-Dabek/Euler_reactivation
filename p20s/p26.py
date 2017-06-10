l_size = 20000


def fraction(denom):
    f_digits = []
    base = 10
    for i in range(l_size):
        while base < denom:
            base *= 10
        f_digits.append(str(int(base / denom)))
        base -= denom * (base // denom)
        if base == 0:
            break
    return f_digits


def find_occurences(l_digits):
    super_key = ('', 0)
    if len(l_digits) < l_size:
        return super_key

    number = ''.join(l_digits)

    for length in range(3, l_size // 10):
        for offset in range(l_size // 10):
            key = ''.join(l_digits[offset:offset + length])

            if len(key) % 2 == 0 and key[:len(key) // 2] == key[-len(key) // 2:]:
                return key[:len(key) // 2], len(key) // 2

            if number.find(key, offset + 1) > 0:
                super_key = key, len(key)
                break
    return super_key


def solve():
    max_k, max_v = 0, 0
    for i in range(2, 1001):
        temp_k, temp_v = find_occurences(fraction(i))
        if temp_v > max_v:
            max_v = temp_v
            max_k = i
    return max_k