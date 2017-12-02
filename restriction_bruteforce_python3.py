import hashlib
import string
import base64
import itertools
import os
import sys

# myKey = base64.b64decode("zEb9kw4Z4gR5XD9jLuAJAa9N39o=")
# mySalt = "nmMt9Q=="


def calc_key(myKey, mySalt):
    
    for i in itertools.product(range(10), repeat=4):
        nPass = ''.join(map(str, i))
    
        code = hashlib.pbkdf2_hmac('sha1', nPass.encode(), base64.b64decode(mySalt), 1000, dklen=None)
    
    
        # print ("trying passcode " + str(nPass) + " with salt " + str(mySalt) + " restriction key " + str(base64.b64encode(code) ))
    
        if base64.b64encode(code).decode() == myKey:
            print ("")
            print ("Your Restrictions Passcode is \"" + nPass + "\"")
            break

def main():
    
    # os.system("clear")
    
#    if len(sys.argv) < 2:

    # print("Usage : python restriction_tool.py <RestrictionsPasswordKey> <RestrictionsPasswordSalt>")
    
    
    print("")
    print("iOS 7/8/9/10 Restriction Password Recovery Tool")
    print("by TwizzyIndy")
    print("Jan-2017")
    print("")
    print("You can get following keys from device's backup.\nYou can obtain them from HomeDomain/Library/Preferences/com.apple.restrictionspassword.plist")
    print("")

    # restrictionKey = raw_input("Enter your RestrictionPasswordKey: ")
    # restrictionSalt = raw_input("Enter your RestrictionPasswordSalt: ")
    restrictionKey = "KXJZN1RVfflCb77DoHvDOGiDrzQ="
    restrictionSalt = "RnGVxg=="

    if restrictionKey or restrictionSalt:
        calc_key(restrictionKey, restrictionSalt)
    
        
    
if __name__ == "__main__":
    main()
