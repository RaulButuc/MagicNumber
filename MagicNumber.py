from random import randint


def play_magic_number(left, right):
    numbers = []
    magic_number = randint(left+1, right-1)
    steps = 0
    game_over = False

    for num in range(left, right):
        numbers.append(num)

    while game_over is False:
        steps += 1
        middle = int((right - left) / 2 + left)
        guess = numbers[middle]

        if guess == magic_number:
            game_over = True
        elif guess < magic_number:
            left = middle
        else:
            right = middle

    return steps


def test_efficiency(left, right):
    number_of_steps = []
    num = right - left
    average = 0
    efficiency = 100

    for test_id in range(left, right + 1):
        number_of_steps.append(play_magic_number(0, 100))
        average += number_of_steps[test_id]

    average /= num
    efficiency -= average

    return efficiency


number_of_tests = 1000000
print("MagicNumber /w iterative binary search efficiency (", number_of_tests," tests): ",
      test_efficiency(0, number_of_tests), "%", sep='')