# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InfoWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_3(object):
    # def traninfo(self, info):
    #     self.textEdit.setPlainText(info)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 422)
        MainWindow.setFixedSize(950, 422)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 950, 400))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlainText('''
                                RRRRRRRRRRR        OOOOOOOO             OOOOOOOO         KK            II     EEEEEEEE\r
                              RRRRRRRRRRRRR      OOOOOOOOOOOO         OOOOOOOOOOOO       KK                   EEE\r
                              RRRRRRR RRR       OOOO      OOOO       OOOO      OOOO      KK           IIII    EEE\r
                              RRRRRRR RRR      OOOO   OO   OOOO     OOOO   OO   OOOO     KK   KKK     IIII    EEE\r
                               RRRRRR RRR     OOOOO  OOOO  OOOOO   OOOOO  OOOO  OOOOO    KK  KK       IIII    EEEEEEEE\r
                                  RRR RRR      OOOO  OOOO  OOOO     OOOO  OOOO  OOOO     KKKKK        IIII    EEE\r
                                  RRR RRR       OOOOO    OOOOO       OOOOO    OOOOO      KKKKK        IIII    EEE\r
                                  RRR RRR        OOOOOOOOOOOO         OOOOOOOOOOOO       KK  KK       IIII    EEE\r
                                  RRR RRR          OOOOOOOO             OOOOOOOO         KK   KKK     IIII    EEEEEEEE\r
        
        
        I . 菜单栏 Models 模式说明
          1.Counting One File 与 Diff Counting Two Files
            单个工程的代码总行数统计 与 前后两个版本工程的代码差异行数统计。
            只能二选一。
          2.Simple OutPut 与 Complex Output
            只输出最后的统计结果 与 详细输出单个文件的差异。
            只能二选一。
            
        II . 菜单栏 Settings 设置说明
          1.IgnoreCase
            比较时忽略大小写差异，单击选中，再次单击取消。
          2.ForceParseALL
            即使两个文件相同也会进行比较，较耗时，单击选中，再次单击取消。
          3.SaveToTxt
            将结果保存到本地（同工作目录）result.txt文件，此时直接保存，不弹出信息框，单击选中，再次单击取消。
            
        III . 两个黑框
          即路径输入框，可直接拖拽文件夹，左边为原始工程或单个工程，右边为最新工程。
          注意！！请拖拽文件夹，不能直接拖拽单个文件！！！
          此外！！除了拖拽的方式，也可直接键盘输入修改！！
          
        IV . 绿色按钮
          即运行按钮。
          
        V . 数码框
          即程序运行时间。
          
        VI . 比较结果信息界面说明
          LANG  语言或配置文件类型
          ADD   新增代码行数
          MOD   修改代码行数
          DEL   删除代码行数
          A&M   新增与修改代码行数之和
          BLK   空行数
          CMT   注释行数
          NBNC  非空非注释行数
          RATE  标准C折算率
          STATE 变更模式
          BASELINE FILE  原工程
          TARGET FILE    新工程
          Total          加权求和折换C
                                    ''')


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Help Information"))

