from tkinter import *
import tkinter
from tkinter import ttk, messagebox
from datetime import datetime
import random
import sqlite3
from googletrans import Translator, LANGUAGES

def create_connection(db_file):
    """Create a database connection to a SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

# Replace MySQL connection with SQLite3 connection
conn = create_connection('travel_app.db')
cursor = conn.cursor()

def trans():
    def Translate():
        translator = Translator()
        translated = translator.translate(text=Input_text.get(1.0, END), src=src_lang.get(), dest=dest_lang.get())

        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)

    trans_w = Tk()
    trans_w.geometry('1080x400')
    trans_w.resizable(300, 300)
    trans_w.config(bg='light coral')
    trans_w.title("Language Translator")

    Label(trans_w, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='light coral').pack()

    Label(trans_w, text="Enter Text", font='arial 13 bold', bg='blue').place(x=200, y=60)

    Input_text = Text(trans_w, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
    Input_text.place(x=30, y=100)

    Label(trans_w, text="Output", font='arial 13 bold', bg='blue').place(x=780, y=60)

    Output_text = Text(trans_w, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
    Output_text.place(x=600, y=100)

    language = list(LANGUAGES.values())

    src_lang = ttk.Combobox(trans_w, values=language, width=22)
    src_lang.place(x=20, y=60)
    src_lang.set('choose input language')

    dest_lang = ttk.Combobox(trans_w, values=language, width=22)
    dest_lang.place(x=890, y=60)
    dest_lang.set('choose output language')

    trans_btn = Button(trans_w, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='blue', activebackground='sky blue')
    trans_btn.place(x=490, y=180)

    trans_w.mainloop()

# Other functions (currency converter, feedback, FAQ, tips, random destination) and main() function remains the same.
def curr():
    root2 = Tk()

    root2.title("Currency Converter")

    Tops = Frame(root2, pady=2, width=1850, height=100, relief="raised")

    Tops.grid(row=0, column=0)

    headlabel = Label(Tops, font=('lato black', 19, 'bold'), text='Currency Converter',

                      bg='CornflowerBlue', fg='black')

    headlabel.grid(row=1, column=0, sticky=W)

    variable1 = StringVar(root2)

    variable2 = StringVar(root2)

    variable1.set("currency")

    variable2.set("currency")

    # Function To For Real Time Currency Conversion

    def RealTimeCurrencyConversion():

        from forex_python.converter import CurrencyRates

        c = CurrencyRates()

        from_currency = variable1.get()

        to_currency = variable2.get()

        if (Amount1_field.get() == ""):

            tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")



        elif (from_currency == "currency" or to_currency == "currency"):

            tkinter.messagebox.showinfo("Error !!",

                                        "Currency Not Selected.\n Please select FROM and TO Currency form menu.")



        else:

            new_amt = c.convert(to_currency, from_currency, float(Amount1_field.get()))

            new_amount = float("{:.4f}".format(new_amt))

            Amount2_field.insert(0, str(new_amount))

    # clearing all the data entered by the user

    def clear_all():

        Amount1_field.delete(0, END)

        Amount2_field.delete(0, END)

    CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

    root2.configure(background='CornflowerBlue')

    root2.geometry("700x400")

    Label_1 = Label(root2, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="CornflowerBlue", fg="black")

    Label_1.grid(row=2, column=0, sticky=W)

    label1 = Label(root2, font=('lato black', 15, 'bold'), text="\t Amount : ", bg="CornflowerBlue", fg="black")

    label1.grid(row=2, column=0, sticky=W)

    label1 = Label(root2, font=('lato black', 15, 'bold'), text="\t From Currency : ", bg="CornflowerBlue", fg="black")

    label1.grid(row=4, column=0, sticky=W)

    label1 = Label(root2, font=('lato black', 15, 'bold'), text="\t To Currency : ", bg="CornflowerBlue", fg="black")

    label1.grid(row=5, column=0, sticky=W)

    label1 = Label(root2, font=('lato black', 15, 'bold'), text="\t Converted Amount : ", bg="CornflowerBlue",
                   fg="black")

    label1.grid(row=9, column=0, sticky=W)

    FromCurrency_option = OptionMenu(root2, variable1, *CurrenyCode_list)

    ToCurrency_option = OptionMenu(root2, variable2, *CurrenyCode_list)

    FromCurrency_option.grid(row=5, column=1, ipadx=45, sticky=E)

    ToCurrency_option.grid(row=4, column=1, ipadx=45, sticky=E)

    # Amount

    Amount1_field = Entry(root2)

    Amount1_field.grid(row=2, column=1, ipadx=28, sticky=E)

    # Converted amount

    Amount2_field = Entry(root2)

    Amount2_field.grid(row=9, column=1, ipadx=31, sticky=E)

    Label_9 = Button(root2, font=('arial', 15, 'bold'), text=" Convert ", padx=2, pady=2, bg="DimGrey", fg="white",

                     command=RealTimeCurrencyConversion)

    Label_9.grid(row=6, column=0)

    Label_1 = Label(root2, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="CornflowerBlue", fg="black")

    Label_1.grid(row=9, column=0, sticky=W)

    Label_9 = Button(root2, font=('arial', 15, 'bold'), text=" Clear All ", padx=2, pady=2, bg="DimGrey", fg="white",

                     command=clear_all)

    Label_9.grid(row=10, column=0)

    # retur=ttk.Button(root2, text="Go back to home", command=main).grid(row=15, column=4, sticky='w')

    root2.mainloop()


# curr()


def feedback():
    from tkinter import ttk
    from tkinter import messagebox

    root4 = Tk()
    frame_header = ttk.Frame(root4)
    frame_header.pack()
    headerlabel = ttk.Label(frame_header, text='FEEDBACK SYSTEM', foreground='blue',
                            font=('Arial', 24))
    headerlabel.grid(row=0, column=1)
    messagelabel = ttk.Label(frame_header,
                             text='PLEASE TELL US WHAT YOU THINK',
                             foreground='green', font=('Arial', 10))
    messagelabel.grid(row=1, column=1)

    frame_content = ttk.Frame(root4)
    frame_content.pack()
    # def submit():
    #     username = entry_name.get()
    #     print(username)
    myvar = StringVar()
    var = StringVar()
    # cmnt= StringVar()
    namelabel = ttk.Label(frame_content, text='Name')
    namelabel.grid(row=0, column=0, padx=5, sticky='sw')
    global entry_name
    entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=myvar)

    f1 = open("Feedback_file.txt", "a")
    f1.write(myvar.get())
    f1.close()
    # f2=open("Feedback_file.txt","r")
    # str=f2.read()
    # print(str)
    # f2.close()

    global textcomment

    global entry_email
    entry_name.grid(row=1, column=0)

    emaillabel = ttk.Label(frame_content, text='Email')
    emaillabel.grid(row=0, column=1, sticky='sw')
    entry_email = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=var)
    entry_email.grid(row=1, column=1)

    commentlabel = ttk.Label(frame_content, text='Comment', font=('Arial', 10))
    commentlabel.grid(row=2, column=0, sticky='sw')
    textcomment = Text(frame_content, width=55, height=10)
    textcomment.grid(row=3, column=0, columnspan=2)

    textcomment.config(wrap='word')

    def clear():
        messagebox.showinfo(title='clear', message='Do you want to clear?')
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        textcomment.delete(1.0, END)

    def submit():
        global entry_name
        global entry_email
        global textcomment
        print('Name:{}'.format(myvar.get()))
        print('Email:{}'.format(var.get()))
        print('Comment:{}'.format(textcomment.get(1.0, END)))
        f1 = open("Feedback_file.txt", "a")
        f1.write('Name:{}'.format(myvar.get()) + '\n')
        f1.write('Email:{}'.format(var.get()) + '\n')
        f1.write('Comment:{}'.format(textcomment.get(1.0, END)) + '\n' + '\n')
        f1.close()
        f2 = open("Feedback_file.txt", "r")
        str = f2.read()
        print(str)
        f2.close()

        messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        textcomment.delete(1.0, END)

    submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=4, column=0, sticky='e')
    clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=4, column=1, sticky='w')
    # retbutton = ttk.Button(frame_content, text='Go back home', command=main).grid(row=4, column=2, sticky='w')
    mainloop()


def read():
    com = Tk()
    com.title("View feedback")
    com.geometry("600x600")
    com.configure(bg='LightPink')
    f2 = open("Feedback_file.txt", "r")
    st = f2.read()
    # print(str)
    label1 = Label(com, text="Feedback helps us improve!", fg="black", bg="LightYellow", font=("Helvetica", 20))
    label1.place(x=5, y=5)
    label2 = Label(com, text=st, fg="black", bg="LightYellow", font=("Helvetica", 15))
    label2.place(x=5, y=50)
    # retur=Button(com, text="Go back to home",command=main,font = 'arial 12 bold',pady = 5)
    # retur.place(x = 400, y=5 )
    f2.close()
    com.mainloop()


# read()
# feedback()

def faq():
    window = Tk()
    window.title("FAQ's")
    window.minsize(width=1100, height=1000)
    window.maxsize(width=2050, height=2050)
    window.configure(bg='lavender blush')
    l = Label(window, text="FREQUENTLY ASKED QUESTIONS", fg="black", font=("Helvetica", 30), bg="lavender blush")
    l.place(x=0, y=10)
    l1 = Label(window, text="Question-->What are some essential carry-ons in a flight?", fg="black", bg="coral1",
               font=("Helvetica", 18))
    l1.place(x=0, y=50)
    l2 = Label(window,
               text="Answer-->Passport,ID,travel documents,sanitiser,snacks,water,power bank and phone charger,wet wipes,earphones,soft blanket or a jacket",
               fg="blue", bg="burlywood1", font=("Helvetica", 16))
    l2.place(x=0, y=90)
    l3 = Label(window, text="Question-->What items should I never put in your check-in?", fg="black", bg="coral1",
               font=("Helvetica", 18))

    l3.place(x=0, y=130)
    l4 = Label(window,
               text="Answer-->Medicine,valubale and delicate items,camera film,cash or credit card,chargers and power banks",
               fg="blue", bg="burlywood1", font=("Helvetica", 16))
    l4.place(x=0, y=170)
    l5 = Label(window, text="Question-->How to determine the best destination for a holiday for me?", fg="black",
               bg="coral1", font=("Helvetica", 18))
    l5.place(x=0, y=210)
    l6 = Label(window,
               text="Answer-->Firstly set a budget and preferably stick to it. Then keep in mind the age group thats going and align it with the activities and terrain you'd prefer and there you have it, a perfect destination for a holiday.",
               fg="blue", bg="burlywood1", font=("Helvetica", 16))
    l6.place(x=0, y=250)
    l7 = Label(window, text="Question-->What travel documents do I NEED to carry at all times?", fg="black",
               bg="coral1", font=("Helvetica", 18))
    l7.place(x=0, y=290)
    l8 = Label(window,
               text="Answer-->Passport,visa,ID,air tickets,proof of accommodation bookings,travel insurance plan details, covid-19 travel documents,",
               fg="blue", bg="burlywood1", font=("Helvetica", 16))
    l8.place(x=0, y=330)
    l9 = Label(window, text="Question-->Can I travel with less than 6 months on my passport?", fg="black", bg="coral1",
               font=("Helvetica", 18))
    l9.place(x=0, y=370)
    l10 = Label(window,
                text="Answer-->Rules state that your passport should be valid for at least 30 days from the date of exit, but it's recommended that you have at least six months on your passport before it expires.",
                fg="blue", bg="burlywood1", font=("Helvetica", 16))

    l10.place(x=0, y=410)

    # retur=Button(window, text="Go back to home",command=main,font=("Helvetica", 18)).place(x=0, y=450)
    mainloop()


# faq()

def tips():
    w = Tk()
    w.title("Travel like a pro!")
    w.geometry("1000x1000")
    # frame = ScrollableFrame(w)
    w.configure(bg='goldenrod1')
    # sb = Scrollbar(
    # w,
    # orient=VERTICAL
    # )
    # sb.grid(row=0, column=1, sticky=W)
    # text1_box.config(yscrollcommand=sb.set)
    # sb.config(command=text1_box.yview)
    l1 = Label(w, text="Travel like a pro!", fg="black", font=("Helvetica", 28), bg="green yellow")  # align,color
    l1.grid(row=0, column=0, sticky=W, pady=2, padx=8)
    l2 = Label(w,
               text="It’s been a while since many of us have travelled abroad,so we know there is huge pent-up demand for\n holidays, with lots of people eager to book a well-deserved break. ",
               fg="black", font=("Helvetica", 16), bg="honeydew1")  # align,color
    l2.grid(row=1, column=0, sticky=W, pady=2, padx=4)
    l3 = Label(w,
               text="If you’re dreaming of your next chance to get away but are unsure what steps you need to take,the\nfollowing advice takes you through everything you need to know to book with confidence this year,\nso that you have a holiday to look forward to.",
               fg="black", font=("Helvetica", 16), bg="honeydew1")
    l3.grid(row=2, column=0, sticky=W, pady=2, padx=4)
    l4 = Label(w, text="1. Use the expertise of an Travel agency to help you plan your trip ", fg="black",
               font=("Helvetica", 16), bg="lavender blush")  # align,color
    l4.grid(row=3, column=0, sticky=W, pady=2, padx=4)
    l5 = Label(w,
               text="Travel agencies are experts at finding the best holiday to suit their customers’ preferences, and at\n a competitive price. They’ll look after you every step of the way, including doing all the research,\n giving you the latest advice for your destination and keeping you up-to-date on any restrictions or\nmeasures that you need to be aware of.",
               fg="black", font=("Helvetica", 16), bg="light blue")  # align,color
    l5.grid(row=4, column=0, sticky=W, pady=2, padx=4)
    l6 = Label(w, text="2. Book a package holiday", fg="black", font=("Helvetica", 16),
               bg="lavender blush")  # align,color
    l6.grid(row=5, column=0, sticky=W, pady=2, padx=4)
    l7 = Label(w,
               text="Booking a package holiday provides the best form of protection for your travel plans,as your holiday will\nbe protected under the Package Travel Regulations.This means you have a right to a replacement holiday\nor a full refund if your holiday is significantly altered by a change in the situation at your destination.",
               fg="black", font=("Helvetica", 16), bg="light blue")  # align,color
    l7.grid(row=6, column=0, sticky=W, pady=2, padx=4)
    l8 = Label(w, text="3. Check the Foreign Office advice for your destination and sign up to the alerts", fg="black",
               font=("Helvetica", 16), bg="lavender blush")  # align,color
    l8.grid(row=7, column=0, sticky=W, pady=2, padx=4)
    l9 = Label(w,
               text="You can keep up to date with Foreign office travel advice for the country you’re visiting, which includes\nlocal rules relating to coronavirus and the latest entry requirements.We recommend signing up to receive\ncountry specific email alerts so that any important updates go straight into your inbox. ",
               fg="black", font=("Helvetica", 16), bg="light blue")  # align,color

    l9.grid(row=8, column=0, sticky=W, pady=2, padx=4)
    l12 = Label(w, text="4. Book early for the most choice and best prices", fg="black", font=("Helvetica", 16),
                bg="lavender blush")  # align,color
    l12.grid(row=11, column=0, sticky=W, pady=2, padx=4)
    l13 = Label(w,
                text="There is massive pent-up demand for holidays, so by booking ahead of others you’ll be able to take\nadvantage of the best deals such as free child places or room upgrades and secure the\naccommodation and resort of your choice.",
                fg="black", font=("Helvetica", 16), bg="light blue")  # align,color

    l13.grid(row=12, column=0, sticky=W, pady=2, padx=4)
    # ret=Button(w, text="Go back to home",command=main)
    # ret.grid(row = 0, column = 1, sticky = W, pady = 2,padx =0)

    w.mainloop()


# tips()


# from tkinter import *
def rand():
    rw = Tk()
    rw.geometry('1000x1000')
    rw.config(bg='orchid2')
    rw.title("Destination chooser")

    def discount():
        d = random.randrange(5, 26, 5)
        return d

    def num():
        r = random.randint(0, 52)
        return r

    def clear():
        l2.pack_forget()
        l3.pack_forget()
        l4.pack_forget()
        l5.pack_forget()

    def pick():
        global l2, l3, l4, l5
        cursor.execute("select * from masterdest")
        list = cursor.fetchall()
        # print(len(list))
        x = num()
        gen = list[x]
        # print(gen)
        disc = discount()
        t = "CONGRATULATIONS! YOU WIN " + str(disc) + "% OFF ON A PLANE TICKET TO: " + str(gen[0])
        # t1="Marvellous adventures await you at: "+str(gen[0])
        t2 = "Voucher is worth between Rs. " + str(gen[1] // 100) + " and " + str(gen[2] // 100)
        t3 = str(gen[0]) + " is known for its " + str(gen[3])
        t4 = "Enjoy!"
        L = Label(rw, text=t, fg="black", bg="pale green", font=("Helvetica", 15))
        L.place(x=130, y=200)
        # l2=Label(rw,text=t1,fg="black",bg="pale green",font=("Helvetica", 15))
        # l2.place(x=20,y=200)
        l3 = Label(rw, text=t2, fg="black", bg="pale green", font=("Helvetica", 15))
        l3.place(x=230, y=240)
        l4 = Label(rw, text=t3, fg="black", bg="pale green", font=("Helvetica", 15))
        l4.place(x=260, y=280)
        l5 = Label(rw, text=t4, fg="black", bg="pale green", font=("Helvetica", 15))
        l5.place(x=450, y=320)

        # clear()

    la = Label(rw,
               text="We at TravelIkinator INC. are glad to announce a collaboration with our friends at FF Airlines.",
               fg="black", bg="pale green", font=("Helvetica", 15))
    la.place(x=40, y=5)

    lb = Label(rw,
               text="Try your luck and win upto 75% discount* on a plane ticket to one of 50 fun filled locations worldwide!",
               fg="black", bg="pale green", font=("Helvetica", 15))
    lb.place(x=30, y=35)
    L1 = Label(rw, text="T&C apply", fg="black", bg="pale green", font=("Helvetica", 10))
    L1.place(x=450, y=390)
    L2 = Label(rw, text="Offer only valid on flights with FF Airlines between 1st September 2022 and 3rd February 2023",
               fg="black", bg="pale green", font=("Helvetica", 10))
    L2.place(x=200, y=370)
    wheel = Button(rw, text="Try your luck!!", command=pick, bg="pale green", font=("Helvetica", 25))
    # cl=Button(rw,text="Clear",command=clear)
    # cl.place(x=20,y=360)

    wheel.place(x=350, y=100)
    # retbutton = Button(rw, text='Go back home',bg="pale green",font=("Helvetica", 16), command=main)
    # retbutton.place(x=20,y=360)

    rw.mainloop()


# rand()


# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox

def main():
    root = Tk()
    # root=Tk()
    root.title('Travel akinator')
    root.minsize(width=1530, height=1800)
    root.maxsize(width=1500, height=1800)
    root.configure(bg="grey94")
    l1 = Label(root, text='Travel akinator', font=("Helvetica", 20, "bold"), fg='black', bg="light cyan")
    l1.place(x=650, y=10)
    l2 = Label(root, text='Welcome to travel akinator', fg='black', bg="light cyan", font=("Helvetica", 16, "bold"))
    l2.place(x=600, y=50)
    l3 = Label(root, text='The one solution to all your travel needs', fg='black', bg="light cyan",
               font=("Helvetica", 16))
    l3.place(x=550, y=80)
    b1 = Button(root, text='Currency converter', fg='black', bg='CornflowerBlue', command=curr, font=("Helvetica", 14))
    b1.place(x=650, y=150)
    b2 = Button(root, text='Language translator', fg='black', bg='CornflowerBlue', command=trans,
                font=("Helvetica", 14))
    b2.place(x=650, y=220)
    b4 = Button(root, text='Tips to travel like a pro!', fg='black', bg='CornflowerBlue', command=tips,
                font=("Helvetica", 14))
    b4.place(x=640, y=290)
    b6 = Button(root, text='Win exciting prizes!', fg='black', bg='CornflowerBlue', command=rand,
                font=("Helvetica", 14))
    b6.place(x=650, y=360)
    b5 = Button(root, text='Write Feedback', fg='black', bg='CornflowerBlue', command=feedback, font=("Helvetica", 14))
    b5.place(x=670, y=430)
    b5 = Button(root, text='View Feedback', fg='black', bg='CornflowerBlue', command=read, font=("Helvetica", 14))
    b5.place(x=670, y=500)
    b3 = Button(root, text='FAQs', fg='black', bg='CornflowerBlue', command=faq, font=("Helvetica", 14))
    b3.place(x=700, y=570)

    logo = PhotoImage(file="C:/Users/NPS-SL-PC1/Desktop/Planepic.png")
    image_label = Label(root, image=logo)
    image_label.place(x=20, y=390)
    logo1 = PhotoImage(file="C:/Users/NPS-SL-PC1/Desktop/sunpic.png")
    image_label1 = Label(root, image=logo1)
    image_label1.place(x=1100, y=30)
    logo2 = PhotoImage(file="C:/Users/NPS-SL-PC1/Desktop/worldpic.png")
    image_label2 = Label(root, image=logo2)
    image_label2.place(x=20, y=5)
    logo3 = PhotoImage(file="C:/Users/NPS-SL-PC1/Desktop/curr.png")
    image_label3 = Label(root, image=logo3)
    image_label3.place(x=1100, y=390)
    logo4 = PhotoImage(file="C:/Users/NPS-SL-PC1/Desktop/traveller.png")
    image_label4 = Label(root, image=logo4)
    image_label4.place(x=900, y=300)
    logo5 = PhotoImage(file="C:/Users/NPS-SL-PC1/Desktop/paris.png")
    image_label5 = Label(root, image=logo5)
    image_label5.place(x=900, y=600)
    logo6 = PhotoImage(file="C:/Users/NPS-SL-PC1/Desktop/vacations.png")
    image_label6 = Label(root, image=logo6)
    image_label6.place(x=500, y=600)
    logo7 = PhotoImage(file="C:/Users/NPS-SL-PC1/Desktop/mountain.png")
    image_label7 = Label(root, image=logo7)
    image_label7.place(x=420, y=270)
    root.mainloop()


main()
