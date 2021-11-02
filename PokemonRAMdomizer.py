import sys
import TrainerDataRando
import WildMonDataRando

if len(sys.argv) != 2:
    print('Usage:')
    print('PokemonRAMdomizer.py <savefile>')
    exit(1)

file = open(sys.argv[1],'rb')
sav = list(bytearray(file.read()))
file.close()
assert len(sav) == 0x8000


#All data is of the form ["pointer","bytearray"]

#The code to Re-Read Trainer Data in sram
ReadTrainer =[0x2000,bytearray.fromhex("FA2BD1A7C0219CD8AF223D77F0B8F53E0EE0B8EA0120FA59D0D6C987213B5D4F0600092A666F01C75A09CD6F5CF1E0B8EA0120C9")]

#The code to reload Wild Data in sram (In bank 2)
LoadWildData=[0x5A60,bytearray.fromhex("21EB4EFA5ED34F06000909F0B8F53E03E0B8EA00202A666FF1E0B8EA002001D369092AEA87D8A7280FE51188D8011400CDB500E1011400092AEAA4D8A7C811A5D8011400C3B5")]

#Bootstrap code in sram
bootstrap =[0x2916,bytearray.fromhex("2180FF018CD63E1822367821FAFF36CD2371237023223683218AD62A666FE9017A00216FD3118BD6016AD63AB82807121B7E121BAF12712370FA89D6B72822FA9CD8FE0A20043EC3C90021B3D67EFE0A280630F23C7718EE3C772100A006011811EAB3D63CEA89D63E0AEA9CD82160BA06023E0AEA010078EA0140CD88D626007418C3")]

#Vanilla TrainerData
TrainerData=[0x3860,TrainerDataRando.GenRandomTrainerData()]

#Vanilla WildMonData
WildMonData=[0x5ab0,WildMonDataRando.GenRandomWildmonData()]

sMapScriptPtr = 0x261A #Location of MapScriptPtr in sram
sTempMapScriptPtr=0x2935 #Location of the TempMapScriptPtr in sram
PatchHramHi = 0xD6 #Hi byte of the PatchHram pointer
PatchHramLo = 0x6A #Lo byte of the PatchHram pointer
sChecksum = 0x3523 #Location of the Checksum in sram (bank 1)

#For every section of data we load it into the sav file at the specified offset (pointer)
for data in [ReadTrainer,LoadWildData,bootstrap,TrainerData,WildMonData]:
        pointer = data[0]
        hex = data[1]
        sav[pointer:pointer+len(hex)] = hex

#If the MapScriptPtr has not been re-directed, re-direct it to our payload in wRAM
if sav[sMapScriptPtr+1] != PatchHramHi: #0xD6xx is in wRAM so we only need to check the hi byte
    sav[sTempMapScriptPtr:sTempMapScriptPtr+2] = sav[sMapScriptPtr:sMapScriptPtr+2]
    sav[sMapScriptPtr:sMapScriptPtr+2] = [PatchHramLo,PatchHramHi]



#Bootstrap code and MapScriptPtr will change the checksum for bank 1, so it needs to be re-calculated
checksum = 0xFF
for x in sav[0x2598:0x3523]: #secion of sram that the check sum is calculated for in bank 1
    checksum -= x
    checksum %= 0x100
sav[sChecksum] = checksum

assert len(sav) == 0x8000
file = open(sys.argv[1],'wb')
file.write(bytearray(sav))
file.close()

print('Done!')
