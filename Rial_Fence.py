class Rial_Fence:
    def Rial_encryption(self, plain_text, key):
        plain_text = plain_text.upper()
        plain_text = plain_text.replace(" ", "")
        keys = {2: 2, 3: 4, 4: 6, 5: 8, 6: 10, 7: 12}
        moves = keys.get(int(key))
        cipher_text = []
        begin = 0
        for x in range(0, int(key)):
            line = []
            begin2 = begin
            if x == 0 or x == int(key) - 1:
                begin2 = x
                while begin2 < len(plain_text):
                    line.append(plain_text[begin2])
                    begin2 += keys.get(int(key))
            else:
                begin2 += x
                moves -= 2
                move = abs(keys.get(int(key)) - moves)
                count = 0
                while begin2 < len(plain_text):
                    count += 1
                    if count % 2 != 0:
                        line.append(plain_text[begin2])
                        begin2 += moves
                    else:
                        line.append(plain_text[begin2])
                        begin2 += move
            cipher_text += line

        cipher = (''.join(cipher_text))
        return cipher.lower()

    def decryptRailFence(self, cipher, key):
        key = int(key)
        rail = [['\n' for i in range(len(cipher))]
                for j in range(key)]

        dir_down = None
        row, col = 0, 0

        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            # place the marker
            rail[row][col] = '*'
            col += 1
            if dir_down:
                row += 1
            else:
                row -= 1

        index = 0
        for i in range(key):
            for j in range(len(cipher)):
                if ((rail[i][j] == '*') and
                        (index < len(cipher))):
                    rail[i][j] = cipher[index]
                    index += 1

        result = []
        row, col = 0, 0
        for i in range(len(cipher)):

            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            if rail[row][col] != '*':
                result.append(rail[row][col])
                col += 1

            if dir_down:
                row += 1
            else:
                row -= 1
        plain = "".join(result)
        return plain.lower()
