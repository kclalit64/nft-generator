from PIL import Image
from IPython.display import display
import os

def select_trait(traits):
    print("\nSelect one: \n")
    for i in range(len(traits)):
        print(str(i+1)+". "+traits[i])
    choice = int(input("\nEnter choice:   "))
    return choice-1

#All traits listed
face = ["White", "Black"]
eyes = ["Regular", "Small", "Rayban", "Hipster", "Focused"]
ears = ["No Earring", "Left Earring", "Right Earring", "Two Earrings"]
hair = ['Up Hair', 'Down Hair', 'Mohawk', 'Red Mohawk', 'Orange Hair', 'Bubble Hair', 'Emo Hair',
 'Thin Hair',
 'Bald',
 'Blonde Hair',
 'Caret Hair',
 'Pony Tails']
mouth = ['Black Lipstick', 'Red Lipstick', 'Big Smile', 'Smile', 'Teeth Smile', 'Purple Lipstick']
nose = ['Nose', 'Nose Ring']

all_traits = [face, eyes, ears, hair, mouth, nose]
params = ["face", "eyes", "ears", "hair", "mouth", "nose"]


#Classify traits
face_files = {
    "White": "face1",
    "Black": "face2"
}


eyes_files = {
    "Regular": "eyes1",
    "Small": "eyes2",
    "Rayban": "eyes3",
    "Hipster": "eyes4",
    "Focused": "eyes5"    
}


ears_files = {
    "No Earring": "ears1",
    "Left Earring": "ears2",
    "Right Earring": "ears3",
    "Two Earrings": "ears4"
}


hair_files = {
    "Up Hair": "hair1",
    "Down Hair": "hair2",
    "Mohawk": "hair3",
    "Red Mohawk": "hair4",
    "Orange Hair": "hair5",
    "Bubble Hair": "hair6",
    "Emo Hair": "hair7",
    "Thin Hair": "hair8",
    "Bald": "hair9",
    "Blonde Hair": "hair10",
    "Caret Hair": "hair11",
    "Pony Tails": "hair12"
}


mouth_files = {
    "Black Lipstick": "m1",
    "Red Lipstick": "m2",
    "Big Smile": "m3",
    "Smile": "m4",
    "Teeth Smile": "m5",
    "Purple Lipstick": "m6"
}


nose_files = {
    "Nose": "n1",
    "Nose Ring": "n2"  
}


#### Generate Images


count = 0
while True:
    print("\n\n############# ~~~~> CREATE YOUR NFT <~~~~ #############")
    print("\n*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n")
    print("☞ ☞ ☞ ☞ ☞ ☞ ☞ ☞ ☞      MAIN MENU      ☜ ☜ ☜ ☜ ☜ ☜ ☜ ☜ ☜\n")
    choices = list()
    for i in range(6):


        print("TRAIT #"+params[i].upper())
        choicex = select_trait(all_traits[i])
        choices.append(choicex)
   
    im1 = Image.open(f'./face_parts/face/{face_files[face[choices[0]]]}.png').convert('RGBA')
    im2 = Image.open(f'./face_parts/eyes/{eyes_files[eyes[choices[1]]]}.png').convert('RGBA')
    im3 = Image.open(f'./face_parts/ears/{ears_files[ears[choices[2]]]}.png').convert('RGBA')
    im4 = Image.open(f'./face_parts/hair/{hair_files[hair[choices[3]]]}.png').convert('RGBA')
    im5 = Image.open(f'./face_parts/mouth/{mouth_files[mouth[choices[4]]]}.png').convert('RGBA')
    im6 = Image.open(f'./face_parts/nose/{nose_files[nose[choices[5]]]}.png').convert('RGBA')


    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)


    #Convert to RGB
    rgb_im = com5.convert('RGB')
    file_name = "image"+str(count)+".png"
    rgb_im.save("./images/" + file_name)
   
    nft = Image.open("./images/"+file_name, mode="r")
    nft.show()


    #continue
    print("Create one more? (0 = no/1 = yes)")
    status = int(input())
    if status==0:
        break
    else:
        count+=1
    clear = lambda: os.system('cls')
    clear()