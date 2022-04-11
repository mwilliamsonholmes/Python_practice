#1) Get the median player

#2) Get the five players in the middle of the league-- That is, in addition to the median player, also get the players two above and the two below.

#3) Add a fake player, called "Average Player," to the exact middle of the list, to show clearly who is above and below average.

#4) Actually, that's not obvious enough. Find "Average Player," and change their name to uppercase: "AVERAGE PLAYER." That'll stand out.

#5) Add five more players with names of your choosing, to the bottom of the list-- They are unranked and we must therefore assume they are terrible.

#6) Oh no-- Now "AVERAGE PLAYER" is no longer in the middle! Find a way to fix this. 

#7) Five more players show up, but they are ranked. Insert them at the appropriate location:- Lacy is one spot ahead of Hubert- Omar is one spot behind Rebecca- Otto is 8th best in the league- Chauncey is 10 spots from the bottom of the league




foosballers = [
  "Mia",
  "Retta",
  "Augustine",
  "Jin",
  "Waylon",
  "Alphonso",
  "Sage",
  "Hubert",
  "Raymon",
  "Rebecca", #middle
  "Monty",
  "Glen",
  "Christi",
  "Patrice",
  "Craig",
  "Dexter",
  "Wally",
  "Ian",
  "Pat"
]
#1
median = len(foosballers) / 2
print(median)


#2
middleFive = foosballers[median-2:median+3]
print(middleFive)
print(foosballers)

#3
foosballers.insert(median, "Average Player")
print(foosballers)

#4
average = foosballers.index("Average Player")
foosballers[average] = "AVERAGE PLAYER"
print(foosballers)

#5
worstPlayers = ["Melissa", "Jackson", "Roo", "Al", "Melinda"]
foosballers += worstPlayers
print(foosballers)

#6

del foosballers[foosballers.index("AVERAGE PLAYER")]
print(foosballers)
median = len(foosballers) / 2
foosballers.insert(median, "AVERAGE PLAYER")
print(foosballers)

#7
hubert = foosballers.index("Hubert")

foosballers.insert(hubert, "Lacy")

rebecca = foosballers.index("Rebecca")
foosballers.insert(rebecca + 1, "Omar")

foosballers.insert(7, "Otto")


foosballers.insert(-9, "Chauncey")
print(foosballers)