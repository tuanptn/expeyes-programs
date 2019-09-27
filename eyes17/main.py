# -*- coding: utf-8; mode: python; indent-tabs-mode: t; tab-width:4 -*-
import sys, time, math, importlib, os, platform, os.path, configparser
from utils import cnf

from QtVersion import *
showVersions()

import pyqtgraph as pg

pf = platform.platform()
print (pf)	
if 'Windows' in pf:
	import diodeIV, editor, filterCircuit, induction, MPU6050, npnCEout, pendulumVelocity
	import plotIV, pnpCEout, pt100, RCtransient, RLCsteadystate, RLCtransient
	import RLtransient, rodPendulum, scope, soundBeats, soundFreqResp, soundVelocity
	import sr04dist, utils, logger, XYplot, i2cLogger

schoolExpts = [ 
[QT_TRANSLATE_NOOP('MainWindow',"Voltage measurement"), 'measure-dc'],
[QT_TRANSLATE_NOOP('MainWindow',"Resistance measurement"), 'res-measure'],
[QT_TRANSLATE_NOOP('MainWindow',"Resistors in Series"), 'res-series'],
[QT_TRANSLATE_NOOP('MainWindow',"Resistors in Parallel"), 'res-parallel'],
[QT_TRANSLATE_NOOP('MainWindow',"Capacitance measurement"), 'cap-measure'],
[QT_TRANSLATE_NOOP('MainWindow',"Capacitors in Series"), 'cap-series'],
[QT_TRANSLATE_NOOP('MainWindow',"Capacitors in Parallel"), 'cap-parallel'],
[QT_TRANSLATE_NOOP('MainWindow',"Resistance by Ohm's law"), 'res-compare'],
[QT_TRANSLATE_NOOP('MainWindow','Direct and Alternating Currents'), 'ac-dc'],
[QT_TRANSLATE_NOOP('MainWindow','AC mains pickup'), 'line-pickup'],
[QT_TRANSLATE_NOOP('MainWindow','Separating AC and DC'), 'acdc-separating'],
[QT_TRANSLATE_NOOP('MainWindow','Conducting Human body'), 'conducting-human'],
[QT_TRANSLATE_NOOP('MainWindow','Resistance of Human body'), 'res-body'],
[QT_TRANSLATE_NOOP('MainWindow','Light Dependent Resistor'), 'ldr'],
[QT_TRANSLATE_NOOP('MainWindow','Lemon Cell'), 'lemon-cell'],
[QT_TRANSLATE_NOOP('MainWindow','Simple AC generator'), 'ac-generator'],
[QT_TRANSLATE_NOOP('MainWindow','Transformer'), 'transformer'],
[QT_TRANSLATE_NOOP('MainWindow','Resistance of Water'), 'res-water'],
[QT_TRANSLATE_NOOP('MainWindow','Generating Sound'), 'sound-generator'],
[QT_TRANSLATE_NOOP('MainWindow','Digitizing Sound'), 'sound-capture'],
[QT_TRANSLATE_NOOP('MainWindow','Stroboscope'), 'stroboscope'],
]


testEquipment = [ 
[QT_TRANSLATE_NOOP('MainWindow','Oscilloscope'),'scope']
#[QT_TRANSLATE_NOOP('MainWindow','Monitor and Control'), 'mon-con']
]


electronicsExpts = [ 
[QT_TRANSLATE_NOOP('MainWindow','Diode Characteristics'),'diodeIV'],
[QT_TRANSLATE_NOOP('MainWindow','NPN Output Characteristics'),'npnCEout'],
[QT_TRANSLATE_NOOP('MainWindow','PNP Output Characteristics'),'pnpCEout'],
#[QT_TRANSLATE_NOOP('MainWindow','AM and FM'), 'amfm']
]

electronicsExptsScope = [ 
[QT_TRANSLATE_NOOP('MainWindow','Oscilloscope'),'scope'],
[QT_TRANSLATE_NOOP('MainWindow','Halfwave Rectifier'),'halfwave'],
[QT_TRANSLATE_NOOP('MainWindow','Fullwave Rectifier'),'fullwave'],
[QT_TRANSLATE_NOOP('MainWindow','Diode Clipping'),'clipping'],
[QT_TRANSLATE_NOOP('MainWindow','Diode Clamping'),'clamping'],
[QT_TRANSLATE_NOOP('MainWindow','IC555 Multivibrator'),'osc555'],
[QT_TRANSLATE_NOOP('MainWindow','Transistor Amplifier (CE)'),'npnCEamp'],
[QT_TRANSLATE_NOOP('MainWindow','Inverting Amplifier'),'opamp-inv'],
[QT_TRANSLATE_NOOP('MainWindow','Non-Inverting Amplifier'),'opamp-noninv'],
[QT_TRANSLATE_NOOP('MainWindow','Integrator using Op-Amp'),'opamp-int'],
[QT_TRANSLATE_NOOP('MainWindow','Logic Gates'),'logic-gates'],
[QT_TRANSLATE_NOOP('MainWindow','Clock Divider Circuit'),'clock-divider']
]

electricalExpts = [ 
[QT_TRANSLATE_NOOP('MainWindow','Plot I-V Curve'),'plotIV'],
[QT_TRANSLATE_NOOP('MainWindow','XY Plotting'),'XYplot'],
[QT_TRANSLATE_NOOP('MainWindow','RLC Steady state response'),'RLCsteadystate'],
[QT_TRANSLATE_NOOP('MainWindow','RC Transient response'),'RCtransient'],
[QT_TRANSLATE_NOOP('MainWindow','RL Transient response'),'RLtransient'],
[QT_TRANSLATE_NOOP('MainWindow','RLC transient response'),'RLCtransient'],
[QT_TRANSLATE_NOOP('MainWindow','Frequency Response of Filter Circuit'),'filterCircuit'],
[QT_TRANSLATE_NOOP('MainWindow','Electromagnetic Induction'),'induction']
]

soundExpts = [
[QT_TRANSLATE_NOOP('MainWindow','Frequency Response of Piezo Buzzer'),'soundFreqResp'],
[QT_TRANSLATE_NOOP('MainWindow','Velocity of Sound'), 'soundVelocity'],
[QT_TRANSLATE_NOOP('MainWindow','Sound beats'), 'soundBeats']
]

mechanicsExpts = [
[QT_TRANSLATE_NOOP('MainWindow','Rod Pendulum with Light barrier'), 'rodPendulum'],
[QT_TRANSLATE_NOOP('MainWindow','Driven Rod Pendulum with Light barrier'), 'drivenRodPendulum'],
[QT_TRANSLATE_NOOP('MainWindow','Pendulum Waveform'),'pendulumVelocity'],
[QT_TRANSLATE_NOOP('MainWindow','Driven Pendulum resonance'),'driven-pendulum'],
[QT_TRANSLATE_NOOP('MainWindow','Distance by HY-SRF04 Echo module'), 'sr04dist']
]

otherExpts = [ 
[QT_TRANSLATE_NOOP('MainWindow','Temperature, PT100 Sensor'), 'pt100'],
[QT_TRANSLATE_NOOP('MainWindow','Data Logger'), 'logger']
]

modulesI2C = [ 
[QT_TRANSLATE_NOOP('MainWindow','Magnetic Hysterisis (MPU925x Sensor)'),'BHCurve'],
[QT_TRANSLATE_NOOP('MainWindow','Luminosity(TSL2561) Logger'),'lightsensorlogger'],
[QT_TRANSLATE_NOOP('MainWindow','MPU-6050 Acccn, Velocity and Temp'), 'MPU6050'],
[QT_TRANSLATE_NOOP('MainWindow','General Purpose I2C Sensors'), 'i2cLogger']
]

pythonCodes = [ 
[QT_TRANSLATE_NOOP('MainWindow','Read Inputs'),  'readInputs'],
[QT_TRANSLATE_NOOP('MainWindow','Set DC Voltages'), 'setVoltages'],
[QT_TRANSLATE_NOOP('MainWindow','Capture Single Input'), 'capture1'],
[QT_TRANSLATE_NOOP('MainWindow','Capture Two Inputs'), 'capture2'],
[QT_TRANSLATE_NOOP('MainWindow','Capture Four Inputs'), 'capture4'],
[QT_TRANSLATE_NOOP('MainWindow','Triangular Waveform'), 'triangularWave'],
[QT_TRANSLATE_NOOP('MainWindow','Arbitrary Waveform'), 'waveforms'],
[QT_TRANSLATE_NOOP('MainWindow','Waveform Table'), 'table'],
[QT_TRANSLATE_NOOP('MainWindow','RC Transient'), 'RCtransient'],
[QT_TRANSLATE_NOOP('MainWindow','RL Transient'), 'RLtransient'],
[QT_TRANSLATE_NOOP('MainWindow','RC Integration'), 'RCintegration'],
[QT_TRANSLATE_NOOP('MainWindow','Clipping with Diode'), 'clipping'],
[QT_TRANSLATE_NOOP('MainWindow','Clamping with Diode'), 'clamping'],
[QT_TRANSLATE_NOOP('MainWindow','Fullwave Rectifier'), 'fullwave'],
[QT_TRANSLATE_NOOP('MainWindow','NPN Ib vs IC plot'), 'npnTransferChar'],
[QT_TRANSLATE_NOOP('MainWindow','Fourier Transform'), 'FourierTransform'],
[QT_TRANSLATE_NOOP('MainWindow','Rod Pendulum'), 'rodpend']
]


#---------------------------------------------------------------------
		
class helpWin(QWebView):
	def __init__(self, name = ''):
		QWebView.__init__(self)
		fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'html', name[1]+'.html')
		self.load(QUrl.fromLocalFile(fn))
		self.setWindowTitle(unicode(self.tr('Help: %s')) %name[0])
		self.setMaximumSize(QSize(500, 1200))
		self.show()
		screen = QDesktopWidget().screenGeometry()
		self.move(screen.width()-self.width()-20, screen.height()-self.height()-60)


class MainWindow(QMainWindow):
	WIDTH = 950
	HEIGHT = 600
	expWidget = None
	expName = ''
	hlpName = ''
	hwin = None
	
	def closeEvent(self, e):
		if self.hwin != None:
			self.hwin.close()

	def __init__(self):
		QMainWindow.__init__(self)
		self.makeMenu()
		self.setMinimumSize(self.WIDTH-100, self.HEIGHT-50)
		self.resize(self.WIDTH,self.HEIGHT)
		self._x = 100
		self._y = 10
		palette = QPalette()								# background color
		palette.setColor(QPalette.Background, QColor(61,168,165)) #("#99ccff")) "#88bbcc"
		self.setPalette(palette)	

		self.helpCB = QCheckBox(self.tr('Enable PopUp Help Window'))
		self.helpCB.stateChanged.connect(self.showHelp)
		#self.helpCB.setStyleSheet('background-color: white')

		self.statusBar = QStatusBar()
		self.setStatusBar(self.statusBar)
		self.statusBar.addWidget(self.helpCB)
		
		self.callExpt(testEquipment[0])					# Start the scope by default
		self.screen = QDesktopWidget().screenGeometry()
		self.show()
		self.move(20, 20)
		
		

	def showHelp(self):
		if self.helpCB.isChecked() == True:
			if self.hwin == None: 
				self.hwin = helpWin((self.title,self.hlpName))
			self.hwin.show()
		else:
			if self.hwin != None: self.hwin.hide()
	
	
	def scope_help(self,e):
		self.hlpName = e[1]
		if self.expName != 'scope':
			explib = importlib.import_module('scope')
			try:
				if self.expWidget != None:
					self.expWidget.timer.stop()     # Stop the timer loop of current widget			
				self.hwin = None
				self.expWidget= None 			    # Let python delete it
				w = explib.Expt(p) 
				self.setWindowTitle(e[0])
				self.setCentralWidget(w)
				self.expWidget = w
				self.expName = 'scope'
			except:
				self.expName = ''
				self.setWindowTitle(self.tr('Failed to load scope'))
		self.hwin = None
		self.title = e[0]
		self.showHelp()
	

	def callExpt(self, e):
		explib = importlib.import_module(e[1])
		try:
			if self.expWidget != None:
				self.expWidget.timer.stop()     # Stop the timer loop of current widget			
			self.hwin = None
			self.expWidget= None 			    # Let python delete it
			w = explib.Expt(p) 
			self.setWindowTitle(self.tr(e[0]))
			self.setCentralWidget(w)
			self.expWidget = w
			self.expName = e[1]
			self.hlpName = e[1]
			self.title = e[0]
			self.showHelp()
		except Exception as err:
			print("Exception:", err)	
			self.expName = ''
			self.setWindowTitle(unicode(self.tr('Failed to load %s')) %e[0])
		return
		
	def runCode(self, e):
		if self.expName != 'editor':
			self.callExpt( ('Python Coding', 'editor'))
		self.expWidget.mycode = e[1]
		self.expWidget.update()

	def setConfig(self,section, key, value):
		"""
		Sets some part of eyes17's configuration
		@param section a section of the configuration file cnf, for
		example: 'ScreenTheme'
		@param key for example: 'Background'
		@param value the text to assign to the key, for example: 'dark'
		"""
		config = configparser.ConfigParser()
		config.read(cnf)
		config[section][key] = value
		with open(cnf,"w") as out: config.write(out)
		return
	
	def setWBG(self):
		"""
		sets a light background for the scope's screen
		"""	
		self.setConfig('ScreenTheme', 'Background', 'light')
		QMessageBox.warning(
			self,
			self.tr('No immediate application'),
			self.tr("Please restart the application to lighten the screen's background")
		)
		return
		
	def setBBG(self):
		"""
		sets a dark background for the scope's screen
		"""	
		self.setConfig('ScreenTheme', 'Background', 'dark')
		QMessageBox.warning(
			self,
			self.tr('No immediate application'),
			self.tr("Please restart the application to darken the screen's background.")
		)
		return
	
	def makeMenu(self):
		bar = self.menuBar()

		mb = bar.addMenu(self.tr("Device"))
		mb.addAction(self.tr('Reconnect'), self.reconnect)
		mb.addAction(self.tr('LightBackGround next time'), self.setWBG)
		mb.addAction(self.tr('DarkBackGround next time'), self.setBBG)

		em = bar.addMenu(self.tr("School Expts"))
		for e in schoolExpts:
			em.addAction(self.tr(e[0]),  lambda item=e: self.scope_help(item))	

		em = bar.addMenu(self.tr("Electronics"))
		for e in electronicsExptsScope:
			em.addAction(self.tr(e[0]),  lambda item=e: self.scope_help(item))	
			
		for e in electronicsExpts:
			em.addAction(self.tr(e[0]),  lambda item=e: self.callExpt(item))	
		
		em = bar.addMenu(self.tr("Electrical"))
		for e in electricalExpts:
			em.addAction(self.tr(e[0]),  lambda item=e: self.callExpt(item))	

		em = bar.addMenu(self.tr("Sound"))
		for e in soundExpts:
			em.addAction(self.tr(e[0]),  lambda item=e: self.callExpt(item))	

		em = bar.addMenu(self.tr("Mechanics"))
		for e in mechanicsExpts:
			em.addAction(self.tr(e[0]),  lambda item=e: self.callExpt(item))	

		em = bar.addMenu(self.tr("Other Expts"))
		for e in otherExpts:
			em.addAction(self.tr(e[0]),  lambda item=e: self.callExpt(item))	

		em = bar.addMenu(self.tr("I2C Modules"))
		for e in modulesI2C:
			em.addAction(self.tr(e[0]),  lambda item=e: self.callExpt(item))	

		em = bar.addMenu(self.tr("PythonCode"))
		for e in pythonCodes:
			em.addAction(self.tr(e[0]),  lambda item=e: self.runCode(item))	


	def reconnect(self):
		global p
		try:
			p.H.disconnect()
		except:
			pass
		p=eyes.open()
		self.expWidget.p = p
		self.expWidget.msg('')
		if p != None: 
			if self.expName == 'scope':
				self.expWidget.recover()
		
# Program starts here
import eyes17.eyes as eyes
p = eyes.open()
if p != None: 
	p.set_sine(1000)
	p.set_sqr1(-1)
	p.set_pv1(0)
	p.set_pv2(0)
	p.set_state(OD1=0)

app = QApplication(sys.argv)

# translation stuff
lang=QLocale.system().name()
t=QTranslator()
t.load("lang/"+lang, os.path.dirname(__file__))
app.installTranslator(t)
t1=QTranslator()
t1.load("qt_"+lang,
	QLibraryInfo.location(QLibraryInfo.TranslationsPath))
app.installTranslator(t1)

mw = MainWindow()
sys.exit(app.exec_())
