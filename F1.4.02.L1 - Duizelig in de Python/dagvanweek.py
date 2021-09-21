#Vraag een dag van de week op (ma,di,wo,do,vr,za,zo) Print alle dagen tot en met de opgegeven dag. 
aantal = 0
week = 'ma','di','wo','do','vr','za','zo'
opgegevendag = input ('Welke dag kies je geef aan in afkorting: ')
while opgegevendag != (week[aantal]):
    print (week[aantal])
    aantal += 1
print (opgegevendag)
