import os, sys
os.system('xdg-open https://www.facebook.com/profile.php?id=100092174587959')
try:
    __import__("acc").menu()
except Exception as e:
    exit(str(e))
