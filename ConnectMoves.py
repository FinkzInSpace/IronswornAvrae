embed
<drac2>
## Session Moves
a, out, BAST = argparse(&ARGS&), [''], ""

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

# Connection Moves

# Make A Connection
if id == 1 or userInput == "Connection" or userInput == "Make A Connection":
	out.append(f''' -title "**Connection Move**: Make A Connection" -desc "When you search out a new relationship or give focus to an existing relationship (not an ally or companion), roll +heart." ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: you create a connection. Give them a role and rank. Whenever your connection aids you on a move closely associated with their role, add +1 and take +1 momentum on a hit." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: you create a connection. Give them a role and rank. Whenever your connection aids you on a move closely associated with their role, add +1 and take +1 momentum on a hit, but this connection comes with a complication or cost. Envision what they reveal or demand. " ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: you don't make a connection and the situation worsens. ***Pay the Price***." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')
    

# Test Your Relationship
if id == 2 or userInput == "Test Relationship" or userInput == "Test Your Relationship":
	out.append(f''' -title "**Connection Move**: Test Your Relationship" -desc "When your relationship with a connection is tested through conflict, betrayal, or circumstance, roll +heart. If you share a bond, add +1." ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: Take the ***Develop Your Relationship*** connection move." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: Take the ***Develop Your Relationship*** connection move, but also envision a demand or complication as a fallout of this test." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: On a miss, or if you have no interest in maintaining this relationship, choose one. \n - Lose the connection: Envision how this impacts you and ***Pay the Price***. \n - Prove your loyalty: Envision what you offer or what they demand, and ***Swear an Iron Vow*** (formidable or greater) to see it done. Until you complete the quest, take no benefit for the connection. If you refuse or fail, the connection is permanently undone." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')
    

# Develop Your Relationship
if id == 3 or userInput == "Develop Relationship" or userInput == "Develop Your Relationship":
	out.append(f''' -title "**Connection Move**: Develop Your Relationship" -desc "When you reinforce your relationship with a connection by doing any of the following... /n - swearing a vow to undertake a perilous quest in their service \n - completing a quest to their benefit \n - leveraging their help in desperate circumstances \n - giving them something of worth \n - sharing a profound moment \n - standing with them against hardship \n - overcoming a test of your relationshi ...you may mark progress per the rank of the connection. \n 
    If you already share a bond with the connection, do not mark progress. Instead, roll +their rank to learn the impact on your legacy: troublesome=+1; dangerous=+2; formidable=+3; extreme=+4; epic=+5." ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: mark 2 ticks on your bonds legacy track." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: take +2 momentum." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: take no lasting benefit." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: Strong Hit only: you may also envision how recent events bolstered your connection's standing and raise their rank by one (if not already epic)." ''')
    

# Forge A Bond
if id == 4 or userInput == "Forge Bond" or userInput == "Forge A Bond":
	out.append(f''' -title "**Connection Move**: Forge A Bond (Progress Move)" -desc "When your relationship with a connection is ready to evolve, roll the challenge dice and compare to your progress." ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: you now share a bond. Mark a reward on your bonds legacy track per the connection's rank: troublesome=1 tick; dangerous=2 ticks; formidable=1 box; extreme=2 boxes; epic=3 boxes. Any allies who share this connection also mark the reward. Then, choose one \n - Bolster their influence: When they aid you on a move closely associated with their role, add +2 instead of +1. \n - Expand their influence: Give them a second role. When they aid you on a move closely associated with either role, add +1 and take +1 momentum on a hit." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: you now share a bond. Mark a reward on your bonds legacy track per the connection's rank: troublesome=1 tick; dangerous=2 ticks; formidable=1 box; extreme=2 boxes; epic=3 boxes. Any allies who share this connection also mark the reward. Then, choose one \n - Bolster their influence: When they aid you on a move closely associated with their role, add +2 instead of +1. \n - Expand their influence: Give them a second role. When they aid you on a move closely associated with either role, add +1 and take +1 momentum on a hit. \n But they ask something more of you first. To gain the bond and the legacy reward, envision the nature of the request, and do it (or Swear an Iron Vow to see it done)." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: they reveal a motivation or background that puts you at odds. If you recommit to this relationship, roll both challenge dice, take the lowest value, and clear that number of progress boxes. Then, raise the connection's rank by one (if not already epic)." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')

if id == 5:
    out.append(f''' -desc "*Error*: There are only 4 Connection Moves" ''')

return '\n'.join(out)

</drac2>
-footer '!SessionMove -t "Move Type" -id # '