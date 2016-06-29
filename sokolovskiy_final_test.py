import re
import os

def reading(way):
    text = open(way, 'r', encoding='utf-8')
    text1 = text.read()
    regexp = '[А-Я]\. ?[А-Я][а-я]*[  ),!?"]'
    names  = re.findall(regexp, text1)
    print('1. все имена в формате "инициал+фамилия":\n')
    for elem in names:
        elem2 = elem.strip('!.,?;:{}[]() <>:+_-–=*/\"#')
        print(elem2)
    print('\n\n')

def reading2(way):
    text = open(way, 'r', encoding='utf-8')
    text1 = text.read()
    regexp = '((?:[А-Я]\. ?(?:[А-Я]\. ?)?[А-Я][а-я]*[ ,)!?"])|(?:[А-Я][а-я]* [А-Я][а-я]*[ ,)"!?]))'
    names  = re.findall(regexp, text1)
    names2 = []
    print('2. вообще все имена в формате "инициал(ы)+фамилия" или "имя+фамилия":\n')
    for elem in names:
        elem2 = elem.strip('!.,?;:{}[]() <>:+_-–=*/\"#')
        names2.append(elem2)
        print(elem2)
    return names2

def making_seconds(names, way):
    second = []
    for elem in names:
        arr = elem.split(' ')
        try:
            arr.remove('')
        except ValueError:
            pass
        second.append(arr[-1])
    return second

def making_firsts(names, way):
    firsts = []
    for elem in names:
        arr = elem.split(' ')
        try:
            arr.remove('')
        except ValueError:
            pass
        try:
            arr.remove(arr[-1])
        except ValueError:
            pass
        firsts.append(''.join(arr))

    array2 = []
    for element in firsts:
        if element not in array2:
            array2.append(element)
    return array2

def destroy_same(array):
    array2 = []
    for element in array:
        if element not in array2:
            array2.append(element)
    return array2

def destroy_same2(array):
    array2 = []
    for element in array:
        if element not in array2:
            array2.append(element)
    return array2

def make_folds(seconds):
    for second in seconds:
        try:
            os.makedirs(second)
        except OSError:
            pass

def m_dic(names, way):
    txt0 = open(way, 'r', encoding='utf-8')
    txt = txt0.read()
    a = re.findall('[A-Я].*(?:[.!?\n]?)', txt)
    dic = {}
    for elem in names:
        for element in a:
            if re.search(elem, element):
                dic[elem] = element
    for el in dic:
        pass
        
        
def making_txts(seconds, firsts, names):
    for root, dirs, files in os.walk('.'):
        pass               

def main():
    val = reading('wiki.txt')
    val1 = reading2('wiki.txt')
    val2 = making_seconds(val1, 'wiki.txt')
    u_firsts = making_firsts(val1, 'wiki.txt')
    u_seconds = destroy_same(val2)
    u_names = destroy_same2(val1)
    fol = make_folds(u_seconds)
    txt = making_txts(u_seconds, u_firsts, u_names)
    valX = m_dic(u_names, 'wiki.txt')


if __name__ ==  '__main__':
    main()


