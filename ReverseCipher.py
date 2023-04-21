#ReverseCipher.py
#https://www.nostarch.com/crackingcodes/ (BSD licensced )

message = 'no gniog thgiferif a si ereht ris gnaadev.'
transalated = ''

i = len(message) - 1
while i >= 0:
    transalated = transalated + message [i]
    i = i -1

print(transalated)
