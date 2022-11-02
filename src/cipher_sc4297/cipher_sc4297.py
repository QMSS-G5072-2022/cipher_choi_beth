def cipher(text, shift, encrypt=True):
    """
    The Caesar Cipher, an encryption technique.
    Each letter in text replaced by a letter some fixed number of positions down the alphabet.

    Parameters
    ----------
    text: The text to be encrypted/decrypted. 
        Type - string.
    shift: The fixed number of positions to be used to replace each letter of the input text. 
        Type - integer.
    encrypt=True: Indicates whether to encrypt or decrypt the input text. Default is to encrypt.
        Type - boolean.
        encrypt=False decrypts the input text.

    Returns
    -------
    The encrypted/decrypted text. 
        Type - string.

    Examples
    --------
    Encrypting:
    >>> from cipher_sc4297 import cipher_sc4297
    >>> text = 'Zebra'
    >>> shift = 2
    >>> encrypt = True
    >>> cipher_sc4297.cipher(text, shift, encrypt)
    'bgdtc'

    Decrypting:
    >>> from cipher_sc4297 import cipher_sc4297
    >>> text = 'bgdtc'
    >>> shift = 2
    >>> encrypt = False
    >>> cipher_sc4297.cipher(text, shift, encrypt)
    'Zebra'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text