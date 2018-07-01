import urllib.request
permittedChars = '._-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

url = 'http://www.deinfo.ufrpe.br/br/docentes'
html = str(urllib.request.urlopen(url).read())
#substitui todos os [at] por @
html = html.replace("[at]", "@")
html = html.replace("(at)", "@")
#grava os índices de todos os @ da str html
indexArroba = [pos for pos, char in enumerate(html) if char == "@"]

emailList = []

#esta funcão escaneia os caracteres antes e depois do @ procurando por caracteres não permitidos e inserindo o email na lista principal
def parseemail(index):
    listAntes = []
    listDepois = []
    strAntes = ""
    strDepois = ""
    count = 1
    while(1):
        if html[index-count] in permittedChars:
            listAntes.append(html[index-count])
            count += 1
        else:
            strAntes = strAntes.join(listAntes[::-1])
            break
    count = 1
    while (1):
        if html[index + count] in permittedChars:
            listDepois.append(html[index + count])
            count += 1
        else:
            strDepois = strDepois.join(listDepois)
            break

    if "." not in strDepois:
        return None
    else:
        emailList.append(strAntes+"@"+strDepois)

for index in indexArroba:
    parseemail(index)
print("Foram escaneados " + str(len(emailList)) + "emails!")
print("Lista de emails: ")
print(emailList)
