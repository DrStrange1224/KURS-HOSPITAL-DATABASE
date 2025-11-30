import sys
from newapp import *

def main():
    DBParser.init('config.ini', 'postgresql')
    
    app = QApplication(sys.argv)

    window = TableViewWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()