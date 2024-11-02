from sys import exit as SYSEXIT
import  ttkbootstrap as TBS
import    globalVars as G
import       strings as S

class Root(TBS.Window): # главное окно программы
    def __init__(self):
        super().__init__(title     = G.app['TV'],
                         themename = 'superhero',
                         minsize   = G.app['size'])
        self.iconbitmap(G.pic['appIcon'])
        self.state     ('zoomed')
        self.buildFrame('root')
        self.mainloop  ()
    def buildFrame(self,type:str,parent=None):
        # parent и frMain = TBS.Frame либо TBS.Labelframe
        if   type == 'root':
            self.frRoot = TBS.Frame(self)
            self.frRoot.pack(fill='both',expand=True,padx=5,pady=5)
            self.buildFrame ( 'rFilters',self.frRoot)   # 'r...' = root
            self.buildFrame ( 'rResult' ,self.frRoot)
        elif type == 'rFilters':
            frMain = TBS.Frame(parent)
            frMain    .pack(anchor='n',fill='x',pady=5)
            self.buildFrame('fLang',frMain) # 'f...' = filters
            self.buildFrame('fSymb',frMain)
        elif type == 'rResult':
            frMain = TBS.Frame(parent)
            frMain    .pack(anchor='s',fill='x',pady=5)
            # self.buildFrame('rLang',frMain)
        elif type == 'fLang':
            strings =   S.layout['root']['lang']
            frMain  = TBS.LabelFrame(parent,text=strings['lfr'])
            frMain.pack(side='left',padx=5,ipady=5)
            for id,lang in strings['vars'].items():
                TBS.Button(frMain,
                           text    = lang,
                           width   = 30,
                           command = lambda id=id:self.filterClicked('lang',id)
                           ).pack(padx=10,pady=5)
        elif type == 'fSymb':
            frMain  = TBS.LabelFrame(parent,text=S.layout['root']['symb']['lfr'])
            frMain.pack(side='left',anchor='n',padx=5,ipady=5)
            for symb in G.uniqueSymbols:
                TBS.Button(frMain,
                           text    = symb,
                           command = lambda id=symb:self.filterClicked('symb',id)
                           ).pack(side='left',padx=5,pady=5)

    # функции выбора фильтров (sel = select)
    def filterClicked(self,type:str,id:str):
        pass

# защита от запуска модуля
if __name__ == '__main__':
    print  ("This is module, please don't execute.")
    SYSEXIT()
