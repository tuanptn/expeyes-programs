# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scope.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 533)
        MainWindow.setStyleSheet("QSlider::groove:vertical{\n"
"    border: 1px solid #565a5e;\n"
"    width: 10px;\n"
"    background: #eee;\n"
"    margin: 0px;\n"
"    border-radius: 4px;\n"
"}\n"
"QSlider::handle:vertical{\n"
"    background: red;\n"
"    border: 1px solid #565a5e;\n"
"    width: 5px;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(138, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 0, 1, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalSlider = QtWidgets.QSlider(self.layoutWidget)
        self.verticalSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.verticalSlider.setMinimum(-100)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout.addWidget(self.verticalSlider)
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.graphPosition = PlotWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphPosition.sizePolicy().hasHeightForWidth())
        self.graphPosition.setSizePolicy(sizePolicy)
        self.graphPosition.setObjectName("graphPosition")
        self.frame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(250, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gaugeLayout = QtWidgets.QGridLayout(self.frame)
        self.gaugeLayout.setContentsMargins(1, 1, 1, 1)
        self.gaugeLayout.setSpacing(2)
        self.gaugeLayout.setObjectName("gaugeLayout")
        self.horizontalLayout.addWidget(self.splitter)
        self.frame_2 = QtWidgets.QFrame(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(2, 2, 2, 2)
        self.formLayout.setSpacing(2)
        self.formLayout.setObjectName("formLayout")
        self.A1 = QtWidgets.QCheckBox(self.frame_3)
        self.A1.setText("")
        self.A1.setObjectName("A1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.A1)
        self.A1Results = QtWidgets.QLabel(self.frame_3)
        self.A1Results.setObjectName("A1Results")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.A1Results)
        self.A1Map = QtWidgets.QComboBox(self.frame_3)
        self.A1Map.setObjectName("A1Map")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.A1Map)
        self.A1Fit = QtWidgets.QCheckBox(self.frame_3)
        self.A1Fit.setObjectName("A1Fit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.A1Fit)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.A2 = QtWidgets.QCheckBox(self.frame_4)
        self.A2.setObjectName("A2")
        self.verticalLayout.addWidget(self.A2)
        self.A2Fit = QtWidgets.QCheckBox(self.frame_4)
        self.A2Fit.setObjectName("A2Fit")
        self.verticalLayout.addWidget(self.A2Fit)
        self.A2Results = QtWidgets.QLabel(self.frame_4)
        self.A2Results.setObjectName("A2Results")
        self.verticalLayout.addWidget(self.A2Results)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.A3 = QtWidgets.QCheckBox(self.frame_5)
        self.A3.setObjectName("A3")
        self.verticalLayout_2.addWidget(self.A3)
        self.A3Fit = QtWidgets.QCheckBox(self.frame_5)
        self.A3Fit.setObjectName("A3Fit")
        self.verticalLayout_2.addWidget(self.A3Fit)
        self.A3Results = QtWidgets.QLabel(self.frame_5)
        self.A3Results.setObjectName("A3Results")
        self.verticalLayout_2.addWidget(self.A3Results)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.line_3 = QtWidgets.QFrame(self.frame_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.MIC = QtWidgets.QCheckBox(self.frame_6)
        self.MIC.setObjectName("MIC")
        self.verticalLayout_3.addWidget(self.MIC)
        self.MICFit = QtWidgets.QCheckBox(self.frame_6)
        self.MICFit.setObjectName("MICFit")
        self.verticalLayout_3.addWidget(self.MICFit)
        self.MICResults = QtWidgets.QLabel(self.frame_6)
        self.MICResults.setObjectName("MICResults")
        self.verticalLayout_3.addWidget(self.MICResults)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.line_4 = QtWidgets.QFrame(self.frame_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_2.addWidget(self.line_4)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_7)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.pushButton_4)
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider_2.setMinimum(5)
        self.horizontalSlider_2.setMaximum(5000)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout_2.addWidget(self.horizontalSlider_2)
        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(40, 0))
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.horizontalSlider_2.valueChanged['int'].connect(MainWindow.set_sine)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.A1Results.setText(_translate("MainWindow", "."))
        self.A1Fit.setText(_translate("MainWindow", "Fit"))
        self.A2.setText(_translate("MainWindow", "A2"))
        self.A2Fit.setText(_translate("MainWindow", "Fit"))
        self.A2Results.setText(_translate("MainWindow", "."))
        self.A3.setText(_translate("MainWindow", "A3"))
        self.A3Fit.setText(_translate("MainWindow", "Fit"))
        self.A3Results.setText(_translate("MainWindow", "."))
        self.MIC.setText(_translate("MainWindow", "MIC"))
        self.MICFit.setText(_translate("MainWindow", "Fit"))
        self.MICResults.setText(_translate("MainWindow", "."))
        self.pushButton.setText(_translate("MainWindow", "Cap(IN1) ?"))
        self.label_2.setText(_translate("MainWindow", "C ="))
        self.pushButton_4.setText(_translate("MainWindow", "Freq(IN2) ?"))
        self.label_7.setText(_translate("MainWindow", "F = . Hz"))
        self.label.setText(_translate("MainWindow", "1mS"))

from pyqtgraph import PlotWidget