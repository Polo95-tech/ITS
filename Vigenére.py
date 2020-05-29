#Variablen in allen Funktionen Bereitstellen
abc = "abcdefghijklmnopqrstuvwxyz"
letter_to_index = dict(zip(abc,range(len(abc))))
index_to_letter = dict(zip(range(len(abc)),abc))
##Entschlüsselt ein Text mit laenge n & schlüssel key
def entschluesseln(key,text,laenge):
    hilfstext = ""
    #Einmal entschüsseln & Häufigkeit wiederholen
    # Entschlüsseln
    split_cipher = [text[i:i +len(key)] for i in range(0,laenge,len(key))]
    for j in split_cipher:
        i = 0
        for x in j:
            number = (letter_to_index[x]-letter_to_index[key[i]]) % len(abc)
            hilfstext += index_to_letter[number]
            i += 1
    return hilfstext
##Verschlüsselt ein Text mit laenge n & schlüssel key
def verschlüsseln(key,text,laenge):
    hilfstext = ""
    #Einmal entschüsseln & Häufigkeit wiederholen
    # Entschlüsseln
    split_cipher = [text[i:i +len(key)] for i in range(0,laenge,len(key))]
    for j in split_cipher:
        i = 0
        for x in j:
            number = (letter_to_index[x]-letter_to_index[key[i]]) % len(abc)
            hilfstext += index_to_letter[number]
            i += 1
    return hilfstext
#Findet das Maximum der Häufigkeit bzw. die Stelle
def stelle_ermitteln(ez):
    max1 = ez[0]
    for j in range(0,26):
        if max1 < ez[j]:
            max1 = ez[j]
            stelle = j
    return (stelle)
def haeufigkeit_bestimmen(laenge,text):
    anzahl = [0] *26
    for i in range(0,26):
        for j in range(0,laenge):
            if text[j] == abc[i]:
                anzahl[i] = anzahl[i] + 1
    return (anzahl)
def schluessellaenge_bestimmen(laenge,anzahl):
    #Hier zu Friedmantest anwenden
    zähler = 0
    nenner = 0
    Id = 0.076 #Koinzidenzindex des deutschen Sprache
    Iz = 0.038 #Kehrwert der unterschiedlichen auftretenden buchstaben 1/26
    #Koinzidenzindex Ic bestimmen 
    hilfsarray = [0.0]*2
    #Zähler ist die Summe aus der Multiplikation der Häufigkeiten an Buchstaben des Chiffrats
    for i in range(0,26):
        zähler = zähler + (anzahl[i]*(anzahl[i]-1))
    #Nenner ergbit sich aus der Länge des Chifferats multipliziert mit der Länge-1
    nenner = laenge * (laenge-1)
    #Hier wird Ic des Chiffrats bestimmt
    hilfsarray[0] = (zähler/nenner)
    #Schlüssel länge bestimmen aus der Umgestellen Formal des Friedmantests
    #k = (Id - Iz) * n / ( Ic * (n - 1) - Iz * n + Id ) ==> n = laenge des texts 
    hilfsarray [1]= ((Id-Iz)*laenge)/((hilfsarray[0]*(laenge-1))-(Iz*laenge)+Id)
    return (hilfsarray)
def haeufigkeitsanalyse(text,ea,laenge,schluessellaenge):
    ##Häufikeitsanalyse länge des schlüssels wiederholen
    GH = [""]*int(schluessellaenge)
    index = 0
    EA=[[0 for x in range(26)] for y in range(int(schluessellaenge))] 
    stelle = [0]*int(schluessellaenge)
    key=""
    #Text in einzel Alphabete teilen
    for j in range(0,int(schluessellaenge)):
        for x in range(0+index,index+ea):
            GH[j] += text[x]
        index += ea
        if index > int(laenge*2/3):
            index = int(laenge*2/3)
    #Häufigkeiten der Einzelalphabete
    for x in range (0,int(schluessellaenge)):
        for i in range(0,26):
            for j in range(0,len(GH[x])):
                if GH[x][j] == abc[i]:
                    EA[x][i] = EA[x][i] + 1
            EA[x][i] = (EA[x][i]/len(GH[x]))*100
    #print(EA)
    for i in range(0,int(schluessellaenge)):
        stelle[i]=stelle_ermitteln(EA[i])
    return(stelle)
def vigenere_quadrat_erstellen():
    #Vigenére-Quadrat erstellen
    quadrat = [""] *26
    index = -1
    index2 = -1
    for i in range(0,26):
        index += 1 
        for j in range(0,26):
            if j+index < 26:
                quadrat[i] += chr(97+index+j)
            else:
               quadrat[i] += chr(97+index2)
               index2 +=1
        index2 = 0 
    return(quadrat)
def schreib_in_datei(text,key,laenge,werte):
    l = int(laenge/(len(key)))
    if l%2 !=0:
        l += 1
    TEXT = [""]*l
    index=0
    for j in range(0,len(key)):
        for x in range(0+index,index+l):
            TEXT[j] += text[x]
        index += l
        if index > int(laenge*2/3):
            index = int(laenge*2/3)
    datei = open('F:/Studium/FH-SWF/6. Semster/IT_Sicherheit/Übung/Übung3/loesung.txt','w')
    datei.write("Textlänge: "+str(laenge))
    datei.write("\nKonistenzindex lautet: "+ str(format(werte[0]*100,'.2f'))+"%")
    datei.write("\nSchlüssellänge lautet: "+ str(format(werte[1],'.0f')))
    datei.write("\nSchlüsselwort lautet: "+key)

    datei.write("\nLösungstext: \n")
    for i in range(0,len(key)):
        datei.write("\n"+TEXT[i])

def main():
    ##Benötigte Variablen
    #Eingabe text aus der Aufgabe 1
    text = "kjegimoeugcmoemgcbkxmojlovpgkbkjqksmtactxmmvqycmoectupgkbkjqkcqkseovmoemslbzvzoyzkbqtumxcqkspgkmoemykimvacftrkmyzmoelkeegclaelllbzvznftkelgiqkwaovircmyzmhvvnvzhvqaelygzgtprzmhvsoelkiqiyeoctnzvglaoelkeegclyvqjrclvcxvznlbbfzjvucftlnmtemxymxvqtbwsdbyfnxzaykmxvciyircmszbnrczlvjyigimxmmxjbkctzjqiywlkihvzgeakzvkizglpkeazzusvctuitjmoemtjknnixqmtwckjakeekilkkqniqnemxbmtemtuqkxmojtkzvyrozvvrzmhvuakbkieoieuctkectjaiywtzvgtpzemndmtzpxbwkevzfptvauiokwwxkokymtuisvkqvzzvlovirkmaelsrknkmyzknxmziwykiawlkeekx"
    text=text.lower()
    anzahl = [0] *26
    hilfstext = ""
    original = text
    wertbestimmung = [0.0] * 2
    key = ""
    #Länge bestimmen
    laenge= len(text)
    #Häufigkeit bestimmen
    anzahl = haeufigkeit_bestimmen(laenge,text)
    #Kositenzbestimmen + Schlüssellänge
    wertbestimmung = schluessellaenge_bestimmen(laenge,anzahl)
    #Aufteilung des Chifferat in Einzelalphabete
    ea = int(laenge/wertbestimmung[1])
    if ea % 2 != 0:
        ea += 1
    ##Häufikeitsanalyse länge des schlüssels wiederholen
    stelle = haeufigkeitsanalyse(text,ea,laenge,wertbestimmung[1])
    #Schlüssel zusammensetzten 4 entspricht dem häufigsten Buchstaben des deutschen ABC ==> e 
    index = int(wertbestimmung[1])-1
    for i in range (0,int(wertbestimmung[1])):
        key += abc[stelle[index]-4]
        index -= 1
    text=entschluesseln(key,original,laenge)
    ##Ausgabenn
    print ("Textlänge: " + str(laenge))
    print ("Konistenzindex lautet: "+ str(format(wertbestimmung[0]*100,'.2f'))+"%")
    print ("Schlüssellänge lautet: "+ str(format(wertbestimmung[1],'.0f')))
    print("Schlüsselwort lautet: "+key)
    print("Lösungstext: ")
    print("")
    print(text)
    print("")
    #Lösung in eine Text Dateischreiben
    schreib_in_datei(text,key,laenge,wertbestimmung)
   
    
if __name__ == "__main__":
    main()







