import wx
from ffutil import FFUtil


class DownloadFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 500), style=wx.DEFAULT_FRAME_STYLE)

        # ffmpeg所在路径
        self.ffLabel = wx.TextCtrl(self, style=wx.TE_LEFT | wx.TE_READONLY, size=(200, - 1))
        ffBtn = wx.Button(self, label='选择FFmpeg路径')
        ffSize = wx.BoxSizer(wx.HORIZONTAL)
        ffSize.Add(self.ffLabel)
        ffSize.Add(ffBtn)

        # 视频地址
        urlLabel = wx.StaticText(self, label="m3u8文件地址：")
        urlLabel.SetForegroundColour('#ffffff')
        self.urlEdit = wx.TextCtrl(self, style=wx.TE_LEFT, size=(200, -1))
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(urlLabel)
        sizer.Add(self.urlEdit)

        # 视频保存路径
        self.savePath = wx.TextCtrl(self, style=wx.TE_LEFT, size=(200, - 1))
        fileBtn = wx.Button(self, label='选择保存路径')
        fileSize = wx.BoxSizer(wx.HORIZONTAL)
        fileSize.Add(self.savePath)
        fileSize.Add(fileBtn)

        sizer2 = wx.BoxSizer(wx.VERTICAL)
        startBtn = wx.Button(self, wx.ID_ANY, label="开始下载", size=(72, 36))
        self.state = wx.StaticText(self, label='准备下载')
        self.state.SetForegroundColour('#ffffff')

        sizer2.Add(ffSize, 0, wx.ALL, 4)
        sizer2.AddSpacer(10)

        sizer2.Add(sizer, 0, wx.ALL, 4)
        sizer2.Add(fileSize, 0, wx.ALL, 4)
        sizer2.Add(startBtn, 0, wx.ALL, 4)
        sizer2.Add(self.state, 0, wx.ALL, 4)

        self.Bind(wx.EVT_BUTTON, self.startDownload, startBtn)
        self.Bind(wx.EVT_BUTTON, self.saveFilePath, fileBtn)
        self.Bind(wx.EVT_BUTTON, self.selectFFPath, ffBtn)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.onEraseBack)
        self.SetSizer(sizer2)
        self.SetMinSize((800, 500))
        self.SetMaxSize((800, 500))
        self.Show()

    def onEraseBack(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetDeviceClippingRegion(rect)
        dc.Clear()
        bmp = wx.Bitmap('res/background.jpg')
        dc.DrawBitmap(bmp, 0, 0)

    def selectFFPath(self, event):
        with wx.FileDialog(self, "Save Path", wildcard=".*", style=wx.FD_OPEN) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            path = fileDialog.GetPath()
            self.ffLabel.SetValue(path)

    def saveFilePath(self, event):
        with wx.FileDialog(self, "Save Path", wildcard=".*", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            path = fileDialog.GetPath()
            self.savePath.SetValue(path)

    def callback(self, future):
        if future.result().strip() == 'success':
            self.state.SetLabel('下载完毕')
            self.state.SetForegroundColour('#1bd061')
        else:
            self.state.SetLabel('下载失败')
            self.state.SetForegroundColour('#f33a32')
        print(future.result())

    def startDownload(self, event):
        videoPath = self.urlEdit.GetValue()
        savePath = self.savePath.GetValue()
        ffPath = self.ffLabel.GetValue()
        if videoPath.strip() == '' or savePath.strip() == '':
            return
        self.state.SetLabel('下载中......')
        ffUtil = FFUtil(videoPath, savePath, ffPath)
        ffUtil.run(self.callback)


if __name__ == '__main__':
    app = wx.App(False)
    frame = DownloadFrame(None, "m3u8 downloader")
    app.MainLoop()
