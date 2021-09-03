import wx
import TestApp
from MyProject1MyFrame1 import MyProject1MyFrame1


class MyProject1MyFrame1Child(MyProject1MyFrame1):
    def __init__(self, parent):
        MyProject1MyFrame1.__init__(self, parent)

    def m_button1OnButtonClick(self, event):
        self.m_staticText1.SetLabel("Hello wxPython!!")
