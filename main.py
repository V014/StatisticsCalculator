import statistics # The standard python class
import customtkinter

def std():
    try:
        data = entry.get()
        entries = data.split(',')
        data_list = [int(x) for x in entries]
        stdev_function = statistics.pstdev if population_var.get() else statistics.stdev
        sample_std = statistics.stdev(data_list)
        ans.configure(text=f"Sample standard deviation: {sample_std}")
        
    except ValueError: ans.config(text="Invalid input")

app = customtkinter.CTk()
app.geometry("400x250")
app.title("Standard Deviation Calculator")

label = customtkinter.CTkLabel(app, text="Insert sample data")
label.pack(padx=5, pady=5)

entry = customtkinter.CTkEntry(app, placeholder_text="eg. 1,2,3,4,5")
entry.pack(padx=5, pady=20)

population_var = customtkinter.BooleanVar()
toggle = customtkinter.CTkCheckBox(app, text="Population data", variable=population_var)
toggle.pack()

calc_btn = customtkinter.CTkButton(app, text="Calculate", command=std)
calc_btn.pack(padx=20, pady=20)

ans = customtkinter.CTkLabel(app, text="")
ans.pack(padx=10, pady=10)

app.mainloop()