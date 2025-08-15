import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

img_happy = mpimg.imread('../../img/kuvitus_2.png')
img_fustrated=mpimg.imread('../../img/kuvitus3.png')


def eventit(tiedosto):
    try:
        oikea= len(tiedosto)
        event=input("How many events are in the data? \n")
        if event=='skip': return False
        elif int(event)==oikea: #eka testi ok
            print("Correct! \n")
            return False
        else: 
            print("Ammount of events was wrong, try again!")
            return True
    except:
        print("Something went wrong with the evaluation. Ask for help!\n")
        return True   


def maksimiE(tiedosto):
    try:
        tied = tiedosto
        oikea = max(max(tied['E1']),max(tied['E2']))
        melkein = min(max(tied['E1']),max(tied['E2'])) #vain toinen data otettu huomioon
        #oppilaan laskema maksimi:
        maks = input("What is the maximum energy of the muon in the data? Use dot as a decimal seperator.\n")
        if maks=='skip': return False
        elif round(float(maks), 2) == round(oikea, 2): 
            print("Correct! \n")
            return False
        elif round(float(maks), 2) == round(melkein, 2):
            print("Remember to exam both of the muons and use the larger one.\n")
            return True
        else: 
            print("Not there yet. Try again!\n")
            return True
    except:
        plt.imshow(img_fustrated)
        plt.show()
        print("Something went wrong with the evaluation. Did you use dot as the decimal seperator? Ask for help!\n")
        return True
    

def minimiE(tiedosto):
    try:
        tied = tiedosto
        oikea = min(min(tied['E1']),min(tied['E2']))
        melkein = max(min(tied['E1']),min(tied['E2'])) #vain toinen data otettu huomioon
        #oppilaan laskema maksimi:
        mini = input("What is the minimum energy of the muon in the data? Use dot as a decimal seperator.\n")
        if mini=='skip': return False
        elif round(float(mini), 2) == round(oikea, 2): 
            print("Perfect! \n")
            return False
        elif round(float(mini), 2) == round(melkein, 2):
            print("Remember to exam both of the muons and use the smaller one.\n")
            return True
        else: 
            print("Not there yet. Try again!\n")
            return True
    except:
        plt.imshow(img_fustrated)
        plt.show()
        print("Something went wrong with the evaluation. Did you use dot as the decimal seperator? Ask for help!\n")
        return True



def tarkista_eventit(vars):
    print('With this function you can check the answer to the first question.\nUse "skip" to exit the text field.\n\n')
    #oikeat=np.array([[48223, 249.377, 2.66819], [33177, 1131.56, 4.01271], [19519, 165.27, 2.67178], [7915, 202.921, 2.66267], [8270, 308.698, 2.85848], [4106, 221.887, 2.57612]])
    nimi_kesken=True
    while nimi_kesken==True:
        nimi=input('Enter your filename (e.g. peakdata1):\n') 
        if nimi in vars:
            nimi_kesken=False
        elif nimi=='skip':
            return print('Evaluation stopped!')
        else:
            print("Invalid filename. Try again!\n")  
 
    kesken=True
    while kesken :
        kesken= eventit(tiedosto=vars[nimi])
    print('Evaluation finished.')


def tarkista_maksimiE(vars):
    print('With this function you can check the answer to the second question.\nUse "skip" to exit the text field.\n\n')
    #oikeat=np.array([[48223, 249.377, 2.66819], [33177, 1131.56, 4.01271], [19519, 165.27, 2.67178], [7915, 202.921, 2.66267], [8270, 308.698, 2.85848], [4106, 221.887, 2.57612]])
    nimi_kesken=True
    while nimi_kesken==True:
        nimi=input('Enter your filename (e.g. peakdata1):\n') 
        if nimi in vars:
            nimi_kesken=False
        elif nimi=='skip':
            return print('Evaluation stopped!')
        else:
            print("Invalid filename. Try again!\n")
        
    kesken=True
    while kesken :
        kesken=maksimiE(tiedosto=vars[nimi])
    print('Evaluation finished.')



def tarkista_minimiE(vars):
    print('With this function you can check the answer to the third question.\nUse "skip" to exit the text field.\n\n')
    #oikeat=np.array([[48223, 249.377, 2.66819], [33177, 1131.56, 4.01271], [19519, 165.27, 2.67178], [7915, 202.921, 2.66267], [8270, 308.698, 2.85848], [4106, 221.887, 2.57612]])
    nimi_kesken=True
    while nimi_kesken==True:
        nimi=input('Enter your filename (e.g. peakdata1):\n') 
        if nimi in vars:
            nimi_kesken=False
        elif nimi=='skip':
            return print('Evaluation stopped!')
        else:
            print("Invalid filename. Try again!\n")
        
    #num=int(nimi[int(len(nimi)-1)])-1
    kesken=True
    while kesken :
        kesken=minimiE(tiedosto=vars[nimi])
    print('Evaluation finished.')


def tarkista_inv_massat(vars):
    lasketut= None
    tiedosto=None
    print('With this function you can check if yuo calculated the invariant mass correctly.\nUse "skip" to exit the text field.\n\n')
    
    nimi=input('Enter your filename (e.g. peakdata1):')
    
    while nimi not in vars: #jos väärä nimi, kysytään uudestaan
        if nimi=='skip':
            return print('Evaluation stopped!')
        else:
            print('Invalid filename. Try again!\n')
            nimi=input('Enter your filename again (e.g. peakdata1):') 
            if nimi=='skip':
                return print('Evaluation stopped!')
   
    try:
        tiedosto= vars[nimi]
        testi=input('\n Name of the variable you used to store the calculatetd invariant mass')
        if testi=='skip':
            return print('Evaluation stopped!')
        else:
            while testi not in vars:
                print('\n Enterd variable was mot found in memory. \n Check that you did run the code for the invarian massa and the variable name is correct.\n')
                testi=input('Name of the variable: ')
                if testi=='skip':
                    return print('Evaluation stopped!')
            try:
                lasketut = vars[testi]
                if np.abs(np.mean(lasketut - tiedosto.M)) < 0.0001:
                    plt.imshow(img_happy)
                    plt.show()
                    return print('Perfect, the calculations were correct!')
                else:
                    return print('Oh no, something went wrong in the calculations. Check the calcutalios carefully and try again.')
            except: return print('Something went wrong with the evaluation. Ask for help!\n')
       
    except: 
        plt.imshow(img_fustrated)
        plt.show()
        print('Something went wrong. Ask for help!\n')
        