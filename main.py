import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

from Caeser import Caeser
from Vigenere import Vigenere
from Rial_Fence import Rial_Fence
from RSA import RSA
from PlayFair import PlayFair
from DES import DES


def encrypt_message():
    input_ciphered.delete(0, END)
    pt = input_plain_text.get()
    key = input_key.get()

    if algo.get() == 'Ceaser cipher':
        caeser = Caeser(pt, int(key)).encrypted()
        input_ciphered.insert(0, caeser)

    if algo.get() == 'Vigenère':
        temp = Vigenere()
        vig_obj = temp.vig_encryption(pt, key)
        input_ciphered.insert(0, vig_obj)

    if algo.get() == 'RailFence':
        temp = Rial_Fence()
        railObj = temp.Rial_encryption(pt, int(key))
        input_ciphered.insert(0, railObj)

    if algo.get() == "RSA":
        rsa_variables = pt.split(",")
        m = rsa_variables[0]
        p = rsa_variables[1]
        q = rsa_variables[2]
        e = rsa_variables[3]
        temp = RSA()
        RAS_Obj = temp.RSA_encryption(p, int(q), int(m))
        input_ciphered.insert(0, RAS_Obj)

    if algo.get() == "Playfair":
        temp = PlayFair()
        playObj = temp.encryption(pt, key)
        input_ciphered.insert(0, playObj)

    if algo.get() == "DES":
        temp = DES()
        Des_obj = temp.DES_encryption(pt, key)
        input_ciphered.insert(0, Des_obj)


def decrypt_message():
    decrypt_msg.delete(0, END)
    cipher = input_ciphered.get()
    key = input_key.get()
    pt = input_plain_text.get()

    if algo.get() == 'Ceaser cipher':
        caeser = Caeser(cipher, int(key)).decrypted()
        decrypt_msg.insert(0, caeser)
    if algo.get() == 'RailFence':
        temp = Rial_Fence()
        RialFence_obj = temp.decryptRailFence(cipher, key)
        decrypt_msg.insert(0,RialFence_obj)

    if algo.get() == "RSA":
        print(cipher)
        rsa_variables = pt.split(",")
        m = rsa_variables[0]
        p = rsa_variables[1]
        q = rsa_variables[2]
        e = rsa_variables[3]
        temp = RSA()
        RSA_Obj = temp.RSA_decryption(p, int(q), int(cipher), int(e))
        decrypt_msg.insert(0, RSA_Obj)

    if algo.get() == "Playfair":
        temp = PlayFair()
        playObj = temp.decryption(cipher, key)
        decrypt_msg.insert(0, playObj)

    if algo.get() == "DES":
        temp = DES()
        Des_obj = temp.DES_decryption(cipher, key)
        print(cipher)
        print(key)
        decrypt_msg.insert(0, Des_obj)

    if algo.get() == 'Vigenère':
        temp = Vigenere()
        vig_obj = temp.decryption(cipher, key)
        decrypt_msg.insert(0, vig_obj)


def checkcmobo():
    val = algo.get()
    messagebox.showinfo("YOUU SELECT", val)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("CRYPTOGRAPHY")

    # creating labels and positioning them on the grid
    label0 = Label(root, text='plain text')
    label0.grid(row=10, column=1)
    label1 = Label(root, text='Key')
    label1.grid(row=11, column=1)
    label2 = Label(root, text='Cipher text')
    label2.grid(row=12, column=1)
    label4 = Label(root, text="decrypted text")
    label4.grid(row=11, column=10)
    label5 = Label(root, text="Choose your algorithm")
    label5.grid(row=10, column=12)

    btn = ttk.Button(root, text='Get value', command=lambda: checkcmobo())
    btn.grid(row=13, column=12)

    # creating entries and positioning them on the grid
    input_plain_text = Entry(root)
    input_plain_text.grid(row=10, column=2, ipadx=50)
    input_key = Entry(root)  # key
    input_key.grid(row=11, column=2, ipadx=50)
    input_ciphered = Entry(root)  # encrypt text
    input_ciphered.grid(row=12, column=2, ipadx=50)
    decrypt_msg = Entry(root)  # decrypted text
    decrypt_msg.grid(row=11, column=11)

    algo = ttk.Combobox(root, width=35, values=('RSA', 'Playfair', 'RailFence', 'Vigenère', 'Ceaser cipher', 'DES'))
    algo.grid(row=11, column=12)

    # creating encryption button to produce the output
    encrypt_btn = Button(root, text="encrypt", bg="blue", fg="white", command=encrypt_message)
    encrypt_btn.grid(row=13, column=2)

    # creating decryption button to produce the output
    decrypt_btn = Button(root, text="decrypt", bg="green", fg="white", command=decrypt_message)
    decrypt_btn.grid(row=13, column=11)
    root.geometry("750x100")
    root.eval('tk::PlaceWindow . center')
    root.mainloop()
