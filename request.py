#!/bin/python
from validate_email import validate_email
import sys
if len(sys.argv) != 2:
    print "Missing Email List File"
    exit()
else:
    email_listfile=sys.argv[1]
    with open(email_listfile,'r') as email:
        for line in email.readlines():
            print "checking: ",line
            #status_mx=validate_email(line.strip(),check=True)
            #print status_mx
            status_email=validate_email(line.strip(),verify=True)
            
            if status_email == True:
                print "\033[97mEmail is :\033[92mwork\033[97m"
                print "----------------------------------------"
                with open('victim-email.txt','a') as truemail:
                    truemail.write(line)
            else:
                print "\033[97mEmail is :\033[91mFake\033[97m"
                print "-----------------------------------------"
                
               # pass
