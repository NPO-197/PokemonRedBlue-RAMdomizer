import random
#We want to import every pokemon from the pokemon index
from PokemonGen1Index import *

#Vanilla wild pokemon data copied from pret/pokered/data/wild/maps (on github)
GrassWaterData = [
    #nothing
    [0
    ,0
    ],
    #Route1
    [25
    ,  3, PIDGEY
	,  3, RATTATA
	,  3, RATTATA
	,  2, RATTATA
	,  2, PIDGEY
	,  3, PIDGEY
	,  3, PIDGEY
	,  4, RATTATA
	,  4, PIDGEY
	,  5, PIDGEY
    ,0
    ],
    #Route2
    [25
    ,3, RATTATA
	,3, PIDGEY
	,4, PIDGEY
	,4, RATTATA
	,5, PIDGEY
    ,3, WEEDLE
	,2, RATTATA
	,5, RATTATA
	,4, WEEDLE
	,5, WEEDLE
    ,0
    ],
    #Route22
    [25
    ,3, RATTATA
    ,3, NIDORAN_M
	,4, RATTATA
	,4, NIDORAN_M
	,2, RATTATA
	,2, NIDORAN_M
	,3, SPEAROW
	,5, SPEAROW
	,3, NIDORAN_F
	,4, NIDORAN_F
    ,0
    ],
    #ViridianForest
    [8
    ,4, WEEDLE
	,5, KAKUNA
	,3, WEEDLE
	,5, WEEDLE
	,4, KAKUNA
	,6, KAKUNA
	,4, METAPOD
	,3, CATERPIE
    ,3, PIKACHU
	,5, PIKACHU
    ,0
    ],
    #Route3
    [20
    ,6, PIDGEY
	,5, SPEAROW
	,7, PIDGEY
	,6, SPEAROW
	,7, SPEAROW
	,8, PIDGEY
	,8, SPEAROW
	,3, JIGGLYPUFF
	,5, JIGGLYPUFF
	,7, JIGGLYPUFF
    ,0],
    #MtMoon1F
    [10
    ,8, ZUBAT
	,7, ZUBAT
	,9, ZUBAT
	,8, GEODUDE
	,6, ZUBAT
	,10, ZUBAT
	,10, GEODUDE
	,8, PARAS
	,11, ZUBAT
	,8, CLEFAIRY
    ,0],
    #MtMoonB1F
    [10
    ,8, ZUBAT
	,7, ZUBAT
	,7, GEODUDE
	,8, GEODUDE
	,9, ZUBAT
	,10, PARAS
	,10, ZUBAT
	,11, ZUBAT
	,9, CLEFAIRY
	,9, GEODUDE
    ,0],
    #MtMoonB2F
    [10
    ,9, ZUBAT
	,9, GEODUDE
	,10, ZUBAT
	,10, GEODUDE
	,11, ZUBAT
	,10, PARAS
	,12, PARAS
	,10, CLEFAIRY
	,12, ZUBAT
	,12, CLEFAIRY
    ,0],
    #Route4
    [20
    ,10, RATTATA
	,10, SPEAROW
	,8, RATTATA
    ,6, EKANS
	,8, SPEAROW
	,10, EKANS
	,12, RATTATA
	,12, SPEAROW
	,8, EKANS
	,12, EKANS
    ,0],
    #Route24
    [25
    ,7, WEEDLE
	,8, KAKUNA
	,12, PIDGEY
	,12, ODDISH
	,13, ODDISH
	,10, ABRA
	,14, ODDISH
    ,13, PIDGEY
	,8, ABRA
	,12, ABRA
    ,0],
    #Route25
    [15
    ,8, WEEDLE
	,9, KAKUNA
	,13, PIDGEY
	,12, ODDISH
	,13, ODDISH
	,12, ABRA
	,14, ODDISH
	,10, ABRA
	,7, METAPOD
	,8, CATERPIE
    ,0],
    #Route9
    [15
	,16, RATTATA
	,16, SPEAROW
	,14, RATTATA
    ,11, EKANS
	,13, SPEAROW
	,15, EKANS
	,17, RATTATA
	,17, SPEAROW
	,13, EKANS
	,17, EKANS
    ,0],
    #Route5
    [15
    ,13, ODDISH
	,13, PIDGEY
	,15, PIDGEY
	,10, MANKEY
	,12, MANKEY
	,15, ODDISH
	,16, ODDISH
	,16, PIDGEY
	,14, MANKEY
	,16, MANKEY
    ,0],
    #Route6
    [15
	,13, ODDISH
	,13, PIDGEY
	,15, PIDGEY
	,10, MANKEY
	,12, MANKEY
	,15, ODDISH
	,16, ODDISH
	,16, PIDGEY
	,14, MANKEY
	,16, MANKEY
    ,0],
    #Route11
    [15
	,14, EKANS
	,15, SPEAROW
	,12, EKANS
	,9, DROWZEE
	,13, SPEAROW
	,13, DROWZEE
	,15, EKANS
    ,17, SPEAROW
	,11, DROWZEE
	,15, DROWZEE
    ,0],
    #RockTunnel1F
    [15
	,16, ZUBAT
	,17, ZUBAT
	,17, GEODUDE
	,15, MACHOP
	,16, GEODUDE
	,18, ZUBAT
	,15, ZUBAT
	,17, MACHOP
	,13, ONIX
	,15, ONIX
    ,0],
    #RockTunnelB1F
    [15
	,16, ZUBAT
	,17, ZUBAT
	,17, GEODUDE
	,15, MACHOP
	,16, GEODUDE
	,18, ZUBAT
	,17, MACHOP
	,17, ONIX
	,13, ONIX
	,18, GEODUDE
	,0],
    #Route10
    [15
	,16, VOLTORB
	,16, SPEAROW
	,14, VOLTORB
	,11, EKANS
	,13, SPEAROW
	,15, EKANS
	,17, VOLTORB
	,17, SPEAROW
	,13, EKANS
	,17, EKANS
    ,0],
    #Route12
    [15
	,24, ODDISH
	,25, PIDGEY
	,23, PIDGEY
	,24, VENONAT
	,22, ODDISH
	,26, VENONAT
	,26, ODDISH
	,27, PIDGEY
	,28, GLOOM
	,30, GLOOM
    ,0],
    #Route8
    [15
	,18, PIDGEY
	,18, MANKEY
	,17, EKANS
	,16, GROWLITHE
	,20, PIDGEY
	,20, MANKEY
	,19, EKANS
	,17, GROWLITHE
	,15, GROWLITHE
	,18, GROWLITHE
    ,0],
    #Route7
    [15
	,19, PIDGEY
	,19, ODDISH
	,17, MANKEY
	,22, ODDISH
	,22, PIDGEY
	,18, MANKEY
	,18, GROWLITHE
	,20, GROWLITHE
	,19, MANKEY
	,20, MANKEY
    ,0],
    #PokemonTower1F
    [0,0],
    #PokemonTower2F
    [0,0],
    #PokemonTower3F
    [10
	,20, GASTLY
	,21, GASTLY
	,22, GASTLY
	,23, GASTLY
	,19, GASTLY
	,18, GASTLY
	,24, GASTLY
	,20, CUBONE
	,22, CUBONE
	,25, HAUNTER
	,0],
    #PokemonTower4F
    [10
	,20, GASTLY
	,21, GASTLY
	,22, GASTLY
	,23, GASTLY
	,19, GASTLY
	,18, GASTLY
	,25, HAUNTER
	,20, CUBONE
	,22, CUBONE
	,24, GASTLY
	,0],
    #PokemonTower5F
    [10
	,20, GASTLY
	,21, GASTLY
	,22, GASTLY
	,23, GASTLY
	,19, GASTLY
	,18, GASTLY
	,25, HAUNTER
	,20, CUBONE
	,22, CUBONE
	,24, GASTLY
	,0],
    #PokemonTower6F
    [15
	,21, GASTLY
	,22, GASTLY
	,23, GASTLY
	,24, GASTLY
	,20, GASTLY
	,19, GASTLY
	,26, HAUNTER
	,22, CUBONE
	,24, CUBONE
	,28, HAUNTER
	,0],
    #PokemonTower7F
    [15
	,21, GASTLY
	,22, GASTLY
	,23, GASTLY
	,24, GASTLY
	,20, GASTLY
	,28, HAUNTER
	,22, CUBONE
	,24, CUBONE
	,28, HAUNTER
	,30, HAUNTER
	,0],
    #Route13
    [20
	,24, ODDISH
	,25, PIDGEY
	,27, PIDGEY
	,24, VENONAT
	,22, ODDISH
	,26, VENONAT
	,26, ODDISH
	,25, DITTO
	,28, GLOOM
	,30, GLOOM
    ,0],
    #Route14
    [15
	,24, ODDISH
	,26, PIDGEY
	,23, DITTO
	,24, VENONAT
	,22, ODDISH
	,26, VENONAT
	,26, ODDISH
	,30, GLOOM
    ,28, PIDGEOTTO
	,30, PIDGEOTTO
	,0],
    #Route15
    [15
	,24, ODDISH
	,26, DITTO
	,23, PIDGEY
	,26, VENONAT
	,22, ODDISH
	,28, VENONAT
	,26, ODDISH
	,30, GLOOM
    ,28, PIDGEOTTO
	,30, PIDGEOTTO
	,0],
    #Route16
    [25
	,20, SPEAROW
	,22, SPEAROW
	,18, RATTATA
	,20, DODUO
	,20, RATTATA
	,18, DODUO
	,22, DODUO
	,22, RATTATA
	,23, RATICATE
	,25, RATICATE
	,0],
    #Route17
    [25
	,20, SPEAROW
	,22, SPEAROW
	,25, RATICATE
	,24, DODUO
	,27, RATICATE
	,26, DODUO
	,28, DODUO
	,29, RATICATE
	,25, FEAROW
	,27, FEAROW
	,0],
    #Route18
    [25
	,20, SPEAROW
	,22, SPEAROW
	,25, RATICATE
	,24, DODUO
	,25, FEAROW
	,26, DODUO
	,28, DODUO
	,29, RATICATE
	,27, FEAROW
	,29, FEAROW
	,0],
    #SafariZoneCenter
    [30
	,22, NIDORAN_M
	,25, RHYHORN
	,22, VENONAT
	,24, EXEGGCUTE
	,31, NIDORINO
	,25, EXEGGCUTE
	,31, NIDORINA
	,30, PARASECT
	,23, SCYTHER
    ,23, CHANSEY
	,0],
    #SafariZoneEast
    [30
	,24, NIDORAN_M
	,26, DODUO
	,22, PARAS
	,25, EXEGGCUTE
	,33, NIDORINO
	,23, EXEGGCUTE
	,24, NIDORAN_F
	,25, PARASECT
	,25, KANGASKHAN
	,28, SCYTHER
    ,0],
    #SafariZoneNorth
    [30
	,22, NIDORAN_M
	,26, RHYHORN
	,23, PARAS
	,25, EXEGGCUTE
	,30, NIDORINO
	,27, EXEGGCUTE
	,30, NIDORINA
    ,32, VENOMOTH
	,26, CHANSEY
	,28, TAUROS
	,0],
    #SafariZoneWest
    [30
	,25, NIDORAN_M
	,26, DODUO
	,23, VENONAT
	,24, EXEGGCUTE
	,33, NIDORINO
	,26, EXEGGCUTE
	,25, NIDORAN_F
    ,31, VENOMOTH
	,26, TAUROS
	,28, KANGASKHAN
	,0],
    #SeaRoutes (Only water encounters)
    [0
    ,5
    ,5, TENTACOOL
	,10, TENTACOOL
	,15, TENTACOOL
	,5, TENTACOOL
	,10, TENTACOOL
	,15, TENTACOOL
	,20, TENTACOOL
	,30, TENTACOOL
	,35, TENTACOOL
	,40, TENTACOOL],
    #SeafoamIslands1F
    [15
	,30, SEEL
	,30, SLOWPOKE
	,30, SHELLDER
	,30, HORSEA
	,28, HORSEA
	,21, ZUBAT
	,29, GOLBAT
	,28, PSYDUCK
	,28, SHELLDER
	,38, GOLDUCK
    ,0],
    #SeafoamIslandsB1F
    [10
	,30, STARYU
	,30, HORSEA
	,32, SHELLDER
	,32, HORSEA
	,28, SLOWPOKE
	,30, SEEL
	,30, SLOWPOKE
	,28, SEEL
	,38, DEWGONG
	,37, SEADRA
    ,0],
    #SeafoamIslandsB2F
    [10
	,30, SEEL
	,30, SLOWPOKE
	,32, SEEL
	,32, SLOWPOKE
	,28, HORSEA
	,30, STARYU
	,30, HORSEA
	,28, SHELLDER
	,30, GOLBAT
	,37, SLOWBRO
    ,0],
    #SeafoamIslandsB3F
    [10
	,31, SLOWPOKE
	,31, SEEL
	,33, SLOWPOKE
	,33, SEEL
	,29, HORSEA
	,31, SHELLDER
	,31, HORSEA
	,29, SHELLDER
	,39, SEADRA
    ,37, DEWGONG
	,0],
    #SeafoamIslandsB4F
    [10
	,31, HORSEA
	,31, SHELLDER
	,33, HORSEA
	,33, SHELLDER
	,29, SLOWPOKE
	,31, SEEL
	,31, SLOWPOKE
	,29, SEEL
	,39, SLOWBRO
    ,32, GOLBAT
	,0],
    #PokemonMansion1F
    [10
	,32, KOFFING
	,30, KOFFING
	,34, PONYTA
	,30, PONYTA
	,34, GROWLITHE
	,32, PONYTA
	,30, GRIMER
	,28, PONYTA
	,37, WEEZING
	,39, MUK
    ,0],
    #PokemonMansion2F
    [10
	,32, GROWLITHE
	,34, KOFFING
	,34, KOFFING
	,30, PONYTA
	,30, KOFFING
	,32, PONYTA
	,30, GRIMER
	,28, PONYTA
	,39, WEEZING
	,37, MUK
    ,0],
    #PokemonMansion3F
    [10
	,31, KOFFING
	,33, GROWLITHE
	,35, KOFFING
	,32, PONYTA
	,34, PONYTA
	,40, WEEZING
	,34, GRIMER
	,38, WEEZING
	,36, PONYTA
	,42, MUK
    ,0],
    #PokemonMansionB1F
    [10
	,33, KOFFING
	,31, KOFFING
	,35, GROWLITHE
	,32, PONYTA
	,31, KOFFING
	,40, WEEZING
	,34, PONYTA
	,35, GRIMER
	,42, WEEZING
	,42, MUK
    ,0],
    #Route21 (Both Water and Grass encounters)
    [25
	,21, RATTATA
	,23, PIDGEY
	,30, RATICATE
	,23, RATTATA
	,21, PIDGEY
	,30, PIDGEOTTO
	,32, PIDGEOTTO
	,28, TANGELA
	,30, TANGELA
	,32, TANGELA
    ,5 #Encounter rate on water
    ,5, TENTACOOL
	,10, TENTACOOL
	,15, TENTACOOL
	,5, TENTACOOL
	,10, TENTACOOL
	,15, TENTACOOL
	,20, TENTACOOL
	,30, TENTACOOL
	,35, TENTACOOL
	,40, TENTACOOL],
    #CeruleanCave1F
    [10
	,46, GOLBAT
	,46, HYPNO
	,46, MAGNETON
	,49, DODRIO
	,49, VENOMOTH
	,52, ARBOK
    ,49, KADABRA
	,52, PARASECT
	,53, RAICHU
	,53, DITTO
	,0],
    #CeruleanCave2F
    [15
	,51, DODRIO
	,51, VENOMOTH
	,51, KADABRA
	,52, RHYDON
	,52, MAROWAK
	,52, ELECTRODE
	,56, CHANSEY
	,54, WIGGLYTUFF
	,55, DITTO
	,60, DITTO
	,0],
    #CeruleanCaveB1F
    [25
	,55, RHYDON
	,55, MAROWAK
	,55, ELECTRODE
	,64, CHANSEY
	,64, PARASECT
	,64, RAICHU
	,57, ARBOK
    ,65, DITTO
	,63, DITTO
	,67, DITTO
	,0],
    #PowerPlant
    [10
	,21, VOLTORB
	,21, MAGNEMITE
	,20, PIKACHU
	,24, PIKACHU
	,23, MAGNEMITE
	,23, VOLTORB
	,32, MAGNETON
	,35, MAGNETON
	,33, ELECTABUZZ
	,36, ELECTABUZZ
    ,0],
    #Route23
    [10
	,26, EKANS
    ,33, DITTO
	,26, SPEAROW
	,38, FEAROW
	,38, DITTO
	,38, FEAROW
	,41, ARBOK
    ,43, DITTO
	,41, FEAROW
	,43, FEAROW
    ,0],
    #VictoryRoad2F
    [10
	,22, MACHOP
	,24, GEODUDE
	,26, ZUBAT
	,36, ONIX
	,39, ONIX
	,42, ONIX
	,41, MACHOKE
	,40, GOLBAT
	,40, MAROWAK
	,43, GRAVELER
	,0],
    #VictoryRoad3F
    [15
	,24, MACHOP
	,26, GEODUDE
	,22, ZUBAT
	,42, ONIX
	,40, VENOMOTH
	,45, ONIX
	,43, GRAVELER
	,41, GOLBAT
	,42, MACHOKE
	,45, MACHOKE
	,0],
    #VictoryRoad1F
    [15
	,24, MACHOP
	,26, GEODUDE
	,22, ZUBAT
	,36, ONIX
	,39, ONIX
	,42, ONIX
	,41, GRAVELER
	,41, GOLBAT
	,42, MACHOKE
	,43, MAROWAK
	,0],
    #DiglettsCave
    [20
	,18, DIGLETT
	,19, DIGLETT
	,17, DIGLETT
	,20, DIGLETT
	,16, DIGLETT
	,15, DIGLETT
	,21, DIGLETT
	,22, DIGLETT
	,29, DUGTRIO
	,31, DUGTRIO
	,0]
]

#If a byte is a "pokemon" return a random pokemon instead
def GenRandomWildmonData():
    Bytes = []
    for Zone in GrassWaterData:
        for byte in Zone:
            if isinstance(byte,POKEMON):
                randommon = random.choice([Mon for Mon in POKEMON])
                Bytes.append(randommon.value)
            else:
                Bytes.append(byte)
    return(bytearray(Bytes))
