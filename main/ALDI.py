from OboardCamDisp import Ui_MainWindow
from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QTimer, QEvent
from subprocess import Popen, PIPE
from time import clock
from prettytable import PrettyTable
# import os


class DiffCount(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(DiffCount, self).__init__(parent)
        self.setupUi(self)
        self.prepParameters()
        self.callBackFunctions()
        self.Timer=QTimer()
        self.OriginPathLE.installEventFilter(self)
        self.NewPathLE.installEventFilter(self)

    def prepParameters(self):
        self.OriginPath = None
        self.NewPath = None
        self.ignore = None
        self.force = None
        self.txt = None
        self.cmd = 'diffcount'
        self.simple = '--for-program-reading'
        self.complex = '--print-files-info'
        self.diffLen = 0

    def callBackFunctions(self):
        self.GoBtn.clicked.connect(self.goComparison)
        self.OriginPathBtn.clicked.connect(self.setOriginPath)
        self.NewPathBtn.clicked.connect(self.setNewPath)
        self.OneBtn.clicked.connect(self.setOneModel)
        self.DiffBtn.clicked.connect(self.setComparisonModel)
        self.SimpleBtn.clicked.connect(self.setSimpleModel)
        self.ComplexBtn.clicked.connect(self.setComplexModel)
        self.IgnoreCkb.stateChanged.connect(self.ignoreCase)
        self.ForceCkb.stateChanged.connect(self.forceParseAll)
        self.FileCkb.stateChanged.connect(self.exportToTxt)
        self.OriginPathLE.textChanged.connect(self.originPathChange)
        self.NewPathLE.textChanged.connect(self.newPathChange)
        # self.IniBtn.clicked.connect(self.addToPath)

    def goComparison(self):
        self.Timer.start(1)
        timelb = clock()
        if self.ChoiceSld.value() == 0:
            if self.OriginPath is not None:
                self.cmd = self.cmd + ' ' + self.OriginPath + ' ' + '-c'
                if self.ignore is not None:
                    self.cmd = self.cmd + ' ' + self.ignore
                if self.force is not None:
                    self.cmd = self.cmd + ' ' + self.force
                if self.ChoiceSld_2.value() == 0:
                    self.cmd = self.cmd + ' ' + self.simple
                else:
                    self.cmd = self.cmd + ' ' + self.complex
                if self.txt is not None:
                    self.cmd = self.cmd + ' ' + self.txt
                info = Popen(self.cmd, shell=True, stdout=PIPE)
                info = info.communicate()[0].decode()
                self.InfoTE.setPlainText(info)
                if self.ChoiceSld_2.value() == 0 and not self.FileCkb.isChecked():
                    print(info)
                    self.cmd = 'diffcount'
                elif self.ChoiceSld_2.value() == 1 and not self.FileCkb.isChecked():
                    lines = info.split('\r\n')
                    for line in lines:
                        line = line.strip()
                        if not len(line):
                            continue
                        linecp = line.split()
                        if linecp[-1] == 'FILE':
                            linecp.pop()
                            linecp.pop()
                            linecp.append('TARGET FILE')
                        if linecp[0] == 'LANG':
                            table = PrettyTable(linecp)
                        elif linecp[0] == 'Counting' or linecp[0] == 'Convert':
                            string = ' '.join(linecp)
                            print(table)
                            print(string)
                        elif linecp[0] == 'Total:' or len(linecp) == 1:
                            string = ' '.join(linecp)
                            print(string)
                        else:
                            table.add_row(linecp)
                    self.cmd = 'diffcount'
                else:
                    self.cmd = 'diffcount'
        else:
            if self.OriginPath is not None and self.NewPath is not None:
                self.cmd = self.cmd + ' ' + self.OriginPath + ' ' + self.NewPath
                if self.ignore is not None:
                    self.cmd = self.cmd + ' ' + self.ignore
                if self.force is not None:
                    self.cmd = self.cmd + ' ' + self.force
                if self.ChoiceSld_2.value() == 0:
                    self.cmd = self.cmd + ' ' + self.simple
                else:
                    self.cmd = self.cmd + ' ' + self.complex
                if self.txt is not None:
                    self.cmd = self.cmd + ' ' + self.txt
                info = Popen(self.cmd, shell=True, stdout=PIPE)
                info = info.communicate()[0].decode()
                self.InfoTE.setPlainText(info)
                if self.ChoiceSld_2.value() == 0 and not self.FileCkb.isChecked():
                    print(info)
                    self.cmd = 'diffcount'
                elif self.ChoiceSld_2.value() == 1 and not self.FileCkb.isChecked():
                    lines = info.split('\r\n')
                    for line in lines:
                        line = line.strip()
                        if not len(line):
                            continue
                        linecp = line.split()
                        if linecp[-1] == 'FILE':
                            linecp.pop()
                            linecp.pop()
                            linecp.pop()
                            linecp.pop()
                            linecp.append('BASELINE FILE')
                            linecp.append('TARGET FILE')
                            self.diffLen = len(linecp)
                        if linecp[0] == 'LANG':
                            table = PrettyTable(linecp)
                        elif linecp[0] == 'Diffcount' or linecp[0] == 'Convert':
                            string = ' '.join(linecp)
                            print(table)
                            self.diffLen = 0
                            print(string)
                        elif linecp[0] == 'Total:' or len(linecp) == 1:
                            string = ' '.join(linecp)
                            print(string)
                        else:
                            if len(linecp) < self.diffLen:
                                linecp.append('None')
                            table.add_row(linecp)
                    self.cmd = 'diffcount'
                else:
                    self.cmd = 'diffcount'
        self.TimeCostLCD.display(clock()-timelb)
        self.Timer.stop()

    def setOriginPath(self):
        dirname = QFileDialog.getExistingDirectory(self, "浏览", '.')
        if dirname:
            self.OriginPathLE.setText(dirname)
            self.OriginPath = dirname

    def setNewPath(self):
        dirname = QFileDialog.getExistingDirectory(self, "浏览", '.')
        if dirname:
            self.NewPathLE.setText(dirname)
            self.NewPath = dirname

    def setOneModel(self):
        self.ChoiceSld.setValue(0)
        self.NewPathLE.setEnabled(False)
        self.NewPathBtn.setEnabled(False)

    def setComparisonModel(self):
        self.ChoiceSld.setValue(1)
        self.NewPathLE.setEnabled(True)
        self.NewPathBtn.setEnabled(True)

    def setSimpleModel(self):
        self.ChoiceSld_2.setValue(0)

    def setComplexModel(self):
        self.ChoiceSld_2.setValue(1)

    def ignoreCase(self):
        if self.IgnoreCkb.isChecked():
            self.ignore = '--ignore-case'
        else:
            self.ignore = None

    def forceParseAll(self):
        if self.ForceCkb.isChecked():
            self.force = '--force-parse-all'
        else:
            self.force = None

    def exportToTxt(self):
        if self.FileCkb.isChecked():
            self.txt = '> result.txt'
        else:
            self.txt = None

    # def dragEnterEvent(self, event):
    #     if event.mimeData().hasUrls():
    #         event.accept()  # must accept the dragEnterEvent or else the dropEvent can't occur !!!
    #     else:
    #         event.ignore()

    def eventFilter(self, object, event):
        if object is self.OriginPathLE:
            if event.type() == QEvent.DragEnter:
                if event.mimeData().hasUrls():
                    # object.setText('')
                    event.accept()
                else:
                    event.ignore()
        if object is self.NewPathLE:
            if event.type() == QEvent.DragEnter:
                if event.mimeData().hasUrls():
                    # object.setText('')
                    event.accept()
                else:
                    event.ignore()
            # if event.type() == QEvent.Drop:
            #     if event.mimeData().hasUrls():  # if file or link is dropped
            #         urlcount = len(event.mimeData().urls())  # count number of drops
            #         url = event.mimeData().urls()[0]  # get first url
            #         print(url)
            #         object.setText(object.text().replace('file:///', ''))
            #         print('aaa')
            #         object.setText(url.toString())  # assign first url to editline
            #         print('eeee')
            return False
        return False

    def originPathChange(self):
        if 0 == self.OriginPathLE.text().find('file:///'):
            self.OriginPathLE.setText(self.OriginPathLE.text().replace('file:///', ''))
            self.OriginPath = self.OriginPathLE.text()

    def newPathChange(self):
        if 0 == self.NewPathLE.text().find('file:///'):
            self.NewPathLE.setText(self.NewPathLE.text().replace('file:///', ''))
            self.NewPath = self.NewPathLE.text()

    # def addToPath(self):
    #     os.environ["PATH"] = os.environ["PATH"] + ';' + str(sys.path[0])+';'


if __name__ == '__main__':
    app = QApplication(argv)
    ui = DiffCount()
    ui.show()
    exit(app.exec_())
