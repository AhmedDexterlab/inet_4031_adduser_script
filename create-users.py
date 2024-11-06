#!/usr/bin/python3
#### Student Name: Ahmed Abdi
#### Program Name: User Creation Script
#### Program Creation Date: 11-06-2024
#### Program Last Updated Date: 11-06-2024

#what are these imports being used for?
# - 'os' is used to execute system commands for creating users and groups.
# - 're' is used for regular expressions to match patterns.
# - 'sys' is used to read input from the command line.
import os
import re
import sys

def main():
    for line in sys.stdin:

        #this "regular expression" is searching for the presence of a character - what is it and why?
                # Skip lines starting with '#' to ignore comments in the input file
        match = re.match("^#",line)

        #what is this field doing?
                # Split the line by ':' to get user details
        fields = line.strip().split(':')

        # Checks if the line is a comment or incorrectly formatted (not 5 fields)
        # If true, skip this line
        if match or len(fields) != 5:
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])
        groups = fields[4].split(',')
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        #print cmd
        os.system(cmd)
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        #print cmd
        os.system(cmd)

        for group in groups:
            #what is this if statement looking for?
                # Skip if the group field is '-'
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                 os.system(cmd)

if __name__ == '__main__':
    main()
