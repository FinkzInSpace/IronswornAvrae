embed
<drac2>
## Session Moves
a, out, DiscTable, ChaosTable = argparse(&ARGS&), [''], "", ""

# type designator
userInput = a.last('t', ' ')
id = a.last('id', 1)
id = int(id)

#Action score calculator
bond = a.last('b',False)
mod = a.last('m', 0)
att = a.last('a', None)
match = False

sroll = "1d6+" +str(mod) + ("+1" if bond else "+0")
ActionScore = vroll(sroll)

croll = "1d10"
cDie1 = vroll(croll)
cDie2 = vroll(croll)

if cDie1.total == cDie2.total: 
	match = True 
out.append(f''' -f "Action Score| {ActionScore.full} with {att}" ''') 
out.append(f''' -f "Challenge Dice| {cDie1.full} | {cDie2.full}" ''')
# Hit Logic
if ActionScore.result.total > cDie1.total and ActionScore.result.total > cDie2.total:
	outcome = "Strong Hit"
elif ActionScore.result.total > cDie1.total and ActionScore.result.total < cDie2.total:
	outcome = "Weak Hit"
elif ActionScore.result.total < cDie1.total and ActionScore.result.total > cDie2.total:
	outcome = "Weak Hit"
else: 
	outcome = "Miss"
 
# Exploration Moves

#Undertake an Expedition
if id == 1 or userInput == "Undertake Expedition" or userInput == "Expedition" or userInput == "Undertake An Expedition":
	out.append(f''' -title "**Exploration Move**: Undertake An Expedition" -desc "When you sail an unfamiliar route through perilous seas, find the way across hazardous terrain, or explore a mysterious site, give the expedition a name and rank. Then, for each segment of the expedition, envision your approach. If you... \n - Move at speed: Roll +edge \n - Keep a low profile: Roll +shadow \n - Stay vigilant: Roll +wits" ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: you reach a waypoint. Envision the location and mark progress per the rank of the expedition." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: you reach a waypoint. Envision the location and mark progress per the rank of the expedition, but this progress costs you. Choose one \n - Suffer costs en route: Make a suffer move (-2), or two suffer moves (-1). \n - Face a peril at the waypoint: Envision what you encounter." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: you are waylaid by a crisis, or arrive at a waypoint to confront an immediate hardship or threat. Do not mark progress, and ***Pay the Price***." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')

#Finish an Expedition
if id == 2 or userInput == "Finish Expedition" or userInput == "Finish An Expedition":
	out.append(f''' -title "**Exploration Move**: Finish An Expedition (Progress Move)" -desc "When your expedition comes to an end, roll the challenge dice and compare to your progress." ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: you reach your destination or complete your survey. Mark a reward on your discoveries legacy track per expedition's rank: troublesome=1 tick; dangerous=2 ticks; formidable=1 box; extreme=2 boxes; epic=3 boxes. Any allies who shared this expedition also mark the reward." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: you reach a waypoint. Envision the location and mark progress per the rank of the expeditionyou reach your destination or complete your survey. Mark a reward on your discoveries legacy track per expedition's rank: troublesome=1 tick; dangerous=2 ticks; formidable=1 box; extreme=2 boxes; epic=3 boxes. Any allies who shared this expedition also mark the reward, but you face an unforeseen complication at the end of your expedition. Make the legacy reward one rank lower (none for a troublesome expedition), and envision what you encounter." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: your destination is lost to you, or you come to understand the true nature or cost of the expedition. Envision what happens and choose one: \n - Abandon the expedition: Envision the cost of this setback and ***Pay the Price***. \n - Return to the expedition: Roll both challenge dice, take the lowest value, and clear that number of progress boxes. Then, raise the expedition's rank by one (if not already epic)." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')
        
#Explore a Waypoint
if id == 3 or userInput == "Explore Waypoint" or userInput == "Waypoint" or userInput == "Explore A Waypoint" or userInput == "Explore":
	out.append(f''' -title "**Exploration Move**: Explore A Waypoint" -desc "When you divert from an expedition to examine a notable location, roll +wits." ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: choose one: \n - Find an opportunity: Envision a favorable insight, situation, resource, or encounter. Then, take +2 momentum. \n - Gain progress: Mark progress on your expedition, per its rank." ''')
        if match: 
            out.append(f''' -f "***Match***: you may instead ***Make a Discovery***." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: you uncover something interesting, but it is bound up in a peril or reveals an ominous aspect of this place. Envision what you encounter. Then, take +1 momentum." ''')
        if match: 
            out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: you encounter an immediate hardship or threat, and must ***Pay the Price***." ''')
        if match: 
            out.append(f''' -f "***Match***: you may instead ***Confront Chaos***." ''')  
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')

#Set A Course
if id == 4 or userInput == "Set Course" or userInput == "Course" or userInput == "Set A Course":
	out.append(f''' -title "**Exploration Move**: Set A Course" -desc "When you travel a known route through perilous seas, across hazardous terrain, or within a mysterious site, roll +supply." ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: you reach your destination and the situation there favors you. Take +1 momentum." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: you arrive, but face a cost or complication. Choose one: \n - Suffer costs en route: Make a suffer move (-2), or two suffer moves (-1). \n - Face a complication at the destination: Envision what you encounter." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: you are waylaid by a significant threat, and must ***Pay the Price***. If you overcome this obstacle, you may push on safely to your destination." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')
       
# Make a Discovery
# Discovery  Table
if id == 5 or userInput == "Make Discovery" or userInput == "Discovery" or userInput == "Make A Discovery":
    sroll = "1d100" 
    sdie = vroll(sroll)
    if sdie.total < 5:
        DiscTable = "Abundant and unusual life."
    elif sdie.total > 5 and sdie.total <= 10:
        DiscTable = "Archive or map with revelatory details."
    elif sdie.total > 10 and sdie.total <= 15:
        DiscTable = "Awe-inspiring natural feature."
    elif sdie.total > 15 and sdie.total <= 19:
        DiscTable = "Beneficial enchantment or powers."
    elif sdie.total > 19 and sdie.total <= 23:
        DiscTable = "Benevolent spirit or apparition."
    elif sdie.total > 23 and sdie.total <= 28:
        DiscTable = "Clues to an enduring mystery."
    elif sdie.total > 28 and sdie.total <= 33:    
        DiscTable = "Extraordinary natural phenomenon."
    elif sdie.total > 33 and sdie.total <= 38:    
        DiscTable = "Majestic or remarkable creature."    
    elif sdie.total > 38 and sdie.total <= 42:   
        DiscTable = "Manifestation of a myth or legend."
    elif sdie.total > 42 and sdie.total <= 47:   
        DiscTable = "Monumental architecture or artistry."
    elif sdie.total > 47 and sdie.total <= 52:
        DiscTable = "Otherworldly path or passage."
    elif sdie.total > 52 and sdie.total <= 57:
        DiscTable = "People with phenomenal abilities."
    elif sdie.total > 57 and sdie.total <= 61:
        DiscTable = "Prized natural resource."
    elif sdie.total > 61 and sdie.total <= 65:
        DiscTable = "Relic of legendary power."
    elif sdie.total > 65 and sdie.total <= 70:
        DiscTable = "Safeguarded or hidden location."
    elif sdie.total > 70 and sdie.total <= 75:    
        DiscTable = "Sizable treasure."
    elif sdie.total > 75 and sdie.total <= 80: 
        DiscTable = "Unique machine or technology."
    elif sdie.total > 80 and sdie.total <= 85: 
        DiscTable = "Well-preserved artifact or specimen."
    elif sdie.total > 85 and sdie.total <= 90: 
        DiscTable = "Wondrous visions or prophesies."
    elif sdie.total > 90 and sdie.total <= 100: 
        DiscTable = "Roll Twice."
    else:
        DiscTable = "ERROR"   
    out.append(f''' -title "**Exploration Move**: Make A Discovery" -desc "When your exploration of a waypoint uncovers something wondrous, roll on the table below or choose one. Then, envision the nature of the discovery and how it is revealed. When you first experience or engage with the discovery, you and your allies may mark two ticks on your discoveries legacy track." -f  "Discovery| {DiscTable}" ''')


# Confront Chaos
# Discovery  Table
if id == 6 or userInput == "Confront Choas" or userInput == "Chaos" or userInput == "Confront":
    sroll = "1d100" 
    sdie = vroll(sroll)
    if sdie.total < 5:
        ChaosTable = "Archive or map bearing a dire warning."
    elif sdie.total > 5 and sdie.total <= 10:
        ChaosTable = "Baneful spells or wards."
    elif sdie.total > 10 and sdie.total <= 15:
        ChaosTable = "Blighted or corrupted habitat."
    elif sdie.total > 15 and sdie.total <= 20:
        ChaosTable = "Cataclysmic natural phenomenon."
    elif sdie.total > 20 and sdie.total <= 25:
        ChaosTable = "Cursed treasure of irresistible lure."
    elif sdie.total > 25 and sdie.total <= 30:
        ChaosTable = "Dead given unnatural life."
    elif sdie.total > 30 and sdie.total <= 35:    
        ChaosTable = "Fanatical followers of a dreadful power."
    elif sdie.total > 35 and sdie.total <= 40:    
        ChaosTable = "Fearsome creature of monstrous size."    
    elif sdie.total > 40 and sdie.total <= 45:   
        ChaosTable = "Harrowing visions or prophesies."
    elif sdie.total > 45 and sdie.total <= 50:
        ChaosTable = "Malevolent being of dreadful power."
    elif sdie.total > 50 and sdie.total <= 55:
        ChaosTable = "Malignant affliction or parasite."
    elif sdie.total > 55 and sdie.total <= 60:
        ChaosTable = "People of monstrous form."
    elif sdie.total > 60 and sdie.total <= 65:
        ChaosTable = "Relic of accursed power."
    elif sdie.total > 65 and sdie.total <= 70:    
        ChaosTable = "Ruinous machine or technology."
    elif sdie.total > 70 and sdie.total <= 75: 
        ChaosTable = "Signs of an awakened evil."
    elif sdie.total > 75 and sdie.total <= 80: 
        ChaosTable = "Site of a baffling disappearance."
    elif sdie.total > 80 and sdie.total <= 85: 
        ChaosTable = "Site of great destruction."
    elif sdie.total > 85 and sdie.total <= 90: 
        ChaosTable = "Site of terrible carnage."
    elif sdie.total > 90 and sdie.total <= 95: 
        ChaosTable = "Swarming creatures of insatiable fury."
    elif sdie.total > 95 and sdie.total <= 100: 
        ChaosTable = "Wrathful spirit or apparition."
    else:
        ChaosTable = "ERROR"   
    out.append(f''' -title "**Exploration Move**: Confront Chaos" -desc "When your exploration of a waypoint uncovers something dreadful, decide the number of aspects: one, two, or three. Roll that number of times or choose that number of aspects on the table below. Then, envision how the encounter begins. For each result, when you first confront that aspect within the scope of the encounter, you and your allies may mark one tick on your discoveries legacy track." -f  "Chaos| {ChaosTable}" ''')
 
if id == 7:
        out.append(f''' -desc "*Error*: There are only 6 Adventure Moves" ''')

return '\n'.join(out)

</drac2>
-footer '!explorationMove -t "Move Type" -id # -m # -a "attribute"'