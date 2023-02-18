import customtkinter
import encrypter
import decrypter

def main():
  customtkinter.set_appearance_mode("dark")
  customtkinter.set_default_color_theme("blue")

  root = customtkinter.CTk()
  root.geometry("1000x500")
  root.wm_title("CatCryption")

  title_label = customtkinter.CTkLabel(master=root, text="CatCryption", font=("Mononoki NF", 40))
  title_label.pack(padx=10, pady=10)

  main_frame = customtkinter.CTkFrame(master=root)
  main_frame.pack(padx=2, pady=2, expand=True, fill="both")

  method_selector = customtkinter.CTkComboBox(master=main_frame, values=["Wave", "Binary", "Morse", "Reverse", "Cesar"], font=("Mononoki NF", 15))
  method_selector.grid(padx=10, pady=10)

  key_entry = customtkinter.CTkEntry(master=main_frame, placeholder_text="Key", font=("Mononoki NF", 16))
  key_entry.grid(padx=10, pady=10, column=1, row=0)

  first_textbox = customtkinter.CTkTextbox(master=main_frame, wrap="word", font=("Mononoki NF", 16))
  first_textbox.grid(padx=10, pady=10, column=0, row=1)

  second_textbox = customtkinter.CTkTextbox(master=main_frame, wrap="word", font=("Mononoki NF", 16))
  second_textbox.grid(padx=10, pady=10, column=1, row=1)

  encrypt_button = customtkinter.CTkButton(master=main_frame, text="Encrypt", font=("Mononoki NF", 16))
  encrypt_button.grid(padx=10, pady=10, column=1, row=2)

  decrypt_button = customtkinter.CTkButton(master=main_frame, text="Decrypt", font=("Mononoki NF", 16))
  decrypt_button.grid(padx=10, pady=10, column=0, row=2)

  root.mainloop()

if __name__ == "__main__":
  main()