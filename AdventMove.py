embed
<drac2>
## Adventure Moves
a, out = argparse(&ARGS&), ['']

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


# TO DO: Add attribute and Bond text
# #!adventureMove -t "Face Danger" -m 2 -a "edge"
# Face Danger
if id == 1 or userInput == "Face Danger":
	out.append(f''' -title "**Adventure Move**: Face Danger" -desc "When you attempt something risky or react to an imminent threat, envision your action and roll. If you act... \n - With speed, mobility, or agility: Roll +edge \n - With resolve, command, or sociability: Roll +heart \n - With strength, endurance, or aggression: Roll +iron \n - With deception, stealth, or trickery: Roll +shadow \n - With expertise, focus, or observation: Roll +wits \n" ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: you are successful. Take +1 momentum." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: you succeed, but not without cost. Make a suffer move (-1)." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: you fail, or your progress is undermined by a dramatic and costly turn of events. ***Pay the Price***." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')
    
#Secure an Advantage
if id == 2 or userInput == "Secure An Adv" or userInput == "Secure Advantage" or userInput == "Secure An Advantage":
	out.append(f''' -title "**Adventure Move**: Secure An Advantage" -desc "When you assess a situation, make preparations, or attempt to gain leverage, envision your action and roll. If you act... \n - With speed, mobility, or agility: Roll +edge \n - With resolve, command, or sociability: Roll +heart \n - With strength, endurance, or aggression: Roll +iron \n - With deception, stealth, or trickery: Roll +shadow \n - With expertise, focus, or observation: Roll +wits \n" ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: you succeed. Take +2 momentum, and add +1 on your next move (not a progress move)." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: you succeed, select either: +2 Momentum, or +1 to your next move (not a progress move)." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: you fail or your assumptions betray you. ***Pay the Price***." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')
        
# Gather Information
if id == 3 or userInput == "Gather Info" or userInput == "Gather Information":
	out.append(f''' -title "**Adventure Move**: Gather Information" -desc "When you search for clues, conduct an investigation, analyze evidence, or do research, roll +wits." ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: you discover something helpful and specific. The path you must follow or action you must take to make progress is made clear. Envision what you learn. Then, take +2 momentum." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: the information provides new insight, but also complicates your quest. Envision what you discover. Then, take +1 momentum." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: your investigation unearths a dire threat or reveals an unwelcome truth that undermines your quest. ***Pay the Price***." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')
        
# Compel
if id == 4 or userInput == "Compel":
	out.append(f''' -title "**Adventure Move**: Compel" -desc "When you try to persuade someone or make them an offer, envision your approach. If you... \n - Charm, pacify, encourage, or barter: Roll +heart \n - Threaten or incite: Roll +iron \n - Lie or swindle: Roll +shadow" ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: they'll do what you want or agree to your conditions. Take +1 momentum." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: they'll do what you want or agree to your conditions, but their agreement comes with a demand or complication. Envision their counteroffer." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: they refuse or make a demand that costs you greatly. ***Pay the Price***." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')
    
# Aid Your Ally
if id == 5 or userInput == "Aid Ally" or userInput == "Aid your Ally":
	out.append(f''' -title "**Adventure Move**: Aid Your Ally" -desc "When you act in direct support of an ally, envision how you aid them. Then, Secure an Advantage or Gain Ground to take action. If you score a hit, they (instead of you) take the benefits of the move. \n If you Gain Ground and score a strong hit, you are both in control. On a weak hit, your ally is in control but you are in a bad spot." ''')
 
# Check Your Gear
if id == 6 or userInput == "Check Gear" or userInput == "Check Your Gear":
	out.append(f''' -title "****Adventure Move**: Check Your Gear" -desc "When you check to see if you have a specific helpful item or resource, roll +supply." ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: you have it, and are ready to act. Take +1 momentum." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: you have it, but must choose one: Your supply is diminished Sacrifice Resources (-1), It is not quite right, and causes a complication or delay Lose Momentum (-2)" ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: you don't have it and the situation grows more perilous. ***Pay the Price***." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')
    
if id == 7:
    out.append(f''' -desc "*Error*: There are only 6 Adventure Moves" ''')

return '\n'.join(out)

</drac2>
-footer '!AdventureMoves -t "Move Type" -id # -m # -a "attribute"'