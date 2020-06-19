import wx
import attr
print(wx.version())
print(attr.__version__)

app = wx.App()
frame = wx.Frame(parent=None, title='Hello World')
frame.Show()
app.MainLoop()

