# erstes Tutorial
# die tutorial reihe die ich nutze, nutze ich nur als inspiration und mache die sachen nicht nach, sondern
# nutze es nur als quelle für Dinge, die ich ausprobeire

def funwithnumber(zahl):
    zahl
    print("das ist der Wert bei der Initialisierung")
    print(zahl)
    zahl = zahl*2
    print("zahl nach der multiplikation mit sich selbst und 2")
    print(zahl)
    zahl = zahl/3
    print("das ist zahl nach einer Division durch 3")
    print(zahl)
    zahl= zahl -8  
    print("das ist deine zahl minus 8")
    print(zahl)
    zahl = zahl+5*3
    print("das ist zahl mit addition von 5 und mulitplikation 3 - kucken wegen punkt vor strich")
    print(zahl)
    zahl= zahl%6
    print("das ist der Rest bei einer division durch 6")
    print(zahl)
    zahl = zahl**3
    print("das ist zahl hoch 3")
    print(zahl)
# führt einige operationen durch +-/Rest hochx

def funwithstring(zeichenkette):
    print("willkommen bei spass mit String")
    print(zeichenkette+"<-das ist deine zeichenkette")
    print(zeichenkette +"\n" +zeichenkette)
    print(zeichenkette + r"\n" +zeichenkette)
# macht paar dinge mit dem String, den man eigegeben hat

def funwithlisten():
    print("willkommen viel spaß mit Listen")

while(): # damit man auch mehrere runden drehen kann, ohne dass das programm beendet
    while(): # damit man die chance bei einer flaschen eingabe hat, noch mal von vorne zu beginnen
        match input("willst du spass mit zahlen, druecke 1 oder willst du spass mit String, dann drueck 2"):
            case 1:
                funwithnumber(int(input("gib eine zahl ein")))
                break
            case 2:
                funwithstring(input("gib eine beliebige zeicehnkette ein"))
                break
            case _:
                print("falsche Eingabe")
    while(): # damit man noch mal eine runde weiter spielen kann, wird man in der schleife gefragt,
             # ob man weiterpsielen will
        match input("willst du noch mal spielen j=ja n=nein"):
            case "y":
                print("viel spaß")
            case "n":
                print("bis später")
                break
            case _:
                print("richtiger spaß vogel aber ich habe ewig zeit")
# ansich könnte man das n case raus nehmen und es im schleifen kopf als == n deklarieren,
# um es als abbruch bedingung zu nutzen
                

print("öüäß") # war nur zum testen, weil die IDE es makiert