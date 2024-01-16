from statistics import stdev, pstdev, mean # The standard python class
import customtkinter # Import the theme class

def std():
    try:
        data = entry.get() # Get data from entry widget
        entries = data.split(',') # Split the data from its commas ['1','2','3']
        data_list = [int(x) for x in entries] # convert the data into int
        stdev_function = pstdev if population_var.get() else stdev # determine standard deviation function 
        std = stdev_function(data_list) # set the selected function in a variable
        mean_ = mean('data_list') # calculate the mean
        cov = std / mean_ * 100 # calculate the coefficient of variation

        std.configure(text=f"Standard deviation: {std}") # display the standard deviation
        cv.configure(text=f"Coefficient of Variation: {cov:.2f}") # display the coefficient of variance
    except ValueError: std.config(text="Invalid input") # in case of wrong input

app = customtkinter.CTk() # declare the window, call it what you like, I went with app
app.geometry("400x300") # declare the size
app.title("Standard Deviation Calculator") # declare the title

label = customtkinter.CTkLabel(app, text="Insert sample data") # declare a label to let the user know wha to do
label.pack(padx=5, pady=5) # apply it to the window

population_var = customtkinter.BooleanVar()
toggle = customtkinter.CTkCheckBox(app, text="Population data", variable=population_var)
toggle.pack()

entry = customtkinter.CTkEntry(app, placeholder_text="eg. 1,2,3,4,5")
entry.pack(padx=5, pady=20)

calc_btn = customtkinter.CTkButton(app, text="Calculate", command=std)
calc_btn.pack(pady=10)

std = customtkinter.CTkLabel(app, text="")
std.pack()

cv = customtkinter.CTkLabel(app, text="")

footer = customtkinter.CTkLabel(app, text="Orbit Media - Copyright© 2024")
footer.pack()

app.mainloop()