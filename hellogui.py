import wx
 
app = wx.App() 
window = wx.Frame(None, title = "Frame - Janela", size = (300,200)) 
panel = wx.Panel(window) 
label = wx.StaticText(panel, label = "Olá Interface Gráfica", pos = (200,100)) 
window.Show(True) 
app.MainLoop()