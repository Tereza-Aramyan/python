'''
 Mutable-String: Manual implementations of functions
'''


from collections.abc import MutableSequence
import string


class MutableString(MutableSequence):
    def __init__(self, item=None):
        self.item = item

    def __getitem__(self, index):
        return self.item[index]

    def __setitem__(self, index, value):
        ref = list(self.item)
        ref[index] = value
        self.item = ''.join(ref)

    def __str__(self):
        return str(self.item)

    def __len__(self):
        return len(self.item)

    def __iter__(self):
        for i in self.item:
            print(i)

    def __repr__(self):
        return self.item

    def __add__(self, string):
        self.item = f'{self.item}{string}'
        return self.item

    def __radd__(self, other):
        pass

    def __delitem__(self, key):
        pass

    def insert(self, index: int, value):
        pass


    def title(self):
        new_lst = tuple(self.item[i].upper() if(self.item[i-1] == ' ' or self.item[i-1].isdigit()) else self.item[i] for i in range(1, len(self.item)))
        return f'{self[0].upper()}{"".join(new_lst)}'


    def capitalize(self):
        return f'{self.item[0].upper()}{self.item[1:].lower()}'

    def center(self, width, fill=None):
        if (fill == None):
            fill = ' '
        return f'{width//2*fill}{self.item}{(width-width//2)*fill}'

    def upper(self):
        return ''.join([chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char for char in self.item])

    def lower(self):
        return ''.join([chr(ord(char) + 32) if 65 <= ord(char) <= 90 else char for char in self.item])

    def startswith(self, string):
        flag = tuple(True for i in range(len(self.item)) if(self.item[0:i] == string))
        if(len(flag) == 0):
            return False
        return flag[0]

    def endswith(self, string):
        flag = tuple(True for i in range(len(self.item)-1,-1,-1) if(self.item[i:len(self.item)] == string))
        if(len(flag) == 0):
            return False
        return flag[0]

    def finding(self,c,start=None, end=None):
        if(end==None):
            end = len(self)-1
        if(start==None):
            start = 0
        matched_list = []
        for i in range(start,end):
            if(self.item[i] == c[0]):
                if((self.item[i] == c[0]) & (i + len(c) -1 <= end)):
                    if(self.item[i+len(c)-1]==c[-1:]):
                        flag = 1
                        for j in range(1,len(c)-2):
                            if(c[j]!=self.item[i+j]):
                                flag = 0
                                break
                        if(flag==1):
                            matched_list.append(i)
                            i += end-1
        return matched_list


    def find(self, string, start=None, end=None):
        res = MutableString.finding(self,string,start,end)
        if(len(res) == 0):
            return -1
        return res[0]

    def rfind(self, s, start=None, end=None):
        res = MutableString.finding(self,s,start,end)
        if(len(res) == 0):
            return -1
        return res[-1]

    def index(self, string, start=None, end=None):
        res = MutableString.finding(self,string,start,end)
        if(len(res) == 0):
            raise ValueError('substring not found')
        return res[0]

    def rindex(self, string, start=None, end=None):
        res = MutableString.finding(self,string,start,end)
        if(len(res) == 0):
            raise ValueError('substring not found')
        return res[-1]

    def split(self, symbol: str):
        new_list = []
        flag = 0
        for i in range(len(self.item)-1):
            if (self.item[i] == symbol):
                new_list.append(self.item[flag:i])
                flag = i+1

        new_list.append(self[flag:])
        if (len(new_list) == 0):
            new_list.append(self)
        return new_list

    def rreplace(self, old, new):
        pass

    def replace(self, old, new):
        res = MutableString.finding(self,old)
        if(len(res) == 0):
            return self

        new_item = f'{self.item[:res[0]]}'
        for el in range(1,len(res)):
            app_str = self.item[res[el-1]+len(old):res[el]]
            new_item = f'{new_item}{new}{app_str}'

        self.item = f'{new_item}{new}{self.item[res[-1]+len(old):]}'
        return self.item

    def ref(self, to_check: str):
        flag = True
        for el in self.item:
            if(str(el) not in to_check):
                flag = False
        return flag

    def isdigit(self):
         return (MutableString.ref(self, string.digits))

    def isalpha(self):
        return (MutableString.ref(self, string.ascii_letters))

    def isalnum(self):
        to_search = f'{string.ascii_letters}{string.digits}'
        return (MutableString.ref(self, to_search))

    def islower(self):
        return (MutableString.ref(self, string.ascii_lowercase))

    def isupper(self):
        return (MutableString.ref(self, string.ascii_uppercase))

    def isspace(self):
        return (MutableString.ref(self, string.whitespace))

    def istitle(self):
        flag = True
        item_list = self.item.split(' ')
        for el in item_list:
            if((str(el)[0] not in string.ascii_uppercase) & (str(el) not in string.punctuation)):
                flag = False
        return flag

    def join(self, iterable):
        new_str = self[0]
        for i in range(1, len(self)):
            new_str = f'{new_str}{iterable}{self.item[i]}'
        return f'{new_str}'

    def format(self, * args, ** kwargs):
        new_str = self.item
        self.item = new_str.format(*args, **kwargs)
        return self.item

    def ord(self, c):
        return ord(c)

    def chr(self, d):
        return chr(c)

    def count(self, string, start=None, end=None):
        res = MutableString.finding(self,string,start,end)
        return len(res)

    def lstrip(self, c=' '):
        start = 0
        while self.item[start] in list(c):
            start += 1
        return self.item[start:]

    def rstrip(self, c=' '):
       end = -1
       while self.item[end] in list(c):
          end -= 1
       if(end == -1):
           return self.item
       return self.item[:end+1]


    def strip(self, c=' '):
        start = 0
        while self.item[start] in list(c):
            start += 1
        end = -1
        while self.item[end] in list(c):
            end -= 1
        if(end == -1):
            end = len(self.item)-1

        result = f'{self[start:end+1]}'
        return result


if __name__ == "__main__":

    text = MutableString('sdsghd kl')
    #print(text.__getitem__(3))
    #text.__setitem__(0,'t')
    #print(text)
    #print(text.__str__())
    #print(text.__len__())
    #text.__iter__()
    #print(text.__repr__())
    #print(text.__add__(' tereza'))
    #text.title()
    #t =MutableString('l')
    #print(text.upper())
    #print(text.lower())
    #print(t.isdigit())
    #print(t.isalnum())
    #print(t.isalpha())
    #print(t.islower())
    #print(t.isupper())
    #print(t.isspace())
    #print(text.title())
    #print(text.capitalize())
    #print(text.center(7,'>>'))
    #print(text.startswith('sd'))
    #print(text.startswith('sk'))
    #print(text.endswith(' kl'))
    #print(text.endswith('dkl'))
    #print(text.find('gh'))
    #print(text.find('gh',4,8))
    #text2 =MutableString('Lgh Agh Ugh')
    #print(text2.rfind('gh'))
    #print(text2.index('gh'))
    #print(text2.index('kk'))
    #print(text2.rindex('gh'))
    #print(text2.rindex('kk'))
    #print(text2.split('a'))
    #print(text2.replace('gh','t'))
    #print(text2.istitle())
    #text_list =MutableString(["aaa",2,"g"])
    #print(text_list.join('>>'))
    #print(text2.count('gh'))
    #print(text2.count('gh',5,8))
    #text3 =MutableString('Lgh {} Agh Ugh')
    #print(text3.format('as'))
    #text4 = MutableString('this is good    ')
    #print(text4.rstrip())
    #print(text4.rstrip('h'))
    #print(text4.rstrip('sid oo'))
    #text5 = MutableString('   this is good ')
    #print(text5.lstrip())
    #print(text5.lstrip('sti'))
    #print(text5.lstrip('s ti'))
    text6 = MutableString('  wire [127:0] debug_ok_to_block_sysbus')
    print(text6.strip('     ;,'))
    print(text6.strip(' xoe'))
    print(text6.strip('stx'))