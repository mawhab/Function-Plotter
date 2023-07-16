import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore
from gui import Ui_fn_plotter_window
from eval import Function_evaluator
import matplotlib.pyplot as plt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_fn_plotter_window()
        self.ui.setupUi(self)
        self.ui.plot_button.clicked.connect(self.plot)
        self.fn_eval = Function_evaluator()

    def plot(self):
        err = ''
        try:
            self.fn_eval.set_function(self.ui.fx_input.text())
            self.fn_eval.set_min_val(self.ui.min_input.text())
            self.fn_eval.set_max_val(self.ui.max_input.text())
        except AssertionError as e:
            err = e.args
        if err:
            self.ui.status_output.clear()
            self.ui.status_output.insertHtml(err)
            self.ui.status_output.setAlignment(QtCore.Qt.AlignHCenter)
            return
        x,y = self.fn_eval.evaluate()
        plt.plot(x,y)
        plt.show()
        # print('Clicked ' + fn + ' ' + min_val + ' ' + max_val)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())