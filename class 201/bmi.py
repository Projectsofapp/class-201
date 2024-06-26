from tkinter import *
window=Tk()


window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_bmi():
    weight = int(weight_entry.get())
    height = int(height_entry.get())/100
    bmi = weight/(height*height)
    bmi = round(bmi, 1)
    name = username.get()


    if bmi < 10.5:
        msg="your are UnderWeight"
    elif bmi > 18.5 and bmi <=24.9:
        msg= "your are Overweight"
    elif bmi > 25 and bmi <= 29.9:
        msg="you are Overweight"
    elif bmi > 30:
        msg = "you are Obese"
    else:
        msg="Something Went Wrong"

    output_message=Label(result_frame, text=name+",your BMI is"+str(bmi)+ "and "+msg, bg = "lightcyan", font=("Calibri", 12), width=42)
    output_message.place(x=20,y=40)
    output_message.pack()


app_label=Label(window, text='BMI CALCULATOR', fg= "black", bg ="lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50,y=20)

name_label=Label(window, text="Your Name", fg ="black", bg = "lightcyan", font=("Calibri", 12))

username=Entry(window, text='',bd=2, width=22)
username.place(x=150, y=92)

height_label=Label(window, text="Enter Height(cm)", fg = "black", bg = "lightcyan", font=("Calibri", 12))
height_label.place(x=150, y=140)

height_entry=Entry(window, text='', bd=5, width=15)
height_entry.place(x=150, y=142)

weight_label=Label(window, text="Enter Weight (Kg)", fg="black", bg = "lightcyan", font=("Calibri", 12))
weight_label.place(x=20, y=185)

weight_entry=Entry(window, text="", bd=2, width=15)
weight_entry.place(x=150, y=187)

calculate_button=Button(window,text="CALCULATE",fg="black", bg= "cyan", bd=4, command=calculate_bmi)
calculate_button.place(x=20, y=250)


result_frame = LabelFrame(window, text="Result", bg = "lightcyan", font=("Calibri",12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=13)
result_label.place(x=20,y=20)
result_label.pack()


window.mainloop()