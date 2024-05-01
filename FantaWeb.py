import webbrowser

class Browser(object):
    def openPage(url: str):
        webbrowser.open(url)

    def openNewPage(url: str):
        webbrowser.open_new_tab(url)

    def openNewSession(url: str):
        webbrowser.open_new(url)