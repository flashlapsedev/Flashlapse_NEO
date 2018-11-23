# import basic libraries
import sys

#import UI functions
import UI_Update_Disable
import UI_Update_Enable
import UI_Update_General

#import custom functions
import Camera
 
# import Qt content
import PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
 
# import generated UI
import FlashLapse_UI

#UI variables
pre_ready = False
sch_ready = False
pre_flip = False
sch_flip = False
 
# create class for Raspberry Pi GUI
class MainWindow(QMainWindow, FlashLapse_UI.Ui_MainWindow):

    def Start_Snapshot(self):
        try:
            pre_ready, sch_ready= UI_Update_General.check_stat(self)
            pre_flip = pre_ready
            sch_flip = sch_ready
            self.Snap_Thread = Camera.Snap()
            self.Snap_Thread.started.connect(lambda: UI_Update_Disable.snap_disable(self,pre_flip,sch_flip))
            self.Snap_Thread.finished.connect(lambda: UI_Update_Enable.snap_enable(self,pre_flip,sch_flip))
            self.Snap_Thread.start()
            
        except Exception as e:
            print(e)

    def Start_Rotate(self):
        try:
            UI_Update_Enable.snap_enable(self)
        except Exception as e:
            print(e)
            
 # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.Snapshot.clicked.connect(lambda: self.Start_Snapshot())
        self.Rotate.clicked.connect(lambda: self.Start_Rotate())
        
 
# main function
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())
 
# python bit to figure how who started This
if __name__ == "__main__":
    main()
