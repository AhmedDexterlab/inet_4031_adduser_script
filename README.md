# inet_4031_adduser_script

# Program Description
This script helps you quickly create multiple user accounts on a Linux system. Instead of adding each user manually, the script reads user details from an input file and automatically creates usernames, sets passwords, and assigns groups. It’s super helpful for managing a lot of accounts at once.

# Program Operation
To use the script, you’ll need:

A Linux system
This Python script (create-users.py)
An input file (create-users.input) with a list of users and their details

# Step One: Clone the repository to your system.

1. Go to the repository folder

2. Ensure the create-users.input file is properly formatted with each user listed as: username:password:last_name:first_name:group1,group2.

3. Make the script executable.

4. Run the script with sudo to add users from the input file.

5. Check that the users were successfully added by verifying them in the system files.
