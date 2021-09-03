# import myTools as myTools
#
# name = input("名前を入力してください: ")
#
# while True:
#     print("[確認] 名前: " + name)
#     if myTools.confirm():
#         break
#     else:
#         name = input("再入力をお願いします: ")
#
# print("処理終了")

import tkinter as tk
from tkinter import messagebox as mbox

# 作成 ウィンドウ
window = tk.Tk()
window.geometry("800x400")

# 作成 ラベル
label = tk.Label(window, text="What's your name?")
label.pack()

# 作成 テキストボックス
text = tk.Entry(window)
text.pack()
text.insert(tk.END, '名前を入力してください')


# イベント ボタン押下
def click_ok():
    s = text.get()
    mbox.showinfo('挨拶', s + 'さん、こんにちは')


# 作成 ボタン
btn_ok = tk.Button(window, text='OK', command=click_ok())
btn_ok.pack()

# 動作 ウィンドウ
window.mainloop()
