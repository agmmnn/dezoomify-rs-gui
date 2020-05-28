from threading import Thread
import subprocess
import webbrowser
import time
import os
import sys

import pyperclip

import requests
import urllib.parse
from bs4 import BeautifulSoup

from PIL import Image
from haishoku.haishoku import Haishoku

import wx


PATH = os.path.dirname(sys.argv[0])
PATHEXC = os.path.dirname(sys.executable)


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"dezoomify-rs GUI \U0001F980 v0.1 ",
            pos=wx.DefaultPosition,
            size=wx.Size(810, 510),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT)
        )
        self.SetBackgroundColour(wx.Colour(45, 56, 72))

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        if os.path.exists("icon.ico"):
            icon = wx.Icon()
            icon.CopyFromBitmap(wx.Bitmap("icon.ico", wx.BITMAP_TYPE_ANY))
            self.SetIcon(icon)

        fgSizer21 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer21.AddGrowableCol(1)
        fgSizer21.SetFlexibleDirection(wx.BOTH)
        fgSizer21.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText21 = wx.StaticText(
            self,
            wx.ID_ANY,
            u"dezoomify-rs GUI \U0001F980",
            wx.DefaultPosition,
            wx.Size(-1, 38),
            0,
        )
        self.m_staticText21.Wrap(-1)

        self.m_staticText21.SetFont(
            wx.Font(
                17,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_LIGHT,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_staticText21.SetForegroundColour(wx.Colour(251, 251, 251))

        fgSizer21.Add(self.m_staticText21, 0, wx.ALL, 5)

        bSizer3.Add(fgSizer21, 0, wx.ALIGN_CENTER, 5)

        fgSizer5 = wx.FlexGridSizer(2, 2, 0, 0)
        fgSizer5.AddGrowableCol(0)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer2 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer2.AddGrowableCol(0)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)

        self.m_url = wx.TextCtrl(
            self,
            wx.ID_ANY,
            u"",
            wx.Point(-1, -1),
            wx.Size(-1, 35),
            0 | wx.BORDER_SIMPLE,
        )
        self.m_url.SetFont(
            wx.Font(
                10,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_url.SetForegroundColour(wx.Colour(251, 251, 251))
        self.m_url.SetBackgroundColour(wx.Colour(75, 84, 104))

        fgSizer2.Add(self.m_url, 1, wx.EXPAND, 6)

        fgSizer5.Add(fgSizer2, 1, wx.EXPAND, 5)

        fgSizer4 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer4.AddGrowableCol(1)
        fgSizer4.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)

        self.m_buttonX = wx.Button(
            self,
            wx.ID_ANY,
            u"\U00002716",
            wx.DefaultPosition,
            wx.Size(-1, 36),
            wx.BORDER_NONE | wx.BU_EXACTFIT,
        )
        self.m_buttonX.SetFont(
            wx.Font(
                wx.NORMAL_FONT.GetPointSize(),
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_buttonX.SetForegroundColour(wx.Colour(251, 251, 251))
        self.m_buttonX.SetBackgroundColour(wx.Colour(68, 66, 83))
        self.m_buttonX.SetToolTip(u"Clear URL")

        fgSizer4.Add(self.m_buttonX, 0, wx.EXPAND, 0)

        self.m_buttonV = wx.Button(
            self,
            wx.ID_ANY,
            u"\U00002714",
            wx.DefaultPosition,
            wx.Size(-1, 36),
            wx.BORDER_NONE | wx.BU_EXACTFIT,
        )
        self.m_buttonV.SetFont(
            wx.Font(
                wx.NORMAL_FONT.GetPointSize(),
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_buttonV.SetForegroundColour(wx.Colour(251, 251, 251))
        self.m_buttonV.SetBackgroundColour(wx.Colour(70, 67, 97))
        self.m_buttonV.SetToolTip(u"Paste")

        fgSizer4.Add(self.m_buttonV, 0, wx.EXPAND, 0)

        self.m_buttonV1 = wx.Button(
            self,
            wx.ID_ANY,
            u"Add \U00002795",
            wx.DefaultPosition,
            wx.Size(100, 36),
            wx.BORDER_NONE | wx.BU_EXACTFIT,
        )
        self.m_buttonV1.SetFont(
            wx.Font(
                wx.NORMAL_FONT.GetPointSize(),
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_buttonV1.SetForegroundColour(wx.Colour(251, 251, 251))
        self.m_buttonV1.SetBackgroundColour(wx.Colour(26, 32, 44))
        self.m_buttonV1.SetToolTip(u"Add to List")

        fgSizer4.Add(self.m_buttonV1, 0, wx.EXPAND, 5)

        fgSizer5.Add(fgSizer4, 1, wx.ALIGN_LEFT | wx.ALIGN_RIGHT | wx.EXPAND, 5)

        bSizer3.Add(fgSizer5, 0, wx.EXPAND, 5)

        bSizer31 = wx.BoxSizer(wx.HORIZONTAL)

        m_listBox1Choices = []
        self.m_listBox1 = wx.ListBox(
            self,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            m_listBox1Choices,
            0 | wx.BORDER_NONE | wx.HSCROLL,
        )
        self.m_listBox1.SetFont(
            wx.Font(
                10,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_listBox1.SetForegroundColour(wx.Colour(251, 251, 251))
        self.m_listBox1.SetBackgroundColour(wx.Colour(75, 84, 104))

        bSizer31.Add(self.m_listBox1, 1, wx.ALL | wx.EXPAND, 0)

        bSizer3.Add(bSizer31, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        fgSizer51 = wx.FlexGridSizer(0, 7, 0, 0)
        fgSizer51.SetFlexibleDirection(wx.BOTH)
        fgSizer51.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_buttonX1 = wx.Button(
            self,
            wx.ID_ANY,
            u"Delete",
            wx.DefaultPosition,
            wx.Size(-1, -1),
            wx.BORDER_NONE | wx.BU_EXACTFIT,
        )
        self.m_buttonX1.SetFont(
            wx.Font(
                wx.NORMAL_FONT.GetPointSize(),
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_buttonX1.SetForegroundColour(wx.Colour(251, 251, 251))
        self.m_buttonX1.SetBackgroundColour(wx.Colour(68, 66, 83))
        self.m_buttonX1.SetToolTip(u"Delete Selected Item")

        fgSizer51.Add(self.m_buttonX1, 0, wx.ALL, 0)

        self.m_buttonX11 = wx.Button(
            self,
            wx.ID_ANY,
            u"Clear All",
            wx.DefaultPosition,
            wx.Size(-1, -1),
            wx.BORDER_NONE | wx.BU_EXACTFIT,
        )
        self.m_buttonX11.SetFont(
            wx.Font(
                wx.NORMAL_FONT.GetPointSize(),
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_buttonX11.SetForegroundColour(wx.Colour(251, 251, 251))
        self.m_buttonX11.SetBackgroundColour(wx.Colour(68, 66, 83))
        self.m_buttonX11.SetToolTip(u"Clear All")

        fgSizer51.Add(self.m_buttonX11, 0, wx.LEFT, 1)

        self.m_buttonV2 = wx.Button(
            self,
            wx.ID_ANY,
            u"Open in Browser",
            wx.DefaultPosition,
            wx.Size(-1, -1),
            wx.BORDER_NONE | wx.BU_EXACTFIT,
        )
        self.m_buttonV2.SetFont(
            wx.Font(
                wx.NORMAL_FONT.GetPointSize(),
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_buttonV2.SetForegroundColour(wx.Colour(251, 251, 251))
        self.m_buttonV2.SetBackgroundColour(wx.Colour(70, 67, 97))
        self.m_buttonV2.SetToolTip(u"Open URL in Browser")

        fgSizer51.Add(self.m_buttonV2, 0, wx.LEFT, 1)

        self.m_buttonSave = wx.Button(
            self,
            wx.ID_ANY,
            u"Save",
            wx.DefaultPosition,
            wx.Size(-1, -1),
            wx.BORDER_NONE | wx.BU_EXACTFIT,
        )
        self.m_buttonSave.SetFont(
            wx.Font(
                wx.NORMAL_FONT.GetPointSize(),
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_buttonSave.SetForegroundColour(wx.Colour(251, 251, 251))
        self.m_buttonSave.SetBackgroundColour(wx.Colour(70, 67, 97))
        self.m_buttonSave.SetToolTip(u'Save List as "list.txt" (!overwrite)')

        fgSizer51.Add(self.m_buttonSave, 0, wx.LEFT, 1)

        self.m_buttonLoad = wx.Button(
            self,
            wx.ID_ANY,
            u"Load",
            wx.DefaultPosition,
            wx.Size(-1, -1),
            wx.BORDER_NONE | wx.BU_EXACTFIT,
        )
        self.m_buttonLoad.SetFont(
            wx.Font(
                wx.NORMAL_FONT.GetPointSize(),
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_buttonLoad.SetForegroundColour(wx.Colour(251, 251, 251))
        self.m_buttonLoad.SetBackgroundColour(wx.Colour(70, 67, 97))
        self.m_buttonLoad.SetToolTip(u'Load "list.txt" File (!add below)')

        fgSizer51.Add(self.m_buttonLoad, 0, wx.LEFT, 1)

        fgSizer51.Add((0, 0), 1, wx.LEFT, 5)

        self.m_status = wx.StaticText(
            self, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_status.Wrap(-1)
        self.m_status.SetFont(
            wx.Font(
                wx.NORMAL_FONT.GetPointSize(),
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_status.SetForegroundColour(wx.Colour(240, 117, 117))
        self.m_status.SetLabel("")

        fgSizer51.Add(self.m_status, 0, wx.ALL, 5)

        bSizer4.Add(fgSizer51, 1, wx.EXPAND, 5)

        self.m_checkBox1 = wx.CheckBox(
            self, wx.ID_ANY, u"Add Copied URLs", wx.DefaultPosition, wx.Size(-1, -1), 0
        )
        self.m_checkBox1.SetValue(True)
        self.m_checkBox1.SetFont(
            wx.Font(
                10,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_checkBox1.SetForegroundColour(wx.Colour(251, 251, 251))
        self.m_checkBox1.SetBackgroundColour(wx.Colour(45, 56, 72))
        self.m_checkBox1.SetToolTip(u"Add Copied URLs to the List Automatically")

        bSizer4.Add(self.m_checkBox1, 0, wx.ALL, 5)

        bSizer3.Add(bSizer4, 0, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_download = wx.Button(
            self,
            wx.ID_ANY,
            u"Start Download",
            wx.DefaultPosition,
            wx.Size(-1, 42),
            wx.BORDER_NONE | wx.BU_EXACTFIT | wx.BORDER_SIMPLE,
        )
        self.m_download.SetFont(
            wx.Font(
                11,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_download.SetForegroundColour(wx.Colour(251, 251, 251))
        self.m_download.SetBackgroundColour(wx.Colour(26, 32, 44))

        bSizer7.Add(self.m_download, 1, wx.EXPAND, 5)

        bSizer3.Add(bSizer7, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_staticText21.Bind(wx.EVT_LEFT_DCLICK, self.m_staticText21OnLeftDClick)
        self.m_listBox1.Bind(wx.EVT_LISTBOX_DCLICK, self.m_listBox1DC)
        self.m_buttonX.Bind(wx.EVT_BUTTON, self.m_buttonXOnButtonClick)
        self.m_buttonV.Bind(wx.EVT_BUTTON, self.m_buttonVOnButtonClick)
        self.m_buttonV1.Bind(wx.EVT_BUTTON, self.m_buttonAddOnButtonClick)
        self.m_buttonX1.Bind(wx.EVT_BUTTON, self.m_buttonDeleteOnButtonClick)
        self.m_buttonX11.Bind(wx.EVT_BUTTON, self.m_buttonClearAllOnButtonClick)
        self.m_buttonV2.Bind(wx.EVT_BUTTON, self.m_buttonOpenBrowserOnButtonClick)
        self.m_buttonSave.Bind(wx.EVT_BUTTON, self.m_buttonSaveOnButtonClick)
        self.m_buttonLoad.Bind(wx.EVT_BUTTON, self.m_buttonLoadOnButtonClick)
        # self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.m_checkBoxEvt )
        self.m_download.Bind(wx.EVT_BUTTON, self.m_downloadOnButtonClick)

        # start cb listener
        t = Thread(target=MainFrame.ClipboardListener, daemon=True, args=[self]).start()

    def __del__(self):
        pass

    # clipboard listener
    def ClipboardListener(self):
        cb = ""
        while 1:
            time.sleep(0.7)
            cb_last = pyperclip.paste()
            if cb != cb_last and "http" in cb_last and self.m_checkBox1.IsChecked():
                cb = cb_last
                self.adder(cb_last)
                # print("url: {}".format(cb_last))
                # need status

    def m_staticText21OnLeftDClick(self, event):
        LibFrame(self).Show()

    # clear textbox button
    def m_buttonXOnButtonClick(self, event):
        self.m_url.SetValue("")

    # edit dialog
    def m_listBox1DC(self, event):
        dialog = EditDialog(None, "Title", "Caption")
        dialog.Center()
        dialog.SetValue(self.m_listBox1.GetStringSelection())
        if dialog.ShowModal() == wx.ID_OK:
            self.m_listBox1.SetString(self.m_listBox1.GetSelection(), dialog.GetValue())
        dialog.Destroy()

    # paste button
    def m_buttonVOnButtonClick(self, event):
        text_data = wx.TextDataObject()
        if wx.TheClipboard.Open():
            success = wx.TheClipboard.GetData(text_data)
            wx.TheClipboard.Close()
        if success:
            self.m_url.SetValue(text_data.GetText())

    # add button
    def m_buttonAddOnButtonClick(self, event):
        url = self.m_url.GetValue()
        if url != "":
            self.adder(url)
            self.m_url.SetValue("")

    # add operator
    def adder(self, url):
        listcount = self.m_listBox1.GetCount()
        listitems = self.m_listBox1.GetStrings()

        # artsandculture story
        if url.startswith("http") and "artsandculture.google.com/story/" in url:
            urlcontent = requests.get(url).text.splitlines()
            storyurls = []
            for line in urlcontent:
                if "/asset/" in line:
                    a = "https://artsandculture.google.com" + urllib.parse.quote(
                        line.split('"')[1]
                    )
                    if a not in storyurls:
                        storyurls.append(a)
            if storyurls:  # if list is not empty add to listbox
                self.m_listBox1.InsertItems(storyurls, listcount)
        # artsandculture artist, usergallery
        elif (
            url.startswith("http")
            and "artsandculture.google.com/entity/" in url
            or "artsandculture.google.com/usergallery/" in url
        ):
            page = requests.get(url)
            bSoup = BeautifulSoup(page.content, "html.parser")
            alllinks = bSoup.find_all("a")
            items = bSoup.find("h3", class_="TzXVdf")
            if items != None:
                print(items.text)
            links = []
            for link in alllinks:
                if "href" in link.attrs:
                    if "asset" in link.attrs["href"]:
                        a = "https://artsandculture.google.com" + urllib.parse.quote(
                            link.attrs["href"]
                        )
                        if a not in links:
                            links.append(a)
            if links:  # if list is not empty add to listbox
                self.m_listBox1.InsertItems(links, listcount)
        elif url.startswith("http") and "\n" not in url and url not in listitems:
            self.m_listBox1.InsertItems([url], listcount)
        elif "\n" in url:  # multi url
            multiurl = []
            for i in url.splitlines():
                if i.startswith("http") and i not in listitems:  # if item is not listed
                    multiurl.append(i)
            if multiurl:  # if list is not empty add to listbox
                self.m_listBox1.InsertItems(multiurl, listcount)

    # delete button
    def m_buttonDeleteOnButtonClick(self, event):
        select = self.m_listBox1.GetSelection()
        if select != -1:
            self.m_listBox1.Delete(select)
            self.status("Selected Item Deleted.", "red", 3)

    # clear list button
    def m_buttonClearAllOnButtonClick(self, event):
        count = self.m_listBox1.GetCount()
        if count != 0:
            dlg = wx.MessageDialog(
                self,
                "Are you sure you want to delete all "
                + str(count)
                + " items in the list?",
                "Clear All List!",
                wx.YES_NO | wx.ICON_INFORMATION,
            )
            if dlg.ShowModal() == wx.ID_YES:
                try:
                    self.m_listBox1.Clear()
                    self.m_listBox1.Update()
                    self.status("List Cleared.", "blue", 3)
                except:
                    pass
            dlg.Destroy()

    # open in browser button
    def m_buttonOpenBrowserOnButtonClick(self, event):
        if self.m_listBox1.GetSelection() != -1:
            wait = wx.BusyCursor()
            selected = self.m_listBox1.GetStringSelection()
            webbrowser.open(selected)
            del wait

    # save button
    def m_buttonSaveOnButtonClick(self, event):
        listcount = self.m_listBox1.GetCount()
        if listcount > 0:
            contentlist = []
            with open("list.txt", "w") as file:
                for x in range(0, listcount):
                    contentlist.append(self.m_listBox1.GetString(x))
                for i in contentlist:
                    file.write("{}\n".format(i))
            self.status(str(listcount) + ' items saved to "list.txt" file..', "blue", 4)

    # load button
    def m_buttonLoadOnButtonClick(self, event):
        listcount = self.m_listBox1.GetCount()
        try:
            with open("list.txt") as file:
                file = file.read().splitlines()
                if file != []:
                    self.m_listBox1.InsertItems(file, listcount)
            self.status("Added " + str(len(file)) + " items.", "blue", 4)
        except:
            pass

    # download button
    def m_downloadOnButtonClick(self, event):
        dt = Thread(target=MainFrame.downloader, daemon=True, args=[self]).start()

    # down op
    def downloader(self):
        # os.path.dirname(sys.argv[0])
        dezpath = PATH + "\\dezoomify-rs.exe"
        listcount = self.m_listBox1.GetCount()
        if listcount != 0:
            infolist = []
            # deactivate down button
            self.m_download.Disable()
            self.m_download.SetLabel("Downloading...")
            self.m_download.Refresh()
            for i in range(0, listcount):
                url = self.m_listBox1.GetString(i)
                # hide console
                stinfo = None
                if os.name == "nt":
                    stinfo = subprocess.STARTUPINFO()
                    stinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                # run process
                p = subprocess.run(
                    [dezpath, "-l", url],
                    capture_output=True,
                    startupinfo=stinfo,
                    shell=True,
                    stdin=subprocess.PIPE,
                )
                if "Image successfully saved" in str(p.stdout):
                    infolist.append((True, i + 1, url))
                else:
                    infolist.append((False, i + 1, url))
            # delete successfully downloaded items
            succ = []
            for i in infolist:
                if i[0] == True:
                    succ.append(i[1] - 1)
            succ.reverse()
            for x in succ:
                self.m_listBox1.Delete(x)
            # status info
            self.m_status.SetForegroundColour(wx.Colour(107, 185, 240))
            self.m_status.SetLabel(
                "Download info: "
                + str(len(succ))
                + " successful, "
                + str(listcount - len(succ))
                + " errors."
            )
            # reactivate down button
            self.m_download.Refresh()
            self.m_download.SetLabel("Start Download")
            self.m_download.Enable(True)
            # print(infolist)

    # status operator
    def status(self, msg, color="white", sec=3):
        # message
        self.m_status.SetLabel(msg)
        # colors
        if color == "red":
            self.m_status.SetForegroundColour(wx.Colour(240, 52, 52))
        elif color == "blue":
            self.m_status.SetForegroundColour(wx.Colour(107, 185, 240))
        elif color == "white":
            self.m_status.SetForegroundColour(wx.Colour(251, 251, 251))
        # duration sec
        wx.CallLater(sec * 1000, self.m_status.SetLabel, "")


# ---------------------------------------------------#
# EditDialog
# ---------------------------------------------------#


class EditDialog(wx.Dialog):
    def __init__(self, parent, title, caption):
        style = wx.CLOSE_BOX | wx.CAPTION
        super(EditDialog, self).__init__(parent, -1, title=u"Edit", style=style)
        input = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE | wx.BORDER_SIMPLE)
        input.SetInitialSize((400, 80))
        buttons = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(input, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(buttons, 0, wx.EXPAND | wx.ALL, 5)
        self.SetSizerAndFit(sizer)
        self.input = input
        self.InitUI()

    def InitUI(self):
        self.SetBackgroundColour(wx.Colour(45, 56, 72))
        self.input.SetFont(
            wx.Font(
                11,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.input.SetForegroundColour(wx.Colour(251, 251, 251))
        self.input.SetBackgroundColour(wx.Colour(75, 84, 104))

    def SetValue(self, value):
        self.input.SetValue(value)

    def GetValue(self):
        return self.input.GetValue()


# ---------------------------------------------------#
# LibFrame
# ---------------------------------------------------#


class LibFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"Downloaded Images \U0001F3DB",
            pos=wx.DefaultPosition,
            size=wx.Size(1067, 640),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(45, 56, 72))

        if os.path.exists("icon.ico"):
            icon = wx.Icon()
            icon.CopyFromBitmap(wx.Bitmap("icon.ico", wx.BITMAP_TYPE_ANY))
            self.SetIcon(icon)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        fgSizer6 = wx.FlexGridSizer(0, 0, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_Label = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Downloaded Images \U0001F3DB",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_Label.Wrap(-1)

        self.m_Label.SetFont(
            wx.Font(
                12,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_Label.SetForegroundColour(wx.Colour(255, 255, 255))

        fgSizer6.Add(self.m_Label, 0, wx.ALL, 10)

        bSizer5.Add(fgSizer6, 0, wx.ALIGN_CENTER, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer7.Add((0, 0), 0, wx.LEFT, 5)

        fgSizer9 = wx.FlexGridSizer(0, 1, 0, 0)
        fgSizer9.SetFlexibleDirection(wx.BOTH)
        fgSizer9.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_thumbnail = wx.StaticBitmap(
            self,
            wx.ID_ANY,
            wx.NullBitmap,
            wx.DefaultPosition,
            wx.Size(200, 140),
            wx.BORDER_NONE,
        )

        bSizer13.Add(self.m_thumbnail, 0, wx.EXPAND, 5)

        self.m_title = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Tiriel Supporting the Dying Myratana and Cursing His Sons",
            wx.DefaultPosition,
            wx.Size(-1, -1),
            0,
        )
        self.m_title.Wrap(160)

        self.m_title.SetFont(
            wx.Font(
                10,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_title.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK)
        )

        bSizer13.Add(self.m_title, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        self.m_artist = wx.StaticText(
            self, wx.ID_ANY, u"William Blake", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_artist.Wrap(160)

        self.m_artist.SetFont(
            wx.Font(
                wx.NORMAL_FONT.GetPointSize(),
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_artist.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK)
        )

        bSizer13.Add(self.m_artist, 0, wx.ALL, 5)

        self.m_infodim = wx.StaticText(
            self, wx.ID_ANY, u"6600x4540px", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_infodim.Wrap(160)

        self.m_infodim.SetFont(
            wx.Font(
                8,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_infodim.SetForegroundColour(wx.Colour(208, 208, 208))

        bSizer13.Add(self.m_infodim, 0, wx.LEFT, 5)

        self.m_infosize = wx.StaticText(
            self, wx.ID_ANY, u"Size: 3.45MB", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_infosize.Wrap(160)

        self.m_infosize.SetFont(
            wx.Font(
                8,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_infosize.SetForegroundColour(wx.Colour(208, 208, 208))

        bSizer13.Add(self.m_infosize, 0, wx.LEFT, 5)

        self.m_infotype = wx.StaticText(
            self, wx.ID_ANY, u"Type: JPG", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_infotype.Wrap(160)

        self.m_infotype.SetFont(
            wx.Font(
                8,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_infotype.SetForegroundColour(wx.Colour(208, 208, 208))

        bSizer13.Add(self.m_infotype, 0, wx.LEFT, 5)

        fgSizer9.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        # Palette
        bSizer8.Add((0, 0), 1, wx.EXPAND, 5)

        fgSizer91 = wx.FlexGridSizer(0, 5, 0, 0)
        fgSizer91.SetFlexibleDirection(wx.BOTH)
        fgSizer91.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_pb1 = wx.Button(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.BORDER_NONE | wx.BORDER_NONE,
        )
        self.m_pb1.SetBackgroundColour(wx.Colour(45, 56, 72))
        self.m_pb1.SetMinSize(wx.Size(40, 20))

        fgSizer91.Add(self.m_pb1, 0, 0, 5)

        self.m_pb2 = wx.Button(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.BORDER_NONE | wx.BORDER_NONE,
        )
        self.m_pb2.SetBackgroundColour(wx.Colour(45, 56, 72))
        self.m_pb2.SetMinSize(wx.Size(40, 20))

        fgSizer91.Add(self.m_pb2, 0, 0, 5)

        self.m_pb3 = wx.Button(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.BORDER_NONE | wx.BORDER_NONE,
        )
        self.m_pb3.SetBackgroundColour(wx.Colour(45, 56, 72))
        self.m_pb3.SetMinSize(wx.Size(40, 20))

        fgSizer91.Add(self.m_pb3, 0, 0, 5)

        self.m_pb4 = wx.Button(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.BORDER_NONE | wx.BORDER_NONE,
        )
        self.m_pb4.SetBackgroundColour(wx.Colour(45, 56, 72))
        self.m_pb4.SetMinSize(wx.Size(40, 20))

        fgSizer91.Add(self.m_pb4, 0, 0, 5)

        self.m_pb5 = wx.Button(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.BORDER_NONE | wx.BORDER_NONE,
        )
        self.m_pb5.SetBackgroundColour(wx.Colour(45, 56, 72))
        self.m_pb5.SetMinSize(wx.Size(40, 20))

        fgSizer91.Add(self.m_pb5, 0, 0, 5)

        bSizer8.Add(fgSizer91, 1, wx.EXPAND, 5)
        ###########

        fgSizer9.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer7.Add(fgSizer9, 0, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_listCtrl1 = wx.ListCtrl(
            self,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.BORDER_NONE,
        )
        self.m_listCtrl1.SetFont(
            wx.Font(
                10,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_listCtrl1.SetForegroundColour(wx.Colour(251, 251, 251))
        self.m_listCtrl1.SetBackgroundColour(wx.Colour(75, 84, 104))
        self.m_listCtrl1.InsertColumn(1, "Title", width=300)
        self.m_listCtrl1.InsertColumn(2, "Artist", width=200)
        self.m_listCtrl1.InsertColumn(3, "Filename", width=325)

        bSizer10.Add(self.m_listCtrl1, 1, wx.EXPAND | wx.LEFT, 4)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        fgSizer10 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer10.SetFlexibleDirection(wx.BOTH)
        fgSizer10.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_buttonRef = wx.Button(
            self,
            wx.ID_ANY,
            u"Refresh",
            wx.DefaultPosition,
            wx.Size(-1, 32),
            wx.BORDER_NONE,
        )
        self.m_buttonRef.SetFont(
            wx.Font(
                10,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_buttonRef.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK)
        )
        self.m_buttonRef.SetBackgroundColour(wx.Colour(70, 67, 97))
        self.m_buttonRef.SetToolTip(u"Refresh List")

        fgSizer10.Add(self.m_buttonRef, 0, wx.LEFT, 4)

        self.m_buttonOpen = wx.Button(
            self,
            wx.ID_ANY,
            u"Open Image",
            wx.DefaultPosition,
            wx.Size(-1, 32),
            wx.BORDER_NONE,
        )
        self.m_buttonOpen.SetFont(
            wx.Font(
                10,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_buttonOpen.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK)
        )
        self.m_buttonOpen.SetBackgroundColour(wx.Colour(70, 67, 97))

        fgSizer10.Add(self.m_buttonOpen, 0, wx.LEFT, 1)

        self.m_buttonEdit = wx.Button(
            self,
            wx.ID_ANY,
            u"Edit Filename",
            wx.DefaultPosition,
            wx.Size(-1, 32),
            wx.BORDER_NONE,
        )
        self.m_buttonEdit.SetFont(
            wx.Font(
                10,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                "Segoe UI Semibold",
            )
        )
        self.m_buttonEdit.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK)
        )
        self.m_buttonEdit.SetBackgroundColour(wx.Colour(70, 67, 97))

        fgSizer10.Add(self.m_buttonEdit, 0, wx.LEFT, 1)

        bSizer14.Add(fgSizer10, 1, wx.EXPAND, 5)

        """self.m_search = wx.TextCtrl(self, wx.ID_ANY, u"Search...", wx.DefaultPosition, wx.Size(
            200, 32), 0 | wx.BORDER_SIMPLE)
        self.m_search.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
								wx.FONTWEIGHT_NORMAL, False, "Segoe UI Semibold"))
        self.m_search.SetForegroundColour(wx.Colour(255, 255, 255))
        self.m_search.SetBackgroundColour(wx.Colour(75, 84, 104))

        bSizer14.Add(self.m_search, 0, wx.ALIGN_RIGHT, 5)"""

        bSizer10.Add(bSizer14, 0, wx.EXPAND, 5)

        bSizer7.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer5.Add(bSizer7, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_thumbnail.Bind(wx.EVT_LEFT_DCLICK, self.openSelectedItem)
        self.m_pb1.Bind(wx.EVT_BUTTON, self.m_pbOnButtonClick)
        self.m_pb2.Bind(wx.EVT_BUTTON, self.m_pbOnButtonClick)
        self.m_pb3.Bind(wx.EVT_BUTTON, self.m_pbOnButtonClick)
        self.m_pb4.Bind(wx.EVT_BUTTON, self.m_pbOnButtonClick)
        self.m_pb5.Bind(wx.EVT_BUTTON, self.m_pbOnButtonClick)
        self.m_listCtrl1.Bind(wx.EVT_LEFT_DCLICK, self.openSelectedItem)
        self.m_listCtrl1.Bind(
            wx.EVT_LIST_ITEM_FOCUSED, self.m_listCtrl1OnListItemFocused
        )
        self.m_buttonRef.Bind(wx.EVT_BUTTON, self.m_buttonRefOnButtonClick)
        self.m_buttonOpen.Bind(wx.EVT_BUTTON, self.openSelectedItem)
        self.m_buttonEdit.Bind(wx.EVT_BUTTON, self.m_buttonEditOnButtonClick)

        list = self.listimages()
        for i in list:
            self.m_listCtrl1.Append(i)
        if self.m_listCtrl1.GetItemCount() > 1:
            self.m_listCtrl1.Select(0)
            self.m_listCtrl1.Focus(0)

    def __del__(self):
        pass

    # list images
    def listimages(self):
        filelist = PATH + "/"  # +"\\Downloaded"
        files = [
            f
            for f in os.listdir(".")
            if os.path.isfile(f) and f.endswith((".jpg", ".jpeg", ".png"))
        ]
        listfinal = []
        for i in files:
            iext = i  # with file .ext
            i = i[: -(len(i.split(".")[-1:][0]) + 1)]  # without file .ext
            if " - " in i:
                listhyp = [i.split(" - ")[0], i.split(" - ")[1], iext]
                if "_" in listhyp[1] and listhyp[1].split("_")[1][0].isdigit():
                    # "Lessing_45.jpg" abc_n.ext : check after "_" if first character is number
                    listhyp[1] = listhyp[1].split("_")[0]
                if " (" in listhyp[1]:
                    # "Aert van der Neer (Dutch 1603"
                    listhyp[1] = listhyp[1].split(" (")[0]
                """if "_ " in listhyp[1]:
                    #"Karl Friedrich Lessing_ German_ 1808"
                    listhyp[1]=listhyp[1].split("_ ")[0]"""
                listfinal.append(listhyp)
            else:  # no artist info
                listfinal.append((i, "", iext))  # append direct
        return listfinal

    # open selected
    def openSelectedItem(self, event):
        if self.m_listCtrl1.GetFirstSelected() != -1:
            path = self.m_listCtrl1.GetItemText(
                self.m_listCtrl1.GetFirstSelected(), 2
            )  # "Downloaded\\"+
            webbrowser.open(path)

    # copy hex code of color
    def m_pbOnButtonClick(self, event):
        pyperclip.copy(
            "%02x%02x%02x" % event.GetEventObject().GetBackgroundColour()[:-1]
        )  # convert rgb to hex

    # refresh
    def m_buttonRefOnButtonClick(self, event):
        self.m_listCtrl1.DeleteAllItems()
        self.m_listCtrl1.Update()
        list = self.listimages()
        for i in list:
            self.m_listCtrl1.Append(i)

    def m_listCtrl1OnListItemFocused(self, event):
        # Title, Artist, file info
        self.m_title.SetLabel(
            self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFirstSelected(), 0)
        )
        self.m_title.Wrap(160)
        self.m_title.Refresh()
        self.m_artist.SetLabel(
            self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFirstSelected(), 1)
        )
        self.m_artist.Wrap(160)
        self.m_artist.Refresh()
        # Thumbnail
        path = self.m_listCtrl1.GetItemText(
            self.m_listCtrl1.GetFirstSelected(), 2
        )  # "Downloaded\\"+
        try:
            self.m_infotype.SetLabel("Type: " + path[-4:].upper())  # file type
            image = Image.open(path)
            self.m_infodim.SetLabel(
                str(image.size[0]) + "x" + str(image.size[1])
            )  # dimensions
            self.m_infosize.SetLabel(
                "Size: " + str(round(os.path.getsize(path) / (1024 * 1024), 2)) + "MB"
            )  # file size
            MAX_SIZE = (200, 140)
            image.thumbnail(MAX_SIZE)
            width, height = image.size
            aa = wx.Bitmap.FromBuffer(width, height, image.tobytes())
            self.m_thumbnail.SetBitmap(wx.NullBitmap)
            self.m_thumbnail.SetBitmap(aa)
        except:
            print("file not found.")
            self.m_thumbnail.SetBitmap(wx.NullBitmap)
        # get palette thread
        Thread(target=LibFrame.getpalette, daemon=True, args=[self]).start()

    def getpalette(self):
        path = self.m_listCtrl1.GetItemText(
            self.m_listCtrl1.GetFirstSelected(), 2
        )  # "Downloaded\\"+
        try:
            gp = Haishoku.getPalette(path)
            palettelist = []
            for i in gp[:5]:
                palettelist.append(i[1])
            print(palettelist)
            self.setpalette(palettelist)
        except:
            empty = [(45, 56, 72)] * 5
            self.setpalette(empty)

    def setpalette(self, plist):
        for n in range(len(plist)):
            i = plist[n]
            exec("self.m_pb{0}.SetBackgroundColour({1})".format(n + 1, i))
        if len(plist) < 5:  # when palette is less than 5
            for n in range(5)[-(5 - len(plist)) :]:
                exec("self.m_pb{0}.SetBackgroundColour((45,56,72))".format(n + 1))

    # edit
    def m_buttonEditOnButtonClick(self, event):
        if self.m_listCtrl1.GetFirstSelected() != -1:
            dialog = EditDialog(None, "Title", "Caption")
            dialog.Center()
            path = self.m_listCtrl1.GetItemText(
                self.m_listCtrl1.GetFirstSelected(), 2
            )  # "Downloaded\\"+
            dialog.SetValue(path)
            if dialog.ShowModal() == wx.ID_OK:
                selected = self.m_listCtrl1.GetFirstSelected()
                try:
                    os.rename(path, dialog.GetValue())
                    self.m_buttonRefOnButtonClick(event)  # refresh
                    # find item
                    indx = self.m_listCtrl1.FindItem(-1, dialog.GetValue())
                    self.m_listCtrl1.Select(indx)
                    self.m_listCtrl1.Focus(indx)
                except FileExistsError:
                    print("FileExistsError")
            dialog.Destroy()


# ------------------------------------------------#


class MainApp(wx.App):
    def OnInit(self):
        mainFrame = MainFrame(None)
        mainFrame.Show(True)
        return True


if __name__ == "__main__":
    app = MainApp()
    app.MainLoop()
