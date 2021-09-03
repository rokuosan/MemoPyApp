import os
import sys
import wx
import memoAppWindowChild


if __name__ == "__main__":
    app = wx.App(False)
    frame = memoAppWindowChild.memoAppWindowChild(None)
    frame.Show(True)
    app.MainLoop()

