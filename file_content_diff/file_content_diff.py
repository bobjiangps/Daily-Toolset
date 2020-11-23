import wx
import os
import wx.html2
import difflib


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
        self.show_button.Bind(wx.EVT_BUTTON, self.show_diff)
        self.clear_button.Bind(wx.EVT_BUTTON, self.clear_text_fields)
        self.file_compare_path = None
        self.file_standard_path = None
        self.result_file = "result.html"
        self.Show()

    def select_file_standard(self, e):
        files_filter = "All files (*.*)|*.*"
        file_dialog = wx.FileDialog(self, message="select single file", defaultDir=os.getcwd(), wildcard=files_filter, style=wx.FD_OPEN)
        file_dialog.ShowModal()
        file_path = file_dialog.GetPath()
        self.text_field_one.SetValue(file_path)
        self.file_standard_path = file_path
        e.Skip()

    def select_file_compare(self, e):
        files_filter = "All files (*.*)|*.*"
        file_dialog = wx.FileDialog(self, message="select single file", defaultDir=os.getcwd(), wildcard=files_filter, style=wx.FD_OPEN)
        file_dialog.ShowModal()
        file_path = file_dialog.GetPath()
        self.text_field_two.SetValue(file_path)
        self.file_compare_path = file_path
        e.Skip()

    def show_diff(self, e):
        file_standard = self.text_field_one.GetValue()
        file_compare = self.text_field_two.GetValue()
        if file_standard != "" and file_compare != "":
            self.diff_file(file_standard, file_compare)
            browser_dialog = wx.Dialog(self, title="check result")
            sizer = wx.BoxSizer(wx.VERTICAL)
            browser = wx.html2.WebView.New(browser_dialog)
            sizer.Add(browser, 1, wx.EXPAND, 10)
            browser_dialog.SetSizer(sizer)
            browser_dialog.SetSize((1200, 600))
            browser.LoadURL(os.path.join(os.getcwd(), self.result_file))
            browser_dialog.ShowModal()
        else:
            wx.MessageBox(message="Please select file!", caption="Error", style=wx.OK | wx.ICON_ERROR)
            # https://discuss.wxpython.org/t/mac-standard-dialog-icons-for-error-question-and-information-are-missing/28447/3
        e.Skip()

    def clear_text_fields(self, e):
        self.text_field_one.SetValue("")
        self.text_field_two.SetValue("")
        e.Skip()

    @staticmethod
    def load_file(file_path):
        with open(file_path) as f:
            return f.readlines()

    def diff_file(self, file_standard, file_compare):
        content_standard = self.load_file(file_standard)
        content_compare = self.load_file(file_compare)
        diff = difflib.HtmlDiff()
        result = diff.make_file(content_standard, content_compare, file_standard.split(os.sep)[-1], file_compare.split(os.sep)[-1], context=True)
        with open(os.path.join(os.getcwd(), self.result_file), 'w') as rf:
            rf.write(result)


if __name__ == "__main__":
    app = wx.App()
    APP()
    app.MainLoop()
