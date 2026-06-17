#cleaning it up june 11, 2026
#january 30? 2025
import tkinter as tk
from tkinter import ttk 
#import the random library  
import random

#creates the main window
root = tk.Tk()
root.title('Zombie Game')
root.configure(background='white') #sets the bg to white
root.geometry("550x360") #sets the size

escapeimg = tk.PhotoImage(file = 'youescaped.png')
dieimg = tk.PhotoImage(file = 'youdied.png')

#background images 
bg1 = tk.PhotoImage(file = "room1.png") #sets the variable bg1 to the file chosen
bg2 = tk.PhotoImage(file = "room2.png")
bg3 = tk.PhotoImage(file = "room3.png")
bg4 = tk.PhotoImage(file = "room4.png")
bg5 = tk.PhotoImage(file = "room5.png")
bgimage= tk.Label(root, text=" ",image = bg1) #makes a label and sets the image to the file in bg
bgimage.place(x = -2,y = 0)

#left doors
ldoor = tk.PhotoImage(file = "ldoor1.png") #sets the variable bg to the file chosen
ldoor2 = tk.PhotoImage(file = "ldoor2.png")
ldoor3 = tk.PhotoImage(file = "ldoor3.png")
ldoor4 = tk.PhotoImage(file = "ldoor4.png")
ldoor5 = tk.PhotoImage(file = "ldoor5.png")
#right doors
rdoor = tk.PhotoImage(file = "rdoor1.png") #sets the variable bg to the file chosen
rdoor2 = tk.PhotoImage(file = "rdoor2.png")
rdoor3 = tk.PhotoImage(file = "rdoor3.png")
#shelves
shelf = tk.PhotoImage(file = "shelf1.png") #sets the variable bg to the file chosen
shelf2 = tk.PhotoImage(file = "shelf2.png")
shelf3 = tk.PhotoImage(file = "shelf3.png")
#crates
crate = tk.PhotoImage(file = "crate1.png") #sets the variable bg to the file chosen
crate2 = tk.PhotoImage(file = "crate2.png")
crate2mid = tk.PhotoImage(file = "crate2middle.png")
crate3 = tk.PhotoImage(file = "crate3.png")

mergedimg = tk.PhotoImage(file ='shelf3crate1.png') #maybe remove?

#the title 
titlelabel = tk.Label(root, text='Zombie Game', font=('Arial', 20, 'bold'), background='white')
titlelabel.grid(row=0, column=0, pady=5, columnspan=5)
titlelabel.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

#label that just explains stuff
label1 = tk.Label(root, text="Get to the tenth room, the exit is there but you'll need a code to escape. Look for usefel items\non your way but be careful not to make much noise, as that could attract zombies. Good luck.", bg='white')
label1.grid(row=1, column=0, pady=10, padx=5, columnspan=5)
label1.place(relx=0.5, rely=0.22, anchor=tk.CENTER)

#setting up variables
global roomvar
roomvar=0
inventory = []
global bulletcounter
bulletcounter = 0
global screwcounter
screwcounter= 0
global bgcounter
bgcounter = 0
global hascode
hascode= 1
global foundcodecounter
foundcodecounter=0
global foundcode
foundcode = ''

global noisevalue
noisevalue = 0

rdoory=tk.PhotoImage(file='door1.png')

global code
code = '' #the code starts off blaank
for i in range(4):
    codenumber1 = random.randint(0,9) #picks a random number from 0 to 9
    code = str(code) + str(codenumber1) #adds the radnom number to the code, and repeats it 4 tiems so the code is a 4 digit number

#when you press the start button (aka where almost all of the main code is)
def start():
    #setting variables and making them global
    global noisevalue
    global bulletcounter
    global screwcounter
    global roomvar
    global code
    #global progress
    roomvar+=1
    #maybe make htem global?
    global Csearchcount
    global S2searchcount
    global Ssearchcount
    global C2searchcount
    Csearchcount = 0
    Ssearchcount = 0
    C2searchcount = 0
    S2searchcount = 0
    startbutton.destroy()
    label1.destroy()
    titlelabel.destroy()
    shelflist=[shelf, shelf2, shelf3]
    cratelist=[crate, crate2, crate2mid, crate3]

    cratelock = 'no'

    if 'tonextroom' in inventory: #in case tonextroom gto added it removes it
        inventory.remove('tonextroom')

    def nextroom():
        global noisevalue
        global bgcounter
        searchableitem1.destroy()
        searchableitem2.destroy()
        searchableitem3.destroy()
        mergedsearchables.destroy()
        bottomtext.destroy()
        searchframe.destroy()

        noisevalue = int(noisebar['value'])
        rdoorlist=['rdoor3.png', 'rdoor1.png', 'rdoor3.png', 'rdoor1.png', 'rdoor2.png'] #FIX RDOOR3 BECAUSE ITS MISSING A PIXEL ONM THE LEFT AND BOITTOM
        ldoorlist=['ldoor2.png', 'ldoor1.png', 'ldoor3.png', 'ldoor4.png', 'ldoor5.png']
        bglist = [bg1, bg2, bg3, bg4, bg5] #ADDDDDDDDDDDDDDD BG 2-4
        if bgcounter == 4: #I could just use roomvar instead
            bgcounter = -1
        bgcounter += 1

        rdoorcounter=rdoorlist[bgcounter]
        ldoorcounter=ldoorlist[bgcounter]

        currentbg=bglist[bgcounter]
        bgimage.config(image=currentbg)

        rdoor.config(file=rdoorcounter)
        ldoor.config(file=ldoorcounter)

        if bgcounter == 1:
            shelf.config(file='shelf1room2.png')
        else:
            shelf.config(file='shelf1.png')

        start()

    def openinventory():
        def x2():
            inventoryframe.destroy()

        inventoryframe = tk.Frame(root)#, width=150, height=80)
        inventoryframe.grid(row=0, column=5, sticky='e')
        inventoryframe.place(relx=1.0, rely=0.0, anchor ='ne')

        inventorytitle = tk.Label(inventoryframe, text='Inventory', font=('Arial', 16))
        inventorytitle.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        xbutton=tk.Button(inventoryframe, text='x', command=x2)
        xbutton.grid(row=0, column=2, sticky='e', padx=5, pady=5)
        xbutton.place(relx=1.0, rely=0.0, anchor ='ne')

        removeitems = tk.Label(inventoryframe, text="Click on an item to drop it.\nThis can't be undone")
        removeitems.grid(row=3, column=0, columnspan=5)

        #dont destroy it, instead just replace the text with the 7th item in the inventory list
        def buttonsetup():
            if len(inventory) > 0:
                item1.grid(row=1, column=0, padx=5, pady=5)
                item1.config(command=lambda b=inventory[0]: destroy_button(b))
                item1.config(padx=5, text=str(inventory[0]))
            if len(inventory) > 1:
                item2.grid(row=1, column=1, padx=5, pady=5)
                item2.config(command=lambda b=inventory[1]: destroy_button(b))
                item2.config(text=str(inventory[1]))
            if len(inventory) > 2:
                item3.grid(row=1, column=2, padx=10, pady=5)
                item3.config(command=lambda b=inventory[2]: destroy_button(b))
                item3.config(text=str(inventory[2]), padx=5)
            if len(inventory) > 3:
                item4.grid(row=2, column=0, padx=5, pady=5)
                item4.config(command=lambda b=inventory[3]: destroy_button(b))
                item4.config(text=str(inventory[3]))
            if len(inventory) > 4:    
                item5.grid(row=2, column=1, padx=5, pady=5)
                item5.config(command=lambda b=inventory[4]: destroy_button(b))
                item5.config(text=str(inventory[4]))
            if len(inventory) > 5: 
                item6.grid(row=2, column=2, padx=5, pady=5)   
                item6.config(command=lambda b=inventory[5]: destroy_button(b))
                item6.config(text=str(inventory[5]))#=tk.Label(inventoryframe, text=str(inventory[5]))

        def inventorysetup():
            maybescrews=-1
            howmanyscrews=0
            for i in range(len(inventory)):
                maybescrews +=1
                if 'screws' in inventory[maybescrews]:
                    howmanyscrews += 1 #goes up for each seperate time theres screws in the inventory
                    inventory[maybescrews] = str(screwcounter) + ' screws'#(inventory[maybescrews]).replace((inventory[maybescrews])[0], str(screwcounter))
                    if howmanyscrews >=2: #if theres more than 2 screwss thing in the list
                        del inventory[maybescrews]
                        maybescrews-=1 #so it doesnt keep goiing too long
        
            maybebullets=-1
            howmanybullets=0
            for i in range(len(inventory)):
                maybebullets +=1
                if 'bullets' in inventory[maybebullets]:
                    howmanybullets += 1 #goes up for each seperate time theres bullets in the inventory
                    inventory[maybebullets] = str(bulletcounter) + ' bullets'#(inventory[maybebullets]).replace((inventory[maybebullets])[0], str(bulletcounter))
                    if howmanybullets >=2: #if theres more than 2 bulletss thing in the list
                        del inventory[maybebullets]
                        maybebullets-=1 #so it doesnt keep goiing too long
            buttonsetup()

        def destroy_button(itemininventory):
            global screwcounter
            global bulletcounter
            inventory.remove(itemininventory)

            #hides them so they only show up when they should
            item1.grid_forget()
            item2.grid_forget()
            item3.grid_forget()
            item4.grid_forget()
            item5.grid_forget()
            item6.grid_forget()
            inventorysetup()

            if 'bullet' not in str(inventory):
                bulletcounter = 0
            if 'screw' not in str(inventory):
                screwcounter = 0

        item1=tk.Button(inventoryframe, text='')#, command=lambda b=item1: destroy_button(b))
        item2=tk.Button(inventoryframe)
        item3=tk.Button(inventoryframe)#, text=str(inventory[2]))
        item4=tk.Button(inventoryframe)#, text=str(inventory[3]))
        item5=tk.Button(inventoryframe)#, text=str(inventory[4]))
        item6=tk.Button(inventoryframe)#, text=str(inventory[5]))
        inventorysetup()
        

    def searchunlockedcrate(): #once a crate is unlocked it is a much better chance to get good things than the normal crates
        global foundcodecounter
        global foundcode
        global thinglabel
        possibleitems = ['bat', 'gun', '2 bullets', '3 bullets', '6 screws', '2 screws', 'crowbar', 'grey key', 'rusty key', 'plank', 'nothing'] #screws and plank are useless. COULD JUST REMOVE THE LIST SIMCE I CAN JJUST PUT THE ITEM NAMES IN THE RADNOM PART
        itemfound = str(random.choices(possibleitems, weights=(13, 13, 14, 12, 2, 5, 13, 3, 6, 7, 12), k=1)) # 11, 7, 7, 4, 7, 1, 2, 6, 10
        itemfound = itemfound.replace('[', '')
        itemfound = itemfound.replace(']', '')
        itemfound = itemfound.replace("'", "")

        if itemfound != 'nothing':
            inventory.append(itemfound)
        thinglabel.config(text='fewkjbkjfesahgfkjsyhgsudhg iukgdhaisudghodrisugheori')

        for i in range (3):#adds the first 3 digits of the code
            foundcode= foundcode + str(code[foundcodecounter]) 
            foundcodecounter+=1#code.replace(typedcode[-1], '')

        if itemfound != '2 bullets' and itemfound != '3 bullets' and itemfound != '6 screws' and itemfound != '2 screws' and itemfound != 'nothing': #this is all just so it only has a when its grammatically correct. so it says 'a bat' but not 'a 6 screws'
            thinglabel.config(text='You found a paper with ' + foundcode + ' written on it,\nand a ' + itemfound + ' in the crate')
            if len(inventory) > 6:
                bottomtext.config(text='You found a paper with ' + foundcode + ' written on it,and a ' + itemfound + '\nbut your inventory is full... Click on inventory and remove an item')
            inventory.append(itemfound)
        elif itemfound != 'nothing':
            thinglabel.config(text='You found a paper with ' + foundcode + ' written on it,\nand ' + itemfound + ' in the crate')
            if len(inventory) > 6:
                bottomtext.config(text='You found a paper with ' + foundcode + ' written on it, and ' + itemfound + '\nbut your inventory is full... Click on inventory and remove an item')
            inventory.append(itemfound)
        if itemfound == 'nothing':
            thinglabel.config(text='You found a paper with ' + foundcode + '\nwritten on it in the crate')

    def lockedcrate():
        global usingbat 
        global thinglabel
        usingbat=0 
        lockedframe = tk.Frame(root, padx=0, pady=0)
        lockedframe.grid(row=2, column=0, columnspan=5, pady=(2, 5))
        lockedframe.place(relx=0.5, rely=0.47, anchor=tk.CENTER)
        itslockedlabel = tk.Label(lockedframe, text='Its locked...', font=('Arial', 16))
        itslockedlabel.grid(row=0, column=0, pady=2, padx=25)
        thinglabel=tk.Label(lockedframe, text="You don't have anything\nto open it with")
        thinglabel.grid(row=2, column=0, pady=1, padx=5)

        def x():
            lockedframe.destroy()

        def wrongkey(): 
            thinglabel.config(text="It doesn't fit") 

        def rightkey(): 
            thinglabel.config(text='It worked!') 
            searchunlockedcrate()

        def breakopenBat(): #if the bat is used, this tracks it 
            global usingbat 
            usingbat=1 
            breakopen()

        def breakopen(): 
            breakingresult=random.choices(("It opened, but you broke your", "It opened", "It didn't open, and you broke your", "It didn't open"), weights=(25, 25, 25, 25), k=1) 
            breakingresult = str(breakingresult).replace('[', '')
            breakingresult = str(breakingresult).replace(']', '')
            breakingresult = str(breakingresult).replace('"', '')
            breakingresult = str(breakingresult).replace("'", "")
            breakingresult = str(breakingresult).replace("nt", "n't") #the ' in didn't gets removed, so this adds it back in

            noisebar['value']+=10 #every time you try to break it, regardless of the result, it is 10 points of noise
     
            if breakingresult == 'It opened, but you broke your' or breakingresult == "It didn't open, and you broke your": #if the tool broke 
                noisebar['value']+=10 #if your tool breaks it is 10 more, so 20 total

                if usingbat==1: 
                    inventory.remove('bat') 
                    breakingresult = breakingresult + ' bat'
                    usebat.destroy()
                else: 
                    inventory.remove('crowbar') 
                    breakingresult = breakingresult + ' crowbar'
                    usecrowbar.destroy()

            thinglabel.config(text=breakingresult)

            if breakingresult == 'It opened, but you broke your' or breakingresult == 'It opened':
                searchunlockedcrate()

        #make the crate have better items if opened up 
        Xbutton = tk.Button(lockedframe, text='x', command=x) #lockedframe.destroy() #maybe do something less permanent? 
        Xbutton.grid(row=0, column=0, pady=5, padx=5, sticky='e')

        buttonframe = tk.Frame(lockedframe)
        buttonframe.grid(row=4, column=0, pady=5, padx=5)

        if 'grey key' in inventory: 
            usegrey = tk.Button(buttonframe, text='Use grey key', command= wrongkey) 
            usegrey.grid(row=0, column=0, pady=5, padx=5)
            thinglabel.config(text='What do you want to open it with?') 
        if 'rusty key' in inventory: 
            userusty = tk.Button(buttonframe, text='Use rusty key', command= rightkey) 
            userusty.grid(row=0, column=1, pady=5, padx=5)
            thinglabel.config(text='What do you want to open it with?') 
        if 'bat' in inventory: 
            usebat = tk.Button(buttonframe, text='Use bat', command= breakopenBat) 
            usebat.grid(row=1, column=0, pady=5, padx=5)
            thinglabel.config(text='What do you want to open it with?') 
        if 'crowbar' in inventory: 
            usecrowbar = tk.Button(buttonframe, text='Use crowbar', command= breakopen) 
            usecrowbar.grid(row=1, column=1, pady=5, padx=5)
            thinglabel.config(text='What do you want to open it with?') 

    def shelfcratesearch():
        global bulletcounter
        global screwcounter
        global progress
        possibleitems = ['bat', 'gun', '2 bullets', '3 bullets', '6 screws', '2 screws', 'crowbar', 'grey key', 'rusty key', 'plank', 'nothing'] #screws and plank are useless. COULD JUST REMOVE THE LIST SIMCE I CAN JJUST PUT THE ITEM NAMES IN THE RADNOM PART
        itemfound = str(random.choices(possibleitems, weights=(13, 9, 14, 6, 6, 11, 12, 1, 2, 11, 15), k=1)) # 11, 7, 7, 4, 7, 1, 2, 6, 10
        itemfound = itemfound.replace('[', '')
        itemfound = itemfound.replace(']', '')
        itemfound = itemfound.replace("'", "")

        noisebar['value']+=5
       
        if itemfound != 'nothing':
            inventory.append(itemfound)

        if itemfound != '2 bullets' and itemfound != '3 bullets' and itemfound != '6 screws' and itemfound != '2 screws' and itemfound != 'nothing': #this is all just so it only has a when its grammatically correct. so it says 'a bat' but not 'a 6 screws'

            bottomtext.config(text=('You found a ' + itemfound))

            if len(inventory) > 6:
                bottomtext.config(text='You found a ' + itemfound + ' but your inventory is full... Click on inventory and remove an item')

        else:
            if 'bullets' in itemfound:
                bulletcounter = bulletcounter + int(itemfound[0])
                inventorylen = int(len(inventory))
                #if bulletcounter != 9 and bulletcounter != 5: #those are amounts you could start with, so if its not that then this wouldnt be your first time getting bullets 

            if 'screws' in itemfound:
                screwcounter = screwcounter + int(itemfound[0])
                
            bottomtext.config(text=('You found ' + itemfound))#changes th etxt at the bottom to explain what happened

            if len(inventory) > 6:
                bottomtext.config(text='You found ' + itemfound + ' but your inventory is full... Click on inventory and remove an item')

    def doorsearch():
        if ldoor in chosenlist and rdoor in chosenlist:
            dooritem = str(random.choices(('tonextroom', 'gun', 'broom', 'crowbar', 'grey key', 'nothing'), weights=(60, 10, 7, 8, 7, 8), k=1))
        else:
            dooritem='tonextroom'
                
        dooritemlist = ['tonextroom', 'gun', 'broom', 'crowbar', 'grey key', 'nothing'] #CAN PROBABLY DELETE
        dooritem = dooritem.replace('[', '')
        dooritem = dooritem.replace(']', '')
        dooritem = dooritem.replace("'", "")
        
        if dooritem != 'tonextroom' and dooritem != 'nothing':
            inventory.append(dooritem)

            noisebar['value']+=10
            bottomtext.config(text=('It was a storage closet. You found a ' + dooritem)) #changes the text at the bottom to say what you found
            if len(inventory) > 6:
                bottomtext.config(text='You found ' + dooritem + ' but your inventory is full... Click on inventory and remove an item')

        elif dooritem == 'nothing':
            bottomtext.config(text=('It was a storage closet. You found nothing'))
        elif dooritem == 'tonextroom': 
            noisebar['value']+=5
            nextroom()

    list123 = [1, 2, 3] #cause it wasnt wortkung with writing out esch of the numbers and this is simpler than trying to  chnag eit

    def cratesearch():
        global Csearchcount
        global C1searches
        Csearchcount +=1
        if Csearchcount ==1:
            C1searches=random.choice(list123)
        if Csearchcount <= C1searches:
            shelfcratesearch()
        else:
           bottomtext.config(text=("You've already searched the whole thing, there's nothing left")) 
    def shelfsearch():
        global Ssearchcount
        global S1searches
        Ssearchcount += 1
        if Ssearchcount ==1:
            S1searches=random.choice(list123)
        
        if Ssearchcount <= S1searches: #if the shelf has been searched equal to or less than the amount it can be searched it runs shelfcrate search to actually search it
            shelfcratesearch()
        else:
           bottomtext.config(text=("You've already searched the whole thing, there's nothing left")) 
    def crate2search():
        global C2searches
        global C2searchcount
        C2searchcount +=1
        if C2searchcount ==1:
            C2searches=random.choice(list123)
        if C2searchcount <= C2searches:
            shelfcratesearch()
        else:
           bottomtext.config(text=("You've already searched the whole thing, there's nothing left")) 
    def shelf2search():
        global S2searchcount
        global S2searches
        S2searchcount += 1
        if S2searchcount ==1:
            S2searches=random.choice(list123)
        if S2searchcount <= S2searches:
            shelfcratesearch()
        else:
           bottomtext.config(text=("You've already searched the whole thing, there's nothing left")) 
    
    attackresult=0
    searchableslist = [shelf, crate]#maybe add a  blank image so it can be less than three?
    #just make it one door so there cant be duplicates of the same door
    doorslist = [ldoor, rdoor]
    chosenlist = []
    realchosenlist = []

    image1 = random.choice(searchableslist)

    searchableslist.append(ldoor) #the doors are only added to the list after the first item is picked so it cant be all doors
    searchableslist.append(rdoor)

    image2 = random.choice(searchableslist)
    if image2 == ldoor or image2 == rdoor: #so there cant be duplicate doors
        searchableslist.remove(image2)
    image3 = random.choice(searchableslist)

    if image3 == crate:
        cratelock = str(random.choices((crate, 'lockedcrate'), weights=(1, 100), k=1)) #60 40 split

    if image1 != ldoor and image1 != rdoor and image2 != ldoor and image2 != rdoor and image3 != ldoor and image3 != rdoor:
        doorimage1 = random.choice(doorslist)
        image3 = doorimage1


    chosenlist.append(image1)
    chosenlist.append(image2)
    chosenlist.append(image3)

    rdoorposition = tk.Label(root, image=rdoor, borderwidth=0, highlightthickness=0)
    ldoorposition = tk.Label(root, image=ldoor, borderwidth=0, highlightthickness=0)

    img1shelf=0
    img2shelf=0
    img3shelf=0
    img1crate=0
    img2crate=0
    img3crate=0

    realchosenlist = [chosenlist]

    searchableitem1 = tk.Label(root, text=" ", image=image1, borderwidth=0, highlightthickness=0) 
    searchableitem1.place(x=50, y=115)
    if image1 == rdoor:
        searchableitem1.place(x=307, y=117)
    if image1 == ldoor:
        searchableitem1.place(x=160, y=117)
    if image1 == shelf:
        img1shelf = random.choice((shelflist))
        shelflist.remove(img1shelf)
        realchosenlist.append(img1shelf)
        searchableitem1.config(image=img1shelf)
        if img1shelf==shelf:
            searchableitem1.place(x=3, y=139)
        if img1shelf==shelf2:
            searchableitem1.place(x=393, y=139)
        if img1shelf==shelf3:
            searchableitem1.place(x=463, y=191)

    if image1 == crate:
        img1crate = random.choice((cratelist))
        cratelist.remove(img1crate)
        realchosenlist.append(img1crate)
        searchableitem1.config(image=img1crate)
        if img1crate==crate:
            searchableitem1.place(x=415, y=249)
        if img1crate==crate2:
            searchableitem1.place(x=437, y=291)
            if crate3 in cratelist: #so there isnt both crate3 and crate2 cause they overlap
                cratelist.remove(crate3) 
        if img1crate==crate2mid:
            if crate2 in cratelist:
                cratelist.remove(crate2)
            searchableitem1.place(x=249, y=249)
        if img1crate==crate3:
            searchableitem1.place(x=451, y=271)   
            if crate2 in cratelist: #so there isnt both crate3 and crate2 cause they overlap
                cratelist.remove(crate2) 
    
    searchableitem2 = tk.Label(root, text=" ", image=image2, borderwidth=0, highlightthickness=0) 
    searchableitem2.place(x=437, y=271)
    if image2 == rdoor:
        searchableitem2.place(x=307, y=117)
    if image2 == ldoor:
        searchableitem2.place(x=160, y=117)
    if image2 == shelf:
        img2shelf = random.choice((shelflist))
        shelflist.remove(img2shelf)
        realchosenlist.append(img2shelf)
        searchableitem2.config(image=img2shelf)
        if img2shelf==shelf:
            searchableitem2.place(x=3, y=139)
        if img2shelf==shelf2:
            searchableitem2.place(x=393, y=139)
        if img2shelf==shelf3:
            searchableitem2.place(x=463, y=191)
    if image2 == crate:
        img2crate = random.choice((cratelist))
        cratelist.remove(img2crate)
        realchosenlist.append(img2crate)
        searchableitem2.config(image=img2crate)
    
        if img2crate==crate:
            searchableitem2.place(x=415, y=249)
        if img2crate==crate2:
            searchableitem2.place(x=437, y=291)
            if crate3 in cratelist: #so there cant be both crate3 and crate2 cause they overlap
                cratelist.remove(crate3) 
        if img2crate==crate2mid:
            if crate2 in cratelist:
                cratelist.remove(crate2)
            searchableitem2.place(x=249, y=249) 
        if img2crate==crate3:
            searchableitem2.place(x=451, y=271)
            if crate2 in cratelist: #so there cant be both crate3 and crate2 cause they overlap
                cratelist.remove(crate2) 

    searchableitem3 = tk.Label(root, text=" ", image=image3, borderwidth=0, highlightthickness=0) 
    searchableitem3.place(x=437, y=271)
    if image3 == rdoor:
        searchableitem3.place(x=307, y=117)
    if image3 == ldoor:
        searchableitem3.place(x=160, y=117) 

    if image3 == shelf:
        img3shelf = random.choice((shelflist))
        shelflist.remove(img3shelf)
        realchosenlist.append(img3shelf)
        searchableitem3.config(image=img3shelf)
        if img3shelf==shelf:
            searchableitem3.place(x=3, y=139)
        if img3shelf==shelf2:
            searchableitem3.place(x=393, y=139)
        if img3shelf==shelf3:
            searchableitem3.place(x=463, y=191)

    if image3 == crate:
        img3crate = random.choice((cratelist))
        cratelist.remove(img3crate)
        realchosenlist.append(img3crate)
        searchableitem3.config(image=img3crate)
        if img3crate==crate:
            searchableitem3.place(x=415, y=249)
        if img3crate==crate2:
            searchableitem3.place(x=437, y=291)
        if img3crate==crate2mid:
            if crate2 in cratelist:
                cratelist.remove(crate2)
            searchableitem3.place(x=249, y=249) 
        if img3crate==crate3:
            searchableitem3.place(x=451, y=271) 

    mergedsearchables=tk.Label(root, text=" ", image=mergedimg, borderwidth=0, highlightthickness=0) 

    if crate3 in realchosenlist and crate in realchosenlist: 
        mergedimg.config(file='crate1crate3.png')
        mergedsearchables.place(x=415, y=249)
    if crate2 in realchosenlist and crate in realchosenlist:
        mergedimg.config(file='crate1crate2.png')
        mergedsearchables.place(x=415, y=249)
    if shelf2 in realchosenlist and crate in realchosenlist: #shelf2 and crate1\
        mergedimg.config(file='shelf2crate1.png')
        mergedsearchables.place(x=393, y=139)
    if shelf3 in realchosenlist and crate in realchosenlist: #shelf2 and crate1
        mergedimg.config(file='shelf3crate1.png')
        mergedsearchables.place(x=415, y=191)
    if shelf2 in realchosenlist and crate2 in realchosenlist:
        mergedimg.config(file='shelf2crate2.png')
        mergedsearchables.place(x=393, y=139)
    if shelf3 in realchosenlist and crate2 in realchosenlist:
        mergedimg.config(file='crate2shelf3.png')
        mergedsearchables.place(x=437, y=191)
    if shelf3 in realchosenlist and crate3 in realchosenlist: 
        mergedimg.config(file='crate3shelf3.png')
        mergedsearchables.place(x=447, y=187)
    
    inventorybutton = tk.Button(root, text='Items', font=('Arial', 16), command=openinventory)
    inventorybutton.grid(row=0, column=3, columnspan=5, pady=(2, 5))
    inventorybutton.place(relx=0.92, rely=0.1, anchor=tk.CENTER)

    roomlabel= tk.Label(root, text='Room: '+ str(roomvar))
    roomlabel.grid(row=2, column=0, columnspan=5, pady=(2, 5))
    roomlabel.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    if roomvar!=1:
        bottomtext=tk.Label(root, text='It led to the next room')
        if attackresult == "You made it!":
            bottomtext.config(text='You escaped to the next room') #if you just got to the next room from escaping the zombie the bottom text updates
    if roomvar==1:
        bottomtext=tk.Label(root)
    bottomtext.grid(row=0, column=0, padx=5)#, sticky='w')
    bottomtext.place(relx=0.0, rely=1.0, anchor ='sw')


    noiseframe = tk.Frame(root, padx=0, pady=0)
    noiseframe.grid(row=0, column=0, columnspan=5, pady=10, padx=10)
    noiseframe.place(relx=0.0, rely=0.0, anchor ='nw')
    
    noiselabel = tk.Label(noiseframe, text='Noise level')
    noiselabel.grid(row=0, column=0, columnspan=5, pady=(2, 5))
    
    noisebar = ttk.Progressbar(noiseframe, maximum=70, mode='determinate')#variable=progress)
    noisebar['value']=noisevalue #this is so it doesnt reset the noise every time start() is triggered by going to a new room. so this sets the value of the progress bar to what it was before the next room
    noisebar.grid( row=1, column=0, padx=6, pady=(0, 5))

    searchframe = tk.Frame(root, padx=0, pady=0)
    searchframe.grid(row=2, column=0, columnspan=5, pady=(2, 5))
    searchframe.place(relx=0.5, rely=0.47, anchor=tk.CENTER)
    searchlabel = tk.Label(searchframe, text='Search:', font=('Arial', 16))
    searchlabel.grid(row=0, column=0, pady=5, padx=6)

    if image1 == ldoor or image2 == ldoor or image3 == ldoor: #fix this if i can think of a better way. it works but is a really dumb inefficient way to do it
        ldoorbutton = tk.Button(searchframe, text='Left door', font=('Arial', 12), command=doorsearch)
        ldoorbutton.grid(row=1, column=0, pady=5)
    if image1 == rdoor or image2 == rdoor or image3 == rdoor:
        rdoorbutton = tk.Button(searchframe, text='Right door', font=('Arial', 12), command=doorsearch)
        rdoorbutton.grid(row=2, column=0, pady=5)
    if image1 == shelf or image2 == shelf or image3 == shelf:
        shelfbutton = tk.Button(searchframe, text='Shelf', font=('Arial', 12), command=shelfsearch)
        shelfbutton.grid(row=3, column=0, pady=5)

    if image1 == crate or image2 == crate or image3 == crate:
        cratebutton = tk.Button(searchframe, text='Crate', font=('Arial', 12), command=cratesearch)
        cratebutton.grid(row=5, column=0, pady=5, padx=5)

    if cratelock == "['lockedcrate']":
        cratebutton.config(text='Locked crate', command=lockedcrate)
        cratelock='no' #this maybe fixes the error where if this if is true when it shouldnt be it says crate button is not defined
    
    #for when theres duplicates
    seen = []
    for number in chosenlist:
        if number in seen:
            if number == shelf:
                shelf2button = tk.Button(searchframe, text='Shelf 2', font=('Arial', 12), command=shelf2search)
                shelf2button.grid(row=4, column=0, pady=5)
                
            if number == crate:
                crate2button = tk.Button(searchframe, text='Crate 2', font=('Arial', 12), command=crate2search)
                crate2button.grid(row=6, column=0, pady=5)
        else:
            seen.append(number)

    global zombiehealth
    zombiehealth = 10

    if noisebar['value']>=60: #THIS NEEDS TO BE MOVED 
        bottomtext.config(text="You've made a lot of noise, be careful...")
    def fixattackresult():
        global attackresult
        global zombiehealth
        global hascode
        attackresult = str(attackresult).replace('[', '')
        attackresult = str(attackresult).replace(']', '')
        attackresult = str(attackresult).replace('"', '')
        attackresult = str(attackresult).replace("'", "")
        attackresult = str(attackresult).replace("nt", "n't")

    def processattackresult():
        global zombiehealth
        global attackresult
        global hascode
        if attackresult == 'It hurt the zombie a little':
            zombiehealth -= 1
            zhealthbar['value']-=1
        if attackresult == 'It hurt the zombie a lot':
            zombiehealth -= 2
            zhealthbar['value']-=2
        if attackresult == 'It hurt the zombie a lot!': #this is only possible when using the gun, but i didnt know whwtehr to change it to say you really hurt it a lot or something, so i just added the explanation mark to distinguish it from tre lot attacks from other weapons
            zombiehealth -= 3
            zhealthbar['value']-=3
        if attackresult == 'It killed the zombie!':
            zombiehealth -= 10
            zhealthbar['value']-=10
        if attackresult ==  'You missed and it attacked you!':
            healthbar['value']-=1.5 #maybe just -1 instead?
        attacklabel2.config(text=attackresult)

        def continueon():
            global hascode
            attackframe.destroy() #gets rid of all the things for the zombie attadk
            healthframe.destroy()
            zhealthframe.destroy()
            noisebar['value']=35 #resetsd the noise to halfway
            bottomtext.config(text='You killed the zombie')

        if zhealthbar['value'] <= 0:
            attacklabel.config(text='You knocked out \nthe zombie!')
            attacklabel2.config(text='There was a paper in its pocket\nwith ' + code + ' written on it')
            optionsframe.destroy() #gets rid of all the attack options
            continuebutton =  tk.Button(attackframe, text='Continue', command=continueon)
            continuebutton.grid(row=3, column=0, columnspan=5, padx=5, pady=5)
            hascode= 4

        if healthbar['value'] <= 0: #if your health goes all the way down
            youdied= tk.Label(root, image=dieimg)
            youdied.place(x = -2,y = 0)
    def usegun():
        global attackresult
        global zombiehealth
        global bulletcounter
        if bulletcounter == 0:
            attacklabel2.config(text="You don't have any bullets!")
        else:
            attackresult=random.choices(('It hurt the zombie a lot!', 'It hurt the zombie a lot', 'It hurt the zombie a little', 'It killed the zombie!'), weights=(50, 30, 10, 10), k=1) #the one with the exclamtion amrk is just for the gun attack and does 3 damage
            bulletcounter-=1 #puts it down 1 since you used a bullet
            fixattackresult()
            processattackresult()
            
            
    def usebatattack(): #not as good as crowbar
        global attackresult
        global zombiehealth
        attackresult=random.choices(('It hurt the zombie a lot', 'It hurt the zombie a little', 'You missed!', 'You missed and it attacked you!'), weights=(20, 45, 11, 24), k=1)
        fixattackresult()
        processattackresult()
        
    def usecrowbarattack():
        global attackresult
        global zombiehealth
        attackresult=random.choices(('It hurt the zombie a lot', 'It hurt the zombie a little', 'You missed!', 'You missed and it attacked you!'), weights=(25, 45, 10, 20), k=1)
        fixattackresult()
        processattackresult()
        
    def useplank():
        global zombiehealth
        global attackresult
        attackresult=random.choices(("It broke and didn't do anything", "It hurt the zombie a little"), weights=(90, 10), k=1)
        fixattackresult()
       
        attacklabel2.config(text=attackresult)
        if attackresult == "It broke and didn't do anything":
            healthbar['value']-=1 
        
        processattackresult()

    def usefists():
        global zombiehealth
        global attackresult
        attackresult=random.choices(('It hurt the zombie a lot', 'It hurt the zombie a little', 'You missed!', 'You missed and it attacked you!'), weights=(10, 30, 20, 40), k=1)
        fixattackresult()
        processattackresult()
    
    def runtonextroom():
        global zombiehealth
        global attackresult
        attackresult=random.choices(("You couldn't get past it", "You made it!"), weights=(10,90), k=1)
        fixattackresult()
        if attackresult == "You couldn't get past it":
            healthbar['value']-=1
        if attackresult == "You made it!":
            #gets rid of all the ui from the zombie attack
            attackframe.destroy() 
            healthframe.destroy()
            zhealthframe.destroy()
            noisebar['value']=0 #resets the noise
            bottomtext.config(text='You made it into the next room')
            nextroom()

    if noisebar['value']>=70: #THIS NEEDS TO BE MOVED 
        searchframe.grid_forget()
        bottomtext.config(text="You were too loud! The zombies heard you!")
        
        healthframe = tk.Frame(root, padx=0, pady=0)
        healthframe.grid(row=0, column=0, columnspan=5, pady=10, padx=10)
        healthframe.place(relx=0.0, rely=0.17, anchor='nw')
        
        healthlabel = tk.Label(healthframe, text='Your health')#, font=('Arial', 16))
        healthlabel.grid(row=0, column=0, columnspan=5, pady=(2, 5)) 
        healthbar = ttk.Progressbar(healthframe, maximum=5, mode='determinate')
        healthbar.grid( row=1, column=0, padx=6, pady=(0, 5))
        healthbar['value']+=5

        zhealthframe = tk.Frame(root, padx=0, pady=0)
        zhealthframe.grid(row=0, column=0, columnspan=5, pady=10, padx=10)
        zhealthframe.place(relx=0.0, rely=0.0, anchor='nw')
        
        zhealthlabel = tk.Label(zhealthframe, text="Zombie's health")#, font=('Arial', 16))
        zhealthlabel.grid(row=0, column=0, columnspan=5, pady=(2, 5)) 
        zhealthbar = ttk.Progressbar(zhealthframe, maximum=10, mode='determinate')
        zhealthbar.grid( row=1, column=0, padx=6, pady=(0, 5))
        zhealthbar['value']+=10

        attackframe = tk.Frame(root, padx=0, pady=0)
        attackframe.grid(row=2, column=2, columnspan=3, pady=(2, 5))
        attackframe.place(relx=0.5, rely=0.47, anchor=tk.CENTER)
        attacklabel= tk.Label(attackframe, text='A zombie appeared!', font=('Arial', 16))
        attacklabel.grid(row=0, column=0, columnspan=5)
        attacklabel2=tk.Label(attackframe, text='What will you do?')
        attacklabel2.grid(row=1, column=0, columnspan=5)
        optionsframe = tk.Frame(attackframe, padx=0, pady=0)
        optionsframe.grid(row=2,column=0, columnspan=5)
        if 'gun' in inventory: 
            attackgun = tk.Button(optionsframe, text='Shoot it', command= usegun) 
            attackgun.grid(row=0, column=0, pady=5, padx=5)
            
        if 'bat' in inventory: 
            attackbat = tk.Button(optionsframe, text='Hit it with a bat', command= usebatattack) 
            attackbat.grid(row=1, column=0, pady=5, padx=5)

        if 'crowbar' in inventory: 
            usecrowbar = tk.Button(optionsframe, text='Hit it with a crowbar', command= usecrowbarattack) 
            usecrowbar.grid(row=2, column=0, pady=5, padx=5)

        if 'plank' in inventory: 
            attackbat = tk.Button(optionsframe, text='Hit it with a plank', command= useplank)  #innefective
            attackbat.grid(row=3, column=0, pady=5, padx=5)

        usepunch = tk.Button(optionsframe, text='Fight it off with your hands', command= usefists)  
        usepunch.grid(row=4, column=0, pady=5, padx=5)
        runaway = tk.Button(optionsframe, text='Run to the next room', command= runtonextroom)  #innefective
        runaway.grid(row=5, column=0, pady=5, padx=5)

        if zhealthbar['value']<=0:
            attacklabel2.config(text='zombie died blegh')

    def youwin():
        #add end cutscene photo and stuff
        youescaped= tk.Label(root, image=escapeimg)
        youescaped.place(x = -2,y = 0)
    
    def end():
        frlabel.config(text='It unlocked!')
        bottomtext.config(text='You unlocked the door')
        continuebutton =  tk.Button(finalroomframe, text='Open the door', command=youwin)
        continuebutton.grid(row=3, column=0, columnspan=5, padx=5, pady=5)

    def keyend():
        usegrey.destroy()
        end()
        
    if roomvar == 10: #if you get to the end
        finalroomframe = tk.Frame(root, padx=0, pady=5)
        finalroomframe.grid(row=2, column=2, columnspan=3)
        finalroomframe.place(relx=0.5, rely=0.47, anchor=tk.CENTER)
        if 'grey key' in inventory:  #if you have the key you instsntly can get in without  a code
            frlabel= tk.Label(finalroomframe, text='The door is locked...', font=('Arial', 16))
            frlabel.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
            usegrey = tk.Button(finalroomframe, text='Use grey key', command= keyend) 
            usegrey.grid(row=1, column=0, pady=5, padx=5, columnspan=5)
        else:
            global typedcode
            frlabel= tk.Label(finalroomframe, text='The door \nhas a keypad...', font=('Arial', 16))
            frlabel.grid(row=0, column=0, columnspan=5, padx=5, pady=(0,5))
            typedcode = ''
            typedcodelabel = tk.Label(finalroomframe, text=typedcode)
            typedcodelabel.grid(row=2, column=0, columnspan=5, pady=(0, 5))
            keypadframe = tk.Frame(finalroomframe, padx=5, pady=5, bg='#4C4C4B')
            keypadframe.grid(row=3, column=0, columnspan=5)
            havecode = tk.Label(finalroomframe, text='')

            if hascode >= 4:
                havecode.config(text = 'The paper you found said\n' + code +', you should try that.')
                havecode.grid(row=1, column=0, columnspan=5) 
            def backspace():
                global typedcode
                typedcode = typedcode.replace(typedcode[-1], '')
                typedcodelabel.config(text=typedcode)


            def destroy_button(buttonnumber):
                global typedcode
                global code

                typedcode = str(typedcode)+str(buttonnumber)
                typedcodelabel.config(text=typedcode)

                if typedcode == code: #if its the right code
                    keypadframe.destroy() #gets rid of the keypad
                    typedcodelabel.destroy() 
                    end()

            rowtracker = 0
            columntracker = -1
            for i in range(10): #\
                thing=i 
                columntracker +=1
                if columntracker >=3:
                    rowtracker += 1
                    columntracker = 0
                if i==0:
                    rowtracker= 3 #this is so the 0 button gets positioned correctly (at the bottom)
                    columntracker=1
                button = tk.Button(keypadframe, text=thing, padx=5)
                button.config(command=lambda b=thing: destroy_button(b))
                button.grid(row=rowtracker, column=columntracker)
                if i==0:
                    rowtracker=0 #after the 0 is positioned, this resets it so the other buttons are placed correct
                    columntracker = -1
            backbutton = tk.Button(keypadframe, text='⇦', command=backspace, padx=2)
            backbutton.grid(row=3, column=2)

#the start button
startbutton = tk.Button(root, text='     Start     ', font=('Arial', 16), command=start)
startbutton.grid(row=2, column=0, columnspan=5, pady=(2, 5))
startbutton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#runs the application
root.mainloop()

