#!/usr/bin/env python

# todo see if you can get images to work with gizmos
# todo remove check boxes
# todo add item types
# todo export data
# todo import data
# todo item data panel

import wx
import wx.dataview
import wx.lib.gizmos as gizmos
import images


class TreeCtrl(wx.TreeCtrl):
    def __init__(self, parent, id, pos, size, style):
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)

        # Does not have columns


class TreeListCtrlA(wx.dataview.TreeListCtrl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Does have SetImageList()


class TreeListCtrlB(gizmos.TreeListCtrl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Does not have SetImageList()
        # Has more user-friendly API


class ImageList(wx.ImageList):
    def __init__(self, height=16, width=16):
        super().__init__(height, width)
        image_size = self.GetSize()
        self.folder = self.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, image_size))
        self.folder_open = self.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, image_size))
        self.file = self.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, image_size))
        self.file_open = self.Add(wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, image_size))
        self.smiles = self.Add(images.Smiles.GetBitmap())


class TreePanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.tree = TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_HAS_BUTTONS | wx.TR_EDIT_LABELS)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.il = ImageList()
        self.tree.SetImageList(self.il)

        root = self.tree.AddRoot("Level 0 Item")
        self.tree.SetItemData(root, None)
        self.tree.SetItemImage(root, self.il.smiles, wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(root, self.il.smiles, wx.TreeItemIcon_Expanded)

        for l1_row in range(3):
            l1_item = self.tree.AppendItem(parent=root, text=f'Level 1 Item: {l1_row}')
            self.tree.SetItemData(l1_item, None)
            self.tree.SetItemImage(l1_item, self.il.folder, wx.TreeItemIcon_Normal)
            self.tree.SetItemImage(l1_item, self.il.folder_open, wx.TreeItemIcon_Expanded)

            for l2_row in range(3):
                l2_item = self.tree.AppendItem(l1_item, f'Level 2 Item: {l2_row}')
                self.tree.SetItemData(l2_item, None)
                self.tree.SetItemImage(l2_item, self.il.file, wx.TreeItemIcon_Normal)
                self.tree.SetItemImage(l2_item, self.il.file_open, wx.TreeItemIcon_Selected)

        self.tree.ExpandAll()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        self.SetSizer(sizer)

        self.tree.Bind(wx.EVT_LEFT_DCLICK, self.OnLeftDClick)
        self.tree.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.tree.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)

    def OnSize(self, event):
        w, h = self.GetClientSize()
        self.tree.SetSize(0, 0, w, h)

    def OnLeftDClick(self, event):
        pos = event.GetPosition()
        item, flags = self.tree.HitTest(pos)
        if item:
            parent = self.tree.GetItemParent(item)
            if parent.IsOk():
                self.tree.SortChildren(item)
        event.Skip()

    def OnRightDown(self, event):
        pos = event.GetPosition()
        item, flag = self.tree.HitTest(pos)
        if item:
            self.tree.SelectItem(item)

    def OnRightUp(self, event):
        pos = event.GetPosition()
        item, flags = self.tree.HitTest(pos)
        if item:
            self.tree.EditLabel(item)


class TreeListPanelA(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.tree = TreeListCtrlA(parent=self, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TR_DEFAULT_STYLE | wx.TR_FULL_ROW_HIGHLIGHT)

        self.il = ImageList()
        self.tree.SetImageList(self.il)

        self.tree.AppendColumn("Main column")
        self.tree.AppendColumn("Col 1")
        self.tree.AppendColumn("Col 2")
        self.tree.AppendColumn("Col 3")
        # self.tree.SetColumnWidth(0, 200)

        self.root = self.tree.GetRootItem()
        self.child_1_a = self.tree.AppendItem(self.root, "Child 1 a")
        self.child_1_b = self.tree.AppendItem(self.root, "Child 1 b")
        self.child_2_a = self.tree.AppendItem(self.child_1_a, "Child 2 a")

        self.tree.SetItemText(self.child_1_a, 1, "New text")

        self.tree.SetItemImage(self.child_1_a, self.il.folder, self.il.file_open)

        self.tree.Expand(self.root)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        self.SetSizer(sizer)

    def OnSize(self, event):
        w, h = self.GetClientSize()
        self.tree.SetSize(0, 0, w, h)


class TreeListPanelB(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.tree = TreeListCtrlB(parent=self, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=gizmos.TR_DEFAULT_STYLE | gizmos.TR_FULL_ROW_HIGHLIGHT)

        # stuff goes here

    def OnSize(self, event):
        w, h = self.GetClientSize()
        self.tree.SetSize(0, 0, w, h)


class Frame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='cG')
        # panel = TreePanel(self)
        # panel = TreeListPanelA(self)
        panel = TreeListCtrlB(self)
        self.Show()


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = Frame()
    app.MainLoop()

