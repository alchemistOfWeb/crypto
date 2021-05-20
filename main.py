import math


def encrypt_by_cezar_cipher(text, encrypt_key):
    eng_low = {'start': ord('a'), 'end': ord('z')}
    eng_upper = {'start': ord('A'), 'end': ord('Z')}

    ciphered = ''

    for cipher_symbol in text:

        code_symbol = ord(cipher_symbol)

        if code_symbol in range(eng_low['start'], eng_low['end'] + 1) \
                or code_symbol in range(eng_upper['start'], eng_upper['end'] + 1):

            new_code = code_symbol + encrypt_key

            if eng_low['end'] < new_code < eng_low['end'] + encrypt_key + 1:
                new_code = eng_low['start'] + (new_code - eng_low['end'] - 1)

            if eng_upper['end'] < new_code < eng_upper['end'] + encrypt_key + 1:
                new_code = eng_upper['start'] + (new_code - eng_upper['end'] - 1)

            cipher_symbol = chr(new_code)

        ciphered += cipher_symbol

    return ciphered


def decrypt_cezar_cipher():
    ...


def encrypt_by_permutation(text, key_word):
    text_len = len(text)
    cols_num = len(key_word)
    rows_num = math.ceil(len(text)/cols_num)

    symbol_matrix = []

    for row in range(cols_num):
        row_list = []

        for col in range(rows_num):
            ind = row*rows_num+col
            row_list.append(text[ind] if ind < text_len else '')

        symbol_matrix.append(row_list)

    symbol_matrix = {key_word[col]: symbol_matrix[col] for col in range(cols_num)}

    symbol_matrix_sorted = [symbol_matrix[col] for col in sorted(key_word)]

    matrix_tr = [*map(list, zip(*symbol_matrix_sorted))]

    for i in range(rows_num):
        matrix_tr[i] = ''.join(matrix_tr[i])

    return ''.join(matrix_tr)


if __name__ == '__main__':

    # CEZAR CIPHER
    with open('input.txt', 'r') as f_inp:
        encrypted = encrypt_by_cezar_cipher(f_inp.read(), 4)

    with open('encrypted.txt', 'w') as f_out:
        f_out.write(encrypted)

    with open('decrypted.txt', 'w') as f_out:
        f_out.write(decrypt_cezar_cipher(encrypted))

    # CIPHER OF PERMUTATION METHOD
    with open('input.txt', 'r') as f_inp:
        encrypted_p = encrypt_by_permutation('simple permutation', 'word')

    with open('encrypted_p.txt', 'w') as f_out:
        f_out.write(encrypted_p)

    with open('decrypted_p.txt', 'w') as f_out:
        f_out.write(decrypt_cezar_cipher(encrypted))

