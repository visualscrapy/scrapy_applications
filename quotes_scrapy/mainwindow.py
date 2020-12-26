import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import qt5reactor
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import twisted
from Layout import Ui_MainWindow
from ZenSpider import ZenSpider

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.on_url_entered)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents
        )

    def crawler_results(self, item):
        row = self.tableWidget.rowCount()
        title = item["title"]
        author = item["author"]
        tag = item["tag"]
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(author))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(tag))

    def on_url_entered(self):
        configure_logging()
        runner = CrawlerRunner()
        runner.crawl(ZenSpider)

        for p in runner.crawlers:
            p.signals.connect(self.crawler_results, signal=signals.item_scraped)

    def closeEvent(self, event):
        super(MainWindow, self).closeEvent(event)
        twisted.internet.reactor.stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    qt5reactor.install()
    main_window = MainWindow()
    main_window.show()
    twisted.internet.reactor.run()







# import scrapy
# from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtCore import QRunnable, pyqtSlot, QThread, pyqtSignal, QTimer
# from PyQt5.QtWidgets import QTableWidgetItem, QLabel
# from scrapy import signals
# from scrapy.crawler import CrawlerProcess, CrawlerRunner
# from twisted.internet import reactor
# from scrapy.utils.log import configure_logging

# from Layout import Ui_MainWindow
# from ZenSpider import ZenSpider


# class MainWindow( QtWidgets.QMainWindow, Ui_MainWindow ) :

#     def __init__(self, parent=None) :
#         super(MainWindow, self).__init__()

#         self.setupUi( self )
#         self.pushButton.pressed.connect( self.on_url_entered )

#     def crawler_results(self, item) :
#         print( "SCRAPED AN ITEM" )
#         ##Do Something here ##

#     def on_url_entered(self) :
#         # global userInput
#         # userInput = self.urlbar.text()
#         configure_logging()
#         runner = CrawlerRunner()
#         runner.crawl(ZenSpider, domain="google.com.au")
#         for p in runner.crawlers :
#             p.signals.connect(self.crawler_results, signal=signals.item_scraped)
#         reactor.run()

# if __name__ == "__main__" :
#     app = QtWidgets.QApplication( [] )
#     main_window = MainWindow()
#     main_window.show()
#     app.exec_()
