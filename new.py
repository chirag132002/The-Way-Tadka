from tkinter import *

root = Tk()
root.geometry("1200x800")
root.title("Restaurant Billing System -B3_44_Chirag Dave")
root.resizable(False, False)

# Background Image
bg_image = PhotoImage(file=r"./bg.png")
bg_label = Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Title
Label(text="THE WAY TADKA", fg="orange", font=("IMPACT", 50, "bold"), bg="black", width ="800").pack()


# Menu
Label(text="MENU", font=("impact", 30), fg="khaki1", bg="black").place(x=60, y=90)
Label(text="WHAT WOULD YOU LIKE TO HAVE?", font=("impact", 25), fg="khaki1", bg="black").place(x=410, y=130)
Label(font=("impact", 18), text="Paneer Butter Masala....Rs.180/plate", fg="black").place(x=10, y=150)
Label(font=("impact", 18), text="Chole Bhature....Rs.100/serving", fg="black").place(x=10, y=200)
Label(font=("impact", 18), text="Biryani.....Rs.150/plate", fg="black").place(x=10, y=250)
Label(font=("impact", 18), text="Samosa......Rs.30/piece", fg="black").place(x=10, y=300)
Label(font=("impact", 18), text="Jalebi..... Rs.20/piece", fg="black").place(x=10, y=350)
Label(font=("impact", 18), text="Naan...Rs.10/serving", fg="black").place(x=10, y=400)
Label(font=("impact", 18), text="Gulab Jamun.......Rs.15/each", fg="black").place(x=10, y=450)

# Entry work
f1 = Frame(root)
f1.place(x=420, y=200)
paneer_butter_masala = StringVar()
chole_bhature = StringVar()
biryani = StringVar()
samosa = StringVar()
jalebi = StringVar()
Naan = StringVar()
gulab_jamun = StringVar()
Total_bill = StringVar()

# Bill
f2 = Frame(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=300, height=300)
f2.place(x=870, y=180)
Bill = Label(f2, text="BILL", font=('impact', 30), bg="lightyellow")
Bill.place(x=117, y=10)

# ENTRY
entry_paneer_butter_masala = Entry(f1, font=("aria", 10, 'bold'), textvariable=paneer_butter_masala, bd=6, width=7, bg="wheat1")
entry_chole_bhature = Entry(f1, font=("aria", 10, 'bold'), textvariable=chole_bhature, bd=6, width=7, bg="wheat1")
entry_biryani = Entry(f1, font=("aria", 10, 'bold'), textvariable=biryani, bd=6, width=7, bg="wheat1")
entry_samosa = Entry(f1, font=("aria", 10, 'bold'), textvariable=samosa, bd=6, width=7, bg="wheat1")
entry_jalebi = Entry(f1, font=("aria", 10, 'bold'), textvariable=jalebi, bd=6, width=7, bg="wheat1")
entry_Naan = Entry(f1, font=("aria", 10, 'bold'), textvariable=Naan, bd=6, width=7, bg="wheat1")
entry_gulab_jamun = Entry(f1, font=("aria", 10, 'bold'), textvariable=gulab_jamun, bd=6, width=7, bg="wheat1")
entry_paneer_butter_masala.grid(row=1, column=1)
entry_chole_bhature.grid(row=2, column=1)
entry_biryani.grid(row=3, column=1)
entry_samosa.grid(row=4, column=1)
entry_jalebi.grid(row=5, column=1)
entry_Naan.grid(row=6, column=1)
entry_gulab_jamun.grid(row=7, column=1)


# Label
lbl_paneer_butter_masala = Label(f1, font=("Times", 15, 'bold') ,text="PANEER BUTTER MASALA", width=25, fg="black")
lbl_chole_bhature = Label(f1, font=("times", 15, 'bold'), text="CHOLE BHATURE", width=20, fg="black")
lbl_biryani = Label(f1, font=("times", 15, 'bold'), text="BIRYANI", width=20, fg="black")
lbl_samosa = Label(f1, font=("times", 15, 'bold'), text="SAMOSA", width=20, fg="black")
lbl_jalebi = Label(f1, font=("times", 15, 'bold'), text="JALEBI", width=20, fg="black")
lbl_Naan = Label(f1, font=("times", 15, 'bold'), text="NAAN", width=20, fg="black")
lbl_gulab_jamun = Label(f1, font=("times", 15, 'bold'), text="GULAB JAMUN", width=20, fg="black")

lbl_paneer_butter_masala.grid(row=1, column=0)
lbl_chole_bhature.grid(row=2, column=0)
lbl_biryani.grid(row=3, column=0)
lbl_samosa.grid(row=4, column=0)
lbl_jalebi.grid(row=5, column=0)
lbl_Naan.grid(row=6, column=0)
lbl_gulab_jamun.grid(row=7, column=0)



# Customer Information
Label(text="CUSTOMER INFORMATION", font=("impact",30 ), fg="khaki1", bg="black").place(x=20, y=580)
Label(font=("impact", 20), text="Name:", fg="black").place(x=10, y=650)
Label(font=("impact", 20), text="Phone Number:", fg="black").place(x=10, y=700)
Label(font=("impact", 20), text="Email Address:", fg="black").place(x=10, y=750)

entry_name = Entry(root, font=("aria", 10, 'bold'), bd=6, width=25, bg="wheat1")
entry_name.place(x=200, y=650)
entry_phone = Entry(root, font=("aria", 10, 'bold'), bd=6, width=25, bg="wheat1")
entry_phone.place(x=200, y=710)
entry_email = Entry(root, font=("aria", 10, 'bold'), bd=6, width=25, bg="wheat1")
entry_email.place(x=200, y=760)

# Payment Options
Label(text="PAYMENT OPTIONS", font=("impact", 30), fg="khaki1", bg="black").place(x=500, y=580)

payment_option = StringVar()
payment_option.set("Cash")  # Default payment option

cash_radio = Radiobutton(root, text="CASH", variable=payment_option, value="Cash", font=("Times", 30, 'bold'), bg="orange")
cash_radio.place(x=500, y=675)
credit_card_radio = Radiobutton(root, text="CARD", variable=payment_option, value="Credit Card", font=("Times", 30, 'bold'), bg="orange")
credit_card_radio.place(x=650, y=675)

# Parcel or Dine-In Option
Label(text="CHOOSE OPTION", font=("impact", 30), fg="khaki1", bg="black").place(x=900, y=580)

option_var = StringVar()
option_var.set("Dine-In")  # Default option

takeaway_radio = Radiobutton(root, text="TAKEAWAY", variable=option_var, value="Takeway", font=("times", 20, 'bold'), bg="lightpink")
takeaway_radio.place(x=850, y=683)
dinein_radio = Radiobutton(root, text="DINE-IN", variable=option_var, value="Dine-In", font=("times", 20, 'bold'), bg="lightpink")
dinein_radio.place(x=1045, y=683)

def Reset():
    entry_paneer_butter_masala.delete(0, END)
    entry_chole_bhature.delete(0, END)
    entry_biryani.delete(0, END)
    entry_samosa.delete(0, END)
    entry_jalebi.delete(0, END)
    entry_Naan.delete(0, END)
    entry_gulab_jamun.delete(0, END)



def calculate_total():
    try:
        a1 = int(paneer_butter_masala.get())
    except:
        a1 = 0
    try:
        a2 = int(chole_bhature.get())
    except:
        a2 = 0
    try:
        a3 = int(biryani.get())
    except:
        a3 = 0
    try:
        a4 = int(samosa.get())
    except:
        a4 = 0
    try:
        a5 = int(jalebi.get())
    except:
        a5 = 0
    try:
        a6 = int(Naan.get())
    except:
        a6 = 0
    try:
        a7 = int(gulab_jamun.get())
    except:
        a7 = 0

    # define cost of each item per quantity
    c1 = 180 * a1
    c2 = 100 * a2
    c3 = 70 * a3
    c4 = 30 * a4
    c5 = 20 * a5
    c6 = 10 * a6
    c7 = 15 * a7

    total_cost = c1 + c2 + c3 + c4 + c5 + c6 + c7
    lbl_total = Label(f2, font=('aria', 20, 'bold'), text="Total", width=10, fg="lightyellow", bg="black")
    lbl_total.place(x=60, y=80)
    entry_total = Entry(f2, font=('aria', 20, 'bold'), textvariable=Total_bill, bd=6, width=10, bg="lightgreen")
    entry_total.place(x=70, y=150)

    # Display the total cost on the Total entry field
    string_total = "Rs.", str("%.2f" % total_cost)
    Total_bill.set(string_total)

def PrintBill():
    bill_window = Toplevel(root)
    bill_window.geometry("400x400")
    bill_window.title("Printed Bill")

    bill_text = f"Customer Information:\nName: {entry_name.get()}\nPhone Number: {entry_phone.get()}\nEmail Address: {entry_email.get()}\n\n"
    bill_text += "Order Summary:\n"
    bill_text += f"Paneer Butter Masala: {paneer_butter_masala.get()}\n"
    bill_text += f"Chole Bhature: {chole_bhature.get()}\n"
    bill_text += f"Biryani: {biryani.get()}\n"
    bill_text += f"Samosa: {samosa.get()}\n"
    bill_text += f"Jalebi: {jalebi.get()}\n"
    bill_text += f"Dosa: {Naan.get()}\n"
    bill_text += f"Gulab Jamun: {gulab_jamun.get()}\n\n"
    bill_text += f"Total: {Total_bill.get()}\n"
    bill_text += f"Payment Option: {payment_option.get()}\n"
    bill_text += f"Dine-in or Takeaway: {option_var.get()}"

    bill_label = Label(bill_window, text=bill_text, font=("arial", 12))
    bill_label.pack()

# Buttons
btn_print_bill = Button(root, bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=10, text="Print Bill", command=PrintBill)
btn_print_bill.place(x=950, y=450)

btn_reset = Button(f1, bd="5", fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=5, text="Reset", command=Reset)
btn_reset.grid(row=8, column=0)

btn_total = Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=5, text="Total", command=calculate_total)
btn_total.grid(row=8, column=1)

root.mainloop()
