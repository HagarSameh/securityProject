class DES:
    def Hex_to_binary(self, s):
        mp = {'0': "0000",
              '1': "0001",
              '2': "0010",
              '3': "0011",
              '4': "0100",
              '5': "0101",
              '6': "0110",
              '7': "0111",
              '8': "1000",
              '9': "1001",
              'A': "1010",
              'B': "1011",
              'C': "1100",
              'D': "1101",
              'E': "1110",
              'F': "1111"}
        binary = ""
        for i in range(len(s)):
            binary = binary + mp[s[i]]
        return binary

    def bin2hex(self, s):
        mp = {"0000": '0',
              "0001": '1',
              "0010": '2',
              "0011": '3',
              "0100": '4',
              "0101": '5',
              "0110": '6',
              "0111": '7',
              "1000": '8',
              "1001": '9',
              "1010": 'A',
              "1011": 'B',
              "1100": 'C',
              "1101": 'D',
              "1110": 'E',
              "1111": 'F'}
        hex = ""
        for i in range(0, len(s), 4):
            ch = ""
            ch = ch + s[i]
            ch = ch + s[i + 1]
            ch = ch + s[i + 2]
            ch = ch + s[i + 3]
            hex = hex + mp[ch]

        return hex

    def chunked_l(self, l):
        chunked_list = list()
        chunk_size = 6

        for i in range(0, len(l), chunk_size):
            chunked_list.append(l[i:i + chunk_size])
        return chunked_list

    def S_Box(self, xor_result):
        s_box = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                  [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                  [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                  [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
                 [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                  [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                  [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                  [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
                 [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                  [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                  [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                  [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
                 [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                  [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                  [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                  [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
                 [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                  [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                  [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                  [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
                 [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                  [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                  [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                  [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
                 [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                  [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                  [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                  [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
                 [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                  [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                  [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                  [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
        result = []  # this will carry the 48 bit
        for x in range(0, 8):
            B = xor_result[x]  # this variable is the B0 ,B1 and each B is 6 bits
            S = s_box[x]  # this variable is the S1 and S2 come from above list
            row = self.bin2dec(
                int(str(B[0]) + str(B[5])))  # row number and the first and last bit in B and then trans into dec
            column = self.bin2dec(
                int(str(B[1]) + str(B[2]) + str(B[3]) + str(B[4])))  # get column num the 4 in the middle
            r = S[row][column]
            r_to_binary = self.dec2bin(r)
            result.append(list(r_to_binary))
        return result

    def dec2bin(self, num):
        res = bin(num).replace("0b", "")
        if len(res) % 4 != 0:
            div = len(res) / 4
            div = int(div)
            counter = (4 * (div + 1)) - len(res)
            for i in range(0, counter):
                res = '0' + res
        return res

    def bin2dec(self, binary0):
        binary1 = binary0
        decimal, i, n = 0, 0, 0
        while binary0 != 0:
            dec = binary0 % 10
            decimal = decimal + dec * pow(2, i)
            binary0 = binary0 // 10
            i += 1
        return decimal

    def xor(self, a, b):
        ans = ""
        for i in range(len(a)):
            if a[i] == b[i]:
                ans = ans + "0"
            else:
                ans = ans + "1"
        return ans

    def f_function(self, R):
        exp_d = [32, 1, 2, 3, 4, 5, 4, 5,
                 6, 7, 8, 9, 8, 9, 10, 11,
                 12, 13, 12, 13, 14, 15, 16, 17,
                 16, 17, 18, 19, 20, 21, 20, 21,
                 22, 23, 24, 25, 24, 25, 26, 27,
                 28, 29, 28, 29, 30, 31, 32, 1]
        f_of_R = []
        for x in exp_d:
            # get 48 bit instead of 32
            f_of_R.append(R[x - 1])
        return f_of_R

    def key_generation(self, key):
        pc1 = [57, 49, 41, 33, 25, 17, 9,
               1, 58, 50, 42, 34, 26, 18,
               10, 2, 59, 51, 43, 35, 27,
               19, 11, 3, 60, 52, 44, 36,
               63, 55, 47, 39, 31, 23, 15,
               7, 62, 54, 46, 38, 30, 22,
               14, 6, 61, 53, 45, 37, 29,
               21, 13, 5, 28, 20, 12, 4]

        binary_key = list(self.Hex_to_binary(key))
        Kp = []
        # get 56 bit instead of 64
        for x in pc1:
            Kp.append(binary_key[x - 1])
        # divides to left and right
        middle = 28
        L = Kp[:middle]
        R = Kp[middle:]
        # rotation table
        rotation = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        all_Left_keys = []
        all_right_keys = []
        # rotate the left and the right key using rotation table
        for x in range(0, 16):
            L = L[rotation[x]:] + L[:rotation[x]]
            all_Left_keys.append(L)
            R = R[rotation[x]:] + R[:rotation[x]]
            all_right_keys.append(R)
        # concatenate the key to return 56
        concatenated_keys = []
        for x in range(0, 16):
            f = all_Left_keys[x] + all_right_keys[x]
            concatenated_keys.append(f)
        # this is the stage of turning the 56 to 48 bit using pc2
        pc2 = [14, 17, 11, 24, 1, 5,
               3, 28, 15, 6, 21, 10,
               23, 19, 12, 4, 26, 8,
               16, 7, 27, 20, 13, 2,
               41, 52, 31, 37, 47, 55,
               30, 40, 51, 45, 33, 48,
               44, 49, 39, 56, 34, 53,
               46, 42, 50, 36, 29, 32]
        final_final_keys = []
        for x in concatenated_keys:
            Kp2 = []
            # get 48 bit instead of 56
            for y in pc2:
                Kp2.append(x[y - 1])
            final_final_keys.append(Kp2)

        return final_final_keys

    def DES_encryption(self, plain, key):
        keys = self.key_generation(key)
        binary_message = self.Hex_to_binary(plain)
        IP = [58, 50, 42, 34, 26, 18, 10, 2,
              60, 52, 44, 36, 28, 20, 12, 4,
              62, 54, 46, 38, 30, 22, 14, 6,
              64, 56, 48, 40, 32, 24, 16, 8,
              57, 49, 41, 33, 25, 17, 9, 1,
              59, 51, 43, 35, 27, 19, 11, 3,
              61, 53, 45, 37, 29, 21, 13, 5,
              63, 55, 47, 39, 31, 23, 15, 7]
        IP_message = []
        # get Ip message form IP list
        for x in IP:
            IP_message.append(binary_message[x - 1])
        # divides to left and right
        middle = 32
        L = IP_message[:middle]
        R = IP_message[middle:]
        all_Left = []
        all_right = []
        per = [16, 7, 20, 21,
               29, 12, 28, 17,
               1, 15, 23, 26,
               5, 18, 31, 10,
               2, 8, 24, 14,
               32, 27, 3, 9,
               19, 13, 30, 6,
               22, 11, 4, 25]
        for x in range(0, 16):
            # get the R of the previous round to be the left of this round
            all_Left.append(R)
            f_of_R = self.f_function(R)
            # f(R) : expansion from 32 to 48
            key_of_the_round = keys[x]
            # xor function between f(R) and its key
            result_of_xor = list(self.xor(f_of_R, key_of_the_round))
            # list of 8 each list contains 6 bits
            chunked_result = self.chunked_l(result_of_xor)
            # S_Box method will return a 32 bit list 4 * 8
            s_box_result = self.S_Box(chunked_result)
            # to make the result flat in one list
            s_box_flat_list = [item for sublist in s_box_result for item in sublist]
            # permutation step
            final_result_after_permutation = []
            for y in per:
                final_result_after_permutation.append(s_box_flat_list[y - 1])
            last_list_after_xor = list(self.xor(final_result_after_permutation, L))
            all_right.append(last_list_after_xor)
            L = all_Left[x]
            R = all_right[x]
        # ------------------------------------------------------------
        final_result_before_finalPermutation = all_right[15] + all_Left[15]
        final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
                      39, 7, 47, 15, 55, 23, 63, 31,
                      38, 6, 46, 14, 54, 22, 62, 30,
                      37, 5, 45, 13, 53, 21, 61, 29,
                      36, 4, 44, 12, 52, 20, 60, 28,
                      35, 3, 43, 11, 51, 19, 59, 27,
                      34, 2, 42, 10, 50, 18, 58, 26,
                      33, 1, 41, 9, 49, 17, 57, 25]
        final_result_after_finalPermutation = []
        for x in final_perm:
            final_result_after_finalPermutation.append(final_result_before_finalPermutation[x - 1])
        to_string = ''.join(final_result_after_finalPermutation)
        ciphered_text = self.bin2hex(to_string)
        return ciphered_text

    def DES_decryption(self, cipher, key):
        keys = self.key_generation(key)
        # here is the reverse which make the decryption
        keys.reverse()
        binary_message = self.Hex_to_binary(cipher)
        IP = [58, 50, 42, 34, 26, 18, 10, 2,
              60, 52, 44, 36, 28, 20, 12, 4,
              62, 54, 46, 38, 30, 22, 14, 6,
              64, 56, 48, 40, 32, 24, 16, 8,
              57, 49, 41, 33, 25, 17, 9, 1,
              59, 51, 43, 35, 27, 19, 11, 3,
              61, 53, 45, 37, 29, 21, 13, 5,
              63, 55, 47, 39, 31, 23, 15, 7]
        IP_message = []
        # get Ip message form IP list
        for x in IP:
            IP_message.append(binary_message[x - 1])
        # divides to left and right
        middle = 32
        L = IP_message[:middle]
        R = IP_message[middle:]
        all_Left_keys = []
        all_right_keys = []
        per = [16, 7, 20, 21,
               29, 12, 28, 17,
               1, 15, 23, 26,
               5, 18, 31, 10,
               2, 8, 24, 14,
               32, 27, 3, 9,
               19, 13, 30, 6,
               22, 11, 4, 25]
        for x in range(0, 16):
            # get the R of the previous round to be the left of this round
            all_Left_keys.append(R)
            f_of_R = self.f_function(R)
            key_of_the_round = keys[x]
            result_of_xor = list(self.xor(f_of_R, key_of_the_round))
            chunked_result = self.chunked_l(result_of_xor)
            # S_Box method will return a 32 bit list 4 * 8
            s_box_result = self.S_Box(chunked_result)
            # to make the result flat in one list
            s_box_flat_list = [item for sublist in s_box_result for item in sublist]
            # permutation step
            final_result_after_permutation = []
            for y in per:
                final_result_after_permutation.append(s_box_flat_list[y - 1])
            last_list_after_xor = list(self.xor(final_result_after_permutation, L))
            all_right_keys.append(last_list_after_xor)
            L = all_Left_keys[x]
            R = all_right_keys[x]

        final_result_before_finalPermutation = all_right_keys[15] + all_Left_keys[15]
        final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
                      39, 7, 47, 15, 55, 23, 63, 31,
                      38, 6, 46, 14, 54, 22, 62, 30,
                      37, 5, 45, 13, 53, 21, 61, 29,
                      36, 4, 44, 12, 52, 20, 60, 28,
                      35, 3, 43, 11, 51, 19, 59, 27,
                      34, 2, 42, 10, 50, 18, 58, 26,
                      33, 1, 41, 9, 49, 17, 57, 25]
        final_result_after_finalPermutation = []
        for x in final_perm:
            final_result_after_finalPermutation.append(final_result_before_finalPermutation[x - 1])
        to_string = ''.join(final_result_after_finalPermutation)
        plain_text = self.bin2hex(to_string)
        return plain_text

    # k = "AABB09182736CCDD"
    # M = "123456ABCD132536"
    # # key = key_generation(k)
    # print("Plain Text: ", M)
    # cipher = DES_encryption(M, k)
    # print("cipher text: ", cipher)
    # print("Plain text: ", DES_decryption(cipher, k))
