import numpy as np
#git test

line = '==============================================='
dline = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

class item():
	def __init__(self, tag, price):
		self.tag = tag
		self.price = price

class perk():
	def __init__(self, tag, description):
		self.tag = tag
		self.description = description

class character():
	def __init__(self, name = ''):
		self.name = name
		self.health = 10
		self.equipment = []
		self.perks = []
		self.currentMoney = 0
		self.rerollPrice = 200
		self.killMin = 10
		self.totalKills = 0
		self.totalDeaths = 0
		self.totalScore = 0
		self.totalPerks = 0
		self.totalHeals = 0		#total times recieved healing
		self.totalItemsTI = 0	#total items turned in
		self.totalMoney = 0		#total money recieved
		self.totalBounties = 0	#total bounty items collected
		self.totalGames = 0
		self.winCondition = 200
		self.won = False

	def heal(self, amount):
		self.health += amount
		self.totalHeals += amount

	def turnIn(self, amount, bounty=0):
		oldBounty = self.totalBounties
		if bounty > 0 and bounty <= 3:
			self.currentMoney += (100*bounty)
			self.totalMoney += (100*bounty)
			self.totalBounties += bounty
			self.totalItemsTI += (1*bounty)
			print(str(100*bounty) + " gold recieved from bounties.")
		if amount > 0 and amount <= 3:
			self.currentMoney += (50*amount)
			self.totalMoney += (50*amount)
			self.totalItemsTI += (1*amount)
			print(str(50*amount) + " gold recieved from weapons collected.")
		if int(self.totalBounties/5) > int(oldBounty/5):
			self.heal(1)
			print("That's 5 Bounties collected. Here's some healing. HP: " + str(self.health))

	def purchase(self, item):
		self.equipment.append(item)
		self.currentMoney -= item.price

	def gainPerk(self, perk):
		self.perks.append(perk)
		self.totalPerks += 1

	def buyEquip(self, item):
		self.equipment.append(item)
		self.currentMoney -= item.price

	def logScore(self, kills, deaths, score):
		if kills < self.killMin:
			 self.permaDie(1)
		self.killMin += 2
		self.totalKills += kills
		if self.totalKills >= self.winCondition:
			self.won = True
		self.totalDeaths += deaths
		if deaths > self.health:
			self.health = 0
		else:
			self.health = 10
		self.totalScore += score
		money = (int(score / 1000) * 50)
		self.currentMoney += money
		self.totalMoney += money

	def permaDie(self, option = 0): #prints out a neat little summary of the character + stats to post to discord for record keeping
		if option == 0:
			print(dline)
			print("Player name: " + self.name)
			print("Perks: ", end='')
			for i in self.perks:
				print(i.tag + ", ", end='')
			print('')
			print("Gold: " + str(self.currentMoney))
			print("Total kills: " + str(self.totalKills))
			print("Total deaths: " + str(self.totalDeaths))
			print("Total score: " + str(self.totalScore))
			print("Total perks: " + str(self.totalPerks))
			print("Total heals: " + str(self.totalHeals))
			print("Total items turned in: " + str(self.totalItemsTI))
			print("Total gold collected: " + str(self.totalMoney))
			print("Total bounties collected: " + str(self.totalBounties))
			print("Total games survived: " + str(self.totalGames))
			print(dline)
			print("You should've played better...")
		elif option == 1:
			print("You did not reach your kill quota. Death is upon you!")
			self.health = 0

def equipmentPicker(amount, list1): #(INT: how many items, LIST[item]: list of available items) -> LIST[item]: list of choices
	counter = amount
	choices = []
	while counter > 0:
		pick = np.random.randint(0, len(list1))
		choices.append(list1[pick])
		counter -= 1
	return choices

def perkPicker(amount, list1): #(INT: how many perks, LIST[perk]: list of available perks) -> LIST[perk]: list of choices
	counter = amount
	copyList = list(list1)
	choices = []
	while counter > 0:
		pick = np.random.randint(0, len(copyList))
		choices.append(copyList[pick])
		copyList.remove(copyList[pick])
		counter -= 1
	return choices

def bountyItem(list1): #(LIST[STR]: list of available items) -> STR: chosen bounty item
	pick = np.random.randint(0, len(list1))
	return list1[pick].tag

def inGame(character):
	gameFinished = False
	while not gameFinished:
		print(line)
		print(repr('"turnin(ti) #ofWeapons #ofBounties" to turn in weapons or "gamefinished(gf) kills deaths score" when game is finished.'))
		command = input()
		commandArr = command.split(" ")
		if commandArr[0].lower() == "turnin" or commandArr[0].lower() == "ti":
			if len(commandArr) == 3:
				character.turnIn(int(commandArr[1]), int(commandArr[2]))
			elif len(commandArr) == 2:
				character.turnIn(int(commandArr[1]))
			else:
				print("That's not the right number of arguments. Try again, moron.")
		elif commandArr[0].lower() == "gamefinished" or commandArr[0].lower() == "gf":
			if len(commandArr) == 4:
				character.logScore(int(commandArr[1]), int(commandArr[2]), int(commandArr[3]))
				gameFinished = True
			else:
				print("That's not the right number of arguments. Try again, moron.")
		else:
			print("What even is that? Try again, moron.")
	return character.health

def victoryScreen(player):
	print(dline)
	print("Player name: " + player.name)
	print("Perks: ", end='')
	for i in player.perks:
		print(i.tag + ", ", end='')
	print('')
	print("Gold: " + str(player.currentMoney))
	print("Total kills: " + str(player.totalKills))
	print("Total deaths: " + str(player.totalDeaths))
	print("Total score: " + str(player.totalScore))
	print("Total perks: " + str(player.totalPerks))
	print("Total heals: " + str(player.totalHeals))
	print("Total items turned in: " + str(player.totalItemsTI))
	print("Total gold collected: " + str(player.totalMoney))
	print("Total bounties collected: " + str(player.totalBounties))
	print("Total games survived: " + str(player.totalGames))
	print(dline)
	print("Let's Goooooooo!!!! POGGERS!!! You won wow!")

availablePerks = [
perk('Acrobat', 'Jumping costs less stamina'),
perk('Cat', 'Take less fall damage'),
perk('Friendly', 'Take and give less damage from allies'),
perk('Fireproof', 'Take  less damage from fire'),
perk('Wrecker', 'Do more damage to structures'),
perk('Smith', 'Repair effectiveness increased'),
perk('Tenacious', 'Passive healing increased'),
perk('Scavenger', "Killing enemies causes them to drop everything they're carrying"),
perk('Brawler', 'Deal more fist damage'),
perk('Fury', 'Gain full stamina on kill'),
perk('Huntsman', 'Throwables deal more damage to archers'),
perk('Rat', 'Crouch movement speed increased'),
perk('Second Wind', 'Gain extra stamina on hit'),
perk('Flesh Wound', 'Stay alive for a short while after reaching 0 hp'),
perk('Ranger', 'Move faster while your bow is drawn'),
perk('Rush', 'Immediately sprint after getting a kill'),
perk('Dodge', 'You can dodge now'),
perk('Bloodlust', 'Kills grant full hp'),
perk('Peasant', "You're a peasant now"),
perk('Merchant', '[NOT IMPLEMENTED]Turning in equipment now gives you double gold'),
perk('Picky', '[NOT IMPLEMENTED]Perk rerolls cost 300 every time'),
perk('Extra Perk', '[NOT IMPLEMENTED]Perks now show up in 4s instead of 3s'),
perk('Extra Stock', '[NOT IMPLEMENTED]Equipment now shows up in 7s instead of 5s'),
perk('Haggler', '[NOT IMPLEMENTED]Everything in the store is now 20 percent cheaper'),
perk('5 Finger Discount', '[NOT IMPLEMENTED]The first item you buy from the store is free every time'),
perk('Bounty Hunter', '[NOT IMPLEMENTED]Every kill you get is also +100 gold now'),
perk('Tactical Retreat', '[NOT IMPLEMENTED]Your minimum kill count now only goes up by 1 instead of 2')]

weaponList = [
item('Cleaver', 100),
item('Carving Knife', 10),
item('Dagger', 80),
item('Wooden Mallet', 10),
item('Blacksmith Hammer', 80),
item('Warhammer', 250),
item('Axe', 250),
item('Short Spear', 100),
item('Short Sword', 100),
item('Arming Sword', 300),
item('Bastard Sword', 500),
item('Mace', 400),
item('Rapier', 400),
item('Falchion', 400),
item('Messer', 550),
item('Heavy Branch', 50),

item('Buckler', 100),
item('Targe', 200),
item('Pavise Shield', 250),
item('Heater Shield', 150),
item('Kite Shield', 200),

item('Hoe', 50),
item('Rusty Fork', 80),
item('Scythe', 80),
item('Quarterstaff', 10),
item('Training Sword', 10),
item('Longsword', 550),
item('Executioners Sword', 800),
item('War Axe', 850),
item('Battle Axe', 850),
item('Pole Axe', 800),
item('Halberd', 1000),
item('Bardiche', 900),
item('Billhook', 550),
item('Estoc', 700),
item('Maul', 900),
item('Eveningstar', 850),
item('Spear', 950),
item('Greatsword', 900),
item('Zweihander', 1000),

item('Recurve Bow', 600),
item('Longbow', 700),
item('Crossbow', 800),

item('Rock', 50),
item('Throwing Knives', 100),
item('Throwing Axe', 150),
item('Fire Bomb', 150),
item('Smoke Bomb', 100),

item('Light Legs', 100),
item('Light Chest', 300),
item('Light Head', 300),
item('Medium Legs', 300),
item('Medium Chest', 600),
item('Medium Head', 600),
item('Heavy Legs', 600),
item('Heavy Chest', 900),
item('Heavy Head', 900),

item('Bandage', 300),
item('Medic Bag', 500),

item('Tool box', 450),
item('Bear Trap', 100),
item('Lute', 10)
]

def main():
	print(line)
	print("Enter character name to start")
	playerName = input()
	player = character(playerName)
	remainingPerks = list(availablePerks)

	run = True
	victory = False
	while run:
		#in game
		player.totalGames += 1
		currentBounty = bountyItem(weaponList)
		print(dline)
		print("Current bounty item is " + currentBounty)
		print("Current kill quota is " + str(player.killMin) + ". You better have that many kills by the end of the game... Or else.")
		charHP = inGame(player)
		if charHP <= 0:
			player.permaDie()
			run = False
			break
		if player.won:
			victory = True
			run = False
			break
		print(dline)
		print("*You feel as though your health has been restored. HP: " + str(player.health))

		#perks
		perkChoices = perkPicker(3, remainingPerks)
		donePerk = False
		while not donePerk:
			print(line)
			print("Pick a perk from the list, 'reroll' to get a new set of perks, 'skip' to pass.")
			for i in range(len(perkChoices)):
				print(perkChoices[i].tag + " - " + perkChoices[i].description + ", ", end='')
			print('')
			print("(Reroll cost = " + str(player.rerollPrice) + ")")
			print("Gold: " + str(player.currentMoney) + ", Lives: " + str(player.health) + ", Kills: " + str(player.totalKills))
			print(line)
			pickedPerk = input().lower()
			if pickedPerk == 'skip':
				donePerk = True
				break
			elif pickedPerk == 'reroll':
				if player.currentMoney >= player.rerollPrice:
					player.currentMoney -= player.rerollPrice
					perkChoices = perkPicker(3, remainingPerks)
					player.rerollPrice *= 2
				else:
					print("Not enough money. Try again, moron.")
			else:
				for i in perkChoices:
					if pickedPerk == i.tag.lower():
						player.gainPerk(i)
						donePerk = True
						break
				if not donePerk:
					print("Not on the list. Try again, moron.")

		#shop
		equipChoices = equipmentPicker(5, weaponList)
		doneEquip = False
		while not doneEquip:
			print(line)
			print("Pick an item from the list, 'done' to finish shopping.")
			for i in range(len(equipChoices)):
				print(equipChoices[i].tag + " - " + str(equipChoices[i].price) + ", ", end='')
			print('')
			print("Gold: " + str(player.currentMoney) + ", Lives: " + str(player.health) + ", Kills: " + str(player.totalKills))
			print(line)
			pickedEquip = input().lower()
			if pickedEquip == 'done':
				doneEquip = True
				break
			bought = False
			for i in equipChoices:
				if pickedEquip == i.tag.lower():
					if player.currentMoney >= i.price:
						player.buyEquip(i)
						equipChoices.remove(i)
						bought = True
					else:
						print("Not enough money. Try again, moron.")
						bought = True
			if not bought:
				print("Not on the list. Try again, moron.")

		print(line)
		print('Begin next game.')
	if player.won:
		victoryScreen(player)

main()