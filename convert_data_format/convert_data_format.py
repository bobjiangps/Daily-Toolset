# -*- coding: UTF-8 -*-
import wx
import os
import json
import yaml


class APP(wx.Frame):

    def __init__(self):
        super().__init__(None, title="Convert Data Format", pos=(200, 200), size=(1000, 600))
        self.Center()
        self.setup_menu_bar()
        self.split_window = wx.SplitterWindow(self)
        self.left_panel = wx.Panel(self.split_window)
        self.right_panel = wx.Panel(self.split_window)
        self.left_panel.SetBackgroundColour(colour="#F5F5F5")
        self.right_panel.SetBackgroundColour(colour="#F5F5F5")
        self.split_window.SplitVertically(self.left_panel, self.right_panel, 490)
        self.split_window.SetMinimumPaneSize(50)
        self.left_box = None
        self.right_box = None
        self.radio_box = None
        self.convert_data_text = None
        self.convert_button = None
        self.convert_result = None
        self.setup_left_panel()
        self.setup_right_panel()
        self.Show()

    def setup_menu_bar(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        about_menu = wx.Menu()
        menu_open = file_menu.Append(wx.ID_OPEN, "Open", "Open File")
        file_menu.AppendSeparator()
        menu_exit = file_menu.Append(wx.ID_EXIT, "Exit", "Exit Application")
        menu_bar.Append(file_menu, "File")
        menu_about = about_menu.Append(wx.ID_ABOUT, 'Info', 'Information')
        menu_bar.Append(about_menu, "About")
        self.Bind(wx.EVT_MENU, self.exit_app, menu_exit)
        self.Bind(wx.EVT_MENU, self.show_info, menu_about)
        self.Bind(wx.EVT_MENU, self.open_file, menu_open)
        self.SetMenuBar(menu_bar)
        # https://github.com/wxWidgets/Phoenix/issues/476

    def setup_left_panel(self):
        self.left_box = wx.BoxSizer(wx.VERTICAL)
        convert_type_message = wx.StaticText(self.left_panel, label="Select type to convert", style=wx.ALIGN_CENTRE)
        self.left_box.Add(convert_type_message, flag=wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, border=10)
        convert_type_list = ["Format Json", "Json to Yaml"]
        self.radio_box = wx.RadioBox(self.left_panel, choices=convert_type_list, majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.left_box.Add(self.radio_box, flag=wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, border=1)
        self.convert_button = wx.Button(self.left_panel, pos=(300, 20), size=(80, 40), label="Convert")
        self.convert_button.Bind(wx.EVT_BUTTON, self.convert_data)
        self.left_box.Add(self.convert_button, flag=wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, border=1)
        self.convert_data_text = wx.TextCtrl(self.left_panel, style=wx.TE_MULTILINE, size=(300, 500))
        self.left_box.Add(self.convert_data_text, flag=wx.ALL | wx.EXPAND, border=10)
        self.left_panel.SetSizerAndFit(self.left_box)

    def setup_right_panel(self):
        self.right_box = wx.BoxSizer(wx.VERTICAL)
        self.convert_result = wx.TextCtrl(self.right_panel, style=wx.TE_READONLY | wx.TE_MULTILINE, size=(300, 600))
        self.right_box.Add(self.convert_result, flag=wx.ALL | wx.EXPAND, border=10)
        self.right_panel.SetSizerAndFit(self.right_box)

    def convert_data(self, e):
        to_convert_text = self.convert_data_text.GetValue()
        convert_type = self.radio_box.GetStringSelection()
        if to_convert_text != "" and convert_type != "":
            try:
                if convert_type == "Format Json":
                    result = json.dumps(json.loads(to_convert_text), indent=4, sort_keys=False, ensure_ascii=False)
                elif convert_type == "Json to Yaml":
                    result = yaml.safe_dump(json.loads(to_convert_text), default_flow_style=False, indent=2)
                self.convert_result.SetValue(result)
            except Exception as err:
                if str(err).find("Expecting property name enclosed in double quotes") >= 0:
                    try:
                        if convert_type == "Format Json":
                            result = json.dumps(json.loads(to_convert_text.replace("“", "\"").replace("”", "\"")), indent=4, sort_keys=False, ensure_ascii=False)
                        elif convert_type == "Json to Yaml":
                            result = yaml.safe_dump(json.loads(to_convert_text.replace("“", "\"").replace("”", "\"")), default_flow_style=False, indent=2)
                        self.convert_result.SetValue(result)
                    except Exception as err:
                        self.convert_result.SetValue("cannot convert data, please check the error message below:\n" + str(err))
                else:
                    self.convert_result.SetValue("cannot convert data, please check the error message below:\n" + str(err))
        else:
            wx.MessageBox(message="No data or type to convert!", caption="Error", style=wx.OK | wx.ICON_ERROR)
        e.Skip()

    def exit_app(self, e):
        self.Close()

    def open_file(self, e):
        files_filter = "All files (*.*)|*.*"
        file_dialog = wx.FileDialog(self, message="select single file", defaultDir=os.getcwd(), wildcard=files_filter, style=wx.FD_OPEN)
        file_dialog.ShowModal()
        file_path = file_dialog.GetPath()
        self.convert_data_text.SetEditable(False)
        with open(file_path, "r") as f:
            file_content = f.read()
            self.convert_data_text.SetValue("")
            self.convert_data_text.SetValue(file_content)
            self.convert_result.SetValue("")
        self.convert_data_text.SetEditable(True)
        e.Skip()

    def show_info(self, e):
        message_info = 'Author:bj\nDate:2020/12/04\nVersion:0.1'
        message = wx.MessageDialog(self, message_info, "INFO", wx.OK)
        message.ShowModal()
        message.Destroy()


if __name__ == "__main__":
    app = wx.App()
    APP()
    app.MainLoop()
