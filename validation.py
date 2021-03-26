from licensing.models import *
from licensing.methods import Key, Helpers, Message, Product, Customer, Data, AI
import logging
import socket
import uuid
RSAPubKey = "<RSAKeyValue><Modusudplus>2o1s3GxdeCFa1xPtkjkCZZGSziMxYAmYVOMGQeZwW9FExEx+z6aW1MVambyz8iS1azisAoucru+rqy1ex1P9kHN6q20UTwS0sJn3k5n+uFen9qEI3ooh2JSz7ArccTTGAw+fEs5b8Ls3ldH2OsfmoVxXcdBtUJZQj3wDQE4ocRDL9M5ybuZjGesxBySeTPVuQjEBpzXElal9vVbcfQubLQZPrHgfr6BxKFf/pt3/6xgewraUyy4HfQly2F3gi9iOoG4Um/8BYIalF0LkYQxv1O5HeKNmDf90TMfAy0CGe+hCr7lVwOLEhYAxO2fo0rxdkHcx6jio5O/DH2or3ISdtQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyI3NDE0MjIiLCJzMVVvNkxka2dxSlk2YWcvRW10U3lKMHFZT2o5d3pYbjRLNnNSYVNUIl0="
#from cryptolens_python2 import *

#HelperMethods.ironpython2730_legacy = True

res = Key.activate(token=auth,\
                   rsa_pub_key=RSAPubKey,\
                   product_id=10254, key="CVWRY-LRSWB-OBQLS-HNRVD", machine_code=Helpers.GetMachineCode(),\
                   friendly_name=socket.gethostname())

if res[0] == None or not Helpers.IsOnRightMachine(res[0]):
    print("An error occured: {0}".format(res[1]))
else:
    print("Success")
    
    license_key = res[0]
    print("Feature 1: " + str(license_key.f1))
    print("License expires: " + str(license_key.expires))
    
    
if res[0] != None:
    # saving license file to disk
    with open('licensefile.skm', 'w') as f:
        f.write(res[0].save_as_string())
        

# read license file from file
with open('licensefile.skm', 'r') as f:
    license_key = LicenseKey.load_from_string(RSAPubKey, f.read())
    logging.error(license_key)
    if not Helpers.IsOnRightMachine(license_key):
        print("NOTE: This license file does not belong to this machine.")
    else:
        print("Feature 1: " + str(license_key.f1))
        print("License expires: " + str(license_key.expires))
    


def validate_date():
    #If you want to make sure that the license file is not too old, you can specify the maximum number of days as shown below (after 30 days, this method will return NoneType).
    # read license file from file
    with open('licensefile.skm', 'r') as f:
        license_key = LicenseKey.load_from_string(pubKey, f.read(), 30)
        
        if license_key == None or not Helpers.IsOnRightMachine(license_key):
            print("NOTE: This license file does not belong to this machine.")
        else:
            print("Feature 1: " + str(license_key.f1))
            print("License expires: " + str(license_key.expires))


def trialKey():
    trial_key = Key.create_trial_key("WyIzODQ0IiwiempTRWs4SnBKTTArYUh3WkwyZ0VwQkVyeTlUVkRWK2ZTOS8wcTBmaCJd", 3941, Helpers.GetMachineCode())

    if trial_key[0] == None:
        print("An error occurred: {0}".format(trial_key[1]))


    RSAPubKey = "<RSAKeyValue><Modulus>sGbvxwdlDbqFXOMlVUnAF5ew0t0WpPW7rFpI5jHQOFkht/326dvh7t74RYeMpjy357NljouhpTLA3a6idnn4j6c3jmPWBkjZndGsPL4Bqm+fwE48nKpGPjkj4q/yzT4tHXBTyvaBjA8bVoCTnu+LiC4XEaLZRThGzIn5KQXKCigg6tQRy0GXE13XYFVz/x1mjFbT9/7dS8p85n8BuwlY5JvuBIQkKhuCNFfrUxBWyu87CFnXWjIupCD2VO/GbxaCvzrRjLZjAngLCMtZbYBALksqGPgTUN7ZM24XbPWyLtKPaXF2i4XRR9u6eTj5BfnLbKAU5PIVfjIS+vNYYogteQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
    auth = "WyIyNTU1IiwiRjdZZTB4RmtuTVcrQlNqcSszbmFMMHB3aWFJTlBsWW1Mbm9raVFyRyJd=="

    result = Key.activate(token=auth,\
                    rsa_pub_key=RSAPubKey,\
                    product_id=3349, \
                    key=trial_key[0],\
                    machine_code=Helpers.GetMachineCode())


    if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
        print("An error occurred: {0}".format(result[1]))
    else:
        print("Success")
        
        license_key = result[0]
        print("Feature 1: " + str(license_key.f1))
        print("License expires: " + str(license_key.expires))
