from tkinter import *
from tkcalendar import DateEntry

pencere = Tk()

pencere.geometry("450x350+700+200")
pencere.configure(bg="#1eebeb")
pencere.title("Üyelik Formu")
pencere.resizable(width=False, height=False)
pencere.bind("<F11>", lambda x: pencere.attributes("-fullscreen", not pencere.attributes("-fullscreen")))
pencere.bind("<Escape>", lambda x: pencere.attributes(exit()))

frame1 = Frame(pencere, bg="#1eebeb")
frame1.grid(row=0, column=0)
frame2 = Frame(pencere, bg="#1eebeb")
frame2.grid(row=0, column=1)
frame3 = Frame(pencere, bg="#1eebeb")
frame3.grid(row=0, column=2)
frame4 = Frame(pencere, bg="#1eebeb")
frame4.grid(row=1, column=2)
frame5=Frame(pencere,bg="#1eebeb")
frame5.place(x=0,y=180)

canvas=Canvas(frame5,bg="#1eebeb",highlightbackground="#1eebeb")
canvas.create_line(25, 5, 400, 5)
canvas.pack()

etiket1 = Label(frame1, text="AD", font="arial 12 bold", bg="#1eebeb")
etiket1.pack()
etiket1 = Label(frame1, text="SOYAD", font="arial 12 bold", bg="#1eebeb")
etiket1.pack()
etiket1 = Label(frame1, text="YAŞ", font="arial 12 bold", bg="#1eebeb")
etiket1.pack()
etiket1 = Label(frame1, text="DOĞUM", font="arial 12 bold", bg="#1eebeb")
etiket1.pack()
etiket1 = Label(frame1, text="CİNSİYET", font="arial 12 bold", bg="#1eebeb")
etiket1.pack()

etiket2 = Label(frame2, text=":", font="arial 12 bold", bg="#1eebeb")
etiket2.pack()
etiket2 = Label(frame2, text=":", font="arial 12 bold", bg="#1eebeb")
etiket2.pack()
etiket2 = Label(frame2, text=":", font="arial 12 bold", bg="#1eebeb")
etiket2.pack()
etiket2 = Label(frame2, text=":", font="arial 12 bold", bg="#1eebeb")
etiket2.pack()
etiket2 = Label(frame2, text=":", font="arial 12 bold", bg="#1eebeb")
etiket2.pack()
from tkinter import messagebox


def kayit():
    mesaj = ""
    if giris1.get() and giris2.get():
        if giris1.get() and giris2.get():
            mesaj += "Kayıt tamamlandı"
            messagebox.showinfo("Bilgi", mesaj)
    elif giris1 and giris2 != StringVar:
        mesaj += "alanı doldur"
        messagebox.showwarning("Uyarı", "Gerekli alanları doldurun")


giris1 = Entry(frame3, bg="light yellow", font="arial 10 bold", justify="center", relief=GROOVE, width=20)
giris1.pack(padx=5, pady=2)
giris2 = Entry(frame3, bg="light yellow", font="arial 10 bold", justify="center", relief=GROOVE, width=20)
giris2.pack(padx=5, pady=2)

spinbox = Spinbox(frame3, bg="light yellow", font="arial 10 bold", justify="center", width=19, from_=18, to=60)
spinbox.pack(padx=5, pady=2)

ival = StringVar(value="\t")

# liste=["OCAK","ŞUBAT","MART","NİSAN","MAYIS","HAZİRAN","TEMMUZ","AĞUSTOS","EYLÜL","EKİM","KASIM","ARALIK"]
# optionmenu=OptionMenu(frame3,ival,*liste)
# optionmenu.config(font="arial 10 bold",width=15)
# optionmenu.pack(padx=5,pady=2)
tarihsecme = DateEntry(frame3, width=19, background="#5142f5", foreground="#faf605", locale="tr_TR",
                       font="arial 10 bold")
tarihsecme.pack(padx=5, pady=2)


def sec():
    print("seçilen cinsiyet " + str(intvar.get()))


intvar = IntVar()

r1 = Radiobutton(frame3, text="ERKEK", variable=intvar, font="arial 10 bold", value=1, command=sec)
r1.pack(padx=5, side=LEFT)
r2 = Radiobutton(frame3, text="KADIN", variable=intvar, font="arial 10 bold", value=2, command=sec)
r2.pack(padx=5, side=LEFT)


resim = PhotoImage(file="images.png")
resimboyut = resim.subsample(2, 2)

resimYukleme = Button(pencere, image=resimboyut, text="Yükle", compound=TOP, width=130, height=130,
                      font="arial 10 bold")
resimYukleme.place(x=300, y=11)

def temiz():
    giris1.delete(0,"end")
    giris2.delete(0,"end")




kaydet = Button(pencere, text="KAYDET", font="arial 12 bold", bg="#e3f707", activebackground="yellow", command=kayit)
kaydet.place(x=100, y=200)
temizle = Button(pencere, text="TEMİZLE", font="arial 12 bold", bg="#ed9fb8", activebackground="#ed9fb8",command=temiz)
temizle.place(x=200, y=200)

pencere.mainloop()

