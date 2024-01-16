import statistics # The standard python class
import customtkinter # Import the theme class

def std():
    try:
        data = entry.get() # Get data from entry widget
        entries = data.split(',') # Split the data from its commas ['1','2','3']
        data_list = [int(x) for x in entries] # convert the data into int
        stdev_function = statistics.pstdev if population_var.get() else statistics.stdev # determine standard deviation function 
        std = stdev_function(data_list)

        ans.configure(text=f"Standard deviation: {std}")

    except ValueError: ans.config(text="Invalid input")

app = customtkinter.CTk()
app.geometry("400x230")
app.title("Standard Deviation Calculator")

label = customtkinter.CTkLabel(app, text="Insert sample data")
label.pack(padx=5, pady=5)

population_var = customtkinter.BooleanVar()
toggle = customtkinter.CTkCheckBox(app, text="Population data", variable=population_var)
toggle.pack()

entry = customtkinter.CTkEntry(app, placeholder_text="eg. 1,2,3,4,5")
entry.pack(padx=5, pady=20)

calc_btn = customtkinter.CTkButton(app, text="Calculate", command=std)
calc_btn.pack(pady=10)

ans = customtkinter.CTkLabel(app, text="")
ans.pack()

footer = customtkinter.CTkLabel(app, text="Orbit Media - Copyright© 2024")
footer.pack()

app.mainloop()