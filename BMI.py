import sys
from GUI import *
class MyForm(QtWidgets.QDialog):
 def __init__(self, parent=None):
     QtWidgets.QWidget.__init__(self, parent)
     self.ui = Ui_Dialog()
     self.ui.setupUi(self)
     self.ui.pbtCalculate.clicked.connect(self.BMI)
     self.setStyleSheet("background: #faf")
     self.ui.lneHeight.setStyleSheet("border-radius: 9px; background: cyan")
     self.ui.lneWeight.setStyleSheet("border-radius: 9px; background: cyan")
     self.ui.pbtCalculate.setStyleSheet("border: 2px solid blue; border-radius: 9px; background: cyan")

 def BMI(self):
    #print("Hello")
    height = self.ui.lneHeight.text()
    weight = self.ui.lneWeight.text()
    #print(height)
    #print(weight)
    bmi = int(weight)/(int(height)*int(height)/10000)
    #print(bmi)
    accuracy = round(bmi, 2)

    if accuracy<18.5:
        range = "You are underweight"
        self.setStyleSheet("background-color: #fb0508;")
    elif accuracy>25:
        range = "You are overweight"
        self.setStyleSheet("background-color: #fb0508;")
    else:
        range = "You have normal weight"
        self.setStyleSheet("background-color: #6de600;")

    self.ui.lblResult.setText("BMI is "+ str(accuracy) + ". " + range)

if __name__ == "__main__":
 app = QtWidgets.QApplication(sys.argv)
 myapp = MyForm()
 myapp.show()
 sys.exit(app.exec_())
