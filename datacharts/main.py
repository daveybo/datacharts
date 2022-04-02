'''
make sure to install pyqt5 and pyqtchart first
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        self.setGeometry(200, 200, 600, 400)
        self.setStyleSheet("background-color: blue;")
        self.setWindowTitle('Test Graphs')

        self.create_pie_chart()

        self.show()

    def create_pie_chart(self):

        # create pie series
        pie_data = {
            "fred": 220,
            "james": 128,
            "bob": 156,
            "bill": 188
        }

        series = QPieSeries()
        for key in pie_data:
            series.append(key, pie_data[key])
        # end for

        chart = QChart()

        # adding slice
        my_slice = QPieSlice()
        my_slice = series.slices()[2]
        my_slice.setExploded(True)
        my_slice.setLabelVisible(True)
        my_slice.setPen(QPen(Qt.darkGreen, 3))
        my_slice.setBrush(Qt.green)

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
