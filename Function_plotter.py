import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout
from PySide2 import QtCore
from gui import Ui_fn_plotter_window
from eval import FunctionEvaluator
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_fn_plotter_window()
        self.ui.setupUi(self)
        self.ui.plot_button.clicked.connect(self.plot)
        self.fn_eval = FunctionEvaluator()

        self.setWindowTitle('Function Plotter')

        # Create a layout for the group box
        layout = QHBoxLayout()
        canvas = FigureCanvas(Figure())
        layout.addWidget(canvas)

        # Set the layout for the group box
        self.ui.plot.setLayout(layout)
        self.ax = canvas.figure.subplots()
        self._drawing =  None

    def plot(self):
        err = ''
        try:
            self.fn_eval.set_function(self.ui.fx_input.text())
            self.fn_eval.set_min_max_val(self.ui.min_input.text(), self.ui.max_input.text())
        except AssertionError as e:
            print('error alo')
            err = e.args
        if err:
            self.ui.status_output.clear()
            self.ui.status_output.insertHtml(err[0])
            self.ui.status_output.setAlignment(QtCore.Qt.AlignHCenter)
            return
        x,y = self.fn_eval.evaluate()
        self.ax.clear()
        self._drawing, = self.ax.plot(x,y)
        self._drawing.figure.canvas.draw()
        self.ui.status_output.clear()
        self.ui.status_output.insertPlainText('Plotted ' + self.ui.fx_input.text())
        self.ui.status_output.setAlignment(QtCore.Qt.AlignHCenter)
        # plt.show()
        # print('Clicked ' + fn + ' ' + min_val + ' ' + max_val)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())