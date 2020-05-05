from PySide2 import QtWidgets, QtCore
from mainWindow import Ui_mainwidget as mPage
from base import Ui_MainWindow as baseWindow
from testFrame import Ui_testPage as testPage
from testFinalFrame import Ui_Form as finalPage

class finalPageApp(finalPage, QtWidgets.QWidget):
    def __init__(self):
        super(finalPageApp,self).__init__()
        self.setupUi(self)

class baseFrameError(Exception):
    def __init__(self):
        """needs to be implemented TODO"""
        pass

class OveriterrationError(Exception):
    def __init__(self):
        """todo"""
        pass
class testFrameApp(testPage, QtWidgets.QWidget):
    def __init__(self):
        super(testFrameApp, self).__init__()
        self.setupUi(self)

class testMainPage(mPage,QtWidgets.QWidget):
    def __init__(self):
        super(testMainPage, self).__init__()
        self.setupUi(self)

class App(baseWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)

        self.nextButton = None
        #testNum contains the row of the test it can be 0,1,2,3
        self.testNum = 0
        #actions
        self.actionRunNewTest.triggered.connect(self.changingToTest)
        self.actionLoad_test_results.triggered.connect(self.loadTestResults)
        if self.nextButton is not None:
            self.nextButton.show()
            self.nextButton.clicked.connect(self.nextButtonPushed)

        #startPage
        newPage = testMainPage()
        self.gridLayout.addWidget(newPage)
        del newPage

    def removingFrame(self):
        """Use it only if there is only one frame in the basegrid otherwise use an other function"""
        if self.gridLayout.count() == 1:
            currentItem = self.gridLayout.itemAt(0)
        else:
            raise baseFrameError

        if currentItem is not None:
            currentWidget = currentItem.widget()
            currentWidget.deleteLater()

        self.gridLayout.removeItem(currentItem)

    def changingToMainPage(self):
        """changing back to the mainPage or startPage"""
        newPage = testMainPage()
        self.removingFrame()
        self.gridLayout.addWidget(newPage)

    def nextButtonPushed(self):
        """Loads the next page when button pushed"""
        self.testNum += 1
        self.changingToTest()
    def saveData(self):
        """TODO saves the data of the finish screen"""
        pass
    def finishButtonPushed(self):
        """TODO collect the data of the finish page"""
        self.saveData()
        self.changingToMainPage()

    def changingToTest(self):
        """ Changing to a testPage also changes between tests"""
        if self.testNum <=3:
            tPage = testFrameApp()
            tPage = self.fillingUpwithColorLabels(self.testNum, tPage)
            try:
                self.removingFrame()
            except baseFrameError:
                print("ERROR")
            self.gridLayout.addWidget(tPage)
            self.connect(tPage.pushButton, QtCore.SIGNAL('clicked()'), self.nextButtonPushed)
        else:
            self.testNum = 0
            fPage = finalPageApp()
            try:
                self.removingFrame()
            except baseFrameError:
                print("ERROR")
            self.gridLayout.addWidget(fPage)
            self.connect(fPage.finishButton, QtCore.SIGNAL('clicked()'), self.finishButtonPushed)


    def fillingUpwithColorLabels(self, testNumber, testFrameAppObject):
        """it fills up the the horizontal
        testNumber can be 0,1,2,3 depends which row of the FM hue test needs to be loaded"""
        tPage = testFrameAppObject
        self.colorLabels = {}
        if testNumber == 0:
            rangeOfColors = range(0, 24)
        elif testNumber == 1:
            rangeOfColors = range(22, 44)
        elif testNumber == 2:
            rangeOfColors = range(42, 65)
        elif testNumber == 3:
            rangeOfColors = range(63, 87)
        else:
            raise OveriterrationError

        for i in rangeOfColors:
            if i == 0:
                value = 85
            else:
                value = i
            colorLabel = QtWidgets.QLabel(tPage)
            colorLabel.setObjectName("colorLabel_"+str(value))
            colorLabel.setText(str(value))
            self.colorLabels[str(value)] = colorLabel
            tPage.horizontalLayout.addWidget(colorLabel)

        return tPage


    def loadTestResults(self):
        pass



if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qtApp = App()
    qtApp.show()
    quit = app.exec_()
