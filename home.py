from tkinter import *
from tkinter import messagebox
import time
import pymysql

time1 = ''


def main_win():
    conn = pymysql.connect(host="localhost", user="root", password="", database="pizza_bill")
    cursor = conn.cursor()
    window = Tk()
    window.config(bg="green")
    window.title("ORDER PIZZA")
    window.geometry("900x750")
    pizza1 = IntVar()
    pizza2 = IntVar()
    pizza3 = IntVar()
    pizza4 = IntVar()
    pizza5 = IntVar()
    Total = IntVar()
    pizza6 = IntVar()
    pizza7 = IntVar()
    name_val = StringVar()
    mob_val = StringVar()
    name_lab = Label(window, bg="crimson", fg="yellow", text="SMOKIN' JOE's PIZZA",
                     font=("Comic Sans MS", 24, "bold italic"),
                     width=20, relief="solid")
    name_lab.place(x=240, y=20)
    tag_lab = Label(window, fg="yellow", bg="green", text="PIZZA TIME, FAMILY TIME",
                    font=("Comic Sans MS", 12, "bold italic"), width=25)
    tag_lab.place(x=390, y=72)
    clock = Label(window, fg="yellow", bg="crimson", font=("Comic Sans MS", 18, "italic"), width=10, relief="solid")
    clock.place(x=370, y=102)
    time1 = ''

    def tick():
        global time1
        time2 = time.strftime('%H:%M:%S')
        if time1 != time2:
            time1 = time2
            clock.config(text=time2)
        clock.after(200, tick)

    tick()

    def add(e):
        s = e.get()
        if s <= 69:
            s = s + 1
        e.set(s)

    def sub(e):
        s = e.get()
        if s >= 1:
            s = s - 1
        e.set(s)

    def out():
        window.destroy()

    def val():
        msg_bx = Tk()
        msg_bx.withdraw()
        messagebox.showwarning("warning", "Invalid Name/Mobile no")

    name_lab = Label(window, fg="yellow", bg="crimson", text="NAME - ", font=("Comic Sans MS", 18, "italic"), width=7,
                     relief="solid")
    name_lab.place(x=20, y=150)
    name_entry = Entry(window, textvar=name_val, width=24, font=18, relief="solid")
    name_entry.place(x=145, y=155)
    mob_lab = Label(window, fg="yellow", bg="crimson", text="MOBILE NO - ", font=("Comic Sans MS", 18, "italic"),
                    relief="solid", width=12)
    mob_lab.place(x=454, y=150)
    mob_entry = Entry(window, textvar=mob_val, width=20, font=18, relief="solid")
    mob_entry.place(x=660, y=155)
    # first one
    photo1 = PhotoImage(file="p1.png")
    Button(window, image=photo1, width=95, height=80, relief="solid").place(x=15, y=215)
    pizza1_button1 = Button(window, text="-", font=12, width=4, relief="solid", command=lambda: sub(pizza1)).place(
        x=130,
        y=212)
    pizza1_entry = Entry(window, textvar=pizza1, width=4, font=35, relief="solid").place(x=195, y=217)
    pizza1_button2 = Button(window, text="+", font=12, width=4, relief="solid", command=lambda: add(pizza1)).place(
        x=254,
        y=212)
    pizza1_lab = Label(window, fg="yellow", bg="crimson", text="MARGHARITA- 200rs",
                       font=("Comic Sans MS", 12, "bold italic"),
                       width=20, relief="solid").place(x=130, y=270)
    # next pizza
    photo2 = PhotoImage(file="p2.png")
    Button(window, image=photo2, width=95, height=80, relief="solid").place(x=475, y=215)
    pizza2_button1 = Button(window, text="-", font=12, width=4, relief="solid", command=lambda: sub(pizza2)).place(
        x=590,
        y=212)
    pizza2_entry = Entry(window, textvar=pizza2, width=4, font=35, relief="solid").place(x=655, y=217)
    pizza2_button2 = Button(window, text="+", font=12, width=4, relief="solid", command=lambda: add(pizza2)).place(
        x=714,
        y=212)
    pizza2_lab = Label(window, fg="yellow", bg="crimson", text="GARLIC BREAD- 45rs/1pc",
                       font=("Comic Sans MS", 12, "bold italic"), width=23, relief="solid").place(x=590, y=270)
    # next line
    # first one
    photo3 = PhotoImage(file="p3.png")
    Button(window, image=photo3, width=95, height=80, relief="solid").place(x=15, y=335)
    pizza3_button1 = Button(window, text="-", font=12, width=4, relief="solid", command=lambda: sub(pizza3)).place(
        x=130,
        y=342)
    pizza3_entry = Entry(window, textvar=pizza3, width=4, font=35, relief="solid").place(x=195, y=347)
    pizza3_button2 = Button(window, text="+", font=12, width=4, relief="solid", command=lambda: add(pizza3)).place(
        x=254,
        y=342)
    pizza3_lab = Label(window, fg="yellow", bg="crimson", text="OLIVE CHEESE DELIGHT- 270rs",
                       font=("Comic Sans MS", 12, "bold italic"), width=30, relief="solid").place(x=130, y=390)
    # next pizza
    photo4 = PhotoImage(file="p4.png")
    Button(window, image=photo4, width=95, height=80, relief="solid").place(x=475, y=335)
    pizza4_button1 = Button(window, text="-", font=12, width=4, relief="solid", command=lambda: sub(pizza4)).place(
        x=590,
        y=342)
    pizza4_entry = Entry(window, textvar=pizza4, width=4, font=35, relief="solid").place(x=655, y=347)
    pizza4_button2 = Button(window, text="+", font=12, width=4, relief="solid", command=lambda: add(pizza4)).place(
        x=714,
        y=342)
    pizza4_lab = Label(window, fg="yellow", bg="crimson", text="COKE (500 ml)- 80rs",
                       font=("Comic Sans MS", 12, "bold italic"), width=20, relief="solid").place(x=590, y=390)
    # next line
    # first one
    photo5 = PhotoImage(file="p5.png")
    Button(window, image=photo5, width=95, height=80, relief="solid").place(x=15, y=462)
    pizza5_button1 = Button(window, text="-", font=12, width=4, relief="solid", command=lambda: sub(pizza5)).place(
        x=130,
        y=462)
    pizza5_entry = Entry(window, textvar=pizza5, width=4, font=35, relief="solid").place(x=195, y=467)
    pizza5_button2 = Button(window, text="+", font=12, width=4, relief="solid", command=lambda: add(pizza5)).place(
        x=254,
        y=462)
    pizza5_lab = Label(window, fg="yellow", bg="crimson", text="WHITE SAUCE PASTA- 310rs",
                       font=("Comic Sans MS", 12, "bold italic"), width=26, relief="solid").place(x=130, y=510)
    # next pizza
    photo6 = PhotoImage(file="p6.png")
    Button(window, image=photo6, width=95, height=80, relief="solid").place(x=475, y=462)
    pizza6_button1 = Button(window, text="-", font=12, width=4, relief="solid", command=lambda: sub(pizza6)).place(
        x=590,
        y=462)
    pizza6_entry = Entry(window, textvar=pizza6, width=4, font=35, relief="solid").place(x=655, y=467)
    pizza6_button2 = Button(window, text="+", font=12, width=4, relief="solid", command=lambda: add(pizza6)).place(
        x=714,
        y=462)
    pizza6_lab = Label(window, fg="yellow", bg="crimson", text="CHOCOLATE SMOOTHIE - 120rs",
                       font=("Comic Sans MS", 12, "bold italic"), width=27, relief="solid").place(x=590, y=510)
    # next line
    # first one
    photo7 = PhotoImage(file="p7.png")
    Button(window, image=photo7, width=95, height=80, relief="solid").place(x=15, y=573)
    pizza7_button1 = Button(window, text="-", font=12, width=4, relief="solid", command=lambda: sub(pizza7)).place(
        x=130,
        y=582)
    pizza7_entry = Entry(window, textvar=pizza7, width=4, font=35, relief="solid").place(x=195, y=587)
    pizza7_button2 = Button(window, text="+", font=12, width=4, relief="solid", command=lambda: add(pizza7)).place(x=254, y=582)
    pizza7_lab = Label(window, fg="yellow", bg="crimson", text="TANGY TOMATO PASTA- 280rs",
                       font=("Comic Sans MS", 12, "bold italic"), width=26, relief="solid").place(x=135, y=630)
    prices = [200, 45, 270, 80, 310, 120, 280]

    def sum_up(e):
        s1 = pizza1.get()
        s2 = pizza2.get()
        s3 = pizza3.get()
        s4 = pizza4.get()
        s5 = pizza5.get()
        s6 = pizza6.get()
        s7 = pizza7.get()
        sum_all = ((s1 * 200) + (s2 * 45) + (s3 * 270) + (s4 * 80) + (s5 * 310) + (s6 * 120) + (s7 * 280))
        tax = sum_all * 0.15
        sum_all += tax
        e.set(sum_all)

    # final buttons
    total_button1 = Button(window, bg="blue", fg="white", text="TOTAL BILL", font=16, width=10, relief="solid",
                           command=lambda: sum_up(Total)).place(x=570,
                                                                y=602)
    total_entry = Entry(window, textvar=Total, width=7, font=35, relief="solid").place(x=715, y=607)

    def bill():
        sum_up(Total)
        n = name_val.get()
        m = mob_val.get()
        p1 = pizza1.get()
        p2 = pizza2.get()
        p3 = pizza3.get()
        p4 = pizza4.get()
        p5 = pizza5.get()
        p6 = pizza6.get()
        p7 = pizza7.get()
        t1 = Total.get()
        s1 = name_val.get()
        s2 = mob_val.get()
        list_3 = []
        list_1 = []
        list_2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        list_4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', ' ']
        token = 0
        for char in s2:
            list_1.append(char)
        for mem in list_1:
            if mem not in list_2:
                token = 1
        for char in s1:
            list_3.append(char)
        for mem in list_3:
            if mem.lower() not in list_4:
                token = 1
        if len(s2) == 10 and (token == 0) and s1 != "":
            sum_up(Total)
            cursor.execute("INSERT INTO bill_o (name, mobile, p1, p2, p3, p4, p5, p6, p7, "
                           "total)  VALUES("'%s'", "'%s'", "'%s'", "'%s'", "'%s'", "'%s'", "'%s'", "'%s'", "'%s'", "'%s'")",
                           (n, m, p1, p2, p3, p4, p5, p6, p7, t1))
            conn.commit()
            list1 = [pizza1, pizza2, pizza3, pizza4, pizza5, pizza6, pizza7]
            window2 = Tk()
            window2.config(bg="green")
            window2.title("YOUR BILL")
            window2.geometry("500x530")
            l = time.strftime('%H:%M:%S')
            name_lab1 = Label(window2, bg="crimson", fg="yellow", text="SMOKIN' JOE's PIZZA",
                              font=("Comic Sans MS", 15, "bold italic"),
                              width=20, relief="solid")
            name_lab1.place(x=120, y=20)
            tag_lab1 = Label(window2, fg="yellow", bg="green", text="PIZZA TIME, FAMILY TIME",
                             font=("Comic Sans MS", 7, "bold italic"), width=25)
            tag_lab1.place(x=220, y=55)
            clock1 = Label(window2, fg="yellow", bg="crimson", text=l, font=("Comic Sans MS", 9, "italic"), width=10,
                           relief="solid")
            clock1.place(x=210, y=75)
            Label(window2, fg="yellow", bg="crimson", text=n, font=("Comic Sans MS", 11, "italic"),
                  relief="solid").place(x=20, y=120)
            Label(window2, fg="yellow", bg="crimson", text=m, font=("Comic Sans MS", 11, "italic"),
                  relief="solid").place(x=385, y=120)
            mar = ('Margharita',)
            gb = ('Garlic', 'Bread')
            ocd = ('Olive', 'Cheese', 'Delight')
            co = ('Coke',)
            wsp = ('White', 'Sauce', 'Pasta')
            cs = ('Chocolate', 'Shake')
            ttp = ('Tangy', 'Tomato', 'Pasta')
            list2 = [mar, gb, ocd, co, wsp, cs, ttp]
            s = ""
            g = 0
            for i in range(0, 7):
                if list1[i].get() != 0:
                    for num in list2[i]:
                        s = s + num + " "
                    Label(window2, text=s, relief="solid", font=("ariel", 14, "bold")).place(x=30, y=180 + g)
                    Label(window2, text=str(list1[i].get()), relief="solid", font=("ariel", 14, "bold")).place(x=290,
                                                                                                               y=180 + g)
                    Label(window2, text=(str(list1[i].get() * prices[i]), "rs"), relief="solid",
                          font=("ariel", 14, "bold")).place(x=410, y=180 + g)
                    g = g + 30
                    s = ""
            t = Total.get() - (Total.get() / 1.15)
            r = round(t)
            Label(window2, text="Tax", relief="solid", font=("ariel", 14, "bold")).place(x=30, y=420)
            Label(window2, text=(str(r), "rs"), relief="solid", font=("ariel", 14, "bold")).place(
                x=410, y=420)
            Label(window2, text="Total", relief="solid", font=("ariel", 14, "bold")).place(x=30, y=450)
            Label(window2, text=(str(Total.get()), "rs"), relief="solid", font=("ariel", 14, "bold")).place(
                x=410, y=450)
        else:
            val()

    # final buttons
    order = Button(window, bg="blue", fg="white", text="ORDER", font=16, width=10, relief="solid",
                   command=bill).place(x=210, y=692)
    get_out = Button(window, bg="red", fg="white", text="EXIT", font=16, width=10, relief="solid", command=out).place(
        x=530,
        y=692)
    window.mainloop()


main_win()
