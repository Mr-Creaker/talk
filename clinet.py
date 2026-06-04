from customtkinter import *
import socket
import threading
import logikatolkmenu

win =logikatolkmenu.AuthWindow()
win.mainloop()
env = win.env
class Window(CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry("500x500")
        self.title("LogiTalk")
       
        self.text = CTkTextbox(self,width=450,height=300,text_color="red",fg_color="white")
        self.text.configure(state="disable")
        self.text.pack(pady=5)
        self.sent_text = CTkEntry(self,width=300,placeholder_text="Введіть повідомлення")
        self.sent_text.place(x=20,y=350)
        self.sent = CTkButton(self,text="Відправити",command=self.send_message)
        self.sent.place(x=350,y=350)
        self.name = env.get("name","ANONIM") 
        self.host = "localhost"
        self.port = 8080
        try:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.sock.connect((self.host,self.port))
            self.sock.send(f"TEXT@{self.name}@{self.name} приєднався до чату \n".encode())
            threading.Thread(target=self.recv_msg,daemon=True).start()
        except:
            self.add_message("Не вдалося підключитися до сервера")
    def recv_msg(self):
        buffer =""
        while True:
            try:
                chunk = self.sock.recv(4096)
                if not chunk:
                    break
                buffer+=chunk.decode(errors="ignore")
                while "\n" in buffer:
                    line,buffer = buffer.split("\n",1)
                    self.handle_line(line.strip())
            except:
                print("Server error")
        self.sock.close()
    def handle_line(self,line):
        if not line:
            return
        parts = line.split("@",3)
        msg_type = parts[0]
        if msg_type == "TEXT":
            if len(parts) >=3:
                author = parts[1]
                message = parts[2:]
                self.add_message(f"{author}:{message}")
        elif msg_type == "PIC":
            pass
    def add_message(self, text):
        self.text.configure(state="normal")
        self.text.insert(END,text+"\n")
        self.text.configure(state="disable")   
    def send_message(self):
        message = self.sent_text.get()
        if message:
            self.add_message(f"{self.name}:{message}")
            data = f"TEXT@{self.name}@{message}\n"
            try:
                self.sock.send(data.encode())
            except:
                print("Error in sentting message")
        self.sent_text.delete(0,END)
    
     # D:\LOGICA\нд12.00\pic2.jpg
#    def send_pic(self):
#        path = r"D:\LOGICA\нд12.00\pic2.jpg"
#        with open(path, "rb") as pic:
#            data = pic.read()
#        print(data)
#Window().send_pic()
Window().mainloop()