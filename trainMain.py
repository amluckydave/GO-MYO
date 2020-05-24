from firstPage.train_UI import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication
from myoLib.dataRev import Win1
from PyQt5.QtWidgets import QDesktopWidget
from myoLib.myoPath import myoPath, myoRawPath
import pyqtgraph as pg
from collections import deque
from PyQt5.QtCore import QTimer, Qt
import time
from myoLib.myoManager import MyoManager, EventType
import numpy as np
import os
from myoLib.init_Pics import init_Pics
from PyQt5.QtGui import QPixmap, QIcon
from firstPage.ges2simCode import ges2code
from myoLib.train_thread import TrainTread
from myoLib.classTrainFile import Classify_Txt

pg.setConfigOptions(leftButtonPan=False)

rawpath = myoRawPath()
linkpath = myoPath()


class Win0(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.skipBtn.clicked.connect(self.skipFunc)
        self.ui.predictBtn.clicked.connect(self.skipFunc)

        init_Pics()
        self.setWindowTitle('goMYO')
        self.setWindowIcon(QIcon(linkpath + r'\logo_png.png'))

        self.screen = QDesktopWidget().screenGeometry()
        sizeF = self.geometry()
        self.move((self.screen.width() - sizeF.width()) / 2,
                  (self.screen.height() - sizeF.height()) / 2)

        self.timer = QTimer(self)
        self.emgcurve = []

        self.myo = None
        self.plotEMG()
        self.initUI()
        self.showPics()

        self.fileNum = 5
        self.transTag = 0
        self.fileName = ''

        self.reSaveTag = 0
        self.didHist = []

    def initUI(self):
        self.ui.connectBtn.clicked.connect(self.connection)
        self.ui.startBtn.clicked.connect(self.start)
        self.ui.saveBtn.clicked.connect(self.pause_sample)
        self.ui.disConnectBtn.clicked.connect(self.disconnection)
        self.ui.openDir.clicked.connect(self.openDir)
        self.ui.nextBtn.clicked.connect(self.nextTab)

        self.ui.againBtn.clicked.connect(self.reSave)
        self.ui.trainBtn.clicked.connect(self.train)

    def showPics(self):
        self.thumb = QPixmap(linkpath + r'\thumb_png.png')
        self.six = QPixmap(linkpath + r'\six_png.png')
        self.ok = QPixmap(linkpath + r'\ok_png.png')
        self.peace = QPixmap(linkpath + r'\peace_png.png')
        self.adduct = QPixmap(linkpath + r'\adduct_png.png')
        self.abduct = QPixmap(linkpath + r'\abduct_png.png')
        self.ring = QPixmap(linkpath + r'\ring_png.png')
        self.fist = QPixmap(linkpath + r'\fist_png.png')
        self.waveIn = QPixmap(linkpath + r'\waveIn_png.png')
        self.waveOut = QPixmap(linkpath + r'\waveOut_png.png')
        self.seven = QPixmap(linkpath + r'\seven_png.png')
        self.relax = QPixmap(linkpath + r'\relax_png.png')

        self.ui.tLabel.setPixmap(self.thumb)
        self.ui.xLabel.setPixmap(self.six)
        self.ui.kLabel.setPixmap(self.ok)
        self.ui.pLabel.setPixmap(self.peace)
        self.ui.adLabel.setPixmap(self.adduct)
        self.ui.abLabel.setPixmap(self.abduct)
        self.ui.gLabel.setPixmap(self.ring)
        self.ui.fLabel.setPixmap(self.fist)
        self.ui.iLabel.setPixmap(self.waveIn)
        self.ui.oLabel.setPixmap(self.waveOut)
        self.ui.vLabel.setPixmap(self.seven)
        self.ui.rLabel.setPixmap(self.relax)

    def skipFunc(self):
        self.hide()
        self.s = Win1()
        sizeS = self.s.geometry()
        self.s.move((self.screen.width() - sizeS.width()) / 2,
                    (self.screen.height() - sizeS.height()) / 2)
        self.s.show()
        self.s.ui.msgBrowser.append(' .............goMyo Started............. \n ')
        self.s.ui.msgBrowser.append(f"All pics have been saved in:\n{linkpath} ")

    def train(self):
        Classify_Txt()
        self.ui.remindLabel.setText('Training an artificial neural network...')
        self.ui.msgBrowser.append('Training an artificial neural network...')
        self.work = TrainTread()
        self.work.signals.connect(self.remindMsg)
        self.work.start()

    def remindMsg(self):
        self.ui.msgBrowser.append("The trained classifier has been created.")
        self.ui.remindLabel.setText("The trained classifier has been created.")

    def nextTab(self):
        if self.transTag == 0:
            self.currentTab = self.ui.setWidget.currentIndex()
            self.ui.codeLabel.setText("GO MYO")
            self.currentTab += 1
            self.ui.setWidget.setCurrentIndex(self.currentTab)
            self.transTag = 1

        if self.transTag == 1:
            self.ui.nextBtn.setEnabled(False)

            gesName = ges2code().outer(self.currentTab)
            if gesName == 'stop':
                self.ui.codeLabel.setText("GO MYO")
                QTimer.singleShot(500, self.disconnection)
                return
            self.ui.codeLabel.setText(f"Waiting for \n{gesName} - {self.fileNum}\n please press ALT to save")
            self.fileName = gesName + '-' + str(self.fileNum)
            self.didHist.append(self.fileName)

            self.fileNum -= 1
            if self.fileNum == 0:
                self.fileNum = 5
                self.transTag = 0

    def plotEMG(self):
        self.emgplot = pg.PlotWidget(name='EMGplot')
        self.emg_data_queue = deque(maxlen=400)
        self.emgplot.setXRange(0, 400)
        self.emgplot.setYRange(0, 3000)

        self.ui.graph_layout.addWidget(self.emgplot)
        for i in range(8):
            c = self.emgplot.plot(pen=(i, 10))
            c.setPos(0, i * 400)

            self.emgcurve.append(c)

    def connection(self):
        self.ui.remindLabel.setText("")
        self.ui.msgBrowser.append("Trying to connect to Myo (connection will timeout in 5 seconds)." + '\n')
        if not self.myo:
            self.myo = MyoManager(sender=self)

        if not self.myo.connected:
            self.myo.connect()

    def disconnection(self):
        self.timer.stop()

        self.ui.connectBtn.setEnabled(True)
        self.ui.disConnectBtn.setEnabled(False)
        self.ui.startBtn.setEnabled(False)
        self.ui.saveBtn.setEnabled(False)

        self.ui.msgBrowser.append("Disconnected from Myo." + '\n')

        if self.myo:
            if self.myo.connected:
                self.myo.disconnect()

    def start(self):
        if self.ui.startBtn.isEnabled():
            self.ui.startBtn.setEnabled(False)
            self.ui.saveBtn.setEnabled(True)

        self.timer_start()

    def timer_start(self):
        self.timer.timeout.connect(self.update_plots_emg)
        self.timer.start()

    def callback(self, dictMsg):
        typeEvt = dictMsg["type"]
        dataEvt = dictMsg["data"]

        if typeEvt == EventType.battery_level:
            self.ui.betteryBar.setValue(dataEvt["battery"])

        if typeEvt == EventType.rssi:
            self.ui.rssiBar.setValue(-dataEvt["rssi"])

        if typeEvt == EventType.connected:
            self.ui.msgBrowser.append("Connected to "
                                      + repr(dataEvt["name"])
                                      + "with mac address: "
                                      + repr(dataEvt["mac_address"])
                                      + '. \n')

            self.ui.connectBtn.setEnabled(False)
            self.ui.disConnectBtn.setEnabled(True)
            self.ui.startBtn.setEnabled(True)
            self.ui.saveBtn.setEnabled(False)

        elif typeEvt == EventType.disconnected:
            if dataEvt["timeout"]:
                self.ui.msgBrowser.append("Connection timed out!" + '\n')
                self.disconnection()

            if dataEvt["unOpenMyo"]:
                self.ui.msgBrowser.append("Unable to connect to Myo Connect. Is Myo Connect running?" + '\n')
                self.disconnection()

        elif typeEvt == EventType.emg:
            self.emg_data_queue.append(dataEvt["emg"])

    def pause_sample(self):
        if self.myo.connected:
            self.timer.stop()
            self.ui.startBtn.setEnabled(True)
            self.ui.saveBtn.setEnabled(False)
            try:
                self.saveEmgFile()
            except:
                self.ui.msgBrowser.append('Please follow the procedure as operating. \n')
                self.disconnection()

    def openDir(self):
        os.system(f"start explorer {linkpath}")

    def update_plots_emg(self):
        buffer0 = []
        buffer1 = []
        buffer2 = []
        buffer3 = []
        buffer4 = []
        buffer5 = []
        buffer6 = []
        buffer7 = []
        emgSolve = self.emg_data_queue
        for emg in emgSolve:
            buffer0.append(emg[0])
            buffer1.append(emg[1])
            buffer2.append(emg[2])
            buffer3.append(emg[3])
            buffer4.append(emg[4])
            buffer5.append(emg[5])
            buffer6.append(emg[6])
            buffer7.append(emg[7])
        all_buffer = [buffer7, buffer6, buffer5, buffer4, buffer3, buffer2, buffer1, buffer0]
        for i in range(8):
            self.emgcurve[i].setData(all_buffer[i])

        del all_buffer
        QApplication.processEvents()

        return emgSolve

    def recognizeEmg(self):
        emg_data = self.update_plots_emg()
        emg_data = np.array([x for x in emg_data]).T

        new = []
        count = 0
        for i in emg_data.flatten('A').tolist():
            new.append(i)
            count += 1
            new.append('\t')
            if count % 8 == 0:
                new.append('\n')

        new = ''.join('%s' % k for k in new)  # surprise code.

        return new

    def saveEmgFile(self):
        new = self.recognizeEmg()
        with open(rawpath + '\\' + self.fileName + '.txt', 'w') as f:
            f.write("{}".format(new))

        self.ui.msgBrowser.append('Success in saving: \n' + self.fileName + '.txt \n')
        if self.reSaveTag == 0:
            self.nextTab()

        time.sleep(0.5)
        self.start()

    def reSave(self):
        self.reSaveTag = 1
        self.fileName = self.didHist[-2]
        self.ui.codeLabel.setText(f"Re_Saving for \n{self.fileName}.txt\n please press ALT to save")

    def reSaveAfter(self):
        self.pause_sample()
        self.reSaveTag = 0
        self.fileName = self.didHist[-1]
        self.ui.codeLabel.setText(f"Waiting for \n{self.fileName}.txt\n please press ALT to save")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Alt:
            if self.reSaveTag == 0:
                self.pause_sample()
            else:
                self.reSaveAfter()
