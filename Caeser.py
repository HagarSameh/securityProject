class Caeser:
    encrypted_txt = []
    encrypted_idx = []

    decrypted_txt = []
    decrypted_idx = []
    alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
                'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
                'x': 23, 'y': 24, 'z': 25}

    def __init__(self, txt, key):
        self.txt = txt
        self.key = key

    def encrypted(self):
        encrypted_txt = []

        for idx in range(len(self.txt)):
            plain_idx = self.alphabet[self.txt[idx]]
            self.encrypted_idx.append((plain_idx + self.key) % 26)

        for idx in range(len(self.txt)):
            encrypted_txt.insert(idx, list(self.alphabet.keys())
            [list(self.alphabet.values()).index(self.encrypted_idx[idx])])
        self.encrypted_txt = ''.join(encrypted_txt)

        return self.encrypted_txt

    def decrypted(self):
        for idx in range(len(self.txt)):
            self.decrypted_idx.append((self.encrypted_idx[idx] - self.key) % 26)
        for dd in range(len(self.decrypted_idx)):
            self.decrypted_txt.insert(dd, list(self.alphabet.keys())[list(self.alphabet.values()).index(self.decrypted_idx[dd])])
        self.decrypted_txt = ''.join(self.decrypted_txt)
        return self.decrypted_txt
