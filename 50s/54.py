file = open('res/54.txt')

figures = {
    'high': 0,
    'pair': 1,
    'two': 2,
    'three': 3,
    'street': 4,
    'flush': 5,
    'full': 6,
    'four': 7,
    's_flush': 8
}


def eval_hand(hand):
    card_dict = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    figure = ('high', 2)

    l_codes = []
    l_colors = []
    if len(hand) < 2:
        return None
    for i_pair in range(len(hand)):
        code = hand[i_pair][0]
        if card_dict.get(code, None) is None:
            code = int(code)
        else:
            code = card_dict[code]
        hand[i_pair] = (code, hand[i_pair][1])
        l_codes.append(code)
        l_colors.append(hand[i_pair][1])

    street = True
    flush = False

    if len(set(l_colors)) == 1:
        flush = True

    sorted_code = sorted(l_codes)
    for i in range(len(sorted_code) - 1):
        if sorted_code[i + 1] - sorted_code[i] != 1:
            street = False
            break

    if flush and street:
        figure = ('s_flush', sorted(set(l_codes), reverse=True))
    elif flush:
        figure = ('flush', sorted(set(l_codes), reverse=True))
    elif street:
        figure = ('street', sorted(set(l_codes), reverse=True))

    single_cards = list(l_codes)
    for s in set(l_codes):
        ind = single_cards.index(s)
        del single_cards[ind]
    single_cards = set(single_cards)
    remain = sorted(list(set(l_codes).difference(single_cards)), reverse=True)

    if not flush and not street:
        if len(set(l_codes)) == 5:
            figure = ('high', sorted(set(l_codes), reverse=True))
        elif len(set(l_codes)) == 4:  # one pair
            figure = ('pair', sorted(set(single_cards), reverse=True) + remain)
        elif len(set(l_codes)) == 3:
            if len(single_cards) == 1:
                figure = ('three', sorted(set(single_cards), reverse=True) + remain)
            elif len(single_cards) == 2:
                figure = ('two', sorted(set(single_cards), reverse=True) + remain)
        elif len(set(l_codes)) == 2:
            if len(single_cards) == 1:
                figure = ('four', sorted(set(single_cards), reverse=True) + remain)
            elif len(single_cards) == 2:
                figure = ('full', sorted(set(single_cards), reverse=True) + remain)
    return figure


hands = file.read().split('\n')
p1_hands = []
p2_hands = []

for i_hand in range(len(hands)):
    temp = hands[i_hand].split(' ')
    p1_hands.append(temp[:5])
    p2_hands.append(temp[5:])

wins_of_p1 = 0
for i, j in zip(p1_hands, p2_hands):
    v1, v2 = eval_hand(i), eval_hand(j)
    if v1 is None or v2 is None:
        continue
    print('one', v1, v2)
    if figures[v1[0]] > figures[v2[0]]:
        print(v1, 'won to', v2)
        wins_of_p1 += 1
    elif figures[v1[0]] < figures[v2[0]]:
        print(v1, 'lost to', v2)
    elif figures[v1[0]] == figures[v2[0]]:
        for ii, jj in zip(v1[1], v2[1]):
            if ii > jj:
                wins_of_p1 += 1
                print(v1, 'won to', v2)
                break
            if jj > ii:
                print(v1, 'lost to', v2)
                break
print(wins_of_p1)
p1_value = []
p2_value = []

# print(hands)
# print(p1_hands)
# print(p2_hands)
