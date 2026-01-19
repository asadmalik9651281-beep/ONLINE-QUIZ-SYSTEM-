# ================= ONLINE QUIZ SYSTEM (3 WINDOWS) =================

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ---------------- MCQs Questions (5) ----------------
mcq_questions = [
    {"q": "Capital of France?", "opt": ["Paris", "London", "Berlin", "Rome"], "ans": "Paris"},
    {"q": "Red Planet?", "opt": ["Earth", "Mars", "Jupiter", "Venus"], "ans": "Mars"},
    {"q": "Python is?", "opt": ["Snake", "Language", "OS", "Car"], "ans": "Language"},
    {"q": "2 + 2 = ?", "opt": ["2", "3", "4", "5"], "ans": "4"},
    {"q": "Tkinter used for?", "opt": ["GUI", "AI", "DB", "Web"], "ans": "GUI"},
]

# ---------------- Written Questions ----------------
written_questions = [
    "What is Python?",
    "What is GUI?",
    "Define OOP."
]

# ================= MCQs QUIZ WINDOW =================
def open_mcq_quiz():
    win = tk.Toplevel()
    win.title("MCQs Quiz")
    win.state("zoomed")
    win.config(bg="black")

    score = 0
    index = 0
    selected = tk.StringVar()

    q_lbl = tk.Label(win, font=("Arial", 20), bg="black", fg="white", wraplength=800)
    q_lbl.pack(pady=40)

    rbs = []
    for _ in range(4):
        rb = tk.Radiobutton(win, font=("Arial", 16),
                            variable=selected, bg="black", fg="white",
                            selectcolor="gray")
        rb.pack(anchor="w", padx=200, pady=5)
        rbs.append(rb)

    def next_q():
        nonlocal score, index
        if selected.get() == mcq_questions[index]["ans"]:
            score += 1
        index += 1
        if index < len(mcq_questions):
            load_q()
        else:
            messagebox.showinfo("Result", f"MCQs Score: {score} / 5")
            win.destroy()

    def load_q():
        selected.set(None)
        q_lbl.config(text=mcq_questions[index]["q"])
        for i in range(4):
            rbs[i].config(text=mcq_questions[index]["opt"][i],
                          value=mcq_questions[index]["opt"][i])

    tk.Button(win, text="Next",
              font=("Arial", 16),
              bg="blue", fg="white",
              command=next_q).pack(pady=30)

    load_q()

# ================= WRITTEN QUIZ WINDOW =================
def open_written_quiz():
    win = tk.Toplevel()
    win.title("Written Quiz")
    win.state("zoomed")
    win.config(bg="black")

    answers = []

    for q in written_questions:
        tk.Label(win, text=q,
                 font=("Arial", 16),
                 bg="black", fg="white").pack(pady=10)
        txt = tk.Text(win, height=3, width=80)
        txt.pack()
        answers.append(txt)

    def submit():
        marks = 0
        for a in answers:
            if a.get("1.0", "end").strip() != "":
                marks += 5
        messagebox.showinfo("Result", f"Written Marks: {marks} / 15")
        win.destroy()

    tk.Button(win, text="Submit",
              font=("Arial", 16),
              bg="green", fg="white",
              command=submit).pack(pady=30)

# ================= QUIZ SELECTION WINDOW =================
def open_quiz_dashboard():
    qdash = tk.Toplevel()
    qdash.title("Quiz Dashboard")
    qdash.state("zoomed")

    bg = Image.open("C:/PROJECT/ONLINE QUIZ SYSTEM FOLDER/Quiz select image.jpeg")
    bg = bg.resize((qdash.winfo_screenwidth(), qdash.winfo_screenheight()))
    bg_img = ImageTk.PhotoImage(bg)

    tk.Label(qdash, image=bg_img).place(x=0, y=0, relwidth=1, relheight=1)
    qdash.bg_img = bg_img

    # MCQs Side
    tk.Label(qdash, text="MCQs QUIZ",
             font=("Arial", 22, "bold"),
             bg="black", fg="white").place(relx=0.25, rely=0.3, anchor="center")

    tk.Button(qdash, text="Attempt MCQs",
              font=("Arial", 16),
              bg="green", fg="white",
              width=18,
              command=open_mcq_quiz).place(relx=0.25, rely=0.4, anchor="center")

    # Written Side
    tk.Label(qdash, text="WRITTEN QUIZ",
             font=("Arial", 22, "bold"),
             bg="black", fg="white").place(relx=0.75, rely=0.3, anchor="center")

    tk.Button(qdash, text="Attempt Written",
              font=("Arial", 16),
              bg="green", fg="white",
              width=18,
              command=open_written_quiz).place(relx=0.75, rely=0.4, anchor="center")

# ================= MAIN DASHBOARD =================
def open_dashboard(name, sid):
    if name == "" or sid == "":
        messagebox.showerror("Error", "Name aur ID zaroori hai")
        return

    login.destroy()

    dash = tk.Tk()
    dash.title("Main Dashboard")
    dash.state("zoomed")

    bg = Image.open("C:/PROJECT/ONLINE QUIZ SYSTEM FOLDER/online quiz system.png")
    bg = bg.resize((dash.winfo_screenwidth(), dash.winfo_screenheight()))
    bg_img = ImageTk.PhotoImage(bg)

    tk.Label(dash, image=bg_img).place(x=0, y=0, relwidth=1, relheight=1)
    dash.bg_img = bg_img

    tk.Label(dash, text="WELCOME",
             font=("Arial", 30, "bold"),
             bg="black", fg="white").place(relx=0.5, rely=0.3, anchor="center")

    tk.Label(dash, text=name,
             font=("Arial", 20),
             bg="black", fg="white").place(relx=0.5, rely=0.37, anchor="center")

    tk.Label(dash, text=f"ID: {sid}",
             font=("Arial", 18),
             bg="black", fg="white").place(relx=0.5, rely=0.43, anchor="center")

    tk.Button(dash, text="Start Quiz",
              font=("Arial", 16),
              bg="black", fg="white",
              width=18,
              command=open_quiz_dashboard).place(relx=0.5, rely=0.52, anchor="center")

    dash.mainloop()

# ================= LOGIN WINDOW =================
login = tk.Tk()
login.title("Login")
login.state("zoomed")

bg = Image.open("C:/PROJECT/ONLINE QUIZ SYSTEM FOLDER/login image.jpeg")
bg = bg.resize((login.winfo_screenwidth(), login.winfo_screenheight()))
bg_img = ImageTk.PhotoImage(bg)

tk.Label(login, image=bg_img).place(x=0, y=0, relwidth=1, relheight=1)
login.bg_img = bg_img

frame = tk.Frame(login, bg="black")
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="Online Quiz System",
         font=("Arial", 24, "bold"),
         bg="black", fg="white").pack(pady=20)

# ---------- Student Name Placeholder ----------
name_entry = tk.Entry(frame, font=("Arial", 14), width=25, fg="grey")
name_entry.insert(0, "Student Name")
name_entry.pack(pady=10)

def name_in(e):
    if name_entry.get() == "Student Name":
        name_entry.delete(0, tk.END)
        name_entry.config(fg="black")

def name_out(e):
    if name_entry.get() == "":
        name_entry.insert(0, "Student Name")
        name_entry.config(fg="grey")

name_entry.bind("<FocusIn>", name_in)
name_entry.bind("<FocusOut>", name_out)

# ---------- Student ID Placeholder ----------
id_entry = tk.Entry(frame, font=("Arial", 14), width=25, fg="grey")
id_entry.insert(0, "Student ID")
id_entry.pack(pady=10)

def id_in(e):
    if id_entry.get() == "Student ID":
        id_entry.delete(0, tk.END)
        id_entry.config(fg="black")

def id_out(e):
    if id_entry.get() == "":
        id_entry.insert(0, "Student ID")
        id_entry.config(fg="grey")

id_entry.bind("<FocusIn>", id_in)
id_entry.bind("<FocusOut>", id_out)

tk.Button(frame, text="Login",
          font=("Arial", 16),
          bg="blue", fg="white",
          command=lambda: open_dashboard(name_entry.get(), id_entry.get())
          ).pack(pady=20)

login.mainloop()

