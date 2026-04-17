import tkinter as tkinter
def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
result_label.config(text="please 
enter a password", fg="orange")
    elif length < 6:
    
result_label.config(text="strength:
   Weak", fg="red")
    elif 6 <= length <= 10:
 result_label.config(text="strength:
  Medium", fg="blue")
    else:

result_label.config(text="strength:
strong", fg="green")

root = tk.Tk()
root.title(password strength 
Checker"")
root.geometry("350x200")

label = tk.Label(root,
text="Enter Password:",
font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, show="*"),
width=30)
entry.pack(pady=5)

check_btn = tk.Button(root,
text="Check Strength",
command=check_strength)
check_btn.pack(pady=10)

result_label = tk.Label(root,
text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()

