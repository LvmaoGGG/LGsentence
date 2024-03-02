import tkinter as tk
import main

x = 0
y = 0
# fonts = 'Aa千里江山行书体'
# fonts = '于是所以我爱你'
fonts = '小雅古籍'
# fonts = 'Aa而墨行书'
# fonts = '段宁软笔行书'
# fonts = '乐府长歌行'
# fonts = '云峰飞云体'
fg = 29

window = tk.Tk()


def on_drag_start(event):
    global x, y
    x = event.x
    y = event.y


def on_drag(event):
    deltax = event.x - x
    deltay = event.y - y
    new_x = window.winfo_x() + deltax
    new_y = window.winfo_y() + deltay
    window.geometry(f"+{new_x}+{new_y}")


def on_drag_stop(event):
    global x, y
    x = 0
    y = 0


window.config(bg='#add123')
window.wm_attributes('-transparentcolor', '#add123')
window.bind("<ButtonPress-1>", on_drag_start)
window.bind("<B1-Motion>", on_drag)
window.bind("<ButtonRelease-1>", on_drag_stop)
window.geometry("1920x200")
window.geometry("+0+900")
window.overrideredirect(True)
label = tk.Label(window, text=main.ruslut, font=(fonts, fg), fg="white", bg="#add123")
label.pack()

# 进入消息循环
window.mainloop()
