class Vigenere:
    def get_key_sequence(self, plain_text, key):
        plain_text = plain_text.upper()
        plain_text = plain_text.replace(" ", "")
        keys = list(key)
        plain_text_length = len(plain_text)
        key_length = len(keys)
        key_list = keys * int(plain_text_length / key_length)
        x = 0
        while len(key_list) < plain_text_length:
            key_list.append(keys[x])
            x += 1
        sequence = (''.join(key_list))
        return sequence

    def create_tabula_recta(self):
        tabula_recta = []
        for r in range(0, 26):
            x = 0
            row = []
            for column in range(0, 26):
                row.append(chr(r + 65 + x))
                x += 1
                if x > (25 - r):
                    x -= 26
            tabula_recta.append(row)
        return tabula_recta

    def vig_encryption(self, plain_text, key):
        plain_text = plain_text.upper()
        plain_text = plain_text.replace(" ", "")
        key_sequence = self.get_key_sequence(plain_text, key).upper()
        table = self.create_tabula_recta()
        alpha_dic = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
                     "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19,
                     "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
        output = []
        for x in range(0, len(key_sequence)):
            output.append(table[int(alpha_dic.get(key_sequence[x])) - 1][alpha_dic.get(plain_text[x]) - 1])

        cipher_text = ''.join(output)
        return cipher_text

    def decryption(self, cipher_text, key):
        key_sequence = self.get_key_sequence(cipher_text, key).upper()
        table = self.create_tabula_recta()
        alpha_dic = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
                     "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19,
                     "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
        output = []
        key_list = list(alpha_dic.keys())
        val_list = list(alpha_dic.values())
        cipher_text = list(cipher_text)
        for x in range(0, len(key_sequence)):
            list1 = table[alpha_dic.get(key_sequence[x]) - 1]
            # print(list1)
            index = list1.index(cipher_text[x]) + 1
            # print(index)
            plain_char = key_list[val_list.index(index)]
            # print(plain_char)
            output.append(plain_char)

        return ''.join(output)

    # plain = "THEBOYHASTHEBALL"
    # key = "VIGVIGVIGVIGVIGV"
    # cipher, key = vig_encryption(plain, key)
    # print(cipher)
    # decryption(cipher, key)
