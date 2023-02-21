import customtkinter
import encrypter
import decrypter
from pyperclip import copy

method = "Wave"

def main():

  # Config
  customtkinter.set_appearance_mode("dark")
  customtkinter.set_default_color_theme("blue")
  #/Config

  # Window
  root = customtkinter.CTk()
  root.geometry("445x390")
  root.wm_title("CatCryption")
  # /Window

  # Title & Frame
  title_label = customtkinter.CTkLabel(master=root, text="CatCryption", font=("Mononoki NF", 40))
  title_label.pack(padx=10, pady=10)

  main_frame = customtkinter.CTkFrame(master=root)
  main_frame.pack(padx=2, pady=2, expand=True, fill="both")
  # /Title & Frame

  # Keys entry
  key_entry = customtkinter.CTkEntry(master=main_frame, placeholder_text="Key", font=("Mononoki NF", 16))
  key_entry.grid(padx=10, pady=10, column=1, row=0, sticky=customtkinter.W)# + customtkinter.E)
  
  only_words_switch = customtkinter.CTkSwitch(master=main_frame, text="Only words", font=("Mononoki NF", 16))

  # /Keys Entry
  # Method selector

  def update_encryption_system(choice):

    global method
    method = choice

    key_entry.grid_remove()
    only_words_switch.grid_remove()

    if choice == "Binary" or choice == "Morse":
      return
    
    if choice == "Wave" or choice == "Cesar":
      key_entry.grid(padx=10, pady=10, column=1, row=0, sticky=customtkinter.E + customtkinter.W)
      return
    
    if choice == "Reverse":
      only_words_switch.grid(padx=10, pady=10, column=1, row=0)

  method_selector = customtkinter.CTkComboBox(master=main_frame, values=["Wave", "Binary", "Morse", "Reverse", "Cesar"], font=("Mononoki NF", 15), state="readonly", command=update_encryption_system)
  method_selector.set("Wave")
  method_selector.grid(padx=10, pady=10, sticky=customtkinter.E, row=0, column=0)
  # /Method selector

  first_textbox = customtkinter.CTkTextbox(master=main_frame, wrap="word", font=("Mononoki NF", 16))
  first_textbox.grid(padx=10, pady=10, column=0, row=1)

  second_textbox = customtkinter.CTkTextbox(master=main_frame, wrap="word", font=("Mononoki NF", 16), state="disabled")
  second_textbox.grid(padx=10, pady=10, column=1, row=1)

  def decrypt():

    global method

    message = str(first_textbox.get("0.0", "end"))

    message.removesuffix("\n")

    key = key_entry.get()
    only_words = bool(only_words_switch.get())

    decrypted_message = ""

    if method == "Wave":
      decrypted_message = decrypter.Decrypter().wave_decryption(message, key)
    elif method == "Cesar":
      decrypted_message = decrypter.Decrypter().cesar_decryption(message, key)
    elif method == "Reverse":
      decrypted_message = decrypter.Decrypter().reverse_decryption(message, only_words)
    elif method == "Binary":
      decrypted_message = decrypter.Decrypter().binary_decryption(message)
    elif method == "Morse":
      decrypted_message = decrypter.Decrypter().morse_decryption(message)

    second_textbox.configure(state="normal")
    second_textbox.delete("0.0", "end")
    second_textbox.insert("0.0", decrypted_message)
    second_textbox.configure(state="disabled")

  def encrypt():
    
    global method

    message = str(first_textbox.get("0.0", "end"))

    message = message.removesuffix("\n")

    key = key_entry.get()
    only_words = bool(only_words_switch.get())

    encrypted_message = ""

    if method == "Wave":
      encrypted_message = encrypter.Encrypter().wave_encryption(message, key)
    elif method == "Cesar":
      encrypted_message = encrypter.Encrypter().cesar_encryption(message, key)
    elif method == "Reverse":
      encrypted_message = encrypter.Encrypter().reverse_encryption(message, only_words)
    elif method == "Binary":
      encrypted_message = encrypter.Encrypter().binary_encryption(message)
    elif method == "Morse":
      encrypted_message = encrypter.Encrypter().morse_encryption(message)
    
    second_textbox.configure(state="normal")
    second_textbox.delete("0.0", "end")
    second_textbox.insert("0.0", encrypted_message)
    second_textbox.configure(state="disabled")

  encrypt_button = customtkinter.CTkButton(master=main_frame, text="Encrypt", font=("Mononoki NF", 16), command=encrypt)
  encrypt_button.grid(padx=10, pady=10, column=1, row=2, sticky=customtkinter.W)

  decrypt_button = customtkinter.CTkButton(master=main_frame, text="Decrypt", font=("Mononoki NF", 16), command=decrypt)
  decrypt_button.grid(padx=10, pady=10, row=2, column=0, sticky=customtkinter.E)

  def copy_to_clipboard():

    global method

    second_textbox_text = str(second_textbox.get("0.0", "end"))
    second_textbox_text.removesuffix("\n")
    key = str(key_entry.get())
    only_words = str(bool(only_words_switch.get()))

    message = ""

    if method == "Wave" or method == "Cesar":
      message = f"Key: {key}\nMessage: {second_textbox_text}"
    if method == "Reverse":
      message = f"Only-Words: {only_words}\nMessage: {second_textbox_text}"
    if method == "Morse" or method == "Binary":
      message = f"Message: {second_textbox_text}"

    copy(message)

  copy_text_button = customtkinter.CTkButton(master=main_frame, text="Copy", width=40, command=copy_to_clipboard)
  copy_text_button.grid(padx=10, pady=10, column=1, row=0, sticky=customtkinter.E)
  root.mainloop()

if __name__ == "__main__":
  main()