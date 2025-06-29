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

## Quest Moves

# Swear an Iron Vow
if id == 1 or userInput == "Swear Vow" or userInput == "Swear an Iron Vow":
	out.append(f''' -title "**Quest Move**: Swear an Iron Vow" -desc "When you swear to complete a quest, write your vow and give it a rank. Then, roll +heart. If you swear this vow to a connection, add +1; if you share a bond, add +2." ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: you are emboldened and it is clear what you must do next. Take +2 momentum." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: you are determined but begin your quest with more questions than answers. Take +1 momentum, and envision what you do to find a path forward." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: you must overcome a significant obstacle before you begin your quest. Envision what stands in your way." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')

# Reach a Milestone
if id == 2 or userInput == "Milestone" or userInput == "Reach a Milestone" or userInput == "Reach A Milestone":
	out.append(f''' -title "**Quest Move**: Reach A Milestone" -desc "When you make headway in your quest by doing any of the following... \n - overcoming a critical obstacle \n - gaining meaningful insight \n - completing a perilous expedition \n - acquiring a crucial item or resource \n - earning vital support \n - defeating a notable foe \n ...you may mark progress per the rank of the vow." ''')

# Fulfull Your Vow
if id == 3 or userInput == "Fulfull Your Vow" or userInput == "Fulfull Vow" or userInput == "Fulfull your Vow":
	out.append(f''' -title "**Quest Move**: Fulfull Your Vow (*Progress Move*)" -desc "When you reach the end of your quest, roll the challenge dice and compare to your progress." ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: your vow is fulfilled. Mark a reward on your quests legacy track per the vow's rank: troublesome=1 tick; dangerous=2 ticks; formidable=1 box; extreme=2 boxes; epic=3 boxes. Any allies who shared this vow also mark the reward." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: your vow is fulfilled. Mark a reward on your quests legacy track per the vow's rank: troublesome=1 tick; dangerous=2 ticks; formidable=1 box; extreme=2 boxes; epic=3 boxes. Any allies who shared this vow also mark the reward, but there is more to be done or you realize the truth of your quest. If you Swear an Iron Vow to set things right, take your full legacy reward. Otherwise, make the legacy reward one rank lower (none for a troublesome quest)." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: your vow is undone through an unexpected complication or realization. Envision what happens and choose one: \n - Give up on the quest: Forsake Your Vow. \n - Recommit to the quest: Roll both challenge dice, take the lowest value and clear that number of progress boxes. Then, raise the vow's rank by one (if not already epic)." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')
    

# Forsake Your Vow
if id == 4 or userInput == "Forsake Vow" or userInput == "Forsake Your Vow" or userInput == "Forsake":
	out.append(f''' -title "**Quest Move**: Forsake Your Vow" -desc "When you renounce your quest, betray your promise, or the goal is lost to you, clear the vow. Then, envision the impact of this failure and choose one or more as appropriate to the nature of the vow. Any allies who shared this vow may also envision a cost. \n - You are demoralized or dispirited: Endure Stress \n - A connection loses faith: Test Your Relationship when you next interact. \n - You must abandon a path or resource: Discard an asset. \n - Someone else pays a price: Envision how a person, being, or community bears the cost of the failure. \n - Someone else takes advantage: Envision how an enemy gains power. \n - Your reputation suffers: Envision how this failure marks you." ''')

if id == 5:
        out.append(f''' -desc "*Error*: There are only 4 Quest Moves" ''')

return '\n'.join(out)

</drac2>
-footer '!questMove -t "Move Type" -id # -m # -a "attribute"'