import wx
import memoApp
import main
import locale
import os
import sys
from memoAppWindow import memoAppWindow


class memoAppWindowChild(memoAppWindow):
    def __init__(self, parent):
        memoAppWindow.__init__(self, parent)

    def m_File_OverwriteOnMenuSelection(self, event):
        # save_file = open(f"{editingFile}.txt", "w")
        save_file = open("write.txt", "w")
        save_file.write(self.m_text.GetValue())
        save_file.close()

    # def m_File_OpenOnMenuSelection(self, event):
    #     app = wx.App()
    #     frame = wx.Frame(None, -1, "開くファイルを選んでください", size=(400,200))
    #     frame.Show()
    #     app.MainLoop()

    def m_File_OpenOnMenuSelection( self, event ):
        # if os.path.exists()
        with open("write.txt", encoding="shift_jis") as f:
            open_file = f.read()
            self.m_text.SetValue(open_file)
