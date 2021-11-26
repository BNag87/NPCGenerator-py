# TO DO- GET THE GENDER/RACE CHOICES WORKING FOR EACH OPTION. ALL BUTTONS FOR THIS GO ON THE FRAME TITLE "TK_GenderRaceFrame"
# ====================IMPORTS====================
# access libraries for gui building

import tkinter as tk
from tkinter import ttk
import random
from tkinter.constants import CENTER, DISABLED, NORMAL


# Need to create a root 'window' for everything to go on
root = tk.Tk()
root.resizable(False, False) 
root.title("Random NPC Generator")
# ====================VARIABLES====================
# region variables

# bunch of tuples that store names appropriate for each race, stored by gender
tu_DragonbornMaleNames = ("Arkul", "Alidorim", "Alixan", "Balxan", "Beljhan", "Belziros", "Balvull", "Brensashi", "Belcrath", "Brenhazar", "Brenjurn", "Ornil",	"Bhahadur", "Claxiajir", "Caerfras", "Caerlin", "Calugar", "Docrath", "Durbarum", "Drelxan", "Eragrax", "Eramorn", "Eranaar", "Myistus", "Faerxan", "Faerjurn", "Frokris", "Faersashi", "Farideh", "Faeroth", "Goraxan", "Gherash", "Greyax", "Goralin", "Ghequll", "Yenciar", "Gorahadur", "Hixan",	"Hiskan", "Hetrin", "Iorfarn", "Iormash", "Iorcrath", "Jaryax",	"Jinrash", "Jinwunax", "Kaedwen", "Krivroth", "Kilyax", "Kilskan", "Kriv", "Kilziros", "Lumiskan", "Lorqiroth",	"Lumisashi", "Morvarax", "Medmorn", "Marsashi", "Myerna", "Nargrax", "Naqrin", "Neslasar", "Narghull", "Nakax", "Nadarr", "Narjhan", "Nesmash", "Ildroth", "Otiythas", "Otivull", "Orlaskan", "Paqull", "Paskan", "Pandjed", "Qelnaar", "Qelqull", "Otiskan", "Rasmorn", "Rasqiroth", "Ravoroth", "Ravobroth", "Rhogar", "Rasghull", "Pruumbish", "Sulprax", "Shaciar", "Suljhan", "Tazlin", "Tazwunax", "Troudorim", "Tarhun", "Trouqiroth", "Uroxan", "Vorjurn", "Vasned", "Villas", "Wulwunax", "Wraseth", "Worqiroth", "Wralin", "Wuvarax", "Wrakris", "Worciar", "Wulvarax", "Wulcrath", "Xarvarax", "Xor", "Xaxis", "Yorzavur", "Yorkris", "Yorkax", "Zarin", "Zragar", "Zrafarn", "Zorfras", "Zaqiroth", "Zraziros")
tu_DragonbornFemaleNames = ("Arihime", "Arizys", "Aqwen", "Azma", "Belbirith", "Belnorae", "Belvyre", "Belkax", "Belbith", "Biri", "Cristhyra", "Crismyse", "Cabirith", "Criswophyl", "Carys", "Carish", "Drysshann", "Drysthibra", "Darina", "Durwarum", "Dagil", "Daar", "Eshsira", "Erlivee", "Eshriel", "Erlipatys", "Erlirinn", "Erlisira", "Eshshann", "Eshrinn", "Eshzys", "Fenys", "Faelarys", "Farideh", "Grigil", "Grisira", "Gurgwen", "Halyassa", "Havilar", "Harann", "Irlyvys", "Irlyrish", "Iriezys", "Jovyre", "Jocoria", "Jheri", "Kanorae", "Kahymm", "Komeila", "Kohime", "Koxora", "Kelshann", "Keldrish", "Kava", "Korina", "Lorarinn", "Liloxiris", "Lilofyire", "Lilorann", "Loralarys", "Liloyassa", "Lorariel", "Lilonys", "Lilodalynn", "Faepatys", "Faegissa", "Fenhymm", "Malzys", "Mibirith", "Mishann", "Nagil", "Nysmeila", "Nysyassa", "Naliann", "Neszys", "Nesgwen", "Nesbis", "Nalyassa", "Nala", "Orinorae", "Orishann",	"Orinorae", "Obis", "Orilarys", "Oliann", "Perthibra", "Pazire", "Perlarys", "Qicys", "Qifyire", "Qimeila", "Quilthibra", "Quilshann", "Quilshann", "Rashifyire", "Ravofarn", "Raiann", "Suwophyl", "Sobith", "Sogwen", "Suliann", "Therbis"	, "Therdalynn", "Theryassa", "Thagwen", "Thava", "Thapora", "Uriqorel", "Ushibith", "Uadjit", "Valmeila", "Valqorel", "Valpatys", "Vyrabith", "Vyrafyire", "Vyrariel", "Wrathibra", "Wrawophyl", "Warina", "Xyriel", "Yavyre", "Yrqwen", "Yrliann", "Zofshann", "Zofsira",	"Zenbis", "Zenbis", "Zofthibra", "Zenpora")
tu_HumanMaleNames = ("Athan", "Armal", "Bundy", "Bowden", "Chell", "Cordus", "Anlow", "Arando", "Bram", "Cale", "Dalkon", "Daylen", "Dodd", "Dungarth", "Dyrk", "Eandro", "Falken", "Feck", "Fenton", "Gryphero", "Hagar", "Jeras", "Krynt", "Lavant", "Leyten", "Madian", "Malfier", "Markus", "Meklan", "Namen", "Navaren", "Nerle", "Nilus", "Ningyan", "Norris", "Quentin", "Semil", "Sevenson", "Steveren", "Talfen", "Tamond", "Taran", "Tavon", "Tegan", "Vanan", "Vincent")
tu_HumanFemaleNames = ("Ayla", "Aluca", "Bethany", "Brandi", "Cara", "Celene", "Azura", "Brey", "Hannah", "Kasaki", "Lorelei", "Mirabel", "Pharana", "Moira", "Rosalyn", "Sachil", "Saidi", "Tanika", "Tura", "Tylsa", "Vencia", "Xandrilla")
tu_DwarfMaleNames = ("Gimond", "Munar", "Balgin", "Munund", "Belgrim", "Ketum", "Barkk", "Balin", "Broor", "Storlin", "Calund", "Kilgol", "Garain", "Gorain", "Garar", "Dimkk", "Goril", "Daltil", "Dalri", "Nalo", "Ketni", "Barlin", "Gargol", "Bofgar", "Gilum", "Durain", "Bofaim", "Callin", "Broak", "Balbur", "Thgrim", "Stortil", "Bolain", "Bulgin", "Klangeddin", "Ortan", "Drund", "Drumin", "Simin", "Buldin", "Hail", "Gimgin")
tu_DwarfFemaleNames = ("Fimola", "Nali", "Simumma", "Broana", "Dimraka", "Dwgini", "Thrgari", "Gormina", "Herunni", "Runbari", "Grii", "Klunni", "Runbura", "Broondi", "Gomana", "Barria", "Fimina", "Kilona", "Nalila", "Bina", "Beltria", "Klraka", "Grutila", "Klona", "Drutila", "Belana", "Gimtila", "Morala", "Stordria", "Gehenna", "Gardina", "Dorrimi", "Daldina", "Broraka", "Fargrima", "Thrgari", "Ovi", "Balgrima", "Bbura", "Herdria", "Thinraka")
tu_ElfMaleNames = ("Adresin","Aduce","Aelrindel","Aerendyl","Aermhar","Aesar","Aeson","Afamrail","Agis","Aglanthol","Ainésilver","Aithlin","Ajaar","Akhelbhen","Akkar","Alabyran", "Albondiel","Alinar","Allain","Alok","Alosrin","Althidon","Amrynn","Anarallath","Andaerean","Andrathath","Anfalen","Anlyth","Aolis","Aquilan","Araevin","Arandron","Aravilar","Arbane","Ardreth","Ardryll","Argus","Arkhun","Arlen","Arun","Ascal","Athtar","Aubric","Aubron","Aulathar","Aulauthar","Aumanas","Aumrauth","Avourel","Baerdelcoam","Baerithryn","Belanor","Beldroth","Bellas","Belstram","Beluar","Bhyrindaar","Biafyndar","Bialaer","Braern","Brindarry","Buttorwyr","Cameron","Chaalmyth","Chathanglas","Cheyrth","Chozzaster","Chylnoth","Cluhurach","Cluym","Cohnal","Conall","Connak","Cornaith","Corym","Cymbiir","Cystenn","Dalyor","Dakath","Dannyd","Daratrine","Darcassan","Darfin","Darthoridan","Deldrach","Delmuth","Delsaran","Dhoelath","Divisav","Drannor","Droth","Druindar","Durlan","Durothil","Dyffros","Earynspieir","Edansyr","Edicuve","Edwyrd","Edyrm","Ehlark","Ehrendil","Eilauver","Elaethan","Elaith","Elandorr","Elanjar","Elashor","Elbauthin","Elbereth","Eldaernth","Eldar","Eldrin","Elénaril","Elenshaer","Elephon","Erdacil","Elidyr","Elion","Elkhazel","Ellisar","Faahresc","Faelyn","Faeranduil","Falael", "Felaern","Fenian","Fhociin","Filarion","Filverel","Finufaranell","Flardryn","Flinar","Gaeleath","Gaelin","Galaeron","Ganamede","Garynnon","Glarald","Glorandal","Grathgor","Haemir","Haladavar","Halafarin","Halamar","Haldreithen","Halgondas","Halpaeril","Halueth","Haryk","Hatharal","Hiflanyl","Horith","Iefyr","Ievos","Ilbryn","Ilimitar","Iliphar","Illithor","Ilphas","Ilrune","Ilthuryn", "Inialos","Injros","Iolas","Iolrath","Itham","Ithraides","Ivlisar","Ivósaar","Ivran","Iymbryl","Iyrandrar","Jandar","Jannalor","Jaonos","Jassin","Jhaan","Jhaartael","Jhaeros","Jharak","Jonik","Jorildyn","Josidiah","Kahvoerm","Kalaerede","Katar","Katyr","Keletheryl","Kelvhan","Kerym","Keryth","Kharis","Khidell","Khiiral","Khilseith","Khuumal","Khyssoun","Kiyuigh","Klaern","Kolvar","Kuskyn","Kuskyn","Kymil","Kyrtaar","Laeroth","Lafarallin","Lamruil","Laosx","Larongar","Lashul","Lathai","Lathlaeril", "Leayonadas", "Lhombaerth", "Lhoris","Lianthorn","Llarm","Luthais","Luvon","Lyari","Lyklor","Lysanthir","Maasli","Maeral","Mardeiym","Marikoth","Marlevaur","Melandrach","Melisander","Merith","Methild","Mhaenal","Mihangyl","Miirphys","Mirthal","Molonym","Morthil","Mothrys","Myrddin","Myriil","Naertho","Naeryndam","Napraeleon","Narbeth","Nardual","Nelaeryn","Nelaeryn","Neldor","Nevarth","Nhamashal","Nieven","Ninthalor","Nopos","Norlorn","Nremyn","Nuvian","Nylian","Nym","Nyvorlas","Oacenth","Oenel","Ohmbryn","Olaurae","Olinsivver","Olithir","Onas","Oncith","Ondabrar","Ondroth","Onvyr","Orist","Orlpar","Ornthalas","Ortauré","Oslarelar","Otaehryn","Othorion","Paeral","Phaendar","Pirphal","Pleufan","Pyrder","Pyrravym","Pywaln","Quynn","Ralnor","Raunaeril","Rauvelore","Reluraun","Rennyn","Reptar","Respen","Rhalyf","Rhangyl","Rhespen","Rhistel","Rhothomir","Rhys","Rilitar","Riluaneth","Rolim","Ruardh","Ruith","Rumathil","Ruvaen","Ruven","Ruvyn","Ryfon","Ryul","Ryvvik","Sadalyn","Saevel","Samblar","Sandevv","Seith","Shael","Silvyr","Strohm","Sylvar","Symkalr","Taanyth","Taegen","Taeglyn","Taeral","Tammson","Tamsin","Tannyll","Tanyl","Taredd","Tarron","Tasar","Tathaln","Tenyajn","Tethir","Thurdan","Tiarshus","Tolthe","Toross","Triandal","Tsaer","Saelethil","Saevel","Sharian","Sinaht","Sudryl","Taenaran","Tanyl","Tarathiel","Tolthe","Ualair","Uevareth","Uldreiyn","Uthorim","Vaalyun","Valderlane","Vaeril","Valmaxian","Vander","Vartan","Venali","Vesper","Vesryn","Vhoadan","Vhoori","Voron","Wylym","Wyn","Wyrran","Xalph","Yhendorn","Zaos","Zelphar","Zulae")
tu_ElfFemaleNames = ("Aribeth", "Aelrue", "Aelynthi", "Aerilaya", "Alais", "Alea", "Allannia","Allisa", "Alynna", "Aloevan", "Alyndra", "Amara","Amra", "Anarzee", "Aravae", "Arlayna", "Arnarra", "Aurae", "Brayrenna", "Calarel", "Chaenath", "Cirilien", "Daenalaia", "Darshee","Duilya", "Ecaeris", "Elanil", "Elanee","Elasha","Eletha","Eloen","Embrae","Esta","Faranni","Fieryat", "Fafriel", "Gaelira","Ghilanna","Gweyr","Hacathra","Halaema","Holone","Ilmadia","Ilyara","Imryll", "Itylra","Jhaer","Ilyrana","Kavrala","Keerla","Keya","Kythaela","Laerdya","Laerune","Leilatha","Llamryl","Lorelei","Lyraesel","Maelyrra","Makaela","Meira","Melarue","Merethyl","Meriel","Mladris","Mylaela","Naevys","Naumys","Nuala","Nushaela","Phantyni","Phyrra","Pollae","Quamara","Roanmara","Ryllae","Saelihn","Saida","Sarya","Seirye","Séonais","Shael","Shalendra","Shanyrria","Shyael","Sorsasta","Syndra","Taenya","Talaedra","Talila","Teryani","Tiatha","Tsarra","Unae","Vashti","Verrona","Yaereene","Yrlissa","Ytharra","Zoastria")
tu_GnomeMaleNames = ("Begnym", "Jinzic", "Borwass", "Snaanbag", "Labkost", "Jenkkig", "Clamdor", "Bitty", "Brena", "Amorette", "Sarug", "Erpos", "Nimin", "Jorhim", "Salmorn", "Vorbar", "Davdri", "Valmin", "Nigrim", "Davkas", "Brocc", "Burgell", "Roondar", "Seebo", "Wrenn", "Zook")
tu_GnomeFemaleNames = ("Tyra", "Tawyn", "Rena", "Zanitina", "Tifapine", "Lyda", "Satra", "Lorifi", "Daphiphina", "Arila", "Zanigani", "Zindira", "Qiroe", "Tifaceli", "Folxi", "Grentina", "Heshana", "Tifamyn", "Myna", "Cartra", "Dedellbop", "Berene", "Dawzelene", "Rikkavikki", "Jorzivie", "Gaia", "Nackle", "Rikkenedol", "Lanziver", "Uvarky", "Ninzeleye", "Forrisiren", "Erbie", "Ralney", "Sacheppe", "Puddlefie", "Jortix", "Temmie")
tu_HalflingMaleNames = ("Adalgrim","Adelard","Alton","Andwise","Anson","Balbo","Bandobras","Beau","Bildren","Bingus","Bodo","Bolger","Bungo","Cade","Calkin","Cotman","Cottar","Drogo","Dudo","Eldon","Falco","Fastolph","Filibert","Flambard","Fosco","Garret","Genrill","Griffo","Halfred","Hildigrim","Hob","Holman","Kepli","Largo","Longo","Letho","Lyle","Milo","Minto","Morro","Mosco","Mungo","Odo","Olo","Osborn","Otho","Paldo","Peregrin","Pervince","Pimpo","Polo","Ponto","Porto","Posco","Ronald","Rorimac","Roscoe","Rufus","Sam","Sancho","Saradac","Seredoc","Theadric","Tolman","Wellby","Wilcome")
tu_HalflingFemaleNames = ("Adaldrida", "Amranth", "Amaryllis", "Angelica", "Aspodel", "Belba", "Belladonna","Berylla","Camellia","Carissa","Celandine","Charmaine","Cora","Crystal","Daisy","Diamond","Donamira","Dora","Eglantine","Elanor","Esmerelda","Euphemia","Gilly","Gwiston","Hilda","Jillian","Lavinia","Lily",	"Lidda","Lobelia","Malva","Marigold","May","Melindy","Mentha","Merla","Mimosa","Mirabella","Myrtle","Pansy","Pearl","Pedderee","Peony","Petrilly","Poppy","Portia","Primula","Prisca","Rose","Ruby","Seraphina","Susannah","Verna","Viloet")

tu_AllMaleNameTuples = (tu_DragonbornMaleNames, tu_HumanMaleNames, tu_DwarfMaleNames, tu_ElfMaleNames, tu_GnomeMaleNames, tu_HalflingMaleNames)
tu_AllFemaleNameTuples = (tu_DragonbornFemaleNames, tu_HumanFemaleNames, tu_DwarfFemaleNames, tu_ElfFemaleNames, tu_GnomeFemaleNames, tu_HalflingFemaleNames)

tu_ALLGenders = ("Male", "Female")

tu_Vowels = ("a", "e", "i", "o", "u")
tu_Consonants = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "m", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")

tu_Races = ("Dragonborn", "Dwarf", "Elf", "Gnome", "Halfling", "Half-Elf", "Half-Orc", "Human", "Tiefling")
tu_Talents = ("Plays a musical instrument", "Speaks several languages fluently", "Unbelievably Lucky", "Perfect Memory", "Great with Animals", "Great with Children", "Great at solving puzzles", "Great at one game", "Great at impersonations", "Draws beautifully", "Sings beautifully", "Drinks everyone under the table", "Expert carpenter", "Expert Cook", "Expert dart thrower and rock skipper", "Expert juggler", "Skilled actor and master of disguise", "Skilled dancer", "Knows thieves' cant")
tu_InteractionTraits = ("Argumentative", "Arrogant", "Blustering", "Rude", "Curious", "Friendly", "Honest", "Hot-Tempered", "Irritable", "Ponderous", "Quiet", "Suspicious")
tu_Mannerisms = ("Prone to singing, whistling or humming quietly", "Speaks in rhyme or some peculiar way", "Particularly high or low voice", "Slurs words, lisps or stutters", "Enunciates overly clearly", "Speaks loudly", "Whispers", "Uses flowery speech or long words", "Frequently uses the wrong word", "Uses colourful oaths and exclamations", "Makes constant jokes or puns", "Prone to predictions of doom", "Fidgets", "Squints", "Stares in to the distance", "Chews something", "Paces", "Taps fingers", "Bites fingernails", "Twirls hair or tugs beard")
tu_Bonds = ("Dedicated to a personal life goal", "Protective of close family members", "Protective of colleagues or compatriots", "Loyal to a benefactor, patron or employer",
            "Captivated by a romantic interest", "Drawn to a special place", "Protective of a sentimental keepsake", "Protective of a valuable possesion", "Out for revenge", "Just looking to live peacefully")

# Used for NPCs alignment. Ideals are arranged 'Good, bad, good, bad...etc' to make results more randomized
tu_IdealsGood = ("Beauty", "Charity", "Greater good", "Life", "Respect", "Self-Sacrifice")
tu_IdealsEvil = ("Domination", "Greed", "Might", "Pain", "Retribution", "Slaughter")
tu_IdealsLawful = ("Community", "Fairness", "Honour", "Logic", "Responsibility", "Tradition")
tu_IdealsChaotic = ("Change", "Creativity", "Freedom", "Independence", "No limits", "Whimsy")
tu_IdealsNeutral = ("Balance", "Aspiration", "Knowledge", "Discovery", "Live and let die", "Glory", "Moderation", "Nation", "Neutrality", "Redemption", "People", "Self-Knowledge")

# variables used to control sizes of elements in gui
var_lblHeadHeight = 1
var_lblContWidth = 35
var_lblHeadWidth = 18
var_lblSmallWidth = 10
var_txtBTNWidth = 5
var_txtBTNPadding = 25

# create an image to use on a button
rollButtonImage = tk.PhotoImage(file=r"C:\Users\Basil\Desktop\NPC Generator\smalld20white.png")

# create a frame to put all alignment option buttons on
TK_AlignmentFrame = tk.Frame(root, highlightbackground="black", highlightthickness=2, padx= 5, pady= 5)
TK_AlignmentFrame.grid(row=9, column=1)

# create a frame to put all race and gender buttons on
TK_GenderRaceFrame = tk.Frame(root, highlightbackground="black", highlightthickness=2, padx=5, pady=5)
TK_GenderRaceFrame.grid(row=9, column=2)
# endregion

# ====================FUNCTIONS====================
# function to generate a random character and return it
def randomCharacter(toggle):
    if toggle == 1:
        character = tu_Consonants[random.randint(0, int(len(tu_Consonants)-1))]
        return character
    elif toggle == 0:
        character = tu_Vowels[random.randint(0, int(len(tu_Vowels)-1))]
        return character
    else:
        print("Something went wrong in the randomCharacter function!")
#------------------------
# function to generate a random last name from a bunch of random letters
def FN_randLastName():
    firstCha = randomCharacter(1)
    CappedfirstCha = firstCha.upper()
    secondCha = randomCharacter(0)
    thirdCha = randomCharacter(1)
    fourthCha = randomCharacter(1)
    fifthCha = randomCharacter(0)
    sixthCha = randomCharacter(1)

    product = (str(CappedfirstCha) + str(secondCha) + str(thirdCha) + str(fourthCha) + str(fifthCha) + str(sixthCha))

    return product
#------------------------
def bark(input):
    print("ADMIN MESSAGE-----> "+str(input))
#------------------------
# function to select a random male/female name based on toggle parameter
def FN_getFirstName(tuple):
    firstName = ""
    firstName = (tuple[random.randint(0, int(len(tuple)-1))])
    return firstName
#------------------------
# function to select a random NPC Talent
def FN_getTalent():
    var_talent = (tu_Talents[random.randint(0, int(len(tu_Talents)-1))])
    return var_talent
#------------------------
# function to select a random NPC Mannerism
def FN_getMannerism():
    var_mannerism = (
        tu_Mannerisms[random.randint(0, int(len(tu_Mannerisms)-1))])
    return var_mannerism
#------------------------
# function to select a random NPC Interaction Trait
def FN_getInterTrait():
    var_interTrait = (tu_InteractionTraits[random.randint(
        0, int(len(tu_InteractionTraits)-1))])
    return var_interTrait
#------------------------
# function to select a random NPC bond
def FN_getBond():
    var_bond = (tu_Bonds[random.randint(0, int(len(tu_Bonds)-1))])
    return var_bond
#------------------------
# function to select a random NPC alignment trait, based on a button matching LG, NG, CG etc...
def FN_GetAlignmentTrait(choice, flavour):
    # region function for setting alignment...
    VAR_InputChoice = int(choice)
    VAR_InputFlavour = int(flavour)

    if VAR_InputChoice == 0 and VAR_InputFlavour == 0:
        # option for lawful good
        var_LawTrait = (tu_IdealsLawful[random.randint(
            0, int(len(tu_IdealsLawful)-1))])
        var_GoodTrait = (
            tu_IdealsGood[random.randint(0, int(len(tu_IdealsGood)-1))])
        lbl_NPCAlignment.config(text=var_LawTrait + " and " + var_GoodTrait)
        lbl_NPCAlignmentHEAD.config(text="Alignment Traits (LG)")
       # print("Fired LG. 'FN_GetAlignmentTrait("+str(VAR_InputChoice)+", "+str(VAR_InputFlavour)+". The result was: "+str(var_LawTrait)+" and "+str(var_GoodTrait))

    elif VAR_InputChoice == 0 and VAR_InputFlavour == 1:
        # option for neutral good
        var_NeutralTrait = (
            tu_IdealsNeutral[random.randint(0, int(len(tu_IdealsNeutral)-1))])
        var_GoodTrait = (
            tu_IdealsGood[random.randint(0, int(len(tu_IdealsGood)-1))])
        lbl_NPCAlignment.config(
            text=var_NeutralTrait + " and " + var_GoodTrait)
        lbl_NPCAlignmentHEAD.config(text="Alignment Traits (NG)")
       # print("Fired NG. 'FN_GetAlignmentTrait("+str(VAR_InputChoice)+", "+str(VAR_InputFlavour)+". The result was: "+str(var_NeutralTrait)+" and "+str(var_GoodTrait))

    elif VAR_InputChoice == 0 and VAR_InputFlavour == 2:
        # option for chaotic good
        var_ChaoticTrait = (
            tu_IdealsChaotic[random.randint(0, int(len(tu_IdealsChaotic)-1))])
        var_GoodTrait = (
            tu_IdealsGood[random.randint(0, int(len(tu_IdealsGood)-1))])
        lbl_NPCAlignment.config(
            text=var_ChaoticTrait + " and " + var_GoodTrait)
        lbl_NPCAlignmentHEAD.config(text="Alignment Traits (CG)")
       # print("Fired CG. 'FN_GetAlignmentTrait("+str(VAR_InputChoice)+", "+str(VAR_InputFlavour)+". The result was: "+str(var_ChaoticTrait)+" and "+str(var_GoodTrait))

    elif VAR_InputChoice == 1 and VAR_InputFlavour == 0:
        # option for Lawful Neutral
        var_LawfulTrait = (
            tu_IdealsLawful[random.randint(0, int(len(tu_IdealsLawful)-1))])
        var_NeutralTrait = (
            tu_IdealsNeutral[random.randint(0, int(len(tu_IdealsNeutral)-1))])
        lbl_NPCAlignment.config(text=var_LawfulTrait +
                                " and " + var_NeutralTrait)
        lbl_NPCAlignmentHEAD.config(text="Alignment Traits (LN)")

    elif VAR_InputChoice == 1 and VAR_InputFlavour == 1:
        # option for True Neutral
        var_TrueTrait = (tu_IdealsNeutral[random.randint(
            0, int(len(tu_IdealsNeutral)-1))])
        var_NeutralTrait = (
            tu_IdealsNeutral[random.randint(0, int(len(tu_IdealsNeutral)-1))])
        lbl_NPCAlignment.config(text=var_TrueTrait +
                                " and " + var_NeutralTrait)
        lbl_NPCAlignmentHEAD.config(text="Alignment Traits (TN)")

    elif VAR_InputChoice == 1 and VAR_InputFlavour == 2:
        # option for Chaotic Neutral
        var_ChaoticTrait = (
            tu_IdealsChaotic[random.randint(0, int(len(tu_IdealsChaotic)-1))])
        var_NeutralTrait = (
            tu_IdealsNeutral[random.randint(0, int(len(tu_IdealsNeutral)-1))])
        lbl_NPCAlignment.config(
            text=var_ChaoticTrait + " and " + var_NeutralTrait)
        lbl_NPCAlignmentHEAD.config(text="Alignment Traits (CN)")

    elif VAR_InputChoice == 2 and VAR_InputFlavour == 0:
        # option for Lawful Evil
        var_LawfulTrait = (
            tu_IdealsLawful[random.randint(0, int(len(tu_IdealsLawful)-1))])
        var_EvilTrait = (
            tu_IdealsEvil[random.randint(0, int(len(tu_IdealsEvil)-1))])
        lbl_NPCAlignment.config(text=var_LawfulTrait + " and " + var_EvilTrait)
        lbl_NPCAlignmentHEAD.config(text="Alignment Traits (LE)")

    elif VAR_InputChoice == 2 and VAR_InputFlavour == 1:
        # option for Neutral Evil
        var_NeutralTrait = (
            tu_IdealsNeutral[random.randint(0, int(len(tu_IdealsNeutral)-1))])
        var_EvilTrait = (
            tu_IdealsEvil[random.randint(0, int(len(tu_IdealsEvil)-1))])
        lbl_NPCAlignment.config(
            text=var_NeutralTrait + " and " + var_EvilTrait)
        lbl_NPCAlignmentHEAD.config(text="Alignment Traits (NE)")

    elif VAR_InputChoice == 2 and VAR_InputFlavour == 2:
        # option for Neutral Evil
        var_ChaoticTrait = (
            tu_IdealsChaotic[random.randint(0, int(len(tu_IdealsChaotic)-1))])
        var_EvilTrait = (
            tu_IdealsEvil[random.randint(0, int(len(tu_IdealsEvil)-1))])
        lbl_NPCAlignment.config(
            text=var_ChaoticTrait + " and " + var_EvilTrait)
        lbl_NPCAlignmentHEAD.config(text="Alignment Traits (CE)")

    else:
        print("Something went wrong when trying to pick an alignment! The indexes used were " + str(VAR_InputChoice)+" and " + str(VAR_InputFlavour)
              )
# endregion
#------------------------
# function to get an npc by race button clicked
def FN_GetNPCByGenderRace(race, gender):
#region     
    print("----->Fired the getnpcbygender function")
    var_InputRace = int(race)
    var_InputGender = int(gender)
    var_RandomRaceNameIndex = 0
    var_PickedName = "[NULL]"
    # 0=Dragonborn, 1=Dwarf, 2=Elf, 3=Gnome, 4=Halfling, 5=Half-Elf, 6=Half-Orc, 7=Human, 8=Tiefling
    # 0=male, female

#region------------------DRAGONBORN GENS
    # get a random index based on the length of the Dragonborn male names index...
    var_RandomRaceNameIndex = random.randint(0, int(len(tu_DragonbornMaleNames)-1))

    # if the race paramater and gender is Dragonborn and male...
    if var_InputRace == 0 and var_InputGender == 0:
        # and then assign a name to a variable, based off that random index...
        var_PickedName = tu_DragonbornMaleNames[var_RandomRaceNameIndex]

        # then get the relevant dropdown to print out the race, gender and name
        DDL_Races.current(0)
        lbl_NPCName.config(text=var_PickedName + " " + FN_randLastName())
        DDL_Gender.current(0)
        
    elif var_InputRace == 0 and var_InputGender == 1:
        var_RandomRaceNameIndex = random.randint(0, int(len(tu_DragonbornFemaleNames)-1))
        var_PickedName = tu_DragonbornFemaleNames[var_RandomRaceNameIndex]

        DDL_Races.current(0)
        lbl_NPCName.config(text=var_PickedName + " " + FN_randLastName())
        DDL_Gender.current(1)
        #endregion
        
#region------------------DWARF GENS
    elif var_InputRace == 1 and var_InputGender == 0:
        var_RandomRaceNameIndex = random.randint(0, int(len(tu_DwarfMaleNames)-1))
        var_PickedName = tu_DwarfMaleNames[var_RandomRaceNameIndex]

        DDL_Races.current(1)
        lbl_NPCName.config(text=var_PickedName + " " + FN_randLastName())
        DDL_Gender.current(0)

    elif var_InputRace == 1 and var_InputGender == 1:
        var_RandomRaceNameIndex = random.randint(
        0, int(len(tu_DwarfFemaleNames)-1))
        var_PickedName = tu_DwarfFemaleNames[var_RandomRaceNameIndex]

        DDL_Races.current(1)
        lbl_NPCName.config(text=var_PickedName + " " + FN_randLastName())
        DDL_Gender.current(1)
        #endregion

#region------------------ELF GENS
    elif var_InputRace == 2 and var_InputGender == 0:
        var_RandomRaceNameIndex = random.randint(0, int(len(tu_ElfMaleNames)-1))
        var_PickedName = tu_ElfMaleNames[var_RandomRaceNameIndex]

        DDL_Races.current(2)
        lbl_NPCName.config(text=var_PickedName + " " + FN_randLastName())
        DDL_Gender.current(0)


    elif var_InputRace == 2 and var_InputGender == 1:
        var_RandomRaceNameIndex = random.randint(0, int(len(tu_ElfFemaleNames)-1))
        var_PickedName = tu_ElfFemaleNames[var_RandomRaceNameIndex]

        DDL_Races.current(2)
        lbl_NPCName.config(text=var_PickedName + " " + FN_randLastName())
        DDL_Gender.current(1)
        #endregion

#region------------------GNOME GENS
    elif var_InputRace == 3 and var_InputGender == 0:
        var_RandomRaceNameIndex = random.randint(0, int(len(tu_GnomeMaleNames)-1))
        var_PickedName = tu_GnomeMaleNames[var_RandomRaceNameIndex]

        DDL_Races.current(3)
        lbl_NPCName.config(text=var_PickedName + " " + FN_randLastName())
        DDL_Gender.current(0)

    elif var_InputRace == 3 and var_InputGender == 1:
        var_RandomRaceNameIndex = random.randint(0, int(len(tu_GnomeFemaleNames)-1))
        var_PickedName = tu_GnomeFemaleNames[var_RandomRaceNameIndex]

        DDL_Races.current(3)
        lbl_NPCName.config(text=var_PickedName + " " + FN_randLastName())
        DDL_Gender.current(1)
        #endregion

#region------------------HALFLING GENS
    elif var_InputRace == 4 and var_InputGender == 0:
        var_RandomRaceNameIndex = random.randint(0, int(len(tu_HalflingMaleNames)-1))
        var_PickedName = tu_HalflingMaleNames[var_RandomRaceNameIndex]

        DDL_Races.current(4)
        lbl_NPCName.config(text=var_PickedName + " " + FN_randLastName())
        DDL_Gender.current(0)

    elif var_InputRace == 4 and var_InputGender == 1:
        var_RandomRaceNameIndex = random.randint(0, int(len(tu_HalflingFemaleNames)-1))
        var_PickedName = tu_HalflingFemaleNames[var_RandomRaceNameIndex]

        DDL_Races.current(4)
        lbl_NPCName.config(text=var_PickedName + " " + FN_randLastName())
        DDL_Gender.current(1)
        #endregion

#region------------------HUMAN GENS
    elif var_InputRace == 7 and var_InputGender == 0:
        var_RandomRaceNameIndex = random.randint(0, int(len(tu_HumanMaleNames)-1))
        var_PickedName = tu_HumanMaleNames[var_RandomRaceNameIndex]

        DDL_Races.current(7)
        lbl_NPCName.config(text=var_PickedName + " " + FN_randLastName())
        DDL_Gender.current(0)

    elif var_InputRace == 7 and var_InputGender == 1:
        var_RandomRaceNameIndex = random.randint(0, int(len(tu_HumanFemaleNames)-1))
        var_PickedName = tu_HumanFemaleNames[var_RandomRaceNameIndex]

        DDL_Races.current(7)
        lbl_NPCName.config(text=var_PickedName + " " + FN_randLastName())
        DDL_Gender.current(1)
#endregion

    else:
        print("Something went wrong when clicking a name! Check FN_GetNPCByGenderRace")
#endregion
#------------------------
# IMPORTANT! Generate an entirely new NPC here
def FN_click():
 # region to generate an entire NPC from a single roll
    # generate a random gender...
    FN_EnableObjects()
    rand_gender_index = random.randint(0, 1)
    VAR_GenderChoice = tu_ALLGenders[rand_gender_index]

    # ...then a race
    rand_race_index = random.randint(0, int(len(tu_Races)-1))

    #now populate the dropdownlist with a random value from their relevant tuples
    VAR_RaceChoice = tu_Races[rand_race_index]
    DDL_Races.current(rand_race_index)
    DDL_Gender.current(rand_gender_index)
        
    talentIndex = random.randint(0,int(len(tu_Talents)-1))
    DDL_Talent.current(talentIndex)
    
    interTraitIndex = random.randint(0,int(len(tu_InteractionTraits)-1))
    DDL_InterTrait.current(interTraitIndex)

    bondTraitIndex = random.randint(0,int(len(tu_Bonds)-1))
    DDL_Bonds.current(bondTraitIndex)

    tuple_chosen = ""

    # if random gender choice is male...
    if VAR_GenderChoice == "Male":
        rand_index = random.randint(0, int(len(tu_AllMaleNameTuples)))-1
        tuple_chosen = tu_AllMaleNameTuples[rand_index]
        VAR_FirstName = FN_getFirstName(tuple_chosen)

    elif VAR_GenderChoice == "Female":
        rand_index = random.randint(0, int(len(tu_AllFemaleNameTuples)))-1
        tuple_chosen = tu_AllFemaleNameTuples[rand_index]
        VAR_FirstName = FN_getFirstName(tuple_chosen)

    else:
        print("Oh shit! Something went wrong when selecting a name based on gender! Check the FN_Click() function.")

    VAR_FirstName = FN_getFirstName(tuple_chosen)
    VAR_LastName = FN_randLastName()
    VAR_Talent = FN_getTalent()
    VAR_InterTrait = FN_getInterTrait()
    VAR_Bond = FN_getBond()
    VAR_RandAlignmentChoice = random.randint(0,2)
    VAR_RandAlignmentFlavour = random.randint(0,2)
    FN_GetAlignmentTrait(VAR_RandAlignmentChoice, VAR_RandAlignmentFlavour)

    lbl_NPCName.config(text=VAR_FirstName + " "+VAR_LastName)
 # endregion
#------------------------
#disable all elements but one overall gen button. fires once at start of program
def FN_DisableObjects():
#region
    btn_DRAGONBORNfemale["state"] = DISABLED
    btn_DRAGONBORNmale["state"] = DISABLED
    btn_DWARFfemale["state"] = DISABLED
    btn_DWARFmale["state"] = DISABLED
    btn_ELFfemale["state"] = DISABLED
    btn_ELFmale["state"] = DISABLED
    btn_HUMANfemale["state"] = DISABLED
    btn_HUMANmale["state"] = DISABLED
    btn_GNOMEfemale["state"] = DISABLED
    btn_GNOMEmale["state"] = DISABLED
    btn_HALFLINGfemale["state"] = DISABLED
    btn_HALFLINGmale["state"] = DISABLED
    
    btn_LawGoodBTN["state"] = DISABLED
    btn_NeutralGoodBTN["state"] = DISABLED
    btn_ChaoticGoodBTN["state"] = DISABLED
    btn_LawNeutralBTN["state"] = DISABLED
    btn_TrueNeutralBTN["state"] = DISABLED
    btn_ChaoticNeutralBTN["state"] = DISABLED
    btn_LawEvilBTN["state"] = DISABLED
    btn_NeutralEvilBTN["state"] = DISABLED
    btn_ChaoticEvilBTN["state"] = DISABLED
    
    DDL_Races["state"] = DISABLED
    DDL_Gender["state"] = DISABLED
    DDL_Talent["state"] = DISABLED
    DDL_Bonds["state"] = DISABLED
    DDL_InterTrait["state"] = DISABLED
#endregion
#------------------------
#disable all elements but one overall gen button. fires once at start of program
def FN_EnableObjects():
   #region
    btn_DRAGONBORNfemale["state"] = NORMAL
    btn_DRAGONBORNmale["state"] = NORMAL
    btn_DWARFfemale["state"] = NORMAL
    btn_DWARFmale["state"] = NORMAL
    btn_ELFfemale["state"] = NORMAL
    btn_ELFmale["state"] = NORMAL
    btn_HUMANfemale["state"] = NORMAL
    btn_HUMANmale["state"] = NORMAL
    btn_GNOMEfemale["state"] = NORMAL
    btn_GNOMEmale["state"] = NORMAL
    btn_HALFLINGfemale["state"] = NORMAL
    btn_HALFLINGmale["state"] = NORMAL

    btn_LawGoodBTN["state"] = NORMAL
    btn_NeutralGoodBTN["state"] = NORMAL
    btn_ChaoticGoodBTN["state"] = NORMAL
    btn_LawNeutralBTN["state"] = NORMAL
    btn_TrueNeutralBTN["state"] = NORMAL
    btn_ChaoticNeutralBTN["state"] = NORMAL
    btn_LawEvilBTN["state"] = NORMAL
    btn_NeutralEvilBTN["state"] = NORMAL
    btn_ChaoticEvilBTN["state"] = NORMAL
    
    DDL_Races["state"] = NORMAL
    DDL_Gender["state"] = NORMAL
    DDL_Talent["state"] = NORMAL
    DDL_Bonds["state"] = NORMAL
    DDL_InterTrait["state"] = NORMAL
#endregion
#------------------------
#Function for the combobox when a new element is selected
#THIS CAN ONLY BE CALLED AFTER THE COMBOBOX HAS BEEN ENABLED!
def callbackFunc(event):
    currentSel = DDL_Races.get()
    genderIdx = DDL_Gender.get()
        
    genderTrueIdx = 0
        
    if genderIdx == "Male":
        genderTrueIdx = 0
    else:
        genderTrueIdx = 1
        
    if currentSel == "Dragonborn":
        FN_GetNPCByGenderRace(0,genderTrueIdx)
    elif currentSel == "Dwarf":
        FN_GetNPCByGenderRace(1,genderTrueIdx)
    elif currentSel == "Elf":
        FN_GetNPCByGenderRace(2,genderTrueIdx)
    elif currentSel == "Gnome":
        FN_GetNPCByGenderRace(3,genderTrueIdx)
    elif currentSel == "Halfling":
        FN_GetNPCByGenderRace(4,genderTrueIdx)
    elif currentSel == "Human":
        FN_GetNPCByGenderRace(7,genderTrueIdx)
    else:
        return

#region -function called when gender dropdown changes its selection
def callbackFuncGender(event):

    genderTrueIdx = 0
    currentGender = DDL_Gender.get()
    currentRace = DDL_Races.get()
        
    if currentGender == "Male":
        genderTrueIdx = 0
    else:
        genderTrueIdx = 1
    
    if currentRace == "Dragonborn":
        FN_GetNPCByGenderRace(0,genderTrueIdx)
    elif currentRace == "Dwarf":
        FN_GetNPCByGenderRace(1,genderTrueIdx)
    elif currentRace == "Elf":
        FN_GetNPCByGenderRace(2,genderTrueIdx)
    elif currentRace == "Gnome":
        FN_GetNPCByGenderRace(3,genderTrueIdx)
    elif currentRace == "Halfling":
        FN_GetNPCByGenderRace(4,genderTrueIdx)
    elif currentRace == "Human":
        FN_GetNPCByGenderRace(7,genderTrueIdx)
    #endregion
# ====================TKINTER WINDOW WORK====================

# -----label creation and positioning
# region
lbl_Title = tk.Label(root, text="NPC GENERATOR", font='Helvetica 16 bold', width=var_lblContWidth, bg="#666", fg="white")
lbl_Title.grid(row=1, column=1, columnspan = 3, sticky = tk.W+tk.E)

lbl_NPCNameHEAD = tk.Label(root, text="Name", font='Helvetica 16 bold',  width=var_lblHeadWidth, bg="#aaa", fg="white")
lbl_NPCNameHEAD.grid(row=2, column=1)
lbl_NPCName = tk.Label(root, text="?", font='Helvetica 12', relief="groove", width=var_lblContWidth, height=var_lblHeadHeight)
lbl_NPCName.grid(row=2, column=2)

lbl_NPCGenderHEAD = tk.Label(root, text="Gender", font='Helvetica 16 bold',  width=var_lblHeadWidth, bg="#aaa", fg="white")
lbl_NPCGenderHEAD.grid(row=3, column=1)

#depreceated. use DDL_Gender instead
#lbl_NPCGender = tk.Label(root, text="?", font='Helvetica 12', relief="groove", width=var_lblContWidth, height=var_lblHeadHeight)
#lbl_NPCGender.grid(row=3, column=2)

lbl_NPCRaceHEAD = tk.Label(root, text="Race", font='Helvetica 16 bold',  width=var_lblHeadWidth, bg="#aaa", fg="white")
lbl_NPCRaceHEAD.grid(row=4, column=1)

#depreceated. use DDL_Races instead
#lbl_NPCRace = tk.Label(root, text="?", font='Helvetica 12', relief="groove", width=var_lblContWidth, height=var_lblHeadHeight)
#lbl_NPCRace.grid(row=4, column=2)

lbl_NPCTalentHEAD = tk.Label(root, text="Talent", font='Helvetica 16 bold', width=var_lblHeadWidth, bg="#aaa", fg="white")
lbl_NPCTalentHEAD.grid(row=5, column=1)

#depreceated. use DDL_Talent instead
#lbl_NPCTalent = tk.Label(root, text="?", font='Helvetica 12', relief="groove", width=var_lblContWidth, height=var_lblHeadHeight)
#lbl_NPCTalent.grid(row=5, column=2)

lbl_NPCInterTraitHEAD = tk.Label(root, text="Interaction Trait", font='Helvetica 16 bold',  width=var_lblHeadWidth, bg="#aaa", fg="white")
lbl_NPCInterTraitHEAD.grid(row=6, column=1)

#depreceated. use DDL_InterTrait instead
#lbl_NPCInterTrait = tk.Label(root, text="?", font='Helvetica 12', relief="groove", width=var_lblContWidth, height=var_lblHeadHeight)
#lbl_NPCInterTrait.grid(row=6, column=2)

lbl_NPCBondHEAD = tk.Label(root, text="Bond", font='Helvetica 16 bold', width=var_lblHeadWidth, bg="#aaa", fg="white")
lbl_NPCBondHEAD.grid(row=7, column=1)

#depreceated. use DDL_Bond instead
#lbl_NPCBond = tk.Label(root, text="?", font='Helvetica 12', relief="groove", width=var_lblContWidth, height=var_lblHeadHeight)
#lbl_NPCBond.grid(row=7, column=2)

lbl_NPCAlignmentHEAD = tk.Label(root, text="Alignment Traits", font='Helvetica 16 bold', width=var_lblHeadWidth, bg="#aaa", fg="white")
lbl_NPCAlignmentHEAD.grid(row=8, column=1)
lbl_NPCAlignment = tk.Label(root, text="?", font='Helvetica 12', relief="groove", width=var_lblContWidth, height=var_lblHeadHeight)
lbl_NPCAlignment.grid(row=8, column=2)
# endregion

# -----button creation and positioning
myButton = tk.Button(TK_GenderRaceFrame, command=FN_click, padx=50, image=rollButtonImage, bg="navy", fg="#FFF")
myButton.grid(row=19, column=2)

# races headers (Male/Female)
lbl_RacesTitleHeader = tk.Label(TK_GenderRaceFrame, text="RACES", font='Helvetica 12 bold', relief="sunken", width=var_lblSmallWidth, height=var_lblHeadHeight)
lbl_RacesTitleHeader.grid(row=8, column=1)
lbl_MaleHeader = tk.Label(TK_GenderRaceFrame, text="Male", font='Helvetica 12 bold', relief="ridge", width=(var_lblSmallWidth)-3, height=var_lblHeadHeight)
lbl_MaleHeader.grid(row=8, column=2)
lbl_FemaleHeader = tk.Label(TK_GenderRaceFrame, text="Female", font='Helvetica 12 bold', relief="ridge", width=(var_lblSmallWidth)-3, height=var_lblHeadHeight)
lbl_FemaleHeader.grid(row=8, column=3)

# male/female Dragonborn buttons
btn_DRAGONBORNmale = tk.Button(TK_GenderRaceFrame, command=lambda: FN_GetNPCByGenderRace(0, 0), padx=50, image=rollButtonImage, bg="black", fg="#FFF")
btn_DRAGONBORNfemale = tk.Button(TK_GenderRaceFrame, padx=50, command=lambda: FN_GetNPCByGenderRace(0, 1), image=rollButtonImage, bg="black", fg="#FFF")
lbl_DragonbornGens = tk.Label(TK_GenderRaceFrame, text="Dragonborn", font='Helvetica 12 bold', relief="ridge",width=var_lblSmallWidth, height=var_lblHeadHeight)
lbl_DragonbornGens.grid(row=9, column=1)
btn_DRAGONBORNmale.grid(row=9, column=2)
btn_DRAGONBORNfemale.grid(row=9, column=3)

# male/female Dwarf buttons
btn_DWARFmale = tk.Button(TK_GenderRaceFrame, command=lambda: FN_GetNPCByGenderRace(1, 0), padx=50, image=rollButtonImage, bg="black", fg="#FFF")
btn_DWARFfemale = tk.Button(TK_GenderRaceFrame, padx=50, command=lambda: FN_GetNPCByGenderRace(1, 1), image=rollButtonImage, bg="black", fg="#FFF")
lbl_DWARFGens = tk.Label(TK_GenderRaceFrame, text="Dwarf", font='Helvetica 12 bold', relief="ridge", width=var_lblSmallWidth, height=var_lblHeadHeight)
lbl_DWARFGens.grid(row=10, column=1)
btn_DWARFmale.grid(row=10, column=2)
btn_DWARFfemale.grid(row=10, column=3)

# male/female ELF buttons
btn_ELFmale = tk.Button(TK_GenderRaceFrame, command=lambda: FN_GetNPCByGenderRace(2, 0), padx=50, image=rollButtonImage, bg="black", fg="#FFF")
btn_ELFfemale = tk.Button(TK_GenderRaceFrame, padx=50, command=lambda: FN_GetNPCByGenderRace(2, 1), image=rollButtonImage, bg="black", fg="#FFF")
lbl_ELFGens = tk.Label(TK_GenderRaceFrame, text="Elf", font='Helvetica 12 bold', relief="ridge", width=var_lblSmallWidth, height=var_lblHeadHeight)
lbl_ELFGens.grid(row=11, column=1)
btn_ELFmale.grid(row=11, column=2)
btn_ELFfemale.grid(row=11, column=3)

# male/female gnome buttons
btn_GNOMEmale = tk.Button(TK_GenderRaceFrame, command=lambda: FN_GetNPCByGenderRace(3, 0), padx=50, image=rollButtonImage, bg="black", fg="#FFF")
btn_GNOMEfemale = tk.Button(TK_GenderRaceFrame, padx=50, command=lambda: FN_GetNPCByGenderRace(3, 1), image=rollButtonImage, bg="black", fg="#FFF")
lbl_GNOMEGens = tk.Label(TK_GenderRaceFrame, text="Gnome", font='Helvetica 12 bold', relief="ridge", width=var_lblSmallWidth, height=var_lblHeadHeight)
lbl_GNOMEGens.grid(row=12, column=1)
btn_GNOMEmale.grid(row=12, column=2)
btn_GNOMEfemale.grid(row=12, column=3)

# male/female Halfling buttons
btn_HALFLINGmale = tk.Button(TK_GenderRaceFrame, command=lambda: FN_GetNPCByGenderRace(4, 0), padx=50, image=rollButtonImage, bg="black", fg="#FFF")
btn_HALFLINGfemale = tk.Button(TK_GenderRaceFrame, padx=50, command=lambda: FN_GetNPCByGenderRace(4, 1), image=rollButtonImage, bg="black", fg="#FFF")
lbl_HALFLINGGens = tk.Label(TK_GenderRaceFrame, text="Halfling", font='Helvetica 12 bold', relief="ridge", width=var_lblSmallWidth, height=var_lblHeadHeight)
lbl_HALFLINGGens.grid(row=13, column=1)
btn_HALFLINGmale.grid(row=13, column=2)
btn_HALFLINGfemale.grid(row=13, column=3)

# male/female human buttons
btn_HUMANmale = tk.Button(TK_GenderRaceFrame, command=lambda: FN_GetNPCByGenderRace(7, 0), padx=50, image=rollButtonImage, bg="black", fg="#FFF")
btn_HUMANfemale = tk.Button(TK_GenderRaceFrame, command=lambda: FN_GetNPCByGenderRace(7, 1), padx=50, image=rollButtonImage, bg="black", fg="#FFF")
lbl_HumanGens = tk.Label(TK_GenderRaceFrame, text="Human", font='Helvetica 12 bold', relief="ridge", width=var_lblSmallWidth, height=var_lblHeadHeight)
lbl_HumanGens.grid(row=15, column=1)
btn_HUMANmale.grid(row=15, column=2)
btn_HUMANfemale.grid(row=15, column=3)


# region -alignment buttons
# top row of alignment button options (good choices)
btn_LawGoodBTN = tk.Button(TK_AlignmentFrame, command=lambda: FN_GetAlignmentTrait(
    0, 0), text="LG", bg="#99f", fg="#FFF", width=var_txtBTNWidth)
btn_LawGoodBTN.grid(row=1, column=1)
btn_NeutralGoodBTN = tk.Button(TK_AlignmentFrame, command=lambda: FN_GetAlignmentTrait(
    0, 1), text="NG", bg="#55a", fg="#FFF", width=var_txtBTNWidth)
btn_NeutralGoodBTN.grid(row=1, column=2)
btn_ChaoticGoodBTN = tk.Button(TK_AlignmentFrame, command=lambda: FN_GetAlignmentTrait(
    0, 2), text="CG", bg="#00a", fg="#FFF", width=var_txtBTNWidth)
btn_ChaoticGoodBTN.grid(row=1, column=3)

# middle row of alignment button options (neutral choices)
btn_LawNeutralBTN = tk.Button(TK_AlignmentFrame, command=lambda: FN_GetAlignmentTrait(
    1, 0), text="LN", bg="#888", fg="#FFF", width=var_txtBTNWidth)
btn_LawNeutralBTN.grid(row=2, column=1)
btn_TrueNeutralBTN = tk.Button(TK_AlignmentFrame, command=lambda: FN_GetAlignmentTrait(
    1, 1), text="TN", bg="#666", fg="#FFF", width=var_txtBTNWidth)
btn_TrueNeutralBTN.grid(row=2, column=2)
btn_ChaoticNeutralBTN = tk.Button(TK_AlignmentFrame, command=lambda: FN_GetAlignmentTrait(
    1, 2), text="CN", bg="#444", fg="#FFF", width=var_txtBTNWidth)
btn_ChaoticNeutralBTN.grid(row=2, column=3)

# bottom row of alignment button options (evil choices)
btn_LawEvilBTN = tk.Button(TK_AlignmentFrame, command=lambda: FN_GetAlignmentTrait(
    2, 0), text="LE", bg="#f33", fg="#FFF", width=var_txtBTNWidth)
btn_LawEvilBTN.grid(row=3, column=1)
btn_NeutralEvilBTN = tk.Button(TK_AlignmentFrame, command=lambda: FN_GetAlignmentTrait(
    2, 1), text="NE", bg="#d22", fg="#FFF", width=var_txtBTNWidth)
btn_NeutralEvilBTN.grid(row=3, column=2)
btn_ChaoticEvilBTN = tk.Button(TK_AlignmentFrame, command=lambda: FN_GetAlignmentTrait(
    2, 2), text="CE", bg="#a11", fg="#FFF", width=var_txtBTNWidth)
btn_ChaoticEvilBTN.grid(row=3, column=3)
# endregion

#-----tooltip creation
    #create a var that is the tooltip...
#tip= tk.tooltip(root)

    #Bind the tooltip with button
#tip.bind_widget(lbl_NPCAlignmentHEAD,balloonmsg="These are what the NPC holds dear to them")
#tip.bind_widget(lbl_NPCBondHEAD,balloonmsg="This is what motivates the NPC the most")
#tip.bind_widget(lbl_NPCInterTraitHEAD,balloonmsg="This is how the NPC deals with others")

#tip.bind_widget(btn_LawEvilBTN,balloonmsg="Lawful Evil, 'Legally selfish'")
#tip.bind_widget(btn_LawNeutralBTN,balloonmsg="Lawful Neutral. 'Play by the rules'")
#tip.bind_widget(btn_LawGoodBTN,balloonmsg="Lawful Good. 'Model citizen'")
#tip.bind_widget(btn_NeutralEvilBTN,balloonmsg="Neutral Evil. 'Immorally indifferent'")
#tip.bind_widget(btn_TrueNeutralBTN,balloonmsg="True Neutral. 'If I don't survive, tell my wife Hello'")
#tip.bind_widget(btn_NeutralGoodBTN,balloonmsg="Neutral Good. 'Do gooder'")
#tip.bind_widget(btn_ChaoticEvilBTN,balloonmsg="Chaotic Evil. 'Fun lovin' criminal'")
#tip.bind_widget(btn_ChaoticNeutralBTN,balloonmsg="Chaotic Neutral. 'Impulse Driven'")
#tip.bind_widget(btn_ChaoticGoodBTN,balloonmsg="Chaotic Good. 'Well intentioned'")


#create dropdown lists for relevant fields
DDL_Races = ttk.Combobox(root, values=tu_Races, width=var_lblContWidth, justify=CENTER)
DDL_Gender = ttk.Combobox(root, values=tu_ALLGenders, width=var_lblContWidth, justify=CENTER)
DDL_Talent = ttk.Combobox(root, values=tu_Talents, width=var_lblContWidth, justify=CENTER)
DDL_InterTrait = ttk.Combobox(root, values=tu_InteractionTraits, width=var_lblContWidth, justify=CENTER)
DDL_Bonds = ttk.Combobox(root, values=tu_Bonds, width=var_lblContWidth, justify=CENTER)

#position the dropdown lists by a grid
DDL_Gender.grid(row=3, column=2)
DDL_Races.grid(row=4, column=2)
DDL_Talent.grid(row=5, column=2)
DDL_InterTrait.grid(row=6, column=2)
DDL_Bonds.grid(row=7, column=2)

#set default values for dropdown lists
DDL_Races.current(0)
DDL_Gender.current(0)
DDL_Talent.current(0)
DDL_InterTrait.current(0)
DDL_Bonds.current(0)

#use '.bind' on a combobox to bind a function to it that is fired per update
DDL_Races.bind("<<ComboboxSelected>>", callbackFunc)
DDL_Gender.bind("<<ComboboxSelected>>", callbackFuncGender)

FN_DisableObjects()
# event loop for our window
root.mainloop()
