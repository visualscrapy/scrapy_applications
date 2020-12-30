from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from scrapy import signals
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy.utils.log import configure_logging
import twisted
from window import Ui_MainWindow
from quotes_scrapy.spiders.qscrapy import QscrapySpider


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.on_url_entered)
        self.pushButton.pressed.connect(self.getComboValue) #Added New
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents
        )

    def crawler_results(self, item):
        row = self.tableWidget.rowCount()
        title = item["title"]
        author = item["author"]
        tags = item["tags"]
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(author))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(tags))

    def on_url_entered(self):
        configure_logging()
        runner = CrawlerProcess()
        runner.crawl(QscrapySpider, page_num=self.getComboValue())

        for p in runner.crawlers:
            p.signals.connect(self.crawler_results, signal=signals.item_scraped)

    def closeEvent(self, event):
        super(MainWindow, self).closeEvent(event)
        # twisted.internet.reactor.stop()
        replay = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close window.',
                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if replay == QMessageBox.Yes:
            event.accept()
            print("Window Closed!")
            twisted.internet.reactor.stop()
        else:
            event.ignore()

    def getComboValue(self):  # crated function
        return self.comboBox.currentText()

if __name__ == "__main__":
    import sys
    if 'twisted.internet.reactor' in sys.modules:
        del sys.modules['twisted.internet.reactor']
    app = QtWidgets.QApplication(sys.argv)
    import qt5reactor
    qt5reactor.install()
    w = MainWindow()
    w.show()
    from twisted.internet import reactor
    reactor.run()
