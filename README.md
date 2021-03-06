Or it can be deployed with Pyinstaller:

First the `.spec` file needs to be created with `pyi-makespec <options> main.py`. Then, in the `.spec` file these paths need to be added so that everything is included in the executable:

```
datas=[
    ("scrapy.cfg", "quotes_scrapy"),
    ("window.py", "quotes_scrapy"),
    ("quotes_scrapy/*", "quotes_scrapy/quotes_scrapy"),
    ("quotes_scrapy/spiders/*", "quotes_scrapy/quotes_scrapy/spiders/")
]
```
Then the application can be deployed with:
```bash
pyinstaller main.spec
(OR)
pyinstaller --onefile main.spec
(OR)
pyinstaller --onefile main.py --log-level DEBUG
(OR)
pyinstaller --onedir main.py
```





References:
``` https://stackoverflow.com/questions/61607889/update-pyqt5-gui-inside-a-main-thread-based-on-signal-from-scrapy
 https://github.com/kivy/kivy/issues/4182 reference for #reactor already installed
```

```
 Add this below code into you main.py if it using twisted.internet.reactor(Error: reactor already installed)
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
```
