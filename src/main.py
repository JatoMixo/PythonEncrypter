import customtkinter
import encrypter
import decrypter

def main():
  customtkinter.set_appearance_mode("dark")
  customtkinter.set_default_color_theme("dark-blue")

  root = customtkinter.CTk()
  root.geometry("500x350")
  root.wm_title("CatCryption")

  root.mainloop()
  pass


if __name__ == "__main__":
  main()