class Col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def text_prog(soup, h):
    i = ""
    if h.find('i') is not None:
        i = h.find('i').text
        h.find('i').decompose()
    else:
        i = Col.HEADER + "présent dans les favoris" + Col.ENDC
    s = h.text + " -> " + i
    return s


def print_prog(soup, d):
    s = Col.WARNING + "\t-sans programme-" + Col.ENDC
    for j in range(len(soup)):
        if soup[j].find_all('input')[1].get('value') == d:
            s = text_prog(soup, soup[j].find('h4'))
            return Col.OKGREEN + "\t" + s + Col.ENDC
    return s


def while_valid_number(dic):
    x = 0
    while True:
        s = input()
        if s.isnumeric():
            x = int(s)
            if not (0 < x < len(dic) + 1):
                print(Col.FAIL + "Ce nombre n'est pas dans la liste," + Col.OKBLUE + " test un autre: ",
                      end='' + Col.ENDC)
            else:
                return x
        else:
            print(
                Col.FAIL + "Fait un effort, ce n'est même pas un nombre ça : " + s + ", " + Col.OKBLUE + "test 1 "
                                                                                                         "idiiiiot: ",
                end='' + Col.ENDC)
