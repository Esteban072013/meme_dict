None
meme_dict ={
    "LOL":"una respuesta a algo gracioso",
    "CRINGE":"algo raro",
    "CREEPY":"aterracor o siniestro",
    "ROFL":"una respuesta a una broma",
    "AGGRO":"ponerse enojado"
}
WORD = input("ingresa la palabraque quieres conultar").upper()

if WORD in meme_dict.keys():
    print ("lo que significa es :",meme_dict[WORD])

else :
    print ("La palabra esta mal escrita o no existe")
