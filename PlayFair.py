class PlayFair:

    def generate_matrix(self, key):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u",
                    "v", "w", "x", "y", "z"]
        playfair_matrix = []
        row = []
        for w in key:
            if w not in row:
                row.append(w)

        for i in alphabet:
            if i == "i" or i == "j" and "i" not in row:
                row.append("i")
            elif i not in row and i != "j" and i != "i":
                row.append(i)
        playfair_matrix.append(row)

        final_matrix = list(self.divide_chunks(row, 5))
        return final_matrix

    def divide_chunks(self, l, n):
        # looping till length l
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def index_2d(self, myList, v):
        for i, x in enumerate(myList):
            if v in x:
                return (i, x.index(v))

    def remove(self, string1):
        return string1.replace(" ", "")

    def where_is_the_space(self, string2):
        list2 = []
        spaces = []
        for x in string2:
            list2.append(x)
        space = " "
        count = -1
        for y in list2:
            count += 1
            if y == space:
                spaces.append(count)
        if len(list2) != 0:
            return spaces
        else:
            return 0

    def encryption(self, plain_text, matrix):
        output_string = []  # output string list will be joined later on
        space = self.where_is_the_space(plain_text)
        plain_text = self.remove(plain_text)
        matrix = self.generate_matrix(matrix)  # this is 2d matrix carry the table
        if len(plain_text) % 2 != 0:  # to put the imaginary (x) if the length is odd
            plain_text = plain_text + 'x'
        # print(plain_text)
        iterate = int(len(plain_text)) / 2
        for x in range(0, len(plain_text), 2):
            if plain_text[x] == 'i' or plain_text[
                x] == 'j':  # check if the letter if j or i or not because in list it named i/j instead
                index1 = self.index_2d(matrix,
                                       "i/j")  # index1 is the tuple that carry the place of fist letter in table ([0],[1])
                index2 = self.index_2d(matrix, plain_text[
                    x + 1])  # index2 is the tuple that carry the place of second letter in table ([0],[1])
            elif plain_text[x + 1] == 'i' or plain_text[x + 1] == 'j':
                index1 = self.index_2d(matrix, plain_text[x])
                index2 = self.index_2d(matrix, "i")
            else:  # here i go when i find no i or j in the plain text
                index1 = self.index_2d(matrix, plain_text[x])
                index2 = self.index_2d(matrix, plain_text[x + 1])
            sameRow = False
            sameColumn = False
            different = False

            if index1[0] == index2[0]:
                # print("sameRow")
                sameRow = True
            elif index1[1] == index2[1]:
                # print("sameColumn")
                sameColumn = True
            else:
                # print("different row and different column")
                different = True

            if sameRow:  # the algorithm if they are in the same row
                if index1[1] == 4:
                    output_string.append(
                        matrix[int(index1[0])][0])  # go to the first of the row if it was the last one in the row
                else:
                    output_string.append(matrix[int(index1[0])][int(index1[1]) + 1])  # shift right

                if index2[1] == 4:
                    output_string.append(matrix[int(index2[0])][0])  # same as above
                else:
                    output_string.append(matrix[int(index2[0])][int(index2[1]) + 1])

            if sameColumn:  # the algorithm if they are in the same column
                if index1[0] == 4:
                    output_string.append(
                        matrix[0][int(index1[1])])  # check if it was the last one in column go to the first one
                else:
                    output_string.append(matrix[int(index1[0]) + 1][int(index1[1])])  # shift down

                if index2[0] == 4:
                    output_string.append(matrix[0][int(index2[1])])
                else:
                    output_string.append(matrix[int(index2[0]) + 1][int(index2[1])])

            if different:
                output_string.append(matrix[index1[0]][index2[1]])  # الاول في اول حرف و التاني في تاني حرف
                output_string.append(matrix[index2[0]][index1[1]])  # الاول في تاني حرف مع التاني في اول حرف

        # print(matrix)
        if space != 0:
            for x in space:
                output_string.insert(x, " ")
        out = (''.join(output_string))
        return out

    def decryption(self, encrypted_text, matrix):
        output_string = []  # output string list will be joined later on
        space = self.where_is_the_space(encrypted_text)
        encrypted_text = self.remove(encrypted_text)
        matrix = self.generate_matrix(matrix)  # this is 2d matrix carry the table
        if len(encrypted_text) % 2 != 0:  # to put the imaginary (x) if the length is odd
            plain_text = encrypted_text + 'x'
        # print(plain_text)
        iterate = int(len(encrypted_text)) / 2
        for x in range(0, len(encrypted_text), 2):
            if encrypted_text[x] == 'i' or encrypted_text[
                x] == 'j':  # check if the letter if j or i or not because in list it named i/j instead
                index1 = self.index_2d(matrix,
                                       "i/j")  # index1 is the tuple that carry the place of fist letter in table ([0],[1])
                index2 = self.index_2d(matrix, encrypted_text[
                    x + 1])  # index2 is the tuple that carry the place of second letter in table ([0],[1])
            elif encrypted_text[x + 1] == 'i' or encrypted_text[x + 1] == 'j':
                index1 = self.index_2d(matrix, encrypted_text[x])
                index2 = self.index_2d(matrix, "i")
            else:  # here i go when i find no i or j in the plain text
                index1 = self.index_2d(matrix, encrypted_text[x])
                index2 = self.index_2d(matrix, encrypted_text[x + 1])
            sameRow = False
            sameColumn = False
            different = False

            if index1[0] == index2[0]:
                # print("sameRow")
                sameRow = True
            elif index1[1] == index2[1]:
                # print("sameColumn")
                sameColumn = True
            else:
                # print("different row and different column")
                different = True

            if sameRow:  # the algorithm if they are in the same row
                if index1[1] == 0:
                    output_string.append(
                        matrix[int(index1[0])][4])  # go to the first of the row if it was the last one in the row
                else:
                    output_string.append(matrix[int(index1[0])][int(index1[1]) - 1])  # shift left

                if index2[1] == 0:
                    output_string.append(matrix[int(index2[0])][4])  # same as above
                else:
                    output_string.append(matrix[int(index2[0])][int(index2[1]) - 1])

            if sameColumn:  # the algorithm if they are in the same column
                if index1[0] == 0:
                    output_string.append(
                        matrix[4][int(index1[1])])  # check if it was the last one in column go to the first one
                else:
                    output_string.append(matrix[int(index1[0]) - 1][int(index1[1])])  # shift up

                if index2[0] == 0:
                    output_string.append(matrix[4][int(index2[1])])
                else:
                    output_string.append(matrix[int(index2[0]) - 1][int(index2[1])])

            if different:
                output_string.append(matrix[index1[0]][index2[1]])  # الاول في اول حرف و التاني في تاني حرف
                output_string.append(matrix[index2[0]][index1[1]])  # الاول في تاني حرف مع التاني في اول حرف

        # print(matrix)
        if space != 0:
            for y in space:
                output_string.insert(y, " ")
        x = ''.join(output_string)
        return x

#
# string = input("Enter the string to be encrypted:")
# key = input("Enter the key:")
#
# print("encrypted string:", encryption(string, key))
# print("After Decryption:", decryption(encryption(string, key), key))
