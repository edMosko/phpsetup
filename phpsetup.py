import os
import shutil

print ("Processing...")
phporigin = "/home/edmosko/Documents/dev/php"
patho = phporigin + "/"
patht = "/var/www/"


phpfiles=[]
dirs=['']
for place in dirs:
    for file in os.listdir(phporigin+place):
        try:
            os.listdir(phporigin + place + '/' + file)
            dirs.append(place + '/' + file)
        except:
            pass
        i = 0
        while (i < len(file)):
            if file[i:]=='.php':
                phpfiles.append(place + '/' + file)
                break
            i += 1


for php in phpfiles:
    document = []
    file = open((phporigin+php),'r', encoding="utf-8")
    isphp = '0'
    array = []
    for line in file:
        linea=[]
        i = 0
        while (i<(len(line))):
            linea.append(line[i])
            i+=1
        line=""
        if (isphp == '1'):
            i = 0
            while (i < len(linea)):
                if (linea[i:]==['?','>','\n']):
                    isphp = '0'
                    break
                i += 1
        pass
        if (isphp == '1'):
            if (linea[(len(linea)-2)]==';'):
                pass
            else:
                linea[(len(linea)-1)]=';'
                linea.append('\n')
        else:
            i = 0
            while (i < len(linea)):
                if (linea[i:]==['<','?','p','h','p','\n']):
                    isphp = '1'
                    break
                i += 1
        for char in linea:
            line += char
        document.append(line)
    file.close()
    file = open((phporigin+php),'w', encoding="utf-8")
    file.truncate(0)
    file.writelines(document)
    file.close()


shutil.rmtree(patht)
shutil.copytree(patho, (patht+"html"))
print("Success!")
