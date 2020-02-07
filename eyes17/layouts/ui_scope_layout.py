# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scope_layout.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(857, 548)
        Form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.Diff = QtWidgets.QCheckBox(Form)
        self.Diff.setMaximumSize(QtCore.QSize(60, 16777215))
        self.Diff.setObjectName("Diff")
        self.gridLayout.addWidget(self.Diff, 1, 3, 1, 1)
        self.msgwin = QtWidgets.QLabel(Form)
        self.msgwin.setObjectName("msgwin")
        self.gridLayout.addWidget(self.msgwin, 1, 0, 1, 2)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pwin = PlotWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(90)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwin.sizePolicy().hasHeightForWidth())
        self.pwin.setSizePolicy(sizePolicy)
        self.pwin.setObjectName("pwin")
        self.frame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 5)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.A1Range = QtWidgets.QComboBox(self.frame_4)
        self.A1Range.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.A1Range.setFont(font)
        self.A1Range.setObjectName("A1Range")
        self.A1Range.addItem("")
        self.A1Range.addItem("")
        self.A1Range.addItem("")
        self.A1Range.addItem("")
        self.A1Range.addItem("")
        self.A1Range.addItem("")
        self.gridLayout_4.addWidget(self.A1Range, 0, 2, 1, 1)
        self.A2Fit = QtWidgets.QCheckBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A2Fit.sizePolicy().hasHeightForWidth())
        self.A2Fit.setSizePolicy(sizePolicy)
        self.A2Fit.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.A2Fit.setFont(font)
        self.A2Fit.setText("")
        self.A2Fit.setObjectName("A2Fit")
        self.gridLayout_4.addWidget(self.A2Fit, 1, 3, 1, 1)
        self.MICFit = QtWidgets.QCheckBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MICFit.sizePolicy().hasHeightForWidth())
        self.MICFit.setSizePolicy(sizePolicy)
        self.MICFit.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.MICFit.setFont(font)
        self.MICFit.setText("")
        self.MICFit.setObjectName("MICFit")
        self.gridLayout_4.addWidget(self.MICFit, 3, 3, 1, 1)
        self.A3Fit = QtWidgets.QCheckBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A3Fit.sizePolicy().hasHeightForWidth())
        self.A3Fit.setSizePolicy(sizePolicy)
        self.A3Fit.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.A3Fit.setFont(font)
        self.A3Fit.setText("")
        self.A3Fit.setObjectName("A3Fit")
        self.gridLayout_4.addWidget(self.A3Fit, 2, 3, 1, 1)
        self.MICBox = QtWidgets.QCheckBox(self.frame_4)
        self.MICBox.setObjectName("MICBox")
        self.gridLayout_4.addWidget(self.MICBox, 3, 0, 1, 2)
        self.A2Range = QtWidgets.QComboBox(self.frame_4)
        self.A2Range.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.A2Range.setFont(font)
        self.A2Range.setObjectName("A2Range")
        self.A2Range.addItem("")
        self.A2Range.addItem("")
        self.A2Range.addItem("")
        self.A2Range.addItem("")
        self.A2Range.addItem("")
        self.A2Range.addItem("")
        self.gridLayout_4.addWidget(self.A2Range, 1, 2, 1, 1)
        self.A1Map = QtWidgets.QComboBox(self.frame_4)
        self.A1Map.setMaximumSize(QtCore.QSize(55, 16777215))
        self.A1Map.setObjectName("A1Map")
        self.gridLayout_4.addWidget(self.A1Map, 0, 1, 1, 1)
        self.A1Fit = QtWidgets.QCheckBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A1Fit.sizePolicy().hasHeightForWidth())
        self.A1Fit.setSizePolicy(sizePolicy)
        self.A1Fit.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.A1Fit.setFont(font)
        self.A1Fit.setText("")
        self.A1Fit.setObjectName("A1Fit")
        self.gridLayout_4.addWidget(self.A1Fit, 0, 3, 1, 1)
        self.A2Box = QtWidgets.QCheckBox(self.frame_4)
        self.A2Box.setObjectName("A2Box")
        self.gridLayout_4.addWidget(self.A2Box, 1, 0, 1, 2)
        self.MICRange = QtWidgets.QComboBox(self.frame_4)
        self.MICRange.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.MICRange.setFont(font)
        self.MICRange.setObjectName("MICRange")
        self.MICRange.addItem("")
        self.MICRange.addItem("")
        self.MICRange.addItem("")
        self.MICRange.addItem("")
        self.gridLayout_4.addWidget(self.MICRange, 3, 2, 1, 1)
        self.A3Box = QtWidgets.QCheckBox(self.frame_4)
        self.A3Box.setObjectName("A3Box")
        self.gridLayout_4.addWidget(self.A3Box, 2, 0, 1, 2)
        self.A1Box = QtWidgets.QCheckBox(self.frame_4)
        self.A1Box.setText("")
        self.A1Box.setObjectName("A1Box")
        self.gridLayout_4.addWidget(self.A1Box, 0, 0, 1, 1)
        self.A3Range = QtWidgets.QComboBox(self.frame_4)
        self.A3Range.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.A3Range.setFont(font)
        self.A3Range.setObjectName("A3Range")
        self.A3Range.addItem("")
        self.A3Range.addItem("")
        self.A3Range.addItem("")
        self.A3Range.addItem("")
        self.gridLayout_4.addWidget(self.A3Range, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 13, 1, 1, 4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pcsFrame = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pcsFrame.sizePolicy().hasHeightForWidth())
        self.pcsFrame.setSizePolicy(sizePolicy)
        self.pcsFrame.setMinimumSize(QtCore.QSize(0, 36))
        self.pcsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pcsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pcsFrame.setObjectName("pcsFrame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.pcsFrame)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setHorizontalSpacing(3)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pcsVal = QtWidgets.QLCDNumber(self.pcsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pcsVal.sizePolicy().hasHeightForWidth())
        self.pcsVal.setSizePolicy(sizePolicy)
        self.pcsVal.setAutoFillBackground(False)
        self.pcsVal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pcsVal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pcsVal.setSmallDecimalPoint(False)
        self.pcsVal.setDigitCount(4)
        self.pcsVal.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.pcsVal.setObjectName("pcsVal")
        self.gridLayout_6.addWidget(self.pcsVal, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.pcsFrame)
        self.label.setMinimumSize(QtCore.QSize(0, 15))
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.pcsFrame)
        self.label_3.setMinimumSize(QtCore.QSize(0, 15))
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)
        self.pcsVal_I = QtWidgets.QLCDNumber(self.pcsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pcsVal_I.sizePolicy().hasHeightForWidth())
        self.pcsVal_I.setSizePolicy(sizePolicy)
        self.pcsVal_I.setAutoFillBackground(False)
        self.pcsVal_I.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pcsVal_I.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pcsVal_I.setSmallDecimalPoint(False)
        self.pcsVal_I.setDigitCount(4)
        self.pcsVal_I.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.pcsVal_I.setObjectName("pcsVal_I")
        self.gridLayout_6.addWidget(self.pcsVal_I, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.pcsFrame, 4, 0, 1, 5)
        self.PV2text = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.PV2text.setMaximumSize(QtCore.QSize(150, 16777215))
        self.PV2text.setMinimum(-3.0)
        self.PV2text.setMaximum(3.0)
        self.PV2text.setObjectName("PV2text")
        self.gridLayout_3.addWidget(self.PV2text, 3, 3, 1, 2)
        self.PV1Label = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PV1Label.sizePolicy().hasHeightForWidth())
        self.PV1Label.setSizePolicy(sizePolicy)
        self.PV1Label.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.PV1Label.setFont(font)
        self.PV1Label.setObjectName("PV1Label")
        self.gridLayout_3.addWidget(self.PV1Label, 2, 0, 1, 1)
        self.PV2slider = QtWidgets.QSlider(self.frame_3)
        self.PV2slider.setMinimum(-3300)
        self.PV2slider.setMaximum(3300)
        self.PV2slider.setOrientation(QtCore.Qt.Horizontal)
        self.PV2slider.setObjectName("PV2slider")
        self.gridLayout_3.addWidget(self.PV2slider, 3, 1, 1, 2)
        self.PV1slider = QtWidgets.QSlider(self.frame_3)
        self.PV1slider.setMinimum(-5000)
        self.PV1slider.setMaximum(5000)
        self.PV1slider.setProperty("value", 0)
        self.PV1slider.setOrientation(QtCore.Qt.Horizontal)
        self.PV1slider.setObjectName("PV1slider")
        self.gridLayout_3.addWidget(self.PV1slider, 2, 1, 1, 2)
        self.PV1text = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.PV1text.setMaximumSize(QtCore.QSize(150, 16777215))
        self.PV1text.setMinimum(-5.0)
        self.PV1text.setMaximum(5.0)
        self.PV1text.setObjectName("PV1text")
        self.gridLayout_3.addWidget(self.PV1text, 2, 3, 1, 2)
        self.SQ1Label = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQ1Label.sizePolicy().hasHeightForWidth())
        self.SQ1Label.setSizePolicy(sizePolicy)
        self.SQ1Label.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.SQ1Label.setFont(font)
        self.SQ1Label.setObjectName("SQ1Label")
        self.gridLayout_3.addWidget(self.SQ1Label, 1, 0, 1, 1)
        self.SQ1DCtext = QtWidgets.QSpinBox(self.frame_3)
        self.SQ1DCtext.setMaximumSize(QtCore.QSize(55, 16777215))
        self.SQ1DCtext.setProperty("value", 50)
        self.SQ1DCtext.setObjectName("SQ1DCtext")
        self.gridLayout_3.addWidget(self.SQ1DCtext, 1, 4, 1, 1)
        self.AWGslider = QtWidgets.QSlider(self.frame_3)
        self.AWGslider.setMinimum(5)
        self.AWGslider.setMaximum(5000)
        self.AWGslider.setOrientation(QtCore.Qt.Horizontal)
        self.AWGslider.setObjectName("AWGslider")
        self.gridLayout_3.addWidget(self.AWGslider, 0, 1, 1, 2)
        self.PV2Label = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PV2Label.sizePolicy().hasHeightForWidth())
        self.PV2Label.setSizePolicy(sizePolicy)
        self.PV2Label.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.PV2Label.setFont(font)
        self.PV2Label.setObjectName("PV2Label")
        self.gridLayout_3.addWidget(self.PV2Label, 3, 0, 1, 1)
        self.SQ1slider = QtWidgets.QSlider(self.frame_3)
        self.SQ1slider.setMinimum(0)
        self.SQ1slider.setMaximum(50000)
        self.SQ1slider.setSliderPosition(1000)
        self.SQ1slider.setOrientation(QtCore.Qt.Horizontal)
        self.SQ1slider.setObjectName("SQ1slider")
        self.gridLayout_3.addWidget(self.SQ1slider, 1, 1, 1, 1)
        self.WGLabel = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WGLabel.sizePolicy().hasHeightForWidth())
        self.WGLabel.setSizePolicy(sizePolicy)
        self.WGLabel.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.WGLabel.setFont(font)
        self.WGLabel.setObjectName("WGLabel")
        self.gridLayout_3.addWidget(self.WGLabel, 0, 0, 1, 1)
        self.AWGtext = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.AWGtext.setMaximumSize(QtCore.QSize(150, 16777215))
        self.AWGtext.setMinimum(1.0)
        self.AWGtext.setMaximum(5000.0)
        self.AWGtext.setObjectName("AWGtext")
        self.gridLayout_3.addWidget(self.AWGtext, 0, 3, 1, 2)
        self.SQ1text = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.SQ1text.setMaximumSize(QtCore.QSize(80, 16777215))
        self.SQ1text.setMaximum(50000.0)
        self.SQ1text.setObjectName("SQ1text")
        self.gridLayout_3.addWidget(self.SQ1text, 1, 3, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 10, 1, 2, 4)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
        self.horizontalSlider_6 = QtWidgets.QSlider(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_6.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_6.setSizePolicy(sizePolicy)
        self.horizontalSlider_6.setMinimum(-3300)
        self.horizontalSlider_6.setMaximum(3300)
        self.horizontalSlider_6.setProperty("value", 99)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.gridLayout_5.addWidget(self.horizontalSlider_6, 1, 3, 1, 1)
        self.trigBox = QtWidgets.QComboBox(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trigBox.sizePolicy().hasHeightForWidth())
        self.trigBox.setSizePolicy(sizePolicy)
        self.trigBox.setMaximumSize(QtCore.QSize(55, 16777215))
        self.trigBox.setObjectName("trigBox")
        self.gridLayout_5.addWidget(self.trigBox, 1, 2, 1, 1)
        self.TBslider = QtWidgets.QSlider(self.frame_6)
        self.TBslider.setMaximum(8)
        self.TBslider.setOrientation(QtCore.Qt.Horizontal)
        self.TBslider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.TBslider.setObjectName("TBslider")
        self.gridLayout_5.addWidget(self.TBslider, 0, 1, 1, 3)
        self.trigEnable = QtWidgets.QCheckBox(self.frame_6)
        self.trigEnable.setChecked(True)
        self.trigEnable.setObjectName("trigEnable")
        self.gridLayout_5.addWidget(self.trigEnable, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_6, 15, 1, 1, 4)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 16, 1, 1, 3)
        self.CCS = QtWidgets.QCheckBox(self.frame)
        self.CCS.setObjectName("CCS")
        self.gridLayout_2.addWidget(self.CCS, 7, 3, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 8, 1, 1, 4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 16, 4, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 12, 1, 1, 4)
        self.RES = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RES.sizePolicy().hasHeightForWidth())
        self.RES.setSizePolicy(sizePolicy)
        self.RES.setObjectName("RES")
        self.gridLayout_2.addWidget(self.RES, 3, 1, 1, 4)
        self.FREQ = QtWidgets.QPushButton(self.frame)
        self.FREQ.setObjectName("FREQ")
        self.gridLayout_2.addWidget(self.FREQ, 5, 1, 1, 4)
        self.OD1 = QtWidgets.QCheckBox(self.frame)
        self.OD1.setObjectName("OD1")
        self.gridLayout_2.addWidget(self.OD1, 7, 1, 1, 2)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 6, 1, 1, 4)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 9, 4, 1, 1)
        self.Wshape = QtWidgets.QComboBox(self.frame)
        self.Wshape.setObjectName("Wshape")
        self.Wshape.addItem("")
        self.Wshape.addItem("")
        self.Wshape.addItem("")
        self.gridLayout_2.addWidget(self.Wshape, 9, 1, 1, 3)
        self.CAP = QtWidgets.QPushButton(self.frame)
        self.CAP.setObjectName("CAP")
        self.gridLayout_2.addWidget(self.CAP, 4, 1, 1, 4)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 4, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.voltMeterCB1 = QtWidgets.QCheckBox(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.voltMeterCB1.setFont(font)
        self.voltMeterCB1.setObjectName("voltMeterCB1")
        self.horizontalLayout.addWidget(self.voltMeterCB1)
        self.voltMeterCB2 = QtWidgets.QCheckBox(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.voltMeterCB2.setFont(font)
        self.voltMeterCB2.setObjectName("voltMeterCB2")
        self.horizontalLayout.addWidget(self.voltMeterCB2)
        self.voltMeterCB3 = QtWidgets.QCheckBox(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.voltMeterCB3.setFont(font)
        self.voltMeterCB3.setObjectName("voltMeterCB3")
        self.horizontalLayout.addWidget(self.voltMeterCB3)
        self.gridLayout_2.addWidget(self.frame_7, 2, 1, 1, 4)
        self.gridLayout.addWidget(self.splitter, 0, 1, 1, 4)
        self.frame_2 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.offsetLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.offsetLayout.setContentsMargins(0, 0, 0, 0)
        self.offsetLayout.setSpacing(3)
        self.offsetLayout.setObjectName("offsetLayout")
        self.slider1 = QtWidgets.QSlider(self.frame_2)
        self.slider1.setStyleSheet("")
        self.slider1.setMinimum(-4)
        self.slider1.setMaximum(4)
        self.slider1.setOrientation(QtCore.Qt.Vertical)
        self.slider1.setObjectName("slider1")
        self.offsetLayout.addWidget(self.slider1)
        self.slider2 = QtWidgets.QSlider(self.frame_2)
        self.slider2.setStyleSheet("")
        self.slider2.setMinimum(-4)
        self.slider2.setMaximum(4)
        self.slider2.setOrientation(QtCore.Qt.Vertical)
        self.slider2.setObjectName("slider2")
        self.offsetLayout.addWidget(self.slider2)
        self.slider3 = QtWidgets.QSlider(self.frame_2)
        self.slider3.setStyleSheet("")
        self.slider3.setMinimum(-4)
        self.slider3.setMaximum(4)
        self.slider3.setOrientation(QtCore.Qt.Vertical)
        self.slider3.setObjectName("slider3")
        self.offsetLayout.addWidget(self.slider3)
        self.slider4 = QtWidgets.QSlider(self.frame_2)
        self.slider4.setStyleSheet("")
        self.slider4.setMinimum(-4)
        self.slider4.setMaximum(4)
        self.slider4.setOrientation(QtCore.Qt.Vertical)
        self.slider4.setObjectName("slider4")
        self.offsetLayout.addWidget(self.slider4)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.Freeze = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Freeze.sizePolicy().hasHeightForWidth())
        self.Freeze.setSizePolicy(sizePolicy)
        self.Freeze.setObjectName("Freeze")
        self.gridLayout.addWidget(self.Freeze, 1, 4, 1, 1)
        self.Cross = QtWidgets.QCheckBox(Form)
        self.Cross.setMaximumSize(QtCore.QSize(70, 16777215))
        self.Cross.setObjectName("Cross")
        self.gridLayout.addWidget(self.Cross, 1, 2, 1, 1)

        self.retranslateUi(Form)
        self.A1Range.setCurrentIndex(2)
        self.A2Range.setCurrentIndex(2)
        self.A1Map.setCurrentIndex(-1)
        self.MICRange.setCurrentIndex(0)
        self.A3Range.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(2)
        self.pushButton_5.clicked.connect(Form.show_fft)
        self.pushButton_4.clicked.connect(Form.save_data)
        self.Wshape.currentIndexChanged['int'].connect(Form.select_wave)
        self.comboBox_2.currentIndexChanged['int'].connect(Form.select_wgain)
        self.AWGslider.valueChanged['int'].connect(Form.awg_slider)
        self.AWGtext.editingFinished.connect(Form.awg_text)
        self.SQ1DCtext.editingFinished.connect(Form.sq1_dc)
        self.SQ1text.editingFinished.connect(Form.sq1_text)
        self.SQ1slider.valueChanged['int'].connect(Form.sq1_slider)
        self.PV1text.editingFinished.connect(Form.pv1_text)
        self.PV2text.editingFinished.connect(Form.pv2_text)
        self.PV1slider.valueChanged['int'].connect(Form.pv1_slider)
        self.PV2slider.valueChanged['int'].connect(Form.pv2_slider)
        self.TBslider.valueChanged['int'].connect(Form.set_timebase)
        self.trigBox.currentIndexChanged['int'].connect(Form.select_trig_source)
        self.horizontalSlider_6.valueChanged['int'].connect(Form.set_trigger)
        self.pushButton.clicked.connect(Form.show_voltmeter)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Diff.setText(_translate("Form", "A2-A1"))
        self.msgwin.setText(_translate("Form", "."))
        self.label_4.setText(_translate("Form", "Measure Voltages"))
        self.A1Range.setItemText(0, _translate("Form", "16V"))
        self.A1Range.setItemText(1, _translate("Form", "8V"))
        self.A1Range.setItemText(2, _translate("Form", "4V"))
        self.A1Range.setItemText(3, _translate("Form", "2.5V"))
        self.A1Range.setItemText(4, _translate("Form", "1V"))
        self.A1Range.setItemText(5, _translate("Form", "0.5V"))
        self.A2Fit.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Amplitude</span> and <span style=\" font-weight:600;\">frequency</span> extracted from the</p><p>sinusoidal signal using least square fitting.</p><p><br/></p><p>This assumes a sine wave input is provided.</p><p><br/></p><p>For mixed signals, use the FOURIER transform button</p><p>below.</p></body></html>"))
        self.MICFit.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Amplitude</span> and <span style=\" font-weight:600;\">frequency</span> extracted from the</p><p>sinusoidal signal using least square fitting.</p><p><br/></p><p>This assumes a sine wave input is provided.</p><p><br/></p><p>For mixed signals, use the FOURIER transform button</p><p>below.</p></body></html>"))
        self.A3Fit.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Amplitude</span> and <span style=\" font-weight:600;\">frequency</span> extracted from the</p><p>sinusoidal signal using least square fitting.</p><p><br/></p><p>This assumes a sine wave input is provided.</p><p><br/></p><p>For mixed signals, use the FOURIER transform button</p><p>below.</p></body></html>"))
        self.MICBox.setText(_translate("Form", "MIC"))
        self.A2Range.setItemText(0, _translate("Form", "16V"))
        self.A2Range.setItemText(1, _translate("Form", "8V"))
        self.A2Range.setItemText(2, _translate("Form", "4V"))
        self.A2Range.setItemText(3, _translate("Form", "2.5V"))
        self.A2Range.setItemText(4, _translate("Form", "1V"))
        self.A2Range.setItemText(5, _translate("Form", "0.5V"))
        self.A1Fit.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Amplitude</span> and <span style=\" font-weight:600;\">frequency</span> extracted from the</p><p>sinusoidal signal using least square fitting.</p><p><br/></p><p>This assumes a sine wave input is provided.</p><p><br/></p><p>For mixed signals, use the FOURIER transform button</p><p>below.</p></body></html>"))
        self.A2Box.setText(_translate("Form", "A2"))
        self.MICRange.setItemText(0, _translate("Form", "4V"))
        self.MICRange.setItemText(1, _translate("Form", "2V"))
        self.MICRange.setItemText(2, _translate("Form", "1V"))
        self.MICRange.setItemText(3, _translate("Form", "0.5V"))
        self.A3Box.setText(_translate("Form", "A3"))
        self.A3Range.setItemText(0, _translate("Form", "4V"))
        self.A3Range.setItemText(1, _translate("Form", "2V"))
        self.A3Range.setItemText(2, _translate("Form", "1V"))
        self.A3Range.setItemText(3, _translate("Form", "0.5V"))
        self.pcsVal.setToolTip(_translate("Form", "<html><head/><body><p>The voltage value at the constant current source output</p></body></html>"))
        self.label.setText(_translate("Form", "Current Source Voltage(V):"))
        self.label_3.setText(_translate("Form", "Current Source (uA):"))
        self.pcsVal_I.setToolTip(_translate("Form", "<html><head/><body><p>The voltage value at the constant current source output</p></body></html>"))
        self.PV2text.setSuffix(_translate("Form", " Volts"))
        self.PV1Label.setText(_translate("Form", "PV1"))
        self.PV2slider.setProperty("class", _translate("Form", "symmetric volts"))
        self.PV1slider.setProperty("class", _translate("Form", "symmetric volts"))
        self.PV1text.setSuffix(_translate("Form", " Volts"))
        self.SQ1Label.setText(_translate("Form", "SQ1"))
        self.SQ1DCtext.setSuffix(_translate("Form", " %"))
        self.AWGslider.setProperty("class", _translate("Form", "symmetric"))
        self.PV2Label.setText(_translate("Form", "PV2"))
        self.SQ1slider.setProperty("class", _translate("Form", "symmetric"))
        self.WGLabel.setText(_translate("Form", "WG"))
        self.AWGtext.setSuffix(_translate("Form", " Hz"))
        self.SQ1text.setSuffix(_translate("Form", " Hz"))
        self.label_5.setText(_translate("Form", "Timebase"))
        self.trigEnable.setText(_translate("Form", "Trigger"))
        self.pushButton_4.setText(_translate("Form", "SAVE Traces"))
        self.CCS.setText(_translate("Form", "CCS"))
        self.pushButton_5.setText(_translate("Form", "Fourier Transform"))
        self.RES.setText(_translate("Form", "Resistance on SEN"))
        self.FREQ.setText(_translate("Form", "Frequency (IN2):"))
        self.OD1.setText(_translate("Form", "OD1"))
        self.comboBox_2.setItemText(0, _translate("Form", "80 mV"))
        self.comboBox_2.setItemText(1, _translate("Form", "1V"))
        self.comboBox_2.setItemText(2, _translate("Form", "3V (Amplitude)"))
        self.Wshape.setItemText(0, _translate("Form", "WG( Sinusoidal )"))
        self.Wshape.setItemText(1, _translate("Form", "WG( Triangle )"))
        self.Wshape.setItemText(2, _translate("Form", "SQ2( Square )"))
        self.CAP.setText(_translate("Form", "Capacitance (IN1):"))
        self.pushButton.setText(_translate("Form", "SHOW ALL"))
        self.voltMeterCB1.setText(_translate("Form", "A1"))
        self.voltMeterCB2.setText(_translate("Form", "A2"))
        self.voltMeterCB3.setText(_translate("Form", "A3"))
        self.Freeze.setText(_translate("Form", "FREEZE"))
        self.Cross.setText(_translate("Form", "Cursor"))

from pyqtgraph import PlotWidget
