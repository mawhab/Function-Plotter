import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout
from PySide2 import QtCore
from gui import Ui_fn_plotter_window
from eval import FunctionEvaluator
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    DEFAULT_VAL = 10
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_window()
        self.setup_outputs()
        self.setup_inputs()

    def setup_window(self):
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

    def setup_inputs(self):
        # set default values for min and max
        self.ui.min_input.setPlaceholderText(str(-MainWindow.DEFAULT_VAL))
        self.ui.max_input.setPlaceholderText(str(MainWindow.DEFAULT_VAL))

    def setup_outputs(self):
        # setup startup status bar
        self.ui.status_output.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ui.status_output.clear()
        self.ui.status_output.insertHtml('Startup')
        self.ui.status_output.setAlignment(QtCore.Qt.AlignHCenter)

    def plot(self):
        '''
        Function is called on plot button press. Take function, min, and max ranges.
        Validate all inputs then evaluate using FunctionEvaluator object.
        Plot the function outputs to the window using embedded figure.
        Update status bar according to output and validation.
        '''
        tmp_min, tmp_max = self.ui.min_input.text(), self.ui.max_input.text()
        if not tmp_min:
            tmp_min = str(-MainWindow.DEFAULT_VAL)
        
        if not tmp_max:
            tmp_max = str(MainWindow.DEFAULT_VAL)
        err = ''
        try:
            self.fn_eval.set_function(self.ui.fx_input.text())
            self.fn_eval.set_min_max_val(tmp_min, tmp_max)
        except AssertionError as e:
            print('error alo')
            err = e.args
        if err:
            self.ui.status_output.clear()
            self.ui.status_output.insertHtml(err[0])
            self.ui.status_output.setAlignment(QtCore.Qt.AlignHCenter)
            self.ui.status_output.setStyleSheet("background-color: rgb(255, 0, 0);")
            return
        x,y = self.fn_eval.evaluate()
        self.ax.clear()
        self._drawing, = self.ax.plot(x,y)
        self._drawing.figure.canvas.draw()
        self.ui.status_output.clear()
        self.ui.status_output.insertHtml('Plotted ' + self.ui.fx_input.text())
        self.ui.status_output.setAlignment(QtCore.Qt.AlignHCenter)
        self.ui.status_output.setStyleSheet("background-color: rgb(0, 255, 0);")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())