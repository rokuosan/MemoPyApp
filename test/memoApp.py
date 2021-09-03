# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class Window
###########################################################################

class Window(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"めも", pos=wx.DefaultPosition, size=wx.Size(800, 600),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(-1, -1), wx.Size(-1, -1))

        self.m_menubar1 = wx.MenuBar(0)
        self.m_File = wx.Menu()
        self.m_File_New = wx.MenuItem(self.m_File, wx.ID_ANY, u"新規作成", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_File_New)

        self.m_File_Save = wx.MenuItem(self.m_File, wx.ID_ANY, u"名前をつけて保存", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_File_Save)

        self.m_File_Overwrite = wx.MenuItem(self.m_File, wx.ID_ANY, u"上書き保存", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_File_Overwrite)

        self.m_File_Open = wx.MenuItem(self.m_File, wx.ID_ANY, u"開く", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_File_Open)

        self.m_menubar1.Append(self.m_File, u"ファイル")

        self.m_Edit = wx.Menu()
        self.m_menubar1.Append(self.m_Edit, u"編集")

        self.m_Format = wx.Menu()
        self.m_menubar1.Append(self.m_Format, u"書式")

        self.m_View = wx.Menu()
        self.m_menubar1.Append(self.m_View, u"表示")

        self.m_Help = wx.Menu()
        self.m_menubar1.Append(self.m_Help, u"ヘルプ")

        self.SetMenuBar(self.m_menubar1)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_text = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.Point(-1, -1), wx.Size(-1, -1),
                                  wx.TE_MULTILINE | wx.TE_WORDWRAP | wx.BORDER_NONE)
        self.m_text.SetMinSize(wx.Size(-1, 600))
        self.m_text.SetMaxSize(wx.Size(-1, 1080))

        bSizer6.Add(self.m_text, 0, wx.EXPAND, 0)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.m_File_NewOnMenuSelection, id=self.m_File_New.GetId())
        self.Bind(wx.EVT_MENU, self.m_File_SaveOnMenuSelection, id=self.m_File_Save.GetId())
        self.Bind(wx.EVT_MENU, self.m_File_OverwriteOnMenuSelection, id=self.m_File_Overwrite.GetId())
        self.Bind(wx.EVT_MENU, self.m_File_OpenOnMenuSelection, id=self.m_File_Open.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def m_File_NewOnMenuSelection(self, event):
        event.Skip()

    def m_File_SaveOnMenuSelection(self, event):
        event.Skip()

    def m_File_OverwriteOnMenuSelection(self, event):
        event.Skip()

    def m_File_OpenOnMenuSelection(self, event):
        event.Skip()
