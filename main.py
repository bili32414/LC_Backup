import os
import shutil
import webbrowser
from tkinter import Tk, Label, Button, Checkbutton, IntVar, messagebox, Entry

root = Tk()
root.title("LC备份器")
root.resizable(False, False)

check = 0
check2 = 0

lock_backup_status = 0
user_name = os.getlogin()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = (screen_width - root.winfo_reqwidth()) / 2.4
y_coordinate = (screen_height - root.winfo_reqheight()) / 2.8

root.geometry("+%d+%d" % (x_coordinate, y_coordinate))


def backup_save():
    global check
    check = 0
    selected_saves = [var1.get(), var2.get(), var3.get()]
    backup_folder = "backup"
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    for i, save in enumerate(selected_saves, start=1):
        if save == 1:
            save_file_path = f"C:\\Users\\{user_name}\\AppData\\LocalLow\\ZeekerssRBLX\\Lethal Company\\LCSaveFile{i}"
            if os.path.exists(save_file_path) and os.path.getsize(save_file_path) == 0:
                messagebox.showinfo("提示", f"LCSaveFile{i} 无存档")
            else:
                try:
                    shutil.copy(save_file_path, os.path.join(backup_folder, f"LCSaveFile{i}"))
                except Exception as e:
                    messagebox.showerror("错误", f"备份LCSaveFile{i}时出错：{e}")
                    check = 1
    if check == 0:
        messagebox.showinfo("提示", "存档备份完成")


def restore_save():
    global check2
    check2 = 0
    backup_folder = "backup"
    for i, save in enumerate([var4.get(), var5.get(), var6.get()], start=1):
        if save == 1:
            save_file_path = os.path.join(backup_folder, f"LCSaveFile{i}")
            original_save_path = f"C:\\Users\\{user_name}\\AppData\\LocalLow\\ZeekerssRBLX\\Lethal Company\\LCSaveFile{i}"
            try:
                shutil.copy(save_file_path, original_save_path)
            except Exception as e:
                check2 = 1
                messagebox.showerror("错误", f"还原LCSaveFile{i}时出错：{e}")
    if check2 == 0:
        messagebox.showinfo("提示", "存档还原完成")


def toggle_backup_lock():
    global lock_backup_status
    if lock_backup_status == 0:
        lock_backup_status = 1
        lock_button.config(text="✔ 已锁定该备份")
        backup_button.config(state="disabled")
        checkbutton1.config(state="disabled")
        checkbutton2.config(state="disabled")
        checkbutton3.config(state="disabled")
    else:
        lock_backup_status = 0
        lock_button.config(text="锁定该版本备份")
        backup_button.config(state="normal")
        checkbutton1.config(state="normal")
        checkbutton2.config(state="normal")
        checkbutton3.config(state="normal")


lock_backup_status = IntVar()
lock_button = Button(root, text="锁定该版本备份", command=toggle_backup_lock)
lock_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


def get_username():
    global user_name
    global temp
    temp = user_name
    # user_name = user_entry.get()
    if user_name == "" or user_name == " ":
        messagebox.showerror("错误", "用户名不能为空或者空格！")

    elif user_name == "关于":
        show_about_info()
        user_name = temp
    else:
        messagebox.showinfo("提示", f"用户名已设置为 {user_name}")
        user_name = user_entry.get()
        user_entry_label.config(text=f"当前用户为 {user_name}")

def show_about_info():
    result = messagebox.askquestion("关于", "2024 @南锣子酱 \n版权所有\nVer: Beta 0.2\n点击是进入作者网站")
    if result == 'no':
        pass  # 确定按钮被点击
    else:
        webbrowser.open("https://bili32414.github.io/")

def autoget_username():
    global user_name
    fetched_username = os.getlogin()
    if fetched_username:
        user_name = fetched_username
        user_entry.delete(0, 'end')
        messagebox.showinfo("提示", f"用户名已设置为 {user_name}")
        user_entry_label.config(text=f"当前用户为 {user_name}")
    else:
        messagebox.showerror("错误", "无法自动获取用户名")


def lock_username():
    global lock_backup_status
    if lock_backup_status == 0:
        lock_backup_status = 1
        user_entry_button.config(state="disabled")
        user_entry_button_auto.config(state="disabled")
    else:
        lock_backup_status = 0
        user_entry_button.config(state="normal")
        user_entry_button_auto.config(state="normal")


Label(root, text="备份存档").grid(row=0, column=0, padx=10, pady=10)
var1 = IntVar()
checkbutton1 = Checkbutton(root, text="LCSaveFile1", variable=var1)
checkbutton1.grid(row=1, column=0, padx=10, pady=5)
var2 = IntVar()
checkbutton2 = Checkbutton(root, text="LCSaveFile2", variable=var2)
checkbutton2.grid(row=2, column=0, padx=10, pady=5)
var3 = IntVar()
checkbutton3 = Checkbutton(root, text="LCSaveFile3", variable=var3)
checkbutton3.grid(row=3, column=0, padx=10, pady=5)
backup_button = Button(root, text="备份", command=backup_save)
backup_button.grid(row=4, column=0, padx=10, pady=10)

Label(root, text="还原存档").grid(row=0, column=1, padx=10, pady=10)
var4 = IntVar()
Checkbutton(root, text="LCSaveFile1", variable=var4).grid(row=1, column=1, padx=10, pady=5)
var5 = IntVar()
Checkbutton(root, text="LCSaveFile2", variable=var5).grid(row=2, column=1, padx=10, pady=5)
var6 = IntVar()
Checkbutton(root, text="LCSaveFile3", variable=var6).grid(row=3, column=1, padx=10, pady=5)
Button(root, text="还原", command=restore_save).grid(row=4, column=1, padx=10, pady=10)

user_entry_label = Label(root, text=f"当前用户为 {user_name}")
user_entry_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

user_entry = Entry(root)
user_entry.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
user_entry_button = Button(root, text="锁定用户名", command=lock_username)
user_entry_button.grid(row=8, column=1, padx=10, pady=10)
user_entry_button = Button(root, text="确定", command=get_username)
user_entry_button.grid(row=8, column=0, padx=10, pady=10)
user_entry_button_auto = Button(root, text="自动获取", command=autoget_username)
user_entry_button_auto.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
