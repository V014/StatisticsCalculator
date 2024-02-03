import statistics as st # The standard python class
import matplotlib
import matplotlib.pyplot as pp
matplotlib.use('TkAgg')  # Set the backend explicitly
from PIL import ImageTk
import customtkinter # Import the theme class

def std():
    try:
        data = entry.get() # Get data from entry widget
        entries = data.split(',') # Split the data from its commas ['1','2','3']
        data_list = [int(x) for x in entries] # convert the data into int
        stdev_function = st.pstdev if population_var.get() else st.stdev # determine standard deviation function 
        result = stdev_function(data_list) # set the selected function in a variable

        mean = st.mean(data_list) # calculate the mean
        cov = result / mean * 100 # calculate the coefficient of variation
        p_var = st.pvariance(data_list)
        sdx = tuple(data_list - mean for data_list in data_list)
        s_var = tuple(data_list*data_list for data_list in sdx)

        label_std.configure(text=f"Standard deviation: {result}") # display the standard deviation
        cv.configure(text=f"Coefficient of Variation: {cov}") # display the coefficient of variance
        label_mean.configure(text=f"Mean: {mean}") # display the mean
        variances.configure(text=f"Variances: {str(sdx)}" )
        squared_variances.configure(text=f"Squared Variances " + str(s_var))
        pvariance.configure(text=f"Population Variances: {str(p_var)}" )
        
        pp.bar(tuple(str(val) for val in data_list), sdx)
        pp.show()  # Display the plot
        # print("Standard deviations: " + str(sdx))
        # print(data_list)
    except ValueError as e: 
        label_error.configure(text=str(e)) # in case of wrong input or error

app = customtkinter.CTk() # declare the window, call it what you like, I went with app
app.geometry("350x450") # declare the size
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

label_mean = customtkinter.CTkLabel(app, text="")
label_mean.pack()

label_std = customtkinter.CTkLabel(app, text="")
label_std.pack()

cv = customtkinter.CTkLabel(app, text="")
cv.pack()

variances = customtkinter.CTkLabel(app, text="")
variances.pack()

squared_variances = customtkinter.CTkLabel(app, text="")
squared_variances.pack()

pvariance = customtkinter.CTkLabel(app, text="")
pvariance.pack()

label_error = customtkinter.CTkLabel(app, text="", text_color='red')
label_error.pack()

footer = customtkinter.CTkLabel(app, text="Orbit Media - Copyright© 2024")
footer.pack()

app.mainloop()