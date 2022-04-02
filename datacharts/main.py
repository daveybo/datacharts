import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen, QColor, QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 600, 400)
        self.setStyleSheet("background-color: blue;")
        self.setWindowTitle('Test Graphs')

        self.show()

        self.create_pie_chart()

    def create_pie_chart(self):

        # create pie series
        series = QPieSeries()
        for i in range(5):
            text = str(i)
            val = i
            series.append(text, val)
        # endfor

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("My Pie Chart")
        chart.legend().setVisible(True)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chart_view)

# end class mainwindow


# main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    sys.exit(app.exec_())
