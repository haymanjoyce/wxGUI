#!/usr/bin/env python

import wx
import images


class TreeCtrl(wx.TreeCtrl):
    def __init__(self, parent, id, pos, size, style):
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)


class ImageList(wx.ImageList):
    def __init__(self, height=16, width=16):
        super().__init__(height, width)
        image_size = self.GetSize()
        self.folder = self.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, image_size))
        self.folder_open = self.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, image_size))
        self.file = self.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, image_size))
        self.fil_open = self.Add(wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, image_size))
        self.custom_1 = self.Add(images.Smiles.GetBitmap())
        print(self.GetImageCount())


class TreePanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.tree = TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_HAS_BUTTONS | wx.TR_EDIT_LABELS)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.il = ImageList()
        self.tree.SetImageList(self.il)

        root = self.tree.AddRoot("Level 0 Item")
        self.tree.SetItemData(root, None)
        self.tree.SetItemImage(root, self.il.folder, wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(root, self.il.folder_open, wx.TreeItemIcon_Expanded)

        for l1_row in range(3):
            l1_item = self.tree.AppendItem(parent=root, text=f'Level 1 Item: {l1_row}')
            self.tree.SetItemData(l1_item, None)
            self.tree.SetItemImage(l1_item, self.il.folder, wx.TreeItemIcon_Normal)
            self.tree.SetItemImage(l1_item, self.il.folder_open, wx.TreeItemIcon_Expanded)

            for l2_row in range(3):
                l2_item = self.tree.AppendItem(l1_item, f'Level 2 Item: {l2_row}')
                self.tree.SetItemData(l2_item, None)
                self.tree.SetItemImage(l2_item, self.il.file, wx.TreeItemIcon_Normal)
                self.tree.SetItemImage(l2_item, self.il.fil_open, wx.TreeItemIcon_Selected)

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

