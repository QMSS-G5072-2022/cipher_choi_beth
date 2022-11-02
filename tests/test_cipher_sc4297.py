from cipher_sc4297 import cipher_sc4297

def test_cipher_word():
    text = 'Zebra'
    shift = 2
    encrypt = True
    expected = 'bgdtc'
    actual = cipher_sc4297.cipher(text, shift, encrypt)
    assert actual == expected