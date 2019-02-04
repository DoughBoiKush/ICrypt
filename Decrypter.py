#before beginning decryption delete all overwritten files meaning the ones with original name and file size
#you must enter correct password else the proccess won't work
 
from os import listdir
from os.path import isfile, join
import pyAesCrypt

my_path = input('Enter files path to decrypt:')
password = input('ENTER PASSWORD TO BEGIN DECRYPTION:')

only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]

for files in only_files:
    print('\nGOING TO DECRYPT '+my_path+files)
    decrypted_file = 'unlocked.'+files
    pyAesCrypt.decryptFile(my_path+files, my_path+decrypted_file, password, bufferSize=64*1024)


print('I have finished Decrypting *_*')
