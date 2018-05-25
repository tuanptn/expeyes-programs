#!/usr/bin/python3
"""
expEYES utility to display plots and export them to other applications
Author  : © 2018 Georges Khaznadar <georgesk@debian.org>
License : GNU GPL version 3
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyqtgraph as pg
import numpy as np
from subprocess import call
from tempfile import NamedTemporaryFile
    

_translate = QCoreApplication. translate

class Exporter:
    List=[]
    def __init__(self, func, label, tooltip=""):
        """
        Creates an exporter instance and register it in Exporter.List
        @param func a function with the profile:
        title, xlabel, ylabel, xdata, ydata -> list of files
        which calls an application in the background and returns a
        list of temporary files to erase.
        @param label a short description
        @param tooltip a longer description
        """
        self.func=func
        self.label=label
        self.tooltip=tooltip
        Exporter.List.append(self)
        return

## define a decorator
def exporter(label, tooltip):
    """
    this decorator allows to change a function with profile:
    title, xlabel, ylabel, xdata, ydata -> list of files
    to an Exporter instance, automatically registered in Exporter.List
    @param label a short description
    @param tooltip a longer description
    """
    def mkExporter(func):
        return Exporter(func,label,tooltip)
    return mkExporter

@exporter(
    _translate("eyesplotter","Grace"),
    _translate("eyesplotter","Fast old-fashioned plotter/analyzer")
)
def grace(title, xlabel, ylabel, xdata, ydata):
    print("DEBUG: xmgrace export still not implemented")
    return []

@exporter(
    _translate("eyesplotter","Qtiplot"),
    _translate("eyesplotter","Modern plotter/analyzer")
)
def qtiplot(title, xlabel, ylabel, xdata, ydata):
    qtiScript="""\
t = newTable("Table1", {rows}, {cols})
t.setColData(1, {xdata})
{templatedYdata}
l=newGraph().activeLayer()
l.setTitle("<font color = blue>{title}</font>")
{TemplatedCurve}
l.setAxisTitle(Layer.Left, "{ylabel}")
l.setAxisTitle(Layer.Bottom, "{xlabel}")
l.enableAxisLabels(Layer.Right, False)
l.enableAxisLabels(Layer.Top, False)
"""
    ydataTemplate="t.setColData({col}, {ydata})"
    curveTemplate="""\
c{num}=l.insertCurve(t, '1', '{num}', Layer.Line, 0, -1)
l.setCurveLineColor({curveCount}, {color})
"""

    rows=len(xdata)
    xdata=str(list(xdata))
    if len(ydata.shape)==1:
        #simple plot
        cols=2
        templatedYdata=ydataTemplate.format(
            col=2,
            ydata=str(list(ydata)),
        )
        TemplatedCurve=curveTemplate.format(
            num=2,
            color=0,
            curveCount=0,
        )
    else:
        for i in range(ydata.shape[0]):
            #multiple plots
            cols=ydata.shape[0]+1
            yd=[]
            for i in range(cols-1):
                yd.append(
                    ydataTemplate.format(
                        col=2+i,
                        ydata=str(list(ydata[i])),
                    ))
            templatedYdata="\n".join(yd)
            c=[]
            for i in range(cols-1):
                c.append(
                    curveTemplate.format(
                        num=2+i,
                        color=i,
                        curveCount=i
                    ))
            TemplatedCurve="\n".join(c)
    script=qtiScript.format(
        rows=rows, cols=cols, xdata=xdata,
        templatedYdata=templatedYdata, TemplatedCurve=TemplatedCurve,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
    )
    temp=NamedTemporaryFile(mode="w", prefix="qti_", delete=False)
    temp.write(script)
    temp.close()
    call("(qtiplot --execute {temp}&)".format(temp=temp.name), shell=True)
    return [temp]

class ExportButton(QPushButton):
    """
    implements a push button which can access data from a PlotWindow
    and export them to an external application, launched in the
    background.
    """
    def __init__(self, parent, exporter):
        """
        @param parent supposedly a PlotWindow instance
        @param exporter an Exporter instance
        """
        assert (isinstance(parent, PlotWindow))
        assert (isinstance(exporter, Exporter))
        QPushButton.__init__(self, exporter.label, parent)
        self.pw=parent
        self.cb=exporter.func
        self.setToolTip(exporter.tooltip)
        self.clicked.connect(self.export)
        return
    
    def export(self):
        self.pw.tmpFiles+=self.cb(self.pw.title,
                                  self.pw.xlabel, self.pw.ylabel,
                                  self.pw.xdata, self.pw.ydata)
        return

class PlotWindow(QWidget):
    """
    Implements a quick plot window, which can export its data to a few other 
    plotting applications
    """
    def closeEvent(self, event):
        from os import unlink
        QWidget.closeEvent(self, event)
        for temp in self.tmpFiles:
            unlink(temp.name)
        return

    def __init__(self, parent=None,
                 xdata=[], ydata=[], xlabel="", ylabel="",
                 title=""):
        """
        The constructor
        @param parent the parent window, defaults to None
        @param xdata a vector for the abscissa; any one-dimensional array or
        iterable will be ok
        @param ydata a vector for the ordinate, or a matrix containing n
        vectors for multiple curves; the shape must be compatible with xdata
        @param xlabel a label for abscissa
        @param ylabel a label for ordinate
        @param title a title for the plot
        """
        QWidget.__init__(self, parent)
        self.xdata=np.array(xdata)
        self.ydata=np.array(ydata)
        self.xlabel=xlabel
        self.ylabel=ylabel
        self.title=title
        self.tmpFiles=[]

        layout = QGridLayout()
        self.setLayout(layout)

        plotWidget = pg.PlotWidget(title=title)
        if len(ydata.shape)==1:
            #simple plot
            plotWidget.plot(x, y)
        else:
            for i in range(ydata.shape[0]):
                #multiple plots
                plotWidget.plot(x, y[i], pen=(i,3))
        # plot goes on top, spanning all columns
        layout.addWidget(plotWidget, 0, 0, 1,(1+len(Exporter.List)))  

        l= QLabel(_translate("eyesplotter","Export to"))
        layout.addWidget(l, 1, 0)
        for col, exp in enumerate(Exporter.List, start=1):
            layout.addWidget(ExportButton(self, exp), 1, col)
        return




if __name__=="__main__":
    app = QApplication([])
    x = np.arange(1000)
    y = np.random.normal(size=(2, 1000))
    w = PlotWindow(xdata=x, ydata=y,
                   xlabel="The pretty abscissa",
                   ylabel="The amazing ordinate",
                   title="Two plot curves")
    w.show()
    app.exec_()
    
