import os

ubicacion_carpeta = "C://NORMALIZAR"

try:
    os.makedirs(ubicacion_carpeta, exist_ok=True) 
    print("Carpeta NORMALIZAR creada.")
except PermissionError:
    print("No tiene permiso para crear la carpeta.")
except Exception as e:
    print("Ocurrió un error:", e)

ubicacion_libro = "C://NORMALIZAR/libro.txt"

historia = """eL oRiGeN eS uNa nOveLa dE mIsTeRiO y sUsPeNsO dE dAn bRoWn qUe cUeNtA lA hIsToRiA
dE rObErT lAnGdOn, uN sYmBoLoGiStA qUe sE vE eNvUeLtO eN uN cOmPlOt qUe pOdRíA cAmBiAr eL rUmBo
dE lA hUmAnIdAd.

EL LIBRO SE DESARROLLA EN ESPAÑA, ESPECÍFICAMENTE EN CIUDADES COMO BILBAO, MADRID Y
BARCELONA, Y MEZCLA ELEMENTOS DE ARTE, RELIGIÓN Y TECNOLOGÍA.

en esta historia, langdon asiste a una presentación de su amigo edmond kirsch, un futurista que afirma haber
descubierto el origen y el destino de la humanidad.

El OrIgEn dE lA hUmAnIdAd y sU dEsTiNo sOn tEmAs cEnTrAlEs qUe gUiAn lA tRama y lOs dEsAfÍoS qUe lOs
pErSoNaJeS dEbEn eNvEnTaR pArA lLeGaR a lA vErDaD.

a tRaVéS dE cOdIgOs, pIsTaS y eNiGmAs, lAnGdOn y aMbRa vIdAl, lA dIrEcToRa dE uN mUsEo, tRaTaN dE
eScApAr dE sUs pErSeGuIdOrEs mIeNtRaS rEvElAn eL mEnSaJe dE kIrScH.

uNa mEzClA dE fIcCiÓn, cOnSpIrAcIóN y cIeNcIa hAcE dE eStA nOvElA uNa aTrAyEnTe rEfLeXiÓn sObRe lA fE y
lA rAzÓn.

pOr lAs cAlLeS dE bArCeLoNa y dEnTrO dE lA sAgRaDa fAmIlIa, lOs pRoTaGoNiStAs vIvEn uNa cArReRa
cOnTrA eL tIeMpO pArA rEvElAr lA vErDaD.

eL oRiGeN iNvItA a lOs lEcToReS a cUeStIoNaRsE sObRe lAs cReEnCiAs rElIgIoSaS y lOs aVaNcEs
tEcNoLóGiCoS qUe pOdRíAn rEvOlUcIoNaR eL mUnDo.

a lO lArGo dE sUs cApÍtUlOs, eL lIbRo mAnTiEnE eL sUsPeNsO y sOrPrEnDe cOn gIrOs iNeSpErAdOs qUe
cOnViErTeN lA lEcTuRa eN uNa eXpErIeNcIa úNiCa.

eL fInAl dE eL oRiGeN pRoPoNe uNa vIsIóN sObRe lA eVoLuCiÓn y eL pApEl dE lA iNtElIgEnCiA aRtIfIcIaL eN
nUeStRo fUtUrO, dEjAnDo a lOs lEcToReS cOn pReGuNtAs pRoFuNdAs y rEfLeXiOnEs."""

with open(ubicacion_libro, 'w') as archivo:
    archivo.write(historia)

with open("C://NORMALIZAR/libro.txt", 'r') as original:
    texto_original = original.read()

with open("C://NORMALIZAR/libro2.txt", 'w') as copia2:
    copia2.write(texto_original)

with open("C://NORMALIZAR/libro3.txt", 'w') as copia3:
    copia3.write(texto_original)

with open("C://NORMALIZAR/libro.txt", 'r') as archivo:
    lineas = archivo.readlines()

with open("C://NORMALIZAR/libro.txt", 'w') as archivo:
    for linea in lineas:
        archivo.write(linea.strip().capitalize() + "\n")

with open("C://NORMALIZAR/libro2.txt", 'r') as archivo:
    texto = archivo.read()

with open("C://NORMALIZAR/libro2.txt", 'w') as archivo:
    archivo.write("VICENTE ROJAS\n")
    archivo.write(texto.upper())  # Todo el texto en mayúsculas

with open("C://NORMALIZAR/libro3.txt", 'r') as archivo:
    texto = archivo.read()

with open("C://NORMALIZAR/libro3.txt", 'w') as archivo:
    archivo.write(texto.lower())  # Todo en minúsculas

with open("C://NORMALIZAR/libro.txt", 'r') as archivo1:
    texto1 = archivo1.read()

with open("C://NORMALIZAR/libro2.txt", 'r') as archivo2:
    texto2 = archivo2.read()

if texto1 == texto2:
    print("Los archivos libro.txt y libro2.txt son iguales.")
else:
    print("Los archivos libro.txt y libro2.txt son diferentes.")
