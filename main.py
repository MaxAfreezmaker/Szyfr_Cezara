# -*- coding: utf-8 -*-
import tkinter as tk

def is_latin_letter(char):
    return char.isalpha() and char.isascii() and char.isalnum()

def ceasar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if is_latin_letter(char):
            base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_char = char

        encrypted_text += encrypted_char

    return encrypted_text

def ceasar_decrypt(text, shift):
    return ceasar_encrypt(text, -shift)

def encrypt_button_clicked():
    text_to_encrypt = input_text.get("1.0", "end-1c")
    shift_amount = int(shift_entry.get())
    encrypted_text = ceasar_encrypt(text_to_encrypt, shift_amount)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

def decrypt_button_clicked():
    text_to_decrypt = input_text.get("1.0", "end-1c")
    shift_amount = int(shift_entry.get())
    decrypted_text = ceasar_decrypt(text_to_decrypt, shift_amount)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", decrypted_text)

# Tworzenie okna
window = tk.Tk()
window.title("Szyfr Cezara")

# Etykieta
label = tk.Label(window, text="Tekst:")
label.pack()

# Pole do wprowadzania tekstu
input_text = tk.Text(window, height=5, width=40, font=("Arial", 12))
input_text.pack()

# Przesunięcie
shift_label = tk.Label(window, text="Przesunięcie:")
shift_label.pack()
shift_entry = tk.Entry(window)
shift_entry.pack()

# Przyciski
encrypt_button = tk.Button(window, text="Zaszyfruj", command=encrypt_button_clicked)
encrypt_button.pack()
decrypt_button = tk.Button(window, text="Odszyfruj", command=decrypt_button_clicked)
decrypt_button.pack()

# Wynik
output_text = tk.Text(window, height=5, width=40, font=("Arial", 12))
output_text.pack()

window.mainloop()
