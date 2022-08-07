import numpy as np
import pypandoc
import re
import os

dictionary_of_features = {}
def docx2txt(dirname='14'):
    full_dirname = os.path.join('/home/andrey/datasets/doc_train/train/', dirname)
    array_of_path_docx = []
    text = ''
    for i in os.listdir(full_dirname):
        if re.fullmatch('[\s.\w]+.docx', i) is not None:
            array_of_path_docx.append(i)
    for i in array_of_path_docx:
        doc = pypandoc.convert_file(os.path.join(full_dirname, i), to='markdown-simple_tables', extra_args=['--wrap=none'])
        text += doc
    return text
text = docx2txt('1')

# Способ добычи нефти
def way_to_get_neft(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT1 = re.compile('УЭЦН')
    OBJECT2 = re.compile('однотруб[\w+] герметизир[\w+]')
    if re.search(OBJECT1, txt):
        return 'ЭЦН'
    elif re.search(OBJECT2, txt):
        return'напорная однотрубная герметизированная система сбора'
    else:
        return 'ЭЦН'

#Абсолютный мининум
def absolute_minimum(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT3 = re.compile('[аА]бсолют[\w\s]+миним[–\s\w,]+[.,\d]+\s*[°]*')
    if re.search(OBJECT3, txt):
        sentense = re.findall(OBJECT3, txt)
        return float('-'+''.join(re.findall(r'[\d]+[.,]*[\d]*', ' '.join(sentense))).replace(',', '.'))
    else:
        return np.NAN

#Абсолютный максимум
def absolute_maximum(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT4 = re.compile('[аА]бсолют[\w\s]+макс[-\s\w]+[+.,\d]+\s*[°]*')
    if re.search(OBJECT4, txt):
        sentense = re.findall(OBJECT4, txt)
        print(sentense)
        return float(''.join(re.findall(r'[\d]+[.,]*[\d]*', ' '.join(sentense))).replace(',', '.'))
    else:
        return np.NAN

#Среднемесячная температура самого холодного месяца
def mean_month_temperature(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT5 = re.compile('холодн[–\s\w,]+месяц[–\s\w,]+[.,\d]+\s*[°]*')
    if re.search(OBJECT5, txt):
        sentense = re.findall(OBJECT5, txt)
        return float('-'+''.join(re.findall(r'[\d]+[.,]*[\d]*', ' '.join(sentense))).replace(',', '.'))

    else:
        return np.NAN

#Средняя температура наиболее холодной пятидневки
def mean_temperature_of_coldest_fivedays(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT6 = re.compile('холодн[–\s\w,]+пятидневк[–\w\s]+[.,\d]+\s*[°]*')
    if re.search(OBJECT6, txt):
        sentense = re.findall(OBJECT6, txt)
        return float('-'+''.join(re.findall(r'[\d]+[.,]*[\d]*', ' '.join(sentense))).replace(',', '.'))
    else:
        return np.NAN

#Кол-во добывающих скважин
def number_of_getting_holes(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT = re.compile('Количество добывающих скважин[\s\шт.]+\d+')
    if re.search(OBJECT, txt):
        sentense = re.findall(OBJECT, txt)
        return int(''.join(re.findall(r'[\d]+[.,]*[\d]*', ' '.join(sentense))).replace(',', '.'))
    else:
        return np.NAN

#Кол-во нагнетательных скважин
def number_of_nagnetat_holes(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT = re.compile('Количество нагнетательных скважин[\s\шт.]+\d+')
    if re.search(OBJECT, txt):
        sentense = re.findall(OBJECT, txt)
        return int(''.join(re.findall(r'[\d]+[.,]*[\d]*', ' '.join(sentense))).replace(',', '.'))
    else:
        return np.NAN

#Газовый фактор, м3/т
def gas_factor(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT = re.compile('Газовый фактор[\D]+[3\s\D]+[.,\d]+')
    if re.search(OBJECT, txt):
        sentense = re.findall(OBJECT, txt)
        return float(''.join(re.findall(r'[\d]+[.,]+[\d]*', ' '.join(sentense))).replace(',', '.'))
    else:
        return np.NAN

#Добыча жидкости, тыс. м3 / год
def getting_of_liquid(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT = re.compile('Максимальный дебит куста скважин по жидкости[\D]+[3\s\D]+[.,\d]+')
    if re.search(OBJECT, txt):
        sentense = re.findall(OBJECT, txt)
        return float(''.join(re.findall(r'[\d]+[.,]+[\d]*', ' '.join(sentense))).replace(',', '.'))

    else:
        return np.NAN
#Добыча нефти, тыс. т / год
def getting_of_neft(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT = re.compile('Максимальный дебит куста скважин по нефти[\D]+[3\s\D]+[.,\d]+')
    if re.search(OBJECT, txt):
        sentense = re.findall(OBJECT, txt)
        return float(''.join(re.findall(r'[\d]+[.,]+[\d]*', ' '.join(sentense))).replace(',', '.'))

    else:
        return np.NAN
#Закачка воды, тыс. м3 / год
def zakachka_of_water(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT = re.compile('Максимальный объем воды на заводнение для системы ППД[\D]+[3\s\D]+[.,\d]+')
    if re.search(OBJECT, txt):
        sentense = re.findall(OBJECT, txt)
        return float(''.join(re.findall(r'[\d]+[.,]+[\d]*', ' '.join(sentense))).replace(',', '.'))

    else:
        return np.NAN
#Вариант прокладки нефтепроводов
def variant_procladki_nefteprovodov(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT1 = re.compile('[пП]роклад[\w\s]+подземн')
    OBJECT2 = re.compile('[пП]роклад[\w\s]+надземн')
    if re.search(OBJECT1, txt):
        return 'подземный'
    elif re.search(OBJECT2, txt):
        return 'надземный'
    else:
        return np.NAN
#Куст
def cust(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT = re.compile('[кК]уст[\s(скважин)]*[№\s]+[\d]+')
    if re.search(OBJECT, txt):
        sentense = re.findall(OBJECT, txt)
        print(sentense)
        return int(''.join(re.findall(r'[\d]+', ' '.join(sentense))[0]))

    else:
        return np.NAN


def type_of_building(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT1 = re.compile('ново[\w\s]+строительство')
    OBJECT2 = re.compile('реконструкц')
    if re.search(OBJECT1, txt):
        return 'новое'
    elif re.search(OBJECT2, txt):
        return 'реконструкция'
    else:
        return np.NAN
def area_of_seysmic(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT1 = re.compile('не сейсмоопасн')
    OBJECT2 = re.compile('сейсмичн[\w\s]+ \d')
    if re.search(OBJECT1, txt):
        return 'не сейсмоопасный'
    elif re.search(OBJECT2, txt):
        sentense = re.findall(OBJECT2, txt)
        return int(sentense[0][-1])
    else:
        return np.NAN

def level_of_responsibility(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT1 = re.compile('повышенн[\w\s]+уров[\w\s]+ответств')
    if re.search(OBJECT1, txt):
        return 'повышенный'
    else:
        return np.NAN
def type_of_energy_suplement(name_of_directory):
    txt = docx2txt(name_of_directory)
    OBJECT = re.compile('блочно-модульн[\w\s]+двухтрансформаторн')
    if re.search(OBJECT, txt):
        return 'внешний'
    else:
        return np.NAN

print(text)
print(zakachka_of_water('1'))
print(cust('6'))














