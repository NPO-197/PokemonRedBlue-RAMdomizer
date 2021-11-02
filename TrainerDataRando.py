import random

#We want to import every pokemon from the pokemon index
from PokemonGen1Index import *

#Vanilla Trainer Data Copied from pret/pokered/data/trainers/parties.asm (on github)
TrainerData =[
    #YoungsterData:
    # Route 3
        [ 11, RATTATA, EKANS, 0],
    	[ 14, SPEAROW, 0],
    # Mt. Moon 1F
    	[ 10, RATTATA, RATTATA, ZUBAT, 0],
    # Route 24
    	[ 14, RATTATA, EKANS, ZUBAT, 0],
    # Route 25
    	[ 15, RATTATA, SPEAROW, 0],
    	[ 17, SLOWPOKE, 0],
    	[ 14, EKANS, SANDSHREW, 0],
    # SS Anne 1F Rooms
    	[ 21, NIDORAN_M, 0],
    # Route 11
    	[ 21, EKANS, 0],
    	[ 19, SANDSHREW, ZUBAT, 0],
    	[ 17, RATTATA, RATTATA, RATICATE, 0],
    	[ 18, NIDORAN_M, NIDORINO, 0],
    # Unused
    	[ 17, SPEAROW, RATTATA, RATTATA, SPEAROW, 0],

    #BugCatcherData:
    # Viridian Forest
    	[ 6, WEEDLE, CATERPIE, 0],
    	[ 7, WEEDLE, KAKUNA, WEEDLE, 0],
    	[ 9, WEEDLE, 0],
    # Route 3
    	[ 10, CATERPIE, WEEDLE, CATERPIE, 0],
    	[ 9, WEEDLE, KAKUNA, CATERPIE, METAPOD, 0],
    	[ 11, CATERPIE, METAPOD, 0],
    # Mt. Moon 1F
    	[ 11, WEEDLE, KAKUNA, 0],
    	[ 10, CATERPIE, METAPOD, CATERPIE, 0],
    # Route 24
    	[ 14, CATERPIE, WEEDLE, 0],
    # Route 6
    	[ 16, WEEDLE, CATERPIE, WEEDLE, 0],
    	[ 20, BUTTERFREE, 0],
    # Unused
    	[ 18, METAPOD, CATERPIE, VENONAT, 0],
    # Route 9
    	[ 19, BEEDRILL, BEEDRILL, 0],
    	[ 20, CATERPIE, WEEDLE, VENONAT, 0],

    #LassData:
    # Route 3
    	[ 9, PIDGEY, PIDGEY, 0],
    	[ 10, RATTATA, NIDORAN_M, 0],
    	[ 14, JIGGLYPUFF, 0],
    # Route 4
    	[ 31, PARAS, PARAS, PARASECT, 0],
    # Mt. Moon 1F
    	[ 11, ODDISH, BELLSPROUT, 0],
    	[ 14, CLEFAIRY, 0],
    # Route 24
    	[ 16, PIDGEY, NIDORAN_F, 0],
    	[ 14, PIDGEY, NIDORAN_F, 0],
    # Route 25
    	[ 15, NIDORAN_M, NIDORAN_F, 0],
    	[ 13, ODDISH, PIDGEY, ODDISH, 0],
    # SS Anne 1F Rooms
    	[ 18, PIDGEY, NIDORAN_F, 0],
    # SS Anne 2F Rooms
    	[ 18, RATTATA, PIKACHU, 0],
    # Route 8
    	[ 23, NIDORAN_F, NIDORINA, 0],
    	[ 24, MEOWTH, MEOWTH, MEOWTH, 0],
    	[ 19, PIDGEY, RATTATA, NIDORAN_M, MEOWTH, PIKACHU, 0],
    	[ 22, CLEFAIRY, CLEFAIRY, 0],
    # Celadon Gym
    	[ 23, BELLSPROUT, WEEPINBELL, 0],
    	[ 23, ODDISH, GLOOM, 0],

    #SailorData:
    # SS Anne Stern
    	[ 18, MACHOP, SHELLDER, 0],
    	[ 17, MACHOP, TENTACOOL, 0],
    # SS Anne B1F Rooms
    	[ 21, SHELLDER, 0],
    	[ 17, HORSEA, SHELLDER, TENTACOOL, 0],
    	[ 18, TENTACOOL, STARYU, 0],
    	[ 17, HORSEA, HORSEA, HORSEA, 0],
    	[ 20, MACHOP, 0],
    # Vermilion Gym
    	[ 21, PIKACHU, PIKACHU, 0],

    #JrTrainerMData:
    # Pewter Gym
    	[ 11, DIGLETT, SANDSHREW, 0],
    # Route 24/Route 25
    	[ 14, RATTATA, EKANS, 0],
    # Route 24
    	[ 18, MANKEY, 0],
    # Route 6
    	[ 20, SQUIRTLE, 0],
    	[ 16, SPEAROW, RATICATE, 0],
    # Unused
    	[ 18, DIGLETT, DIGLETT, SANDSHREW, 0],
    # Route 9
    	[ 21, GROWLITHE, CHARMANDER, 0],
    	[ 19, RATTATA, DIGLETT, EKANS, SANDSHREW, 0],
    # Route 12
    	[ 29, NIDORAN_M, NIDORINO, 0],

    #JrTrainerFData:
    # Cerulean Gym
    	[ 19, GOLDEEN, 0],
    # Route 6
    	[ 16, RATTATA, PIKACHU, 0],
    	[ 16, PIDGEY, PIDGEY, PIDGEY, 0],
    # Unused
    	[ 22, BULBASAUR, 0],
    # Route 9
    	[ 18, ODDISH, BELLSPROUT, ODDISH, BELLSPROUT, 0],
    	[ 23, MEOWTH, 0],
    # Route 10
    	[ 20, PIKACHU, CLEFAIRY, 0],
    	[ 21, PIDGEY, PIDGEOTTO, 0],
    # Rock Tunnel B1F
    	[ 21, JIGGLYPUFF, PIDGEY, MEOWTH, 0],
    	[ 22, ODDISH, BULBASAUR, 0],
    # Celadon Gym
    	[ 24, BULBASAUR, IVYSAUR, 0],
    # Route 13
    	[ 24, PIDGEY, MEOWTH, RATTATA, PIKACHU, MEOWTH, 0],
    	[ 30, POLIWAG, POLIWAG, 0],
    	[ 27, PIDGEY, MEOWTH, PIDGEY, PIDGEOTTO, 0],
    	[ 28, GOLDEEN, POLIWAG, HORSEA, 0],
    # Route 20
    	[ 31, GOLDEEN, SEAKING, 0],
    # Rock Tunnel 1F
    	[ 22, BELLSPROUT, CLEFAIRY, 0],
    	[ 20, MEOWTH, ODDISH, PIDGEY, 0],
    	[ 19, PIDGEY, RATTATA, RATTATA, BELLSPROUT, 0],
    # Route 15
    	[ 28, GLOOM, ODDISH, ODDISH, 0],
    	[ 29, PIKACHU, RAICHU, 0],
    	[ 33, CLEFAIRY, 0],
    	[ 29, BELLSPROUT, ODDISH, TANGELA, 0],
    # Route 20
    	[ 30, TENTACOOL, HORSEA, SEEL, 0],

    #PokemaniacData:
    # Route 10
    	[ 30, RHYHORN, LICKITUNG, 0],
    	[ 20, CUBONE, SLOWPOKE, 0],
    # Rock Tunnel B1F
    	[ 20, SLOWPOKE, SLOWPOKE, SLOWPOKE, 0],
    	[ 22, CHARMANDER, CUBONE, 0],
    	[ 25, SLOWPOKE, 0],
    # Victory Road 2F
    	[ 40, CHARMELEON, LAPRAS, LICKITUNG, 0],
    # Rock Tunnel 1F
    	[ 23, CUBONE, SLOWPOKE, 0],

    #SuperNerdData:
    # Mt. Moon 1F
    	[ 11, MAGNEMITE, VOLTORB, 0],
    # Mt. Moon B2F
    	[ 12, GRIMER, VOLTORB, KOFFING, 0],
    # Route 8
    	[ 20, VOLTORB, KOFFING, VOLTORB, MAGNEMITE, 0],
    	[ 22, GRIMER, MUK, GRIMER, 0],
    	[ 26, KOFFING, 0],
    # Unused
    	[ 22, KOFFING, MAGNEMITE, WEEZING, 0],
    	[ 20, MAGNEMITE, MAGNEMITE, KOFFING, MAGNEMITE, 0],
    	[ 24, MAGNEMITE, VOLTORB, 0],
    # Cinnabar Gym
    	[ 36, VULPIX, VULPIX, NINETALES, 0],
    	[ 34, PONYTA, CHARMANDER, VULPIX, GROWLITHE, 0],
    	[ 41, RAPIDASH, 0],
    	[ 37, GROWLITHE, VULPIX, 0],

    #HikerData:
    # Mt. Moon 1F
    	[ 10, GEODUDE, GEODUDE, ONIX, 0],
    # Route 25
    	[ 15, MACHOP, GEODUDE, 0],
    	[ 13, GEODUDE, GEODUDE, MACHOP, GEODUDE, 0],
    	[ 17, ONIX, 0],
    # Route 9
    	[ 21, GEODUDE, ONIX, 0],
    	[ 20, GEODUDE, MACHOP, GEODUDE, 0],
    # Route 10
    	[ 21, GEODUDE, ONIX, 0],
    	[ 19, ONIX, GRAVELER, 0],
    # Rock Tunnel B1F
    	[ 21, GEODUDE, GEODUDE, GRAVELER, 0],
    	[ 25, GEODUDE, 0],
    # Route 9/Rock Tunnel B1F
    	[ 20, MACHOP, ONIX, 0],
    # Rock Tunnel 1F
    	[ 19, GEODUDE, MACHOP, GEODUDE, GEODUDE, 0],
    	[ 20, ONIX, ONIX, GEODUDE, 0],
    	[ 21, GEODUDE, GRAVELER, 0],

    #BikerData:
    # Route 13
    	[ 28, KOFFING, KOFFING, KOFFING, 0],
    # Route 14
    	[ 29, KOFFING, GRIMER, 0],
    # Route 15
    	[ 25, KOFFING, KOFFING, WEEZING, KOFFING, GRIMER, 0],
    	[ 28, KOFFING, GRIMER, WEEZING, 0],
    # Route 16
    	[ 29, GRIMER, KOFFING, 0],
    	[ 33, WEEZING, 0],
    	[ 26, GRIMER, GRIMER, GRIMER, GRIMER, 0],
    # Route 17
    	[ 28, WEEZING, KOFFING, WEEZING, 0],
    	[ 33, MUK, 0],
    	[ 29, VOLTORB, VOLTORB, 0],
    	[ 29, WEEZING, MUK, 0],
    	[ 25, KOFFING, WEEZING, KOFFING, KOFFING, WEEZING, 0],
    # Route 14
    	[ 26, KOFFING, KOFFING, GRIMER, KOFFING, 0],
    	[ 28, GRIMER, GRIMER, KOFFING, 0],
    	[ 29, KOFFING, MUK, 0],

    #BurglarData:
    # Unused
    	[ 29, GROWLITHE, VULPIX, 0],
    	[ 33, GROWLITHE, 0],
    	[ 28, VULPIX, CHARMANDER, PONYTA, 0],
    # Cinnabar Gym
    	[ 36, GROWLITHE, VULPIX, NINETALES, 0],
    	[ 41, PONYTA, 0],
    	[ 37, VULPIX, GROWLITHE, 0],
    # Mansion 2F
    	[ 34, CHARMANDER, CHARMELEON, 0],
    # Mansion 3F
    	[ 38, NINETALES, 0],
    # Mansion B1F
    	[ 34, GROWLITHE, PONYTA, 0],

    #EngineerData:
    # Unused
    	[ 21, VOLTORB, MAGNEMITE, 0],
    # Route 11
    	[ 21, MAGNEMITE, 0],
    	[ 18, MAGNEMITE, MAGNEMITE, MAGNETON, 0],

    #UnusedJugglerData:
    # none

    #FisherData:
    # SS Anne 2F Rooms
    	[ 17, GOLDEEN, TENTACOOL, GOLDEEN, 0],
    # SS Anne B1F Rooms
    	[ 17, TENTACOOL, STARYU, SHELLDER, 0],
    # Route 12
    	[ 22, GOLDEEN, POLIWAG, GOLDEEN, 0],
    	[ 24, TENTACOOL, GOLDEEN, 0],
    	[ 27, GOLDEEN, 0],
    	[ 21, POLIWAG, SHELLDER, GOLDEEN, HORSEA, 0],
    # Route 21
    	[ 28, SEAKING, GOLDEEN, SEAKING, SEAKING, 0],
    	[ 31, SHELLDER, CLOYSTER, 0],
    	[ 27, MAGIKARP, MAGIKARP, MAGIKARP, MAGIKARP, MAGIKARP, MAGIKARP, 0],
    	[ 33, SEAKING, GOLDEEN, 0],
    # Route 12
    	[ 24, MAGIKARP, MAGIKARP, 0],

    #SwimmerData:
    # Cerulean Gym
    	[ 16, HORSEA, SHELLDER, 0],
    # Route 19
    	[ 30, TENTACOOL, SHELLDER, 0],
    	[ 29, GOLDEEN, HORSEA, STARYU, 0],
    	[ 30, POLIWAG, POLIWHIRL, 0],
    	[ 27, HORSEA, TENTACOOL, TENTACOOL, GOLDEEN, 0],
    	[ 29, GOLDEEN, SHELLDER, SEAKING, 0],
    	[ 30, HORSEA, HORSEA, 0],
    	[ 27, TENTACOOL, TENTACOOL, STARYU, HORSEA, TENTACRUEL, 0],
    # Route 20
    	[ 31, SHELLDER, CLOYSTER, 0],
    	[ 35, STARYU, 0],
    	[ 28, HORSEA, HORSEA, SEADRA, HORSEA, 0],
    # Route 21
    	[ 33, SEADRA, TENTACRUEL, 0],
    	[ 37, STARMIE, 0],
    	[ 33, STARYU, WARTORTLE, 0],
    	[ 32, POLIWHIRL, TENTACOOL, SEADRA, 0],

    #CueBallData:
    # Route 16
    	[ 28, MACHOP, MANKEY, MACHOP, 0],
    	[ 29, MANKEY, MACHOP, 0],
    	[ 33, MACHOP, 0],
    # Route 17
    	[ 29, MANKEY, PRIMEAPE, 0],
    	[ 29, MACHOP, MACHOKE, 0],
    	[ 33, MACHOKE, 0],
    	[ 26, MANKEY, MANKEY, MACHOKE, MACHOP, 0],
    	[ 29, PRIMEAPE, MACHOKE, 0],
    # Route 21
    	[ 31, TENTACOOL, TENTACOOL, TENTACRUEL, 0],

    #GamblerData:
    # Route 11
    	[ 18, POLIWAG, HORSEA, 0],
    	[ 18, BELLSPROUT, ODDISH, 0],
    	[ 18, VOLTORB, MAGNEMITE, 0],
    	[ 18, GROWLITHE, VULPIX, 0],
    # Route 8
    	[ 22, POLIWAG, POLIWAG, POLIWHIRL, 0],
    # Unused
    	[ 22, ONIX, GEODUDE, GRAVELER, 0],
    # Route 8
    	[ 24, GROWLITHE, VULPIX, 0],

    #BeautyData:
    # Celadon Gym
    	[ 21, ODDISH, BELLSPROUT, ODDISH, BELLSPROUT, 0],
    	[ 24, BELLSPROUT, BELLSPROUT, 0],
    	[ 26, EXEGGCUTE, 0],
    # Route 13
    	[ 27, RATTATA, PIKACHU, RATTATA, 0],
    	[ 29, CLEFAIRY, MEOWTH, 0],
    # Route 20
    	[ 35, SEAKING, 0],
    	[ 30, SHELLDER, SHELLDER, CLOYSTER, 0],
    	[ 31, POLIWAG, SEAKING, 0],
    # Route 15
    	[ 29, PIDGEOTTO, WIGGLYTUFF, 0],
    	[ 29, BULBASAUR, IVYSAUR, 0],
    # Unused
    	[ 33, WEEPINBELL, BELLSPROUT, WEEPINBELL, 0],
    # Route 19
    	[ 27, POLIWAG, GOLDEEN, SEAKING, GOLDEEN, POLIWAG, 0],
    	[ 30, GOLDEEN, SEAKING, 0],
    	[ 29, STARYU, STARYU, STARYU, 0],
    # Route 20
    	[ 30, SEADRA, HORSEA, SEADRA, 0],

    #PsychicData:
    # Saffron Gym
    	[ 31, KADABRA, SLOWPOKE, MR_MIME, KADABRA, 0],
    	[ 34, MR_MIME, KADABRA, 0],
    	[ 33, SLOWPOKE, SLOWPOKE, SLOWBRO, 0],
    	[ 38, SLOWBRO, 0],

    #RockerData:
    # Vermilion Gym
    	[ 20, VOLTORB, MAGNEMITE, VOLTORB, 0],
    # Route 12
    	[ 29, VOLTORB, ELECTRODE, 0],

    #JugglerData:
    # Silph Co. 5F
    	[ 29, KADABRA, MR_MIME, 0],
    # Victory Road 2F
    	[ 41, DROWZEE, HYPNO, KADABRA, KADABRA, 0],
    # Fuchsia Gym
    	[ 31, DROWZEE, DROWZEE, KADABRA, DROWZEE, 0],
    	[ 34, DROWZEE, HYPNO, 0],
    # Victory Road 2F
    	[ 48, MR_MIME, 0],
    # Unused
    	[ 33, HYPNO, 0],
    # Fuchsia Gym
    	[ 38, HYPNO, 0],
    	[ 34, DROWZEE, KADABRA, 0],

    #TamerData:
    # Fuchsia Gym
    	[ 34, SANDSLASH, ARBOK, 0],
    	[ 33, ARBOK, SANDSLASH, ARBOK, 0],
    # Viridian Gym
    	[ 43, RHYHORN, 0],
    	[ 39, ARBOK, TAUROS, 0],
    # Victory Road 2F
    	[ 44, PERSIAN, GOLDUCK, 0],
    # Unused
    	[ 42, RHYHORN, PRIMEAPE, ARBOK, TAUROS, 0],

    #BirdKeeperData:
    # Route 13
    	[ 29, PIDGEY, PIDGEOTTO, 0],
    	[ 25, SPEAROW, PIDGEY, PIDGEY, SPEAROW, SPEAROW, 0],
    	[ 26, PIDGEY, PIDGEOTTO, SPEAROW, FEAROW, 0],
    # Route 14
    	[ 33, FARFETCHD, 0],
    	[ 29, SPEAROW, FEAROW, 0],
    # Route 15
    	[ 26, PIDGEOTTO, FARFETCHD, DODUO, PIDGEY, 0],
    	[ 28, DODRIO, DODUO, DODUO, 0],
    # Route 18
    	[ 29, SPEAROW, FEAROW, 0],
    	[ 34, DODRIO, 0],
    	[ 26, SPEAROW, SPEAROW, FEAROW, SPEAROW, 0],
    # Route 20
    	[ 30, FEAROW, FEAROW, PIDGEOTTO, 0],
    # Unused
    	[ 39, PIDGEOTTO, PIDGEOTTO, PIDGEY, PIDGEOTTO, 0],
    	[ 42, FARFETCHD, FEAROW, 0],
    # Route 14
    	[ 28, PIDGEY, DODUO, PIDGEOTTO, 0],
    	[ 26, PIDGEY, SPEAROW, PIDGEY, FEAROW, 0],
    	[ 29, PIDGEOTTO, FEAROW, 0],
    	[ 28, SPEAROW, DODUO, FEAROW, 0],

    #BlackbeltData:
    # Fighting Dojo
    	[ 37, HITMONLEE, HITMONCHAN, 0],
    	[ 31, MANKEY, MANKEY, PRIMEAPE, 0],
    	[ 32, MACHOP, MACHOKE, 0],
    	[ 36, PRIMEAPE, 0],
    	[ 31, MACHOP, MANKEY, PRIMEAPE, 0],
    # Viridian Gym
    	[ 40, MACHOP, MACHOKE, 0],
    	[ 43, MACHOKE, 0],
    	[ 38, MACHOKE, MACHOP, MACHOKE, 0],
    # Victory Road 2F
    	[ 43, MACHOKE, MACHOP, MACHOKE, 0],

    #Green1Data:
    	[ 5, SQUIRTLE, 0],
    	[ 5, BULBASAUR, 0],
    	[ 5, CHARMANDER, 0],
    # Route 22
    	[ 0xFF, 9, PIDGEY, 8, SQUIRTLE, 0],
    	[ 0xFF, 9, PIDGEY, 8, BULBASAUR, 0],
    	[ 0xFF, 9, PIDGEY, 8, CHARMANDER, 0],
    # Cerulean City
    	[ 0xFF, 18, PIDGEOTTO, 15, ABRA, 15, RATTATA, 17, SQUIRTLE, 0],
    	[ 0xFF, 18, PIDGEOTTO, 15, ABRA, 15, RATTATA, 17, BULBASAUR, 0],
    	[ 0xFF, 18, PIDGEOTTO, 15, ABRA, 15, RATTATA, 17, CHARMANDER, 0],

    #ProfOakData:
    # Unused
    	[ 0xFF, 66, TAUROS, 67, EXEGGUTOR, 68, ARCANINE, 69, BLASTOISE, 70, GYARADOS, 0],
    	[ 0xFF, 66, TAUROS, 67, EXEGGUTOR, 68, ARCANINE, 69, VENUSAUR, 70, GYARADOS, 0],
    	[ 0xFF, 66, TAUROS, 67, EXEGGUTOR, 68, ARCANINE, 69, CHARIZARD, 70, GYARADOS, 0],

    #ChiefData:
    # none

    #ScientistData:
    # Unused
    	[ 34, KOFFING, VOLTORB, 0],
    # Silph Co. 2F
    	[ 26, GRIMER, WEEZING, KOFFING, WEEZING, 0],
    	[ 28, MAGNEMITE, VOLTORB, MAGNETON, 0],
    # Silph Co. 3F/Mansion 1F
    	[ 29, ELECTRODE, WEEZING, 0],
    # Silph Co. 4F
    	[ 33, ELECTRODE, 0],
    # Silph Co. 5F
    	[ 26, MAGNETON, KOFFING, WEEZING, MAGNEMITE, 0],
    # Silph Co. 6F
    	[ 25, VOLTORB, KOFFING, MAGNETON, MAGNEMITE, KOFFING, 0],
    # Silph Co. 7F
    	[ 29, ELECTRODE, MUK, 0],
    # Silph Co. 8F
    	[ 29, GRIMER, ELECTRODE, 0],
    # Silph Co. 9F
    	[ 28, VOLTORB, KOFFING, MAGNETON, 0],
    # Silph Co. 10F
    	[ 29, MAGNEMITE, KOFFING, 0],
    # Mansion 3F
    	[ 33, MAGNEMITE, MAGNETON, VOLTORB, 0],
    # Mansion B1F
    	[ 34, MAGNEMITE, ELECTRODE, 0],

    #GiovanniData:
    # Rocket Hideout B4F
    	[ 0xFF, 25, ONIX, 24, RHYHORN, 29, KANGASKHAN, 0],
    # Silph Co. 11F
    	[ 0xFF, 37, NIDORINO, 35, KANGASKHAN, 37, RHYHORN, 41, NIDOQUEEN, 0],
    # Viridian Gym
    	[ 0xFF, 45, RHYHORN, 42, DUGTRIO, 44, NIDOQUEEN, 45, NIDOKING, 50, RHYDON, 0],

    #RocketData:
    # Mt. Moon B2F
    	[ 13, RATTATA, ZUBAT, 0],
    	[ 11, SANDSHREW, RATTATA, ZUBAT, 0],
    	[ 12, ZUBAT, EKANS, 0],
    	[ 16, RATICATE, 0],
    # Cerulean City
    	[ 17, MACHOP, DROWZEE, 0],
    # Route 24
    	[ 15, EKANS, ZUBAT, 0],
    # Game Corner
    	[ 20, RATICATE, ZUBAT, 0],
    # Rocket Hideout B1F
    	[ 21, DROWZEE, MACHOP, 0],
    	[ 21, RATICATE, RATICATE, 0],
    	[ 20, GRIMER, KOFFING, KOFFING, 0],
    	[ 19, RATTATA, RATICATE, RATICATE, RATTATA, 0],
    	[ 22, GRIMER, KOFFING, 0],
    # Rocket Hideout B2F
    	[ 17, ZUBAT, KOFFING, GRIMER, ZUBAT, RATICATE, 0],
    # Rocket Hideout B3F
    	[ 20, RATTATA, RATICATE, DROWZEE, 0],
    	[ 21, MACHOP, MACHOP, 0],
    # Rocket Hideout B4F
    	[ 23, SANDSHREW, EKANS, SANDSLASH, 0],
    	[ 23, EKANS, SANDSHREW, ARBOK, 0],
    	[ 21, KOFFING, ZUBAT, 0],
    # Pokémon Tower 7F
    	[ 25, ZUBAT, ZUBAT, GOLBAT, 0],
    	[ 26, KOFFING, DROWZEE, 0],
    	[ 23, ZUBAT, RATTATA, RATICATE, ZUBAT, 0],
    # Unused
    	[ 26, DROWZEE, KOFFING, 0],
    # Silph Co. 2F
    	[ 29, CUBONE, ZUBAT, 0],
    	[ 25, GOLBAT, ZUBAT, ZUBAT, RATICATE, ZUBAT, 0],
    # Silph Co. 3F
    	[ 28, RATICATE, HYPNO, RATICATE, 0],
    # Silph Co. 4F
    	[ 29, MACHOP, DROWZEE, 0],
    	[ 28, EKANS, ZUBAT, CUBONE, 0],
    # Silph Co. 5F
    	[ 33, ARBOK, 0],
    	[ 33, HYPNO, 0],
    # Silph Co. 6F
    	[ 29, MACHOP, MACHOKE, 0],
    	[ 28, ZUBAT, ZUBAT, GOLBAT, 0],
    # Silph Co. 7F
    	[ 26, RATICATE, ARBOK, KOFFING, GOLBAT, 0],
    	[ 29, CUBONE, CUBONE, 0],
    	[ 29, SANDSHREW, SANDSLASH, 0],
    # Silph Co. 8F
    	[ 26, RATICATE, ZUBAT, GOLBAT, RATTATA, 0],
    	[ 28, WEEZING, GOLBAT, KOFFING, 0],
    # Silph Co. 9F
    	[ 28, DROWZEE, GRIMER, MACHOP, 0],
    	[ 28, GOLBAT, DROWZEE, HYPNO, 0],
    # Silph Co. 10F
    	[ 33, MACHOKE, 0],
    # Silph Co. 11F
    	[ 25, RATTATA, RATTATA, ZUBAT, RATTATA, EKANS, 0],
    	[ 32, CUBONE, DROWZEE, MAROWAK, 0],

    #CooltrainerMData:
    # Viridian Gym
    	[ 39, NIDORINO, NIDOKING, 0],
    # Victory Road 3F
    	[ 43, EXEGGUTOR, CLOYSTER, ARCANINE, 0],
    	[ 43, KINGLER, TENTACRUEL, BLASTOISE, 0],
    # Unused
    	[ 45, KINGLER, STARMIE, 0],
    # Victory Road 1F
    	[ 42, IVYSAUR, WARTORTLE, CHARMELEON, CHARIZARD, 0],
    # Unused
    	[ 44, IVYSAUR, WARTORTLE, CHARMELEON, 0],
    	[ 49, NIDOKING, 0],
    	[ 44, KINGLER, CLOYSTER, 0],
    # Viridian Gym
    	[ 39, SANDSLASH, DUGTRIO, 0],
    	[ 43, RHYHORN, 0],

    #CooltrainerFData:
    # Celadon Gym
    	[ 24, WEEPINBELL, GLOOM, IVYSAUR, 0],
    # Victory Road 3F
    	[ 43, BELLSPROUT, WEEPINBELL, VICTREEBEL, 0],
    	[ 43, PARASECT, DEWGONG, CHANSEY, 0],
    # Unused
    	[ 46, VILEPLUME, BUTTERFREE, 0],
    # Victory Road 1F
    	[ 44, PERSIAN, NINETALES, 0],
    # Unused
    	[ 45, IVYSAUR, VENUSAUR, 0],
    	[ 45, NIDORINA, NIDOQUEEN, 0],
    	[ 43, PERSIAN, NINETALES, RAICHU, 0],

    #BrunoData:
    	[ 0xFF, 53, ONIX, 55, HITMONCHAN, 55, HITMONLEE, 56, ONIX, 58, MACHAMP, 0],

    #BrockData:
    	[ 0xFF, 12, GEODUDE, 14, ONIX, 0],

    #MistyData:
    	[ 0xFF, 18, STARYU, 21, STARMIE, 0],

    #LtSurgeData:
    	[ 0xFF, 21, VOLTORB, 18, PIKACHU, 24, RAICHU, 0],

    #ErikaData:
    	[ 0xFF, 29, VICTREEBEL, 24, TANGELA, 29, VILEPLUME, 0],

    #KogaData:
    	[ 0xFF, 37, KOFFING, 39, MUK, 37, KOFFING, 43, WEEZING, 0],

    #BlaineData:
    	[ 0xFF, 42, GROWLITHE, 40, PONYTA, 42, RAPIDASH, 47, ARCANINE, 0],

    #SabrinaData:
    	[ 0xFF, 38, KADABRA, 37, MR_MIME, 38, VENOMOTH, 43, ALAKAZAM, 0],

    #GentlemanData:
    # SS Anne 1F Rooms
    	[ 18, GROWLITHE, GROWLITHE, 0],
    	[ 19, NIDORAN_M, NIDORAN_F, 0],
    # SS Anne 2F Rooms/Vermilion Gym
    	[ 23, PIKACHU, 0],
    # Unused
    	[ 48, PRIMEAPE, 0],
    # SS Anne 2F Rooms
    	[ 17, GROWLITHE, PONYTA, 0],

    #Green2Data:
    # SS Anne 2F
    	[ 0xFF, 19, PIDGEOTTO, 16, RATICATE, 18, KADABRA, 20, WARTORTLE, 0],
    	[ 0xFF, 19, PIDGEOTTO, 16, RATICATE, 18, KADABRA, 20, IVYSAUR, 0],
    	[ 0xFF, 19, PIDGEOTTO, 16, RATICATE, 18, KADABRA, 20, CHARMELEON, 0],
    # Pokémon Tower 2F
    	[ 0xFF, 25, PIDGEOTTO, 23, GROWLITHE, 22, EXEGGCUTE, 20, KADABRA, 25, WARTORTLE, 0],
    	[ 0xFF, 25, PIDGEOTTO, 23, GYARADOS, 22, GROWLITHE, 20, KADABRA, 25, IVYSAUR, 0],
    	[ 0xFF, 25, PIDGEOTTO, 23, EXEGGCUTE, 22, GYARADOS, 20, KADABRA, 25, CHARMELEON, 0],
    # Silph Co. 7F
    	[ 0xFF, 37, PIDGEOT, 38, GROWLITHE, 35, EXEGGCUTE, 35, ALAKAZAM, 40, BLASTOISE, 0],
    	[ 0xFF, 37, PIDGEOT, 38, GYARADOS, 35, GROWLITHE, 35, ALAKAZAM, 40, VENUSAUR, 0],
    	[ 0xFF, 37, PIDGEOT, 38, EXEGGCUTE, 35, GYARADOS, 35, ALAKAZAM, 40, CHARIZARD, 0],
    # Route 22
    	[ 0xFF, 47, PIDGEOT, 45, RHYHORN, 45, GROWLITHE, 47, EXEGGCUTE, 50, ALAKAZAM, 53, BLASTOISE, 0],
    	[ 0xFF, 47, PIDGEOT, 45, RHYHORN, 45, GYARADOS, 47, GROWLITHE, 50, ALAKAZAM, 53, VENUSAUR, 0],
    	[ 0xFF, 47, PIDGEOT, 45, RHYHORN, 45, EXEGGCUTE, 47, GYARADOS, 50, ALAKAZAM, 53, CHARIZARD, 0],

    #Green3Data:
    	[ 0xFF, 61, PIDGEOT, 59, ALAKAZAM, 61, RHYDON, 61, ARCANINE, 63, EXEGGUTOR, 65, BLASTOISE, 0],
    	[ 0xFF, 61, PIDGEOT, 59, ALAKAZAM, 61, RHYDON, 61, GYARADOS, 63, ARCANINE, 65, VENUSAUR, 0],
    	[ 0xFF, 61, PIDGEOT, 59, ALAKAZAM, 61, RHYDON, 61, EXEGGUTOR, 63, GYARADOS, 65, CHARIZARD, 0],

    #LoreleiData:
    	[ 0xFF, 54, DEWGONG, 53, CLOYSTER, 54, SLOWBRO, 56, JYNX, 56, LAPRAS, 0],

    #ChannelerData:
    # Unused
    	[ 22, GASTLY, 0],
    	[ 24, GASTLY, 0],
    	[ 23, GASTLY, GASTLY, 0],
    	[ 24, GASTLY, 0],
    # Pokémon Tower 3F
    	[ 23, GASTLY, 0],
    	[ 24, GASTLY, 0],
    # Unused
    	[ 24, HAUNTER, 0],
    # Pokémon Tower 3F
    	[ 22, GASTLY, 0],
    # Pokémon Tower 4F
    	[ 24, GASTLY, 0],
    	[ 23, GASTLY, GASTLY, 0],
    # Unused
    	[ 24, GASTLY, 0],
    # Pokémon Tower 4F
    	[ 22, GASTLY, 0],
    # Unused
    	[ 24, GASTLY, 0],
    # Pokémon Tower 5F
    	[ 23, HAUNTER, 0],
    # Unused
    	[ 24, GASTLY, 0],
    # Pokémon Tower 5F
    	[ 22, GASTLY, 0],
    	[ 24, GASTLY, 0],
    	[ 22, HAUNTER, 0],
    # Pokémon Tower 6F
    	[ 22, GASTLY, GASTLY, GASTLY, 0],
    	[ 24, GASTLY, 0],
    	[ 24, GASTLY, 0],
    # Saffron Gym
    	[ 34, GASTLY, HAUNTER, 0],
    	[ 38, HAUNTER, 0],
    	[ 33, GASTLY, GASTLY, HAUNTER, 0],

    #AgathaData:
    	[ 0xFF, 56, GENGAR, 56, GOLBAT, 55, HAUNTER, 58, ARBOK, 60, GENGAR, 0],

    #LanceData:
    	[ 0xFF, 58, GYARADOS, 56, DRAGONAIR, 56, DRAGONAIR, 60, AERODACTYL, 62, DRAGONITE, 0]]

#If a byte is a "pokemon" return a random pokemon instead
def GenRandomTrainerData():
    Bytes = []
    for Trainer in TrainerData:
        for byte in Trainer:
            if isinstance(byte,POKEMON):
                randommon = random.choice([Mon for Mon in POKEMON])
                Bytes.append(randommon.value)
            else:
                Bytes.append(byte)
    return(bytearray(Bytes))
