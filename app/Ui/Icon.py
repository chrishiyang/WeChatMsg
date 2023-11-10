from PyQt5.QtGui import QIcon


class Icon:
    Default_avatar_path = './app/data/icons/default_avatar.svg'
    MainWindow_Icon = QIcon('./app/data/icons/logo.svg')
    Default_avatar = QIcon(Default_avatar_path)
    Output = QIcon('./app/data/icons/output.svg')
    Back = QIcon('./app/data/icons/back.svg')
    ToDocx = QIcon('app/data/icons/word.svg')
    ToCSV = QIcon('app/data/icons/csv.svg')
    ToHTML = QIcon('app/data/icons/html.svg')