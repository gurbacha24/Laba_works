def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]

    for p_char, k_char in zip(plaintext, keyword_repeated):
        if 'A' <= p_char <= 'Z':  # eng upper
            shift = (ord(p_char) - ord('A') + ord(k_char.upper()) - ord('A')) % 26
            ciphertext += chr(shift + ord('A'))
        elif 'a' <= p_char <= 'z':  # eng lower
            shift = (ord(p_char) - ord('a') + ord(k_char.lower()) - ord('a')) % 26
            ciphertext += chr(shift + ord('a'))
        elif 'А' <= p_char <= 'Я':  # rus upper
            shift = (ord(p_char) - ord('А') + ord(k_char.upper()) - ord('А')) % 33
            ciphertext += chr(shift + ord('А'))
        elif 'а' <= p_char <= 'я':  # rus lower
            shift = (ord(p_char) - ord('а') + ord(k_char.lower()) - ord('а')) % 33
            ciphertext += chr(shift + ord('а'))
        else:
            ciphertext += p_char  # other char
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]

    for c_char, k_char in zip(ciphertext, keyword_repeated):
        if 'A' <= c_char <= 'Z':  # eng upper
            shift = (ord(c_char) - ord('A') - (ord(k_char.upper()) - ord('A'))) % 26
            plaintext += chr(shift + ord('A'))
        elif 'a' <= c_char <= 'z':  # eng lower
            shift = (ord(c_char) - ord('a') - (ord(k_char.lower()) - ord('a'))) % 26
            plaintext += chr(shift + ord('a'))
        elif 'А' <= c_char <= 'Я':  # rus upper
            shift = (ord(c_char) - ord('А') - (ord(k_char.upper()) - ord('А'))) % 33
            plaintext += chr(shift + ord('А'))
        elif 'а' <= c_char <= 'я':  # rus lower
            shift = (ord(c_char) - ord('а') - (ord(k_char.lower()) - ord('а'))) % 33
            plaintext += chr(shift + ord('а'))
        else:
            plaintext += c_char  # other char
    return plaintext
