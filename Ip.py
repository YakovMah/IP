import tkinter as tk
import socket as s


#Get my IP
my_hostname = s.gethostname()
#Display my hostname
print("Youer Hostname is: " + my_hostname)

#Get my ip
my_ip = s.gethostbyname(my_hostname)
print("Your My IP Address is: " + my_ip)


s = s.socket(s.AF_INET, s.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
local_ip = s.getsockname()[0]
s.close()

"""
 # Set the Ip 
host = "Facebook.com"
# Fetch the IP
ip = s.gethostbyname(host)
"""
def button1_clicked():
    result_label_1.config(text=my_ip)

def button2_clicked():
    result_label_2.config(text=my_hostname)

def button3_clicked():
    result_label_3.config(text=local_ip)

# Create the main window
window = tk.Tk()
window.title("IP Checker")
#Create the window size
window.geometry("420x420")
#Create The Icons In Window
icon_path = "icons\ip.ico"
window.iconbitmap(icon_path)

#Create the label widget
label =tk.Label(window,text="IP Cheker",font="20" "bold_font")
#Pack the label into the window
label.pack()

# Create buttons
button1 = tk.Button(window, padx=10, pady=10,font="10", text="Extranl IP", command=button1_clicked)
button2 = tk.Button(window, padx=10, pady=10,font="8",text="Host Name", command=button2_clicked)
button3 = tk.Button(window, padx=10, pady=10,font="8",text="Intranl IP", command=button3_clicked)

# Create a label to display the result
result_label_1 = tk.Label(window, text="" ,font="14")
result_label_2 = tk.Label(window, text="" ,font="14")
result_label_3 = tk.Label(window,text="", font="14")

# Pack the widgets
button1.pack(padx=10, pady=10)
result_label_1.pack(padx=10, pady=10)
button2.pack(padx=10, pady=10)
result_label_2.pack(pady=10)
button3.pack(padx=10, pady=10)
result_label_3.pack(padx=10, pady=10)

# Who Is Written The App 
# Create a label with your desired text
label = tk.Label(window, text="Written By Yakov_M.",font=3, padx=3, pady=3)
label.pack(side="left", anchor="s")

#What The Version Is This App

# Create a label with your desired text
label = tk.Label(window, text="V1.0",font=3, padx=3, pady=3)
label.pack(side="right", anchor="s")

# Start the GUI event loop
window.mainloop()




