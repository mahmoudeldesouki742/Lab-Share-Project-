
import tkinter as tk

# نعمل النافذة
window = tk.Tk()
window.title("LabShare - Login v2.4.1")
window.geometry("330x380")
window.configure(bg="white")
window.resizable(False, False)            # نمنع تغيير الحجم


# ---------- الدوال (الحاجات اللي بتحصل لما نضغط زرار) ----------

# تخفي رسالة التحذير
def hide_warning():
    warning.place_forget()      # place_forget = اخفي العنصر
    close_button.place_forget()


# تظهر أو تخفي كلمة السر
def show_hide_password():
    if password_box.cget("show") == "":   # لو ظاهرة
        password_box.config(show="*")     # نخفيها بنجوم
    else:
        password_box.config(show="")      # نظهرها


# زرار تسجيل الدخول
def sign_in():
    print("اسم المستخدم:", username_box.get())   # get() تجيب اللي مكتوب
    print("كلمة السر:", password_box.get())


# ---------- الجزء العلوي ----------

# مربع اللوجو (x = من الشمال ، y = من فوق)
tk.Label(window, text="LAB", bg="black", fg="white",
         font=("Arial", 10, "bold")).place(x=15, y=15, width=45, height=45)

# اسم البرنامج
tk.Label(window, text="LabShare", bg="white",
         font=("Arial", 13, "bold")).place(x=70, y=13)

# الوصف الصغير
tk.Label(window, text="Laboratory Management System", bg="white",
         fg="gray", font=("Arial", 8)).place(x=70, y=40)


# ---------- التبويبات ----------

tk.Button(window, text="Researcher", bg="white",
          relief="flat").place(x=15, y=75, width=145, height=28)

tk.Button(window, text="Administrator", bg="lightgray",
          relief="flat").place(x=160, y=75, width=145, height=28)


# ---------- رسالة التحذير ----------

warning = tk.Label(window, text="Role permission warning: Elevation requires 2FA token",
                   bg="pink", fg="red", font=("Arial", 8))
warning.place(x=15, y=112, width=290, height=25)

# زرار X يخفي الرسالة
close_button = tk.Button(window, text="X", bg="pink", fg="red",
                         relief="flat", command=hide_warning)
close_button.place(x=285, y=112, width=20, height=25)


# ---------- اسم المستخدم ----------

tk.Label(window, text="Workstation Username", bg="white",
         font=("Arial", 8, "bold")).place(x=15, y=150)

tk.Label(window, text="SYS_UID", bg="white", fg="gray",
         font=("Arial", 7)).place(x=255, y=152)

# خانة الكتابة
username_box = tk.Entry(window, bg="whitesmoke", relief="flat")
username_box.insert(0, "marwan-alsadany")      # نص مكتوب جاهز
username_box.place(x=15, y=172, width=290, height=28)


# ---------- كلمة السر ----------

tk.Label(window, text="Access Key / Password", bg="white",
         font=("Arial", 8, "bold")).place(x=15, y=210)

tk.Label(window, text="Forgot Key?", bg="white", fg="gray",
         font=("Arial", 7)).place(x=245, y=212)

# show="*" يخلي الحروف تظهر نجوم
password_box = tk.Entry(window, bg="whitesmoke", relief="flat", show="*")
password_box.insert(0, "123456")
password_box.place(x=15, y=232, width=290, height=28)

# زرار العين
tk.Button(window, text="eye", bg="whitesmoke", relief="flat",
          command=show_hide_password).place(x=265, y=233, width=38, height=26)


# ---------- تذكر الجلسة ----------

tk.Checkbutton(window, text="Remember terminal session", bg="white",
               fg="gray", font=("Arial", 8)).place(x=12, y=270)

tk.Label(window, text="NODE_04", bg="lightgray", fg="gray",
         font=("Arial", 7)).place(x=255, y=273)


# ---------- زرار الدخول ----------

tk.Button(window, text="Sign In to Workstation", bg="#4a6572", fg="white",
          font=("Arial", 9, "bold"), relief="flat",
          command=sign_in).place(x=15, y=305, width=290, height=32)


# ---------- الروابط اللي تحت ----------

tk.Label(window, text="Request Laboratory Account", bg="white",
         fg="gray", font=("Arial", 7)).place(x=15, y=345)

tk.Label(window, text="Diagnostics", bg="white", fg="gray",
         font=("Arial", 7)).place(x=250, y=345)


# ---------- تشغيل النافذة (آخر سطر دايما) ----------

window.mainloop()