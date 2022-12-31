from customtkinter import * 
import os,time,datetime
from pygame import mixer
import datetime

def main():
    mixer.init()
    mainscreen=CTk()
    mainscreen.geometry("1920x1080")
    mainscreen.attributes('-fullscreen',True)
    mainscreen.title("Made by HieuLX")
    mainscreen.iconbitmap(r"C:\Users\laidu\OneDrive\Máy tính\Python Exam\Thuy Hang\Photos\cake_candles_icon_199451.ico")

    #//////////////////////////////////////////////////
    font_1=("Stencil",25,"bold","italic")
    font_2=("Times new roman",20,"bold","italic")
    font_3=("Monotype Corsiva",80,"bold","italic")
    font_4=("Stencil",100,"bold","italic")
    font_5=("Goudy Stout",60,"bold","italic")
    font_6=("STCaiyun",25)
    def font_size(x):
        font=("Goudy Stout",x,"bold","italic")
        return font
    
    #//////////////////////////////////////////////////
    getscreen=CTkToplevel(mainscreen)
    getscreen.title("Made by HieuLX")
    getscreen.geometry("600x300")
    getscreen.iconbitmap(r"C:\Users\laidu\OneDrive\Máy tính\Python Exam\Thuy Hang\Photos\birthdaycakewithcandles_79795.ico")

    def pgb():
        Name=entry_username.get()
        Date=entry_password.get()
        progressbar=CTkProgressBar(getscreen,
                                    # orient='horizontal',
                                    mode='determinate',
                                    )
        progressbar.determinate_value=0
        progressbar.place(x=50,y=250,height=20,width=500)
        progressbar.determinate_speed=2
        progressbar.start()
    
        def stop():
            progressbar.stop()
            time.sleep(0.5)
            getscreen.destroy()
            rendermainscreen(Name,Date)
        getscreen.after(2000,stop)
    #//////////////////////////////////////////////////
    label_1=CTkLabel(getscreen,
                    text="Enter User Account ",
                    text_color="Blue",
                    font=font_1,
                    )
    label_1.place(x=130,y=0,height=50,width=400)

    label_username=CTkLabel(getscreen,
                    text="Username",
                    text_color="Red",
                    font=font_2
                    )
    label_username.place(x=0,y=50,height=40,width=150)

    entry_username=CTkEntry(getscreen,
                    width=300,
                    text_color="Pink",
                    font=font_2
                    )
    entry_username.place(x=150,y=50,height=45,width=400)

    label_password=CTkLabel(getscreen,
                    text="Password",
                    text_color="Red",
                    font=font_2
                    )
    label_password.place(x=0,y=100,height=40,width=150)

    entry_password=CTkEntry(getscreen,
                    width=300,
                    text_color="Pink",
                    font=font_2
                    )
    entry_password.place(x=150,y=100,height=45,width=400)

    button_login=CTkButton(getscreen,
                            text="Log in",
                            text_color="Black",
                            font=font_2,
                            command=pgb)
    button_login.place(x=300,y=150,height=60,width=100)
    #//////////////////////////////////////////////////
    def music_countdown():
        music_countdown=mixer.music.load(r"C:\Users\laidu\OneDrive\Máy tính\Python Exam\Thuy Hang\Music\Countdown.mp3")
        mixer.music.play()
    def music_hpbd():
        musci_hpbd=mixer.music.load(r"C:\Users\laidu\OneDrive\Máy tính\Python Exam\Thuy Hang\Music\BDmusic.mp3")
        mixer.music.play()
    def music_second():
        musci_hpbd=mixer.music.load(r"C:\Users\laidu\OneDrive\Máy tính\Python Exam\Thuy Hang\Music\kimgiay.mp3")
        mixer.music.play()    
    #//////////////////////////////////////////////////
    def rendermainscreen(Name,Date):
        mainscreen.configure(bg="lightBlue")
         #//////////////////////////////////////////////////
        def update_color(x):
            x.configure(text_color="Green")
            x.after(300,update_color1,x)
        def update_color1(x):
            x.configure(text_color="Red")
            x.after(300,update_color,x)

        def countdown(k):
            now=datetime.datetime.now()
            x=58-datetime.datetime.now().second
            s,m,h,d,mon,y=now.second,now.minute,now.hour,now.day,now.month,now.year
            label_time.configure(text="  %s-%s-%s    %s-%s-%s  "%(h,m,s+2,d,mon,y))

            if x>10 and k==0:
                music_second()
                label_countdown.configure(text=str(x)+ " ")
            elif x<=10 and k==0 and x>=1:
                music_countdown()
                label_countdown.configure(text=str(x)+ " ")
            if x==0 and k==0:
                k+=1
                label_countdown.configure(text='',
                                        font=font_5)
                # update_color(label_countdown)              
            if x==57 and k==1:
                mainscreen.destroy()
            label_countdown.after(1000,countdown,k)

         #//////////////////////////////////////////////////
        label_pleasewait=CTkLabel(mainscreen,
                            text="\n\n\nPlease wait" "." +"\n\n\n",
                            text_color="Blue",
                            font=font_5
                            )
        def dots(x,y):
            k=59-datetime.datetime.now().second
            if k==0 or k==59:
                y=1
            if k==0 or k==59 and y==1:
                label_pleasewait.configure(text="\n Happy birtday \n "+Name+" \n"+" %s-%s-%s "%(Date[:2],Date[2:4],Date[4:8]),
                                            font=font_3)
                update_color(label_pleasewait)
                label_pleasewait.after(500,dots,0,y)

            if k==58 and y==1:
                return
            if k>0 and y==0:
                label_pleasewait.configure(text="\nPlease wait" +(x)*"." +"\n\n\n")
                if x<3:
                    label_pleasewait.after(500,dots,x+1,y)
                else :
                    label_pleasewait.after(500,dots,0,y)
        dots(0,0)
        label_pleasewait.place(x=0,y=0,height=800,width=1920)

        label_countdown=CTkLabel(mainscreen,
                                text=""+" ",
                                text_color="Red",
                                font=font_4
                                )
        label_countdown.place(x=0,y=700,width=1920,height=200)
        
        label_time=CTkLabel(mainscreen,
                            text="",
                            font=font_6,
                            text_color="Brown")
        label_time.place(x=1500,y=0,width=400,height=60)
        
        countdown(0)
    mainscreen.mainloop()
    def Render():
        # os.system("color 0A")
        os.system("cls")
        def render(file):
            text=file.readline().rstrip("\n")
            print(text)
            if text=="":
                return
            time.sleep(0.1)
            render(file)
        hpbd=open(r"C:\Users\laidu\OneDrive\Máy tính\Python Exam\THUY HANG\ASCII Photos\hpbd.txt",mode="r",encoding="UTF-8")
        render(hpbd)
        hpbd.close()
        time.sleep(5)
        os.system("cls")
        image_code=open(r"C:\Users\laidu\OneDrive\Máy tính\Python Exam\THUY HANG\ASCII Photos\NTHang.txt",mode="r",encoding="UTF-8")
        render(image_code)
        image_code.close()
    music_hpbd()
    Render()
    time.sleep(25)
main()