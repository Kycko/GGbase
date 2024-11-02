from sys import exit as SYSEXIT

# базовые переменные приложения
app = {'title'  : 'GeoGuessr helper by Kycko',
       'version': 'v.000a',
       'size'   : (1000, 600)}
app   ['TV']    = app['title']+' '+app['version']   # название главного окна

# папки
dir = {'libs':'libs/'}
dir   ['pics'] = dir['libs']+'pics/'
dir['appPics'] = dir['pics']+'app/'

# изображения
# ↓ нельзя здесь создавать PhotoImage: нужны master-объекты
pic = {'appIcon':dir['appPics']+'app.ico'}

# спец. символы языков
uniqueSymbols = ('t1','t2','t3')    # пока что тестовые, потом заменить

# защита от запуска модуля
if __name__ == '__main__':
    print  ("This is module, please don't execute.")
    SYSEXIT()
