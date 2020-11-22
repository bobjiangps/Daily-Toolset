# # https://www.yiibai.com/wxpython/wx_textctrl_class.html
# # http://codingdict.com/article/9460
# import wx
#
# app = wx.App()
# window = wx.Frame(None, title="Select two files to show diff", pos=(300, 300), size=(400, 200))
# panel = wx.Panel(window)
# label = wx.StaticText(panel, label="Hello World", pos=(100, 100))
# text_field_one = wx.TextCtrl(panel, pos=(20, 20), size=(270, 40))
# text_field_two = wx.TextCtrl(panel, pos=(20, 80), size=(270, 40))
# select_button_one = wx.Button(panel, pos=(300, 20), size=(80, 40), label="Select File")
# select_button_two = wx.Button(panel, pos=(300, 80), size=(80, 40), label="Select File")
# show_button = wx.Button(panel, pos=(40, 120), size=(100, 60), label="Show Diff")
# clear_button = wx.Button(panel, pos=(160, 120), size=(100, 60), label="Clear")
# window.Show(True)
# app.MainLoop()


import wx
import os


class APP(wx.Frame):

    def __init__(self):
        super().__init__(None, title="Select two files to show diff", pos=(300, 300), size=(400, 200))
        panel = wx.Panel(self)
        self.text_field_one = wx.TextCtrl(panel, pos=(20, 20), size=(270, 40))
        self.text_field_two = wx.TextCtrl(panel, pos=(20, 80), size=(270, 40))
        self.select_button_one = wx.Button(panel, pos=(300, 20), size=(80, 40), label="Select File")
        self.select_button_two = wx.Button(panel, pos=(300, 80), size=(80, 40), label="Select File")
        self.show_button = wx.Button(panel, pos=(40, 120), size=(100, 60), label="Show Diff")
        self.clear_button = wx.Button(panel, pos=(160, 120), size=(100, 60), label="Clear")
        self.select_button_one.Bind(wx.EVT_BUTTON, self.select_file_standard)
        self.select_button_two.Bind(wx.EVT_BUTTON, self.select_file_compare)
        self.clear_button.Bind(wx.EVT_BUTTON, self.clear_text_fields)
        self.file_compare_path = None
        self.file_standard_path = None
        self.Show()

    def select_file_standard(self, e):
        files_filter = "All files (*.*)|*.*"
        file_dialog = wx.FileDialog(self, message="选择单个文件", defaultDir=os.getcwd(), wildcard=files_filter, style=wx.FD_OPEN)
        file_dialog.ShowModal()
        file_path = file_dialog.GetPath()
        self.text_field_one.SetValue(file_path)
        self.file_standard_path = file_path
        e.Skip()

    def select_file_compare(self, e):
        files_filter = "All files (*.*)|*.*"
        file_dialog = wx.FileDialog(self, message="选择单个文件", defaultDir=os.getcwd(), wildcard=files_filter, style=wx.FD_OPEN)
        file_dialog.ShowModal()
        file_path = file_dialog.GetPath()
        self.text_field_two.SetValue(file_path)
        self.file_compare_path = file_path
        e.Skip()

    def clear_text_fields(self, e):
        self.text_field_one.SetValue("")
        self.text_field_two.SetValue("")
        e.Skip()


if __name__ == "__main__":
    app = wx.App()
    APP()
    app.MainLoop()
