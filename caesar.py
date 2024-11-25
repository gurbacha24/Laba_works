import typing as tp

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if 'A' <= char <= 'Z':  # eng upper
            shift_amount = (ord(char) - ord('A') + shift) % 26
            ciphertext += chr(shift_amount + ord('A'))
        elif 'a' <= char <= 'z':  # eng lower
            shift_amount = (ord(char) - ord('a') + shift) % 26
            ciphertext += chr(shift_amount + ord('a'))
        elif 'А' <= char <= 'Я':  # ru upper
            shift_amount = (ord(char) - ord('А') + shift) % 33
            ciphertext += chr(shift_amount + ord('А'))
        elif 'а' <= char <= 'я':  # ru lower
            shift_amount = (ord(char) - ord('а') + shift) % 33
            ciphertext += chr(shift_amount + ord('а'))
        else:  # other char
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        if 'A' <= char <= 'Z':  # eng upper
            shift_amount = (ord(char) - ord('A') - shift) % 26
            plaintext += chr(shift_amount + ord('A'))
        elif 'a' <= char <= 'z':  # eng lower
            shift_amount = (ord(char) - ord('a') - shift) % 26
            plaintext += chr(shift_amount + ord('a'))
        elif 'А' <= char <= 'Я':  # ru upper
            shift_amount = (ord(char) - ord('А') - shift) % 33
            plaintext += chr(shift_amount + ord('А'))
        elif 'а' <= char <= 'я':  # ru lower
            shift_amount = (ord(char) - ord('а') - shift) % 33
            plaintext += chr(shift_amount + ord('а'))
        else:
            plaintext += char  # other char
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
