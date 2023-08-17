from tkinter import *

window = Tk()
window.minsize(width=170, height=150)
window.title("BMI Calculator")

label1 = Label(text="Enter Your Weight (kg)")
label1.pack()

entry1 = Entry(width=10)
entry1.pack()

label2 = Label(text="Enter Your Height (cm)")
label2.pack()

entry2 = Entry(width=10)
entry2.pack()

def calculate():
    if entry1.get() == "" or entry2.get() == "":
        label3.config(text="Enter both weight and height")
    else:
        try:
            weight = int(entry1.get())
            height = int(entry2.get())
            result = weight / pow(height, 2) * 10000

            if result < 18.5:
                label3.config(text=f"Your BMI is {round(result, 2)}. You are Under Weight")
            elif 18.5 <= result <= 24.9:
                label3.config(text=f"Your BMI is {round(result, 2)}. You are Normal")
            elif 25 <= result <= 29.9:
                label3.config(text=f"Your BMI is {round(result, 2)}. You are Over Weight")
            elif 30 <= result <= 34.9:
                label3.config(text=f"Your BMI is {round(result, 2)}. You are Obesity (Class 1)")
            elif 35 <= result <= 39.9:
                label3.config(text=f"Your BMI is {round(result, 2)}. You are Obesity (Class 2)")
            else:
                label3.config(text=f"Your BMI is {round(result, 2)}. You are Extreme Obesity")

        except:
            label3.config(text="Enter a valid number!")

button = Button(text="Calculate", command=calculate)
button.pack()

label3 = Label(text="")
label3.pack()

window.mainloop()
