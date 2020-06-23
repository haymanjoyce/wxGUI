#!/usr/bin/env python

import wx


class TreeCtrl(wx.TreeCtrl):

    def __init__(self, parent, id, pos, size, style):
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)


class TreePanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.tree = TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_HAS_BUTTONS | wx.TR_EDIT_LABELS)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        root = self.tree.AddRoot("Level 0 Item")
        self.tree.SetItemData(root, None)

        for l1_row in range(3):
            l1_item = self.tree.AppendItem(parent=root, text=f'Level 1 Item: {l1_row}')
            self.tree.SetItemData(l1_item, None)

            for l2_row in range(3):
                l2_item = self.tree.AppendItem(l1_item, f'Level 2 Item: {l2_row}')
                self.tree.SetItemData(l2_item, None)

        self.tree.ExpandAll()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        self.SetSizer(sizer)

    def OnSize(self, event):
        w, h = self.GetClientSize()
        self.tree.SetSize(0, 0, w, h)


class Frame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='cG')
        panel = TreePanel(self)
        self.Show()


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = Frame()
    app.MainLoop()

