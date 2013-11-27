import os, sys

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *

import ui_form

oldpath = os.environ["PATH"]
cwd = os.getcwd()
rpath = os.path.join(cwd, "..","Resources", "Resources")
os.environ["PATH"] = os.path.join(rpath, "bin") + os.pathsep + oldpath
print("new path is: %s" % os.environ["PATH"])

os.environ["R"] = \
    os.path.join(cwd, rpath, "bin")

os.environ["R_HOME"] = \
    os.path.join(cwd, rpath)


from rpy2 import robjects as ro

print("main started")

class HelloWorldDlg(QtGui.QDialog, ui_form.Ui_Dialog):
    def __init__(self, parent=None):
        super(HelloWorldDlg, self).__init__(parent)
        self.setupUi(self)
        
        self.result_lbl.setText("Results is %d" % ro.r("2+3")[0])
        


if __name__ == '__main__':
    #pass        
    app = QApplication(sys.argv)
    form = HelloWorldDlg()
    form.show()
    form.raise_()
    app.exec_()