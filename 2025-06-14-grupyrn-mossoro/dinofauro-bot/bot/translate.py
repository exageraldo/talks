CHANGE_LETTERS = {
    'b': 'f',
    'j': 'f',
    'p': 'f',
    's': 'f',
    'x': 'f',
    'v': 'f',
    'z': 'f',
    'ç': 'f',
    'B': 'F',
    'J': 'F',
    'P': 'F',
    'S': 'F',
    'X': 'F',
    'V': 'F',
    'Z': 'F',
    'Ç': 'F',
    'ci': 'fi',
    'ce': 'fe',
    'CI': 'FI',
    'CE': 'FE',
    'Ci': 'Fi',
    'Ce': 'Fe',
}


def translate(text: str) -> str:
    for letter in CHANGE_LETTERS:
        if letter in text:
            text = text.replace(letter, CHANGE_LETTERS[letter])

    while text != text.replace('ff', 'f'):
        text = text.replace('ff', 'f')

    return text
