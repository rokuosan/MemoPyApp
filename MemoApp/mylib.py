import os
import sys
import wx


# これはウィンドウを表示する関数
def create_window(name, width, height):
    app = wx.App()
    frame = wx.Frame(None, -1, f"{name}", size=(width, height))
    frame.Show()
    app.MainLoop()