import wx
import os


class APP(wx.Frame):

    def __init__(self):
        super().__init__(None, title="Convert Data Format", pos=(200, 200), size=(1000, 600))
        self.Center()
        self.split_window = wx.SplitterWindow(self)
        self.left_panel = wx.Panel(self.split_window)
        self.right_panel = wx.Panel(self.split_window)
        self.left_panel.SetBackgroundColour(colour="#F5F5F5")
        self.right_panel.SetBackgroundColour(colour="#F5F5F5")
        self.split_window.SplitVertically(self.left_panel, self.right_panel, 490)
        self.split_window.SetMinimumPaneSize(50)

        self.left_box = wx.BoxSizer(wx.VERTICAL)
        convert_type_message = wx.StaticText(self.left_panel, label="Select type to convert", style=wx.ALIGN_CENTRE)
        self.left_box.Add(convert_type_message, flag=wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, border=10)
        convert_type_list = ["Format Json", "Json to Yaml"]
        self.radio_box = wx.RadioBox(self.left_panel, choices=convert_type_list, majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.left_box.Add(self.radio_box, flag=wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, border=1)
        self.convert_button = wx.Button(self.left_panel, pos=(300, 20), size=(80, 40), label="Convert")
        self.left_box.Add(self.convert_button, flag=wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, border=1)
        self.convert_data_text = wx.TextCtrl(self.left_panel, style=wx.TE_MULTILINE, size=(300, 500))
        self.left_box.Add(self.convert_data_text, flag=wx.ALL | wx.EXPAND, border=10)
        self.left_panel.SetSizerAndFit(self.left_box)

        self.right_box = wx.BoxSizer(wx.VERTICAL)
        self.convert_result = wx.TextCtrl(self.right_panel, style=wx.TE_MULTILINE, size=(300, 600))
        self.right_box.Add(self.convert_result, flag=wx.ALL | wx.EXPAND, border=10)
        self.right_panel.SetSizerAndFit(self.right_box)

        self.Show()


if __name__ == "__main__":
    app = wx.App()
    APP()
    app.MainLoop()
