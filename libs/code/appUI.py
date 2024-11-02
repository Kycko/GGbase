from sys import exit as SYSEXIT
import  ttkbootstrap as TBS
import    globalVars as G

class Root(TBS.Window): # главное окно программы
    def __init__(self):
        super().__init__(title     = G.app['TV'],
                         themename = 'superhero',
                         minsize   = G.app['size'])
        self.iconbitmap(G.pic['appIcon'])
        self.state     ('zoomed')
        self.buildUI   ()
        self.mainloop  ()
    def buildUI(self):
        pass

# защита от запуска модуля
if __name__ == '__main__':
    print  ("This is module, please don't execute.")
    SYSEXIT()
