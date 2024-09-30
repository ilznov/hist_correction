from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from histogram import Histogram
from compare_mathods import compareMathods

import math
import cv2 as cv
import numpy as np




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 623)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 623))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_Original = QtWidgets.QLabel(self.centralwidget, alignment=Qt.AlignCenter)
        self.label_Original.setMinimumSize(QtCore.QSize(350, 350))
        self.label_Original.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_Original.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"\n"
"")
        self.label_Original.setText("")
        self.label_Original.setObjectName("label_Original")
        self.horizontalLayout_8.addWidget(self.label_Original)
        self.label_Edit = QtWidgets.QLabel(self.centralwidget, alignment=Qt.AlignCenter)
        self.label_Edit.setMinimumSize(QtCore.QSize(350, 350))
        self.label_Edit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_Edit.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"")
        self.label_Edit.setText("")
        self.label_Edit.setObjectName("label_Edit")
        self.horizontalLayout_8.addWidget(self.label_Edit)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setMinimumSize(QtCore.QSize(420, 550))
        self.groupBox.setMaximumSize(QtCore.QSize(420, 16777215))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_Histogram = Histogram(self.groupBox)
        self.label_Histogram.setMinimumSize(QtCore.QSize(420, 200))
        self.label_Histogram.setMaximumSize(QtCore.QSize(420, 200))
        self.label_Histogram.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"")
        self.label_Histogram.setProperty("text", "")
        self.label_Histogram.setObjectName("label_Histogram")
        self.verticalLayout_2.addWidget(self.label_Histogram)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_Dark = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Dark.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_Dark.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Dark.setFont(font)
        self.pushButton_Dark.setObjectName("pushButton_Dark")
        self.horizontalLayout_2.addWidget(self.pushButton_Dark)
        self.spinBox_Dark = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_Dark.setMinimumSize(QtCore.QSize(50, 30))
        self.spinBox_Dark.setMaximumSize(QtCore.QSize(50, 30))
        self.spinBox_Dark.setSizeIncrement(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_Dark.setFont(font)
        self.spinBox_Dark.setMinimum(1)
        self.spinBox_Dark.setMaximum(10)
        self.spinBox_Dark.setObjectName("spinBox_max")
        self.horizontalLayout_2.addWidget(self.spinBox_Dark)
        spacerItem1 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_Bright = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Bright.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_Bright.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Bright.setFont(font)
        self.pushButton_Bright.setObjectName("pushButton_Bright")
        self.horizontalLayout_3.addWidget(self.pushButton_Bright)
        self.spinBox_Bright = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_Bright.setMinimumSize(QtCore.QSize(50, 30))
        self.spinBox_Bright.setMaximumSize(QtCore.QSize(50, 30))
        self.spinBox_Bright.setSizeIncrement(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_Bright.setFont(font)
        self.spinBox_Bright.setMinimum(1)
        self.spinBox_Bright.setMaximum(10)
        self.spinBox_Bright.setObjectName("spinBox_min")
        self.horizontalLayout_3.addWidget(self.spinBox_Bright)
        spacerItem3 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.pushButton_Linear_correction = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Linear_correction.setMinimumSize(QtCore.QSize(300, 50))
        self.pushButton_Linear_correction.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Linear_correction.setFont(font)
        self.pushButton_Linear_correction.setObjectName("pushButton_Linear_correction")
        self.horizontalLayout_4.addWidget(self.pushButton_Linear_correction)
        spacerItem5 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.pushButton_Histogram_Equalization = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Histogram_Equalization.setMinimumSize(QtCore.QSize(300, 50))
        self.pushButton_Histogram_Equalization.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Histogram_Equalization.setFont(font)
        self.pushButton_Histogram_Equalization.setObjectName("pushButton_Histogram_Equalization")
        self.horizontalLayout_5.addWidget(self.pushButton_Histogram_Equalization)
        spacerItem7 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.pushButton_Adaptive_Histogram_Equalization = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Adaptive_Histogram_Equalization.setMinimumSize(QtCore.QSize(300, 50))
        self.pushButton_Adaptive_Histogram_Equalization.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Adaptive_Histogram_Equalization.setFont(font)
        self.pushButton_Adaptive_Histogram_Equalization.setObjectName("pushButton_Adaptive_Histogram_Equalization")
        self.horizontalLayout_6.addWidget(self.pushButton_Adaptive_Histogram_Equalization)
        spacerItem9 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem10 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.pushButton_Compare_Methods = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Compare_Methods.setMinimumSize(QtCore.QSize(300, 50))
        self.pushButton_Compare_Methods.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Compare_Methods.setFont(font)
        self.pushButton_Compare_Methods.setObjectName("pushButton_Compare_Methods")
        self.horizontalLayout_7.addWidget(self.pushButton_Compare_Methods)
        spacerItem11 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 1, 0, 1, 1)
        self.horizontalLayout_9.addWidget(self.groupBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.actionOpen.triggered.connect(self.loadImage)
        self.actionSave.triggered.connect(self.savePhoto)
        self.actionExit.triggered.connect(sys.exit)

        self.pushButton_Linear_correction.clicked.connect(
            self.pushButton_Linear_correction_Clicked)
        self.pushButton_Histogram_Equalization.clicked.connect(
            self.pushButton_Hist_Equalization_Clicked)
        self.pushButton_Adaptive_Histogram_Equalization.clicked.connect(
            self.pushButton_Adaptive_Histogram_Equalization_Clicked)


        self.pushButton_Compare_Methods.clicked.connect(
            self.pushButton_Compare_Mathods_Clicked)
        
        self.spinBox_Dark.valueChanged["int"].connect(self.get_Dark_value)
        self.spinBox_Bright.valueChanged["int"].connect(self.get_Bright_value)

        
        self.pushButton_Dark.clicked.connect(self.pushButton_Dark_Clicked)
        self.pushButton_Bright.clicked.connect(self.pushButton_Bright_Clicked)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Dark_value = 1
        self.Bright_value = 1
        self.filename = None
        self.filename_save = None
        self.result = None


    def loadImage(self):
        """ This function will load the user selected image
            and set it to label using the setPhoto function
        """
        try:
            self.clean()
            self.filename = QFileDialog.getOpenFileName(
                filter="Image (*.*)")[0]
            str(self.filename)
            f = open(self.filename, "rb")
            chunk = f.read()
            chunk_arr = np.frombuffer(chunk, dtype=np.uint8)
            self.image = cv.imdecode(chunk_arr, cv.IMREAD_COLOR)
            f.close()
            tmp = self.checkSizeImage(self.image, self.label_Original)
            self.setPhoto(tmp)
            tmp = self.checkSizeImage(self.image, self.label_Edit)
            self.setPhoto(tmp, 0)
            self.result = self.image
            self.show_histogram(self.image)
        except:
            None

    def clean(self):
        self.label_Edit.clear()

    def setPhoto(self, image, check=1):
        """ This function will take image input and resize it
            only for display purpose and convert it to QImage
            to set at the label.
        """
        frame = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = QImage(
            frame,
            frame.shape[1],
            frame.shape[0],
            frame.strides[0],
            QImage.Format_RGB888)
        if check == 1:
            self.label_Original.setPixmap(QtGui.QPixmap.fromImage(image))
        else:
            self.label_Edit.setPixmap(QtGui.QPixmap.fromImage(image))

    def savePhoto(self):
        """ This function will save the result.
        """
        try:
            self.filename_save = QFileDialog.getSaveFileName(
                filter="png Image (*.png)"
            )[0]
            try:
                _, im_buf_arr = cv.imencode(".jpg", self.result_correction)
            except:
                _, im_buf_arr = cv.imencode(".jpg", self.result)
            im_buf_arr.tofile(self.filename_save)
        except:
            self.errorSavePhoto()



    def errorSavePhoto(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("ERROR")
        msg.setText(
            "You have not edited the image or you have not uploaded the image!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def checkImage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("ERROR")
        msg.setText("You have not select a file!!!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def checkSizeImage(self, image, label):
        """ This function will check the image's size
            and scale the image to fit window
        """
        height, width = image.shape[:2]
        if height >= width:
            k = label.height() / height
            height = int(image.shape[0]*k)
            width = int(image.shape[1]*k)
        elif width > height:
            k = label.width() / width
            height = int(image.shape[0]*k)
            width = int(image.shape[1]*k)
        math.floor(height)
        math.floor(width)
        return cv.resize(image, (width, height), interpolation=cv.INTER_AREA)


    def pushButton_Linear_correction_Clicked(self):
        try:
            self.result_correction = self.linear_correction(self.result)
            tmp = self.checkSizeImage(self.result_correction, self.label_Edit)
            self.setPhoto(tmp, 0)
            self.show_histogram(self.result_correction)
        except:
            self.checkImage()

    def pushButton_Hist_Equalization_Clicked(self):
        try:
        #     self.result_correction = self.equalize_Hist_cv(self.image)
            self.result_correction = self.histogram_equalization(self.result)
            # self.result_correction = self.adaptive_histogram_equalization_cv(self.result)
        #     self.result_correction = self.adaptive_histogram_equalization(self.result)
            tmp = self.checkSizeImage(self.result_correction, self.label_Edit)
            self.setPhoto(tmp, 0)
            self.show_histogram(self.result_correction)
        except:
            self.checkImage()

    def pushButton_Adaptive_Histogram_Equalization_Clicked(self):
        try:
            # self.result_correction = self.adaptive_histogram_equalization(self.result)
            self.result_correction = self.adaptive_histogram_equalization_cv(self.result)
            tmp = self.checkSizeImage(self.result_correction, self.label_Edit)
            self.setPhoto(tmp, 0)
            self.show_histogram(self.result_correction)
        except:
            self.checkImage()        

    def pushButton_Compare_Mathods_Clicked(self):
        try:
            compareMathods(self.result)
        except:
            self.checkImage()
    
    def get_Dark_value(self, value):
        self.Dark_value = value

    def get_Bright_value(self, value):
        self.Bright_value = value

    def pushButton_Dark_Clicked(self, value):
        try:
            value=self.Dark_value/10
            self.result = cv.convertScaleAbs(self.image, alpha=value, beta=0)
            tmp = self.checkSizeImage(self.result, self.label_Edit)
            self.setPhoto(tmp, 0)
            self.setPhoto(tmp, 1)
            self.show_histogram(self.result)
        except:
            self.checkImage()

    def pushButton_Bright_Clicked(self):
        try:
            value=self.Bright_value/10 + 1
            self.result = cv.convertScaleAbs(self.image, alpha=value, beta=0)
            tmp = self.checkSizeImage(self.result, self.label_Edit)
            self.setPhoto(tmp, 0)
            self.setPhoto(tmp, 1)
            self.show_histogram(self.result)
        except:
            self.checkImage()

    def show_histogram(self, img):
        try:
            self.label_Histogram.canvas.axes.clear()
            self.label_Histogram.canvas.axes.axis("off")
            self.label_Histogram.canvas.axes.hist(img.ravel(), 256, [0, 256])
            self.label_Histogram.canvas.axes.grid()
            self.label_Histogram.canvas.draw()
        except:
            self.checkImage()

    def linear_correction(self, image):
        img = self.check_Grayscale(image)
        H, W = img.shape[:2]
        min_val = np.min(img)
        max_val = np.max(img)

        for i in range(H):
            for j in range(W):
                img[i, j] = ((img[i, j] - min_val) / (max_val - min_val)) * 255

        return img

    def equalize_Hist_cv(self, img):
        GrayImage = self.check_Grayscale(img)
        return(cv.equalizeHist(GrayImage))
    
    def histogram_equalization(self, img):
        image = self.check_Grayscale(img)
        # Розрахунок гістограми
        hist, _ = np.histogram(image.flatten(), 256, [0, 256])
        cdf = hist.cumsum()  # розрахунок кумулятивної суми гістограми
        cdf = (cdf - cdf.min())*255/(cdf.max()-cdf.min())  # нормалізація CDF
        cdf = cdf.astype('uint8')  # перетворення типу на 'uint8'

        # Застосування CDF для виконання еквалізації гістограми
        img_equalized = cv.LUT(image, cdf)

        return img_equalized
    
    def adaptive_histogram_equalization_cv(self, img):
        image = self.check_Grayscale(img)
        clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

        # Застосування адаптивного вирівнювання гістограми
        clahe_image = clahe.apply(image)
        return clahe_image
    
    def adaptive_histogram_equalization(self, image, grid_size=(8, 8)):
        image = self.check_Grayscale(image)
        h, w = image.shape
        # Крок 1: Розбиття зображення на блоки
        block_h = h // grid_size[0]
        block_w = w // grid_size[1]

        # Створюємо порожню матрицю для нового зображення
        equalized_image = np.zeros_like(image)

        def manual_histogram_equalization(block):
            # Аналог глобального вирівнювання гістограми для кожного блоку
            hist = np.zeros(256)
            for pixel in block.flatten():
                    hist[pixel] += 1

            cdf = hist.cumsum()
            cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())

            equalized_block = np.interp(block.flatten(), range(0, 256), cdf_normalized).reshape(block.shape).astype(np.uint8)
            
            return equalized_block

        # Проходимо по кожному блоку і застосовуємо вирівнювання гістограми
        for i in range(0, h, block_h):
            for j in range(0, w, block_w):
                # Виділяємо блок зображення
                block = image[i:i+block_h, j:j+block_w]

                # Викликаємо функцію для вирівнювання гістограми для блоку
                block_equalized = manual_histogram_equalization(block)

                # Записуємо оброблений блок назад у результуюче зображення
                equalized_image[i:i+block_h, j:j+block_w] = block_equalized

        return equalized_image

    def check_Grayscale(self, img):
        if len(img.shape) == 2:
            out = np.copy(img)
        else:
            out = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return out



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Dark.setText(_translate("MainWindow", "Dark"))
        self.pushButton_Bright.setText(_translate("MainWindow", "Bright"))
        self.pushButton_Linear_correction.setText(_translate("MainWindow", "Linear correction"))
        self.pushButton_Histogram_Equalization.setText(_translate("MainWindow", "Histogram equalization"))
        self.pushButton_Adaptive_Histogram_Equalization.setText(_translate("MainWindow", "Adaptive Histogram equalization"))
        self.pushButton_Compare_Methods.setText(_translate("MainWindow", "Compare Methods"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
