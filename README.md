# PokemonRedBlue-RAMdomizer
Proof of concept python script that will edit a pokemon red or blue sav file so that, in effect, the game will be randomized upon loading the save file.

# What this is
Long story short it's a simplifyed randomizer that can run on an unmodifyed Pokemon Red / Blue cartridge.
So a normal randomizer for a game like Pokemon Red/Blue like the one found here: https://github.com/Dabomstew/universal-pokemon-randomizer
Works by taking a ROM and randomizing different tables, say the wild pokemon that apear on a given route, to create a new experiance for the player.
This is a RAMdomizer, it dose not modify the ROM at all, it only modifies a .sav file, (ie. the external RAM present on the cartridge).
It dose so with the intent to re-create the experiance of a Randomized rom, that is to randomize which pokemon apear on a given route and in trainer battles.
This will allow for playing a randomized version of Pokemon Red/Blue on real hardware, without the need for a flashcart, by uploading a modifyed sav file to a cart.
You will still need a method to upload the sav file to a real cartridge or to load the sav file into an emulator, running pokemon red/blue.
(Note the random encounters are stored in the save file, not generated during gameplay.)

# How to use
You will need to be able to run python code on your pc. 
Simply download the .zip from the distributions page, 
open a cmd window and provide the path to the the .sav file you would like to edit (make backups first!)
Once the sav file has been "randomized" you will need to load in the sav file onto your cart or emulator, and have fun!

# Important Disclaimer:
This is entirly a proof of concept, the game should be playable, however as of now, the only functionalty is randomizing grass/water encounters, and randomizing trainer battles.
Fishing pokemon, Starter Pokemon, In game trades, gift pokemon ect. are still as in vanilla.
The goal of this project was simply to see what is possible, not to make a fully fleshed out randomizer. 
That isn't to say that adding such featurs are impossible, 
Actually i'd suspect it would be possible to add most, if not all, of those features into the remaing free space in the save file. 
If there is any interest in seeing that through, I'd be glad to continue working on this project, at least for the time being I plan on taking a break from this project.

# How dose this work?
That's a great question, thank you for asking that... :)  
Simply put this RAMdomizer makes use of an ACE (Arbatrary Code Execution) exploit in pokemon red / blue to run custom code stored in RAM once every frame, 
the custom script detects if wild pokemon data or enemy trainer data gets loaded into work ram, 
and then overwrites the vanilla data with randomized data stored in the sav file, before any battle starts.
I will be sure to add a more detailed explination / links to relavent videos in the next few days... (11/1/21) 





