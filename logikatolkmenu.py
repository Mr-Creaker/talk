from customtkinter import *
from PIL import Image
#import os
#import subprocess
#import sys
class AuthWindow(CTk):
    def __init__(self):
       super().__init__()
       self.geometry('700x400')
       self.title('Вхід')
       self.resizable(True, False)
       self.left_frame  = CTkFrame(self)
       self.left_frame.pack(side='left', fill='both')

       img_ctk = CTkImage(light_image=Image.open('D:\LOGICA\нд12.00\pic2.jpg'), size=(450, 400))
       self.img_label = CTkLabel(self.left_frame, text='Welcome', image=img_ctk, font=('Helvetica', 60, 'bold'))
       self.img_label.pack()
       main_font = ('Helvetica', 20, 'bold')
       self.right_frame = CTkFrame(self, fg_color='white')
       self.right_frame.pack_propagate(False)
       self.right_frame.pack(side='right', fill='both', expand='True')
       CTkLabel(self.right_frame, text='LogiTalk', font=main_font, text_color='#6753cc').pack(pady=60)

       self.name_entry = CTkEntry(self.right_frame, placeholder_text='☻ ім`я',
                                  height=45, font=main_font,corner_radius=25, fg_color='#eae6ff', border_color='#eae6ff',
                                  text_color='#6753cc', placeholder_text_color='#6753cc')
       self.name_entry.pack(fill='x', padx=10)
       self.settings_button = CTkButton(self.right_frame, text='Налаштування', height=45,
                                        corner_radius=25, fg_color='#eae6ff', font=main_font, text_color='#6753cc', compound='left')
       self.settings_button.pack(fill='x', padx=10, pady=5)

       self.connect_button = CTkButton(self.right_frame, text='УВІЙТИ', height=45,
                                        corner_radius=25, fg_color='#d06fc0', font=main_font, text_color='white',command=self.go_to_app)
       self.connect_button.pack(fill='x', padx=50, pady=10)
    def go_to_app(self):
       self.env={"name":self.name_entry.get()}
       self.destroy()
       # subprocess.Popen([sys.executable, "D:/LOGICA/нд12.00/LogiTalk/logikatolk.py"], env=self.env)
if __name__=="__main__":
    window = AuthWindow()
    window.mainloop()
