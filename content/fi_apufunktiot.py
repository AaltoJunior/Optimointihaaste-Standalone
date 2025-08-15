import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

img_happy = mpimg.imread('../../img/kuvitus_2.png')
img_fustrated=mpimg.imread('../../img/kuvitus3.png')


def eventit(tiedosto):
    try:
        oikea= len(tiedosto)
        event=input("Montako tapahtumaa datassa on? \n")
        if event=='skip': return False
        elif int(event)==oikea: #eka testi ok
            print("Oikea vastaus! \n")
            return False
        else: 
            print("Tapahtumien lukumäärä oli väärä, kokeilkaa uudestaan.")
            return True
    except:
        print("Jotain pielessä tarkistuksessa, kysykää assarilta apua.\n")
        return True   


def maksimiE(tiedosto):
    try:
        tied = tiedosto
        oikea = max(max(tied['E1']),max(tied['E2']))
        melkein = min(max(tied['E1']),max(tied['E2'])) #vain toinen data otettu huomioon
        #oppilaan laskema maksimi:
        maks = input("Myonin maksimi energia datassa? Käytä desimaalierottimena pistettä.\n")
        if maks=='skip': return False
        elif round(float(maks), 2) == round(oikea, 2): 
            print("Oikea vastaus! \n")
            return False
        elif round(float(maks), 2) == round(melkein, 2):
            print("Muistakaa tutkia molempien myonien Energiat ja palauttakaa kaikista suurin.\n")
            return True
        else: 
            print("Ei ihan, yrittäkää uudestaan.\n")
            return True
    except:
        plt.imshow(img_fustrated)
        plt.show()
        print("Jotain pielessä maksimin tarkistuksessa.\n Olihan desimaalierottimena piste?\n Pyytäkää assari apuun jos ongelma ei ratkea.\n")
        return True
    

def minimiE(tiedosto):
    try:
        tied = tiedosto
        oikea = min(min(tied['E1']),min(tied['E2']))
        melkein = max(min(tied['E1']),min(tied['E2'])) #vain toinen data otettu huomioon
        #oppilaan laskema maksimi:
        mini = input("Mikä oli pienin Myonin energia datassa? Käytä desimaalierottimena pistettä.\n")
        if mini=='skip': return False
        elif round(float(mini), 2) == round(oikea, 2): 
            print("Hienoa! \n")
            return False
        elif round(float(mini), 2) == round(melkein, 2):
            print("Muistakaa tutkia molmpien myonien energiat ja palauttakaa kaikista pienin.\n")
            return True
        else: 
            print("Vastaus oli väärä, tarkistakaa että kirjoititte sen oikein.\n")
            return True
    except:
        plt.imshow(img_fustrated)
        plt.show()
        print("Jotain meni pieleen minimin tarkistuksessa.\n Käytittehän pistettä pilkun sijaan? \n Kysykää assarilta apua jos ongelma ei selviä.\n")
        return True



def tarkista_eventit(vars):
    print('Tällä ohjelmalla voit tarkistaa vastauksesi ensimmäiseen kysymykseen. \n Voit poistua tekstikentästä kirjoittamalla "skip" missä tahansa vaiheessa.\n\n')
    #oikeat=np.array([[48223, 249.377, 2.66819], [33177, 1131.56, 4.01271], [19519, 165.27, 2.67178], [7915, 202.921, 2.66267], [8270, 308.698, 2.85848], [4106, 221.887, 2.57612]])
    nimi_kesken=True
    while nimi_kesken==True:
        nimi=input('Kirjoita tiedostosi nimi (esim. piikkidata1):\n') 
        if nimi in vars:
            nimi_kesken=False
        elif nimi=='skip':
            return print('Tarkistus keskeytetty')
        else:
            print("Tiedoston nimi on virheellinen. Koittakaa uudestaan.\n")  
 
    kesken=True
    while kesken :
        kesken= eventit(tiedosto=vars[nimi])
    print('Tarkistus päättynyt.')


def tarkista_maksimiE(vars):
    print('Tarkastusohjelma toiselle kysymykselle.\n Voit poistua tekstikentästä kirjoittamalla "skip" missä tahansa vaiheessa.\n\n')
    #oikeat=np.array([[48223, 249.377, 2.66819], [33177, 1131.56, 4.01271], [19519, 165.27, 2.67178], [7915, 202.921, 2.66267], [8270, 308.698, 2.85848], [4106, 221.887, 2.57612]])
    nimi_kesken=True
    while nimi_kesken==True:
        nimi=input('Kirjoita tiedostosi nimi (esim. piikkidata1):\n') 
        if nimi in vars:
            nimi_kesken=False
        elif nimi=='skip':
            return print('Tarkistus keskeytetty')
        else:
            print("Tiedoston nimi on virheellinen. Koittakaa uudestaan.\n")
        
    kesken=True
    while kesken :
        kesken=maksimiE(tiedosto=vars[nimi])
    print('Tarkistus päättynyt.')



def tarkista_minimiE(vars):
    print('Tarkastusohjelma kolmannelle kysymykselle.\n Voit poistua tekstikentästä kirjoittamalla "skip" missä tahansa vaiheessa.\n\n')
    #oikeat=np.array([[48223, 249.377, 2.66819], [33177, 1131.56, 4.01271], [19519, 165.27, 2.67178], [7915, 202.921, 2.66267], [8270, 308.698, 2.85848], [4106, 221.887, 2.57612]])
    nimi_kesken=True
    while nimi_kesken==True:
        nimi=input('Kirjoita tiedostosi nimi (esim. piikkidata1):\n') 
        if nimi in vars:
            nimi_kesken=False
        elif nimi=='skip':
            return print('Tarkistus keskeytetty')
        else:
            print("Tiedoston nimi on virheellinen. Koittakaa uudestaan.\n")
        
    #num=int(nimi[int(len(nimi)-1)])-1
    kesken=True
    while kesken :
        kesken=minimiE(tiedosto=vars[nimi])
    print('Tarkistus päättynyt.')


def tarkista_inv_massat(vars):
    lasketut= None
    tiedosto=None
    print('Tällä ohjelmalla voit tarkistaa laskitko invariantin massan oikein. Voit poistua tekstikentästä kirjoittamalla "skip" missä tahansa vaiheessa.\n')
    
    nimi=input('Kirjoita tiedostosi nimi (esim. piikkidata1):')
    
    while nimi not in vars: #jos väärä nimi, kysytään uudestaan
        if nimi=='skip':
            return print('Tarkistus keskeytetty')
        else:
            print('Tiedoston nimi on virheellinen, tarkistakaa että kirjoititte sen oikein \n')
            nimi=input('Tiedostosi nimi uudestaan (esim. piikkidata1):') 
            if nimi=='skip':
                return print('Tarkistus keskeytetty')
   
    try:
        tiedosto= vars[nimi]
        testi=input('\n Muuttujan nimi johon tallensitte laskemanne invariantin massan arvot:')
        if testi=='skip':
            return print('Tarkistus keskeytetty')
        else:
            while testi not in vars:
                print('\n Muuttujan nimi ei vastannut mitään muistin muuttujaa. \n Tarkistakaa että ajoitte invariantin massan laskutoimituksen, ja tallensitte tulokset juuri tällä nimellä.\n')
                testi=input('Antakaa muuttujan nimi uudestaan: ')
                if testi=='skip':
                    return print('Tarkistus keskeytetty')
            try:
                lasketut = vars[testi]
                if np.abs(np.mean(lasketut - tiedosto.M)) < 0.0001:
                    plt.imshow(img_happy)
                    plt.show()
                    return print('Hienoa, laskitte invariantin massan oikein!')
                else:
                    return print('Oi voi, jotain meni laskussa pieleen. Tarkistakaa lasku huolella ja koittakaa sitten uudestaan.')
            except: return print('Tarkistuksessa meni jotain pieleen, kysykää neuvoa assarilta.')
       
    except: 
        plt.imshow(img_fustrated)
        plt.show()
        print('Jotain meni pieleen, kysykää neuvoa assarilta.')
        