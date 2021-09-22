# name of student: Matthew
# number of student: 99067338
# purpose of program: wisselgeld uitrekenen 
# function of program: rekent wisselgeld uit 
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # hij rekent het om naar centen en vraagy hvl je hebt betaald 
paid = int(float(input('Paid amount: ')) * 100) # hij rekent het om naar centen en vraagt hvl je hebt betaald
change = paid - toPay # wisselgeld is betaald - to pay 

if change > 0: # als het wisselgeld groter dan 0 euro is dan gaat ie de rest uitvoeren 
  coinValue = 200 # start getal wisselgeld
  
  while change > 0 and coinValue > 0: # als de chaneg and coinvalue groter is dan 0 doe dan het gene achter de : 
    nrCoins = change // coinValue # deel change door coinvalue

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # 
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # hij vraagt hoeveel van je het aantal dat ie aangeeft hebt 
      change -= nrCoinsReturned * coinValue # 

# comment on code below: coin values hij begint bij 200 cent en gaat dan verder naar beneden tot einde 
    if coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # als change groter is dan 0 dan doe die de print 
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')