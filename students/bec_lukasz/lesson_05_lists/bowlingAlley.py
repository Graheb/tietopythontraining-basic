pins_number, balls_rolled = \
    input('Input two numbers: ').split()
bowling = ['I'] * int(pins_number)
for i in range(int(balls_rolled)):
    left, right = input().split()
    for j in range(int(left) - 1, int(right)):
        bowling[j] = '.'
print(''.join(bowling))
