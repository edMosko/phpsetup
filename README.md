# phpsetup
A python script that checks all your PHP code for missing semicolons and puts the site's content in the apache server, ready for testing.

# How to use
Just change the path at line 5 to the path of your php origin and the path at line 7 to the path of your server and run it.

# What does it do?
The code will look at the origin directory and all subdirectories for .php files and is gonna fix all missing semicolons, then it's gonna copy every file from the origin to the target path.
