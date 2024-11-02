from sys import exit as SYSEXIT

# надписи элементов интерфейса (labels, labelFrames[lfr], buttons, checkBoxes, toolTips)
layout = {'root':{'lang':{'lfr' :'  Языковая группа  ',
                          'vars':{'en' :'English',
                                  'fr' :'Français',
                                  'es' :'Español',
                                  'lat':'другие Latin',
                                  'cyr':'Кириллица',
                                  'ch' :'中国人 (китайский)',
                                  'kor':'한국인 (корейский)',
                                  'jap':'日本語 (японский)',
                                  'ind':'भारतीय (хинди)',
                                  'ar' :'الأبجدية العربية (арабский)',
                                  'izr':'יִשׂרְאֵלִי (иврит)'}},
                  'symb':{'lfr' :'  Символы  '}}}

# защита от запуска модуля
if __name__ == '__main__':
    print  ("This is module, please don't execute.")
    SYSEXIT()
