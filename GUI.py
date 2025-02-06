import AFFINE
from customtkinter import *
from PIL import Image

def affine_cipher(master):
    # Frame
    frame = CTkFrame(master=master, 
                     width=960,height=540, corner_radius=10)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Lable
    lable = CTkLabel(master=frame, text="Affine Cipher",
                     width=120, height=25, font= ("Algerian", 70), corner_radius=8)
    lable.place(relx=0.5, rely=0.12, anchor=CENTER)

    # Input
    input = CTkEntry(master=frame, placeholder_text="Enter the message...",
                     width=720, height=75, font= ("default", 20), corner_radius=10)
    input.place(relx=0.5, rely=0.3, anchor=CENTER)

    key_a = CTkEntry(master=frame, placeholder_text="Enter key a...",
                     width=135, height=50, font= ("default", 20), corner_radius=10)
    key_a.place(relx=0.2, rely=0.5, anchor=CENTER)

    key_b = CTkEntry(master=frame, placeholder_text="Enter key b...",
                     width=135, height=50, font= ("default", 20), corner_radius=10)
    key_b.place(relx=0.4, rely=0.5, anchor=CENTER)
    
    # Event button
    def encrypt_event():
        try:
            # Input values
            message = str(input.get()).upper()
            a = int(key_a.get())
            b = int(key_b.get())
            key = [a, b]
            
            # Lable text
            text = "Encrypted message: "
            lb_text.set(text)
            
            # Results message
            affine_encrypted_text = AFFINE.affine_encrypt(message, key)
            results_message.set(affine_encrypted_text)
            
            # ERROR
            error_message = ""
            if message == "":
                lb_text.set("Encryption error: ")
                error_message += "Message is empty!   "
                results_message.set(error_message)
            elif message.isalpha() == False:
                lb_text.set("Encryption error: ")
                error_message += "Message must be Alphabet!   "
                results_message.set(error_message)
        except:
            # ERROR
            error_message = ""
            lb_text.set("Encryption error: ")
            
            if message == "":
                error_message += "Message is empty!   "
                results_message.set(error_message)
            elif message.isalpha() == False:
                lb_text.set("Encryption error: ")
                error_message += "Message must be Alphabet!   "
                results_message.set(error_message)
            
            if key_a.get() == "":
                error_message += "Key 'a' is empty!   "
                results_message.set(error_message)
            elif key_a.get().isnumeric() == False:
                error_message += "Key 'a' must be a integer!   "
                results_message.set(error_message)
            
            if key_b.get() == "":
                error_message += "Key 'b' is empty!   "
                results_message.set(error_message)
            elif key_b.get().isnumeric() == False:
                error_message += "Key 'b' must be a integer!   "
                results_message.set(error_message)

    def decrypt_event():
        try:
            # Input values
            message = str(input.get()).upper()
            a = int(key_a.get())
            b = int(key_b.get())
            key = [a, b]
            
            # Lable text
            text = "Decrypted message: "
            lb_text.set(text)
            
            # Results message
            affine_decrypted_text = AFFINE.affine_decrypt(message, key)
            results_message.set(affine_decrypted_text)
            
            # ERROR
            error_message = ""
            if message == "":
                lb_text.set("Decryption error: ")
                error_message += "Message is empty!   "
                results_message.set(error_message)
            elif message.isalpha() == False:
                lb_text.set("Decryption error: ")
                error_message += "Message must be Alphabet!   "
                results_message.set(error_message)
        except:
            # ERROR
            error_message = ""
            lb_text.set("Decryption error: ")
            
            if message == "":
                error_message += "Message is empty!   "
                results_message.set(error_message)
            elif message.isalpha() == False:
                lb_text.set("Decryption error: ")
                error_message += "Message must be Alphabet!   "
                results_message.set(error_message)
            
            if key_a.get() == "":
                error_message += "Key 'a' is empty!   "
                results_message.set(error_message)
            elif key_a.get().isnumeric() == False:
                error_message += "Key 'a' must be a integer!   "
                results_message.set(error_message)
            elif a % 2 == 0:
                error_message = "Can't decrypt this message!   "
                results_message.set(error_message)
            
            if key_b.get() == "":
                error_message += "Key 'b' is empty!   "
                results_message.set(error_message)
            elif key_b.get().isnumeric() == False:
                error_message += "Key 'b' must be a integer!   "
                results_message.set(error_message)
            
    # Button    
    button = CTkButton(master=frame, text="Encrypt",command=encrypt_event,
                       width=135, height=50, font= ("Cascadia Code", 20), border_width=0, corner_radius=8)
    button.place(relx=0.6, rely=0.5, anchor=CENTER)
    
    button = CTkButton(master=frame, text="Decrypt", command=decrypt_event,
                       width=135, height=50, font= ("Cascadia Code", 20), border_width=0, corner_radius=8)
    button.place(relx=0.8, rely=0.5, anchor=CENTER)

    # Results
    lb_text = StringVar()
    lb_text.set("Results: ")
    results_lb = CTkLabel(master=frame, textvariable=lb_text,
                          width=120, height=50, font= ("Cascadia Code", 20), corner_radius=8)
    results_lb.place(relx=0.15, rely=0.6)
    
    results_message = StringVar()
    results = CTkEntry(master=frame, textvariable=results_message, state="readonly",
                       width=720, height=75, font= ("default", 20), corner_radius=10)
    results.place(relx=0.5, rely=0.8, anchor=CENTER)

def main():
    app = CTk()
    app.geometry("1280x720")
    app.title("AFFINE")

    set_default_color_theme("theme.json")
    
    image  = Image.open("background.jpg")
    background_image = CTkImage(image, size=(1280, 720))
    bg_lbl = CTkLabel(app, text="", image=background_image)
    bg_lbl.place(x=0, y=0)
    
    affine_cipher(app)
    
    
    app.resizable(False,False)
    app.mainloop()

if __name__ == '__main__':
    main()
