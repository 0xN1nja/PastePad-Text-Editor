"""
File : pastepad.py
Author : Abhimanyu Sharma
GitHub : https://github.com/0xN1nja
"""
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
import os
import webbrowser
import datetime

main_application = tk.Tk()
main_application.geometry("1200x800")
main_application.title("PastePad Text Editor")
main_application.wm_iconbitmap("icon.ico")
main_menu = tk.Menu()
new_icon = tk.PhotoImage(file="icons2/new.png")
new_window_icon = tk.PhotoImage(file="icons2/new_window.png")
open_icon = tk.PhotoImage(file="icons2/open.png")
save_icon = tk.PhotoImage(file="icons2/save.png")
save_as_icon = tk.PhotoImage(file="icons2/save_as.png")
exit_icon = tk.PhotoImage(file="icons2/exit.png")
file = tk.Menu(main_menu, tearoff=False)
edit = tk.Menu(main_menu, tearoff=False)
copy_icon = tk.PhotoImage(file="icons2/copy.png")
cut_icon = tk.PhotoImage(file="icons2/cut.png")
paste_icon = tk.PhotoImage(file="icons2/paste.png")
select_all_icon = tk.PhotoImage(file="icons2/select_all.png")
clear_all_icon = tk.PhotoImage(file="icons2/clear_all.png")
undo_icon = tk.PhotoImage(file="icons2/undo.png")
redo_icon = tk.PhotoImage(file="icons2/redo.png")
find_icon = tk.PhotoImage(file="icons2/find.png")
view = tk.Menu(main_menu, tearoff=False)
tool_bar_icon = tk.PhotoImage(file="icons2/status_bar.png")
status_bar_icon = tk.PhotoImage(file="icons2/tool_bar.png")
color_theme = tk.Menu(main_menu, tearoff=False)
light_default_icon = tk.PhotoImage(file="icons2/light_default.png")
light_plus_icon = tk.PhotoImage(file="icons2/light_plus.png")
dark_icon = tk.PhotoImage(file="icons2/dark.png")
red_icon = tk.PhotoImage(file="icons2/red.png")
monokai_icon = tk.PhotoImage(file="icons2/monokai.png")
night_blue_icon = tk.PhotoImage(file="icons2/night_blue.png")
theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)
color_dict = {
    "Light Default": ("#000000", "#ffffff"),
    "Light Plus": ("#474747", "#e0e0e0"),
    "Dark": ("#c4c4c4", "#2d2d2d"),
    "Red": ("#2d2d2d", "#ffe8e8"),
    "Monokai": ("#d3b774", "#474747"),
    "Night Blue": ("#ededed", "#6b9dc2"),
}


def open_source_code(event=None):
    webbrowser.open("https://github.com/0xN1nja/PastePad-Text-Editor")


def get_date_time(event=None):
    dt = datetime.datetime.now().strftime("%H:%M:%S")
    dt2 = datetime.datetime.today()
    dt2 = datetime.datetime(dt2.year, dt2.month, dt2.day)
    text_content = str(dt) + " " + "PM" + " " + str(dt2)
    text_editor.tag_config("left", justify=tk.LEFT)
    text_editor.insert(tk.INSERT, text_content[:22] + " ", "left")


timeImage = tk.PhotoImage(file="icons2/time2.png")
about = tk.Menu(main_menu, tearoff=False)
about.add_command(label="Check Out My GitHub", command=lambda: webbrowser.open("https://github.com/0xN1nja"))
about.add_command(label="Get Source Code", command=open_source_code)
main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Color Theme", menu=color_theme)
main_menu.add_cascade(label="About", menu=about)
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state="readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0, column=0, padx=5)
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable=size_var, state="readonly")
font_size["values"] = tuple(range(8, 81, 2))
font_size.grid(row=0, column=1, padx=5)
font_size.current(2)
bold_icon = tk.PhotoImage(file="icons2/bold.png")
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)
italic_icon = tk.PhotoImage(file="icons2/italic.png")
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)
underline_icon = tk.PhotoImage(file="icons2/underline.png")
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)
font_icon = tk.PhotoImage(file="icons2/font_color.png")
font_color_btn = ttk.Button(tool_bar, image=font_icon)
font_color_btn.grid(row=0, column=5, padx=5)
align_left_icon = tk.PhotoImage(file="icons2/align_left.png")
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)
align_center_icon = tk.PhotoImage(file="icons2/align_center.png")
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)
align_right_icon = tk.PhotoImage(file="icons2/align_right.png")
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)
text_editor = tk.Text(main_application, undo=True)
text_editor.config(wrap="word", relief=tk.FLAT)
scroll_bar = ttk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
context_menu = tk.Menu(tearoff=False)
context_menu.add_command(label="Cut", image=cut_icon, compound=tk.LEFT,
                         command=lambda: text_editor.event_generate("<Control-x>"))
context_menu.add_command(label="Copy", image=copy_icon, compound=tk.LEFT,
                         command=lambda: text_editor.event_generate("<Control-c>"))
context_menu.add_command(label="Paste", image=paste_icon, compound=tk.LEFT,
                         command=lambda: text_editor.event_generate("<Control-v>"))
context_menu.add_separator()
context_menu.add_command(label="Select All", image=select_all_icon, compound=tk.LEFT,
                         command=lambda: text_editor.event_generate("<Control-a>"))
context_menu.add_command(label="Clear All", image=clear_all_icon, compound=tk.LEFT,
                         command=lambda: text_editor.delete(1.0, tk.END))
context_menu.add_separator()
context_menu.add_command(label="Undo", image=undo_icon, compound=tk.LEFT,
                         command=lambda: text_editor.event_generate("<Control-z>"))
context_menu.add_command(label="Redo", image=redo_icon, compound=tk.LEFT,
                         command=lambda: text_editor.event_generate("<Control-y>"))


def popup_menu(event=None):
    context_menu.tk_popup(event.x_root, event.y_root)


text_editor.bind("<Button-3>", popup_menu)
current_font_family = "Arial"
current_font_size = 12


def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)
text_editor.configure(font=("Arial", 12))


def change_bold():
    text_property = tk.font.Font(font=text_editor["font"])
    if text_property.actual()["weight"] == "normal":
        text_editor.configure(font=(current_font_family, current_font_size, "bold"))
    if text_property.actual()["weight"] == "bold":
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))


bold_btn.configure(command=change_bold)


def change_italic():
    text_property = tk.font.Font(font=text_editor["font"])
    if text_property.actual()["slant"] == "roman":
        text_editor.configure(font=(current_font_family, current_font_size, "italic"))
    if text_property.actual()["slant"] == "italic":
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))


italic_btn.configure(command=change_italic)


def change_underline():
    text_property = tk.font.Font(font=text_editor["font"])
    if text_property.actual()["underline"] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, "underline"))
    if text_property.actual()["underline"] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))


underline_btn.configure(command=change_underline)


def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_font_color)


def align_left():
    text_content = text_editor.get(1.0, "end-1c")
    text_editor.tag_config("left", justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "left")


align_left_btn.configure(command=align_left)


def align_center():
    text_content = text_editor.get(1.0, "end-1c")
    text_editor.tag_config("center", justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "center")


align_center_btn.configure(command=align_center)


def align_right():
    text_content = text_editor.get(1.0, "end-1c")
    text_editor.tag_config("right", justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "right")


align_right_btn.configure(command=align_right)
status_bar = ttk.Label(main_application, text="Status Bar")
status_bar.pack(side=tk.BOTTOM)
text_changed = False
is_saved = False


def changed(event=None):
    global text_changed, is_saved
    text_changed = True
    if text_editor.edit_modified() and not url:
        words = len(text_editor.get(1.0, "end-1c").split())
        char = len(text_editor.get(1.0, "end-1c"))
        status_bar.config(text=f"Characters : {char} Words : {words}")
        main_application.title("*Untitled* - PastePad Text Editor")
        is_saved = False
    elif text_editor.edit_modified() and url:
        words = len(text_editor.get(1.0, "end-1c").split())
        char = len(text_editor.get(1.0, "end-1c"))
        status_bar.config(text=f"Characters : {char} Words : {words}")
        main_application.title(f"*{os.path.basename(url)}* - PastePad Text Editor")
        is_saved = False
    text_editor.edit_modified(False)


text_editor.bind("<<Modified>>", changed)
url = ""


def new_file(event=None):
    global url
    url = ""
    text_editor.delete(1.0, tk.END)
    main_application.title("*Untitled* - PastePad Text Editor")


def open_new_window(event=None):
    os.startfile("pastepad.exe")


def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select To Open File",
                                     filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    try:
        with open(url, "r") as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(f"{url} - PastePad Text Editor"))


def save_file(event=None):
    global url, is_saved
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, "w", encoding="utf-8") as fw:
                fw.write(content)
            main_application.title(f"{os.path.basename(url)} - PastePad Text Editor")
            is_saved = True
        else:
            url = filedialog.asksaveasfilename(defaultextension=".txt",
                                               filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
            content2 = text_editor.get(1.0, tk.END)
            with open(url, "w", encoding="utf-8") as fw:
                fw.write(content2)
            main_application.title(f"{os.path.basename(url)} - PastePad Text Editor")
            is_saved = True
    except:
        return


def save_as(event=None):
    global url, is_saved
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        with open(url, "w") as fw:
            fw.write(content)
        main_application.title(f"{os.path.basename(url)} - PastePad Text Editor")
        is_saved = True
    except:
        return


def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed and not is_saved:
            mbox = messagebox.askyesnocancel("Warning", "Do You Want To Save The File ? ")
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, "w", encoding="utf-8") as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode="w", defaultextension=".txt",
                                                   filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return


file.add_command(label="New", image=new_icon, compound=tk.LEFT, accelerator="(Ctrl+N)", command=new_file)
file.add_command(label="New Window", image=new_window_icon, compound=tk.LEFT, accelerator="(Ctrl+Shift+N)",
                 command=open_new_window)
file.add_separator()
file.add_command(label="Open", image=open_icon, compound=tk.LEFT, accelerator="(Ctrl+O)", command=open_file)
file.add_separator()
file.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator="(Ctrl+S)", command=save_file)
file.add_command(label="Save As", image=save_as_icon, compound=tk.LEFT, accelerator="(Ctrl+Shift+S)", command=save_as)
file.add_separator()
file.add_command(label="Exit", image=exit_icon, compound=tk.LEFT, accelerator="(Alt+F4)", command=exit_func)


def find_func(event=None):
    def find():
        word = find_entry.get()
        text_editor.tag_remove("match", "1.0", tk.END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config("match", foreground="red", background="yellow")

    def replace():
        word = find_entry.get()
        replace_text = replace_entry.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_d = tk.Toplevel()
    find_d.geometry("450x250+500+200")
    find_d.title("Find/Replace")
    find_d.resizable(0, 0)
    find_frame = ttk.LabelFrame(find_d, text="Find/Replace")
    find_frame.pack(pady=20)
    text_find_label = ttk.Label(find_frame, text="Find : ")
    text_replace_label = ttk.Label(find_frame, text="Replace : ")
    find_entry = ttk.Entry(find_frame, width=30)
    replace_entry = ttk.Entry(find_frame, width=30)
    find_btn = ttk.Button(find_frame, text="Find", command=find)
    replace_btn = ttk.Button(find_frame, text="Replace", command=replace)
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)
    find_entry.grid(row=0, column=1, padx=4, pady=4)
    replace_entry.grid(row=1, column=1, padx=4, pady=4)
    find_btn.grid(row=2, column=0, padx=8, pady=4)
    replace_btn.grid(row=2, column=1, padx=8, pady=4)
    find_d.mainloop()


edit.add_command(label="Cut", image=cut_icon, compound=tk.LEFT, accelerator="(Ctrl+X)",
                 command=lambda: text_editor.event_generate("<Control-x>"))
edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT, accelerator="(Ctrl+C)",
                 command=lambda: text_editor.event_generate("<Control-c>"))
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="(Ctrl+V)",
                 command=lambda: text_editor.event_generate("<Control-v>"))
edit.add_separator()
edit.add_command(label="Select All", image=select_all_icon, compound=tk.LEFT, accelerator="(Ctrl+A)",
                 command=lambda: text_editor.event_generate("<Control-a>"))
edit.add_command(label="Clear All", image=clear_all_icon, compound=tk.LEFT, accelerator="(Ctrl+Shift+X)",
                 command=lambda: text_editor.delete(1.0, tk.END))
edit.add_separator()
edit.add_command(label="Undo", image=undo_icon, compound=tk.LEFT, accelerator="(Ctrl+Z)",
                 command=lambda: text_editor.event_generate("<Control-z>"))
edit.add_command(label="Redo", image=redo_icon, compound=tk.LEFT, accelerator="(Ctrl+Y)",
                 command=lambda: text_editor.event_generate("<Control-y>"))
edit.add_separator()
edit.add_command(label="Find", image=find_icon, compound=tk.LEFT, accelerator="(Ctrl+F)", command=find_func)
edit.add_command(label="Get Time And Date", image=timeImage, compound=tk.LEFT, accelerator="(F5)",
                 command=get_date_time)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)


def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True


view.add_checkbutton(label="Tool Bar", onvalue=True, offvalue=False, variable=show_toolbar, image=tool_bar_icon,
                     compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label="Status Bar", onvalue=True, offvalue=False, variable=show_statusbar, image=status_bar_icon,
                     compound=tk.LEFT, command=hide_statusbar)


def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, foreground=fg_color)


count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT,
                                command=change_theme)
    count += 1
main_application.protocol("WM_DELETE_WINDOW", exit_func)
main_application.config(menu=main_menu)
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-Shift-KeyPress-N>", open_new_window)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Shift-KeyPress-S>", save_as)
main_application.bind("<Alt-F4>", exit_func)
main_application.bind("<Control-Shift-KeyPress-X>", lambda event=None: text_editor.delete(1.0, tk.END))
main_application.bind("<Control-f>", find_func)
main_application.bind("<F5>", get_date_time)
main_application.mainloop()