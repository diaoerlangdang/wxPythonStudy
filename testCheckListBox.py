#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2018-1-4

@author: wise
'''
import wx
class TestApp(wx.Frame):
    def __init__(self,parent,title):
        super(TestApp,self).__init__(parent,title=title,size=(500,300))
        #最小大小
        self.SetMinSize((500, 300))
        #初始化ui
        self.InitUI()
        #居中
        self.Centre()
        #显示
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        titleFont = font
        font.SetPointSize(9)
        titleFont.SetPointSize(12)

        #间隙
        hvGap = 5;

        #主布局、水平
        mainHBox = wx.BoxSizer(wx.HORIZONTAL)

        #左侧布局、垂直
        leftVBox = wx.BoxSizer(wx.VERTICAL)

        #案例标题
        st1 = wx.StaticText(panel,label='测试案例')
        st1.SetFont(titleFont)
        leftVBox.Add(st1,flag=wx.LEFT|wx.RIGHT|wx.TOP, border = hvGap)

        #案例列表
        self.checkListBox =  wx.CheckListBox(panel, choices = ['测试案例1','测试案例2','测试案例3'])
        self.Bind(wx.EVT_CHECKLISTBOX, self.onCheckListBoxSelect, self.checkListBox)
        leftVBox.Add(self.checkListBox, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border = hvGap)
        leftVBox.Add((-1, 10))

        #全选
        self.selectAllCheckBox = wx.CheckBox(panel, label='全选', style=wx.CHK_3STATE)
        self.selectAllCheckBox.SetFont(font)
        self.Bind(wx.EVT_CHECKBOX, self.onCheckBoxSelectAll, self.selectAllCheckBox)
        leftVBox.Add(self.selectAllCheckBox,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border = hvGap)

        leftVBox.Add((-1, 10))


        mainHBox.Add(leftVBox, proportion = 1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border = hvGap)

        
        #右侧布局、垂直
        rightVBbox = wx.BoxSizer(wx.VERTICAL)
        
        '''hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel,label='测试文件')
        st1.SetFont(font)
        
        hbox1.Add(st1,flag=wx.RIGHT,border=8)
        tc = wx.TextCtrl(panel)
        hbox1.Add(tc,proportion=1)
        self.selectFileBtn = wx.Button(panel, label='选择文件', size=(70, 30))
        #self.Bind(wx.EVT_BUTTON, self.OnClickSelectFile, self.selectFileBtn)  #未实现
        hbox1.Add(self.selectFileBtn, flag=wx.LEFT|wx.RIGHT, border=hvGap)
        rightVBbox.Add(hbox1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,border=hvGap)
        
        rightVBbox.Add((-1,hvGap))'''

        #日志标题
        st2 = wx.StaticText(panel,label='日志')
        st2.SetFont(titleFont)
        rightVBbox.Add(st2,flag=wx.LEFT|wx.RIGHT|wx.TOP, border = hvGap)
        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.logTextCtrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_READONLY)
        hbox3.Add(self.logTextCtrl, proportion=1, flag=wx.EXPAND)
        rightVBbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND|wx.TOP, 
            border=hvGap)

        rightVBbox.Add((-1, 10))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)

        #串口选择
        self.ComChoice = wx.Choice(panel, choices=['串口1','串口2','串口3','串口4'], size=(100, 30))
        #self.Bind(wx.EVT_BUTTON, self.onClickedRefreshBtn, self.refreshBtn)
        hbox5.Add(self.ComChoice, flag=wx.LEFT|wx.BOTTOM, border=5)

        #刷新串口按钮
        self.refreshBtn = wx.Button(panel, label='刷新串口', size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.onClickedRefreshBtn, self.refreshBtn)
        hbox5.Add(self.refreshBtn, flag=wx.LEFT|wx.BOTTOM, border=5)

        #开始测试按钮
        self.startBtn = wx.Button(panel, label='开始', size=(60, 30))
        self.Bind(wx.EVT_BUTTON, self.onClickedStartBtn, self.startBtn)
        hbox5.Add(self.startBtn, flag=wx.LEFT|wx.BOTTOM, border=5)

        #停止测试按钮
        self.stopBtn = wx.Button(panel, label='停止', size=(60, 30))
        self.Bind(wx.EVT_BUTTON, self.onClickedStopBtn, self.stopBtn)
        hbox5.Add(self.stopBtn, flag=wx.LEFT|wx.BOTTOM, border=5)
        rightVBbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=hvGap)

        mainHBox.Add(rightVBbox, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border = hvGap)
        
        panel.SetSizer(mainHBox)

        #默认全选
        self.selectAllCheckBox.Set3StateValue(wx.CHK_CHECKED)
        self.selectListAll(True)
        self.checkListBox.SetSelection(1) #选中某行
        #self.checkListBox.SetSelection(-1) #取消选中

    #check列表 是否选中
    def onCheckListBoxSelect(self,event):
        #选中个数
        selectCount = len(self.checkListBox.GetChecked())

        #全不选
        if selectCount == 0:
            self.selectAllCheckBox.Set3StateValue(wx.CHK_UNCHECKED)
            pass
        #全选
        elif selectCount == self.checkListBox.GetCount():
            self.selectAllCheckBox.Set3StateValue(wx.CHK_CHECKED)
            pass
        #未全选
        else:
            self.selectAllCheckBox.Set3StateValue(wx.CHK_UNDETERMINED) 
            pass
        pass

    #全选check box
    def onCheckBoxSelectAll(self, event):
        self.selectListAll(self.selectAllCheckBox.Get3StateValue() == wx.CHK_CHECKED)
        pass

    #设置check box 不全选，需要checkBox支持3个状态，checkBox 为控件
    def setCheckBoxSelectNotAll(self, checkBox):
        checkBox.Set3StateValue(wx.CHK_UNDETERMINED)
        pass

    #选中所有或全部不选 isSelected=true 为全选；否则为全不选
    def selectListAll(self,isSelected):

        #全选
        if isSelected:
            #全选
            self.checkListBox.SetChecked(range(0,self.checkListBox.GetCount()))
            pass
        else :
            #全不选
            self.checkListBox.SetChecked([]) 
            pass
        pass

    #刷新串口列表
    def onClickedRefreshBtn(self,event):
        print('刷新串口列表')
        pass

    #开始测试
    def onClickedStartBtn(self,event):
        print('开始测试')
        pass

    #停止测试
    def onClickedStopBtn(self,event):
        print('停止测试')
        pass
        
if __name__ == '__main__':
    app = wx.App()
    TestApp(None,title="测试软件")
    app.MainLoop()