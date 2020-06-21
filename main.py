#!/usr/bin/env python

import wx


class Frame(wx.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # self.parent = None
        # self.id = wx.ID_AUTO_LOWEST
        self.title = 'cG'
        self.pos = wx.DefaultPosition
        self.size = wx.DefaultSize
        self.style = wx.DEFAULT_FRAME_STYLE

        panel = wx.Panel(self, -1)

        button = wx.Button(panel, 1003, "Close me")
        button.SetPosition((20, 20))
        self.Bind(wx.EVT_BUTTON, self.on_close_frame, button)
        self.Bind(wx.EVT_CLOSE, self.on_close_window)
        tree = TreeControl(panel)

    def on_close_frame(self, event):
        self.Close(True)

    def on_close_window(self, event):
        self.Destroy()


class TreeControl(wx.TreeCtrl):
    def __init__(self, parent):
        super().__init__(parent)
        self.init()

    def init(self):
        pass


if __name__ == '__main__':
    app = wx.App()
    frame = Frame()
    frame.Show()
    app.MainLoop()

