import numpy as np

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
perk('Merchant', 'Turning in equipment now gives you double gold'),
perk('Picky', 'Perk rerolls cost 300 every time'),
perk('Extra Perk', 'Perks now show up in 4s instead of 3s'),
perk('Extra Stock', 'Equipment now shows up in 7s instead of 5s'),
perk('Haggler', 'Everything in the store is now 20 percent cheaper'),
perk('5 Finger Discount', 'The first item you buy from the store is free every time'),
perk('Bounty Hunter', 'Every kill you get is also +100 gold now'),
perk('Tactical Retreat', 'Your minimum kill count now only goes up by 1 instead of 2')]

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

def equipmentPicker(amount, list1): #(INT: how many items, LIST[item]: list of available items) -> LIST[STR]: list of choices
	counter = amount
	choices = []
	while counter > 0:
		pick = np.random.randint(0, len(list1))
		choices.append(list1[pick].tag+" - "+str(list1[pick].price))
		counter -= 1
	return choices

def perkPicker(amount, list1): #(INT: how many perks, LIST[STR]: list of available perks) -> LIST[STR]: list of choices
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
	while !gameFinished:
		command = raw_input("(turnin #ofWeapons #ofBounties) to turn in weapons or (gamefinished kills deaths score) when game is finished.")
		commandArr = command.split(" ")
		if commandArr[0].lower() == "turnin" || commandArr[0].lower() == "ti":
			if commandArr[2]:
				character.turnin(int(commandArr[1]), int(commandArr[2]))
			else:
				character.turnin(int(commandArr[1]))
		elif commandArr[0].lower() == "gamefinished" || commandArr[0].lower() == "gf":
			character.logScore(int(commandArr[1]), int(commandArr[2]), int(commandArr[3]))
			gameFinished = True
	return character.health

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
		self.totalKills = 0
		self.totalDeaths = 0
		self.totalScore = 0
		self.totalPerks = 0
		self.totalHeals = 0		#total times recieved healing
		self.totalItemsTI = 0	#total items turned in
		self.totalMoney = 0		#total money recieved
		self.totalBounties = 0	#total bounty items collected
		self.totalGames = 0

	def heal(self, amount):
		self.health += amount
		self.totalHeals += amount

	def turnIn(self, amount, bounty=0):
		if bounty > 0 && bounty <= 3:
			self.currentMoney += (100*bounty)
			self.totalMoney += (100*bounty)
			self.totalBounties += (1*bounty)
			self.totalItemsTI += (1*bounty)
		if amount > 0 && <= 3:
			self.currentMoney += (50*amount)
			self.totalMoney += (50*amount)
			self.totalItemsTI += (1*amount)

	def purchase(self, item):
		self.equipment.push(item)
		self.currentMoney -= item.price

	def gainPerk(self, perk):
		self.perks.push(perk)
		self.totalPerks += 1

	def logScore(self, kills, deaths, score):
		self.totalKills += kills
		self.totalDeaths += deaths
		self.health -= deaths-1
		self.totalScore += score
		money = (int(score / 1000) * 50)
		self.money += money
		self.totalMoney += money

	def permaDie(self): #prints out a neat little summary of the character + stats to post to discord for record keeping
		pass

print(equipmentPicker(5, weaponList))
print(perkPicker(3, availablePerks))
print(bountyItem(weaponList))

def main():
	playerName = raw_input("Enter character name to start")
	player = character(playerName)
	remainingPerks = list(availablePerks)

	run = True
	while run:
		charHP = inGame(player)
		if charHP <= 0:
			player.permaDie()
			run = False
			break
		print(perkPicker(3, remainingPerks))
		pickedPerk = raw_input("Pick a perk from the list:")
		



main()