SEQUENCE_LENGTH = 100
WORD_TO_FACTOR = {
    3: "Three",
    5: "Five",
}
FACTORS = [3, 5]

def _is_multiple_of(number, factor):
    if factor == 0: return False
    return number % factor == 0


def _get_number_representation(number):
    return ''.join(
        [ 
            WORD_TO_FACTOR[factor]
            for factor in FACTORS
            if _is_multiple_of(number, factor) 
        ]
    )


def get_hundred_numbers():
    '''Returns hundred numbers from 1 to 100. 
       Replaces multiples of 3 with "Three" and multiples of 5 with "Five".
       Multiples of both are replaced with "ThreeFive"
    '''
    for number in range(1, SEQUENCE_LENGTH + 1):
        number_repr = _get_number_representation(number)
        yield (number_repr or number)


if __name__ == "__main__":
    for number in get_hundred_numbers():
        print(number)

