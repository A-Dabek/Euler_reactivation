encrypted = open('res/59.txt')

codons = encrypted.read().split(',')
codons = [int(i) for i in codons]

key = [ord('g'), ord('o'), ord('c')]  # 97-122
is_decoded = False
decoded_text = []

while not is_decoded:
    is_decoded = True
    i_key = 0
    decoded_text = []
    no_space_since = 0

    key[2] += 1
    if key[2] > 122:
        key[2] = 97
        key[1] += 1
        if key[1] > 122:
            key[1] = 97
            key[0] += 1
            if key[0] > 122:
                break

    for char in codons:
        decrypted_char = char ^ key[i_key]
        i_key = (i_key + 1) % 3
        if decrypted_char < 31 or decrypted_char == 131:
            is_decoded = False
            break
        if chr(decrypted_char) != ' ':
            no_space_since += 1
        else:
            no_space_since = 0
        if no_space_since > 15:
            is_decoded = False
            break
        decoded_text.append(decrypted_char)

print(key, sum(decoded_text))
