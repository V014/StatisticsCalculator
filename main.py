from msilib.schema import TextStyle
from statistics import median, stdev, pstdev, mean # The standard python class
import customtkinter # Import the theme class

def std():
    try:
        data = entry.get() # Get data from entry widget
        entries = data.split(',') # Split the data from its commas ['1','2','3']
        data_list = [int(x) for x in entries] # convert the data into int
        stdev_function = pstdev if population_var.get() else stdev # determine standard deviation function 
        result = stdev_function(data_list) # set the selected function in a variable
        mean_ = mean(data_list) # calculate the mean
        median_ = median
        # print(mean_)
        cov = result / mean_ * 100 # calculate the coefficient of variation

        std.configure(text=f"Standard deviation: {result}") # display the standard deviation
        cv.configure(text=f"Coefficient of Variation: {cov}") # display the coefficient of variance
        mn.configure(text=f"Mean: {mean_}") # display the mean
    except ValueError: std.config(text="Invalid input") # in case of wrong input

app = customtkinter.CTk() # declare the window, call it what you like, I went with app
app.geometry("350x350") # declare the size
app.title("Statistics Calculator") # declare the title

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(frame, text="Insert data", font=("Arial",24)) # declare a label to let the user know wha to do
label.pack(padx=5, pady=5) # apply it to the window

entry = customtkinter.CTkEntry(frame, placeholder_text="eg. 2,4,6,8")
entry.pack(padx=5, pady=20)

calc_btn = customtkinter.CTkButton(frame, text="Calculate", command=std)
calc_btn.pack(pady=10)

population_var = customtkinter.BooleanVar()
toggle = customtkinter.CTkCheckBox(frame, text="Population data", variable=population_var)
toggle.pack()

mn = customtkinter.CTkLabel(app, text="")
mn.pack()

std = customtkinter.CTkLabel(app, text="")
std.pack()

cv = customtkinter.CTkLabel(app, text="")
cv.pack()

footer = customtkinter.CTkLabel(app, text="Orbit Media - Copyright© 2024")
footer.pack()

app.mainloop()