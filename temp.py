# am Anfang = Kirish PYthonga

#Hausaufgaben: vom ersten Unterricht

#print('Hello World')

#print('Guten Abend')

#print(2+4*2)
#print(19/5)
#print(2**4)


#zweiten Unterricht

#print("Nexia", "Tico", "Damas", 'korganlar qilar havas')

#print(5**4)

#print(22/4)

#Unterrciht drei (Özgaruvchilar) Variable

#hallo = "Hello World!"
#print(hallo)


#nachricht = "Heute es gibt Regnen"
#print(nachricht) 

#Unterricht vier STRING (Text)

#straße = "Lindenstraße"
#hausnummer = 14
#plz = 27356
#stadt = "Rotenburg Wümme"

#print(f"{straße}, {hausnummer}, {plz}, {stadt}")  

#Unterricht funf Zahlen (Sonlar)

#zahl = int(input("Schreiben Sie bitte Ihr Zahl"))
#print(f"{zahl} ning {zahl**2} kvadratiga teng")
#print(f"{zahl} ning bölinmasi {zahl//2} ga teng")

#alt = int(input("Wie alt sind Sie?>>>"))
#jahr = 2021-alt
#print(f"Sie sind im {jahr} geboren")

#zahl0 = int(input("Schreiben Sie bitte einen Zahl!>>>"))
#zahl = int(input("Schreiben Sie bitte Ihr zweiten Zahl!>>"))
#print(f"{zahl+zahl0}, {zahl*zahl0}, {zahl/zahl0}, {zahl-zahl0}.")

#Unterricht sechs LIST (Röyxatlar)

#freunden = ['deryl', 'andre', 'emir']
#print('Moin kommst du heute zum Fussball mit', freunden[1].title())
#print(freunden[0].upper(), 'Wie geht es dir?')
#print(freunden[2].capitalize(), 'Was hast du für heute vor')

#history_m = ['abu bakr r.anhu', 'umar r.anhu', 'oisha binti abu bakr r.a']
#modern_m = ['stiv jobs', 'bill geyts', 'muhammad ali']
#print(f" Ich kenne sehr gut vom history_m {history_m.pop(0)},\n modern_m {modern_m.pop(2)} auch kenn ich  gut")

#freunden = [ ]
#freunden.append('deryl')
#freunden.append('emir')
#freunden.append('andre')
#print(freunden)

#Unterricht 8 Mit LISTEN arbeiten(Röyxatlar bn ishlash)

#print("Fangt wie Al")

#landern = ['usbekistan', 'deutschland', 'polen', 'frankreich', 's.arabien']
#landern.sort()
#print(landern)

#print(sorted(landern,reverse=False))

#zahlen = list(range(120,1200,10))
#print(f"Alle Zahlen {zahlen}, \n{sum(zahlen)}, \n{min(zahlen)}, \n{max(zahlen)}")
#print(len(zahlen))
#print(zahlen[:20])


#essens = ['nudeln', 'pizza', 'osh', 'kartoffeln']
#abendsessen = essens [:]
#print(essens)
#print(abendsessen)

#Unterricht neun (FOR_ takrorlash operatori)
#names = ['emir', 'deryl', 'tafara', 'andre']
#for friends in names:
#    print(f" {friends.title()}, Assalomu aleykum")
    
#zahl = list(range(10,100,3))  
#for zahlen in zahl:
#    print(zahlen**3)


#films = [ ]
#print(" Özizingiz sevgan 5 ta kinoni nomini kiriting")
#for filme in range(5):
    #films.append(input(f"{filme+1}-kino:"))
    #print(films)
    

#print("Bugun necha kishi bilan körishdingiz?")    
#people = [ ]
#for leute in range(5):
#    people.append(input(f"{leute}-Ismlarini ham kiritsangiz!:>>"))
#print(f"Bugun siz körishgan insonlar röyxati: {people}")
  

#IF - ELSE zehn UNterricht

#cars = ['jeep', 'hyundai', 'captiva', 'gm']
#for car in cars:
#  if car=='gm':
#   print(car.upper())
#  else:
#   print(f"siz izlayotgan avtollar{car.title()}")   

#Unterricht 16 NESTING (ya'ni lug'atlar ichga ro'yxatlar yoki 
#ro'yxatlar ichiga lug'tlar joylashni o'rganamiz)
#gm = []
#for n in range(10):
#    new_avtos = {
#        'model':'captiva',
#        'rang':None,
#        'yil':2020,
#        'narh':None,
#        'korobka':None,
#        'km':00
#        }
#    gm.append(new_avtos)
#    
#for car in gm[:3]:
#    car['rang'] ='qor'   


#info0 = {
 #       'ismi':'Muhammad sodiq Muhammadyusuf',
 #       'kasbi':'imom',
 #       't_joyi':'andijon',
 #       'millati':'uzbek'}
#info1 = {
   # 'ismi':'Muhammadali',
    #'familiyasi':'Eshonqulov',
   # 't_yili':1994,
  #  'kasbi':'oqituvchi',
 #   't_joyi':'jizzah'}

#info0['kitoblarii']='ammalar niyatlarga bogliqdir'
#info1['biznes']='yuksalish loyihasi'
#peoples = [info0, info1 ]
#for people in peoples:
    #print(f"{people['ismi'].title()}"
         # f"{people['kasbi']}")

#print(f"Men xurmat qilgan insonlar: {info0['ismi'].title()}",
  #    f"\nkasblari {info0[ 'kasbmi']}",
  #    f"\n{info0['t_joyi']} shaxrida tug'ilganlar",
  #    f"\nmillati {info0['millati']}",
      
  #    f"\nism shariflari : {info1['ismi'].title()}, {info1['familiyasi']}",
  #    f"\ntugilgan joylari {info1['t_joyi']}")
  
name = input("Ismingizni kiritsangiz!") 
print(f"{name.title()} Siz yoqtirgan uchta sevimli kino!")
filme = []
for n in range(3):
    filme.append(input(f"{n+1} - kino:>>>"))
print(filme)