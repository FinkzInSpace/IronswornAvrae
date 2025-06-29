embed
<drac2>
## Session Moves
a, out, DActionTable = argparse(&ARGS&), [''], ""

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
 
## Combat Moves

# Enter The Fray
if id == 1 or userInput == "Enter The Fray" or userInput == "Fray" or userInput == "Enter Fray":
	out.append(f''' -title "**Combat Move**: Enter The Fray" -desc "When you initiate combat or are forced into a fight, envision your objective and give it a rank. If the combat includes discrete challenges or phases, set an objective with a rank for each. Then, roll to see if you are in control. If you are... \n - On the move or maneuvering: Roll +edge \n - In command or facing off against your foe: Roll +heart \n - In the thick of it at close quarters: Roll +iron \n - Preparing to act against an unaware foe: Roll +shadow \n - Caught in a trap or sizing up the situation: Roll +wits" ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: you take both: \n - +2 Momentum \n - You are in control." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: choose one: \n - +2 Momentum \n - You are in control." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: the fight begins with you in a bad spot." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')
        
# Gain Ground
if id == 2 or userInput == "Gain Ground" or userInput == "Ground":
	out.append(f''' -title "**Combat Move**: Gain Ground" -desc "When you are in control and take action in a fight to reinforce your position or move toward an objective, envision your approach and roll. If you are... \n - In pursuit, fleeing, or maneuvering: Roll +edge \n - Charging boldly into action, coming to the aid of others, negotiating, or commanding: Roll +heart \n - Gaining leverage with force, powering through, or making a threat: Roll +iron \n - Hiding, preparing an ambush, or misdirecting: Roll +shadow \n - Coordinating a plan, studying a situation, or cleverly gaining leverage: Roll +wits" ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: choose two: \n - Mark Progress \n - +2 Momentum \n - Add +1 on your next move (not a progress move)." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: choose one: \n - Mark Progress \n - +2 Momentum \n - Add +1 on your next move (not a progress move)." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: your foe gains the upper hand, the fight moves to a new location, or you encounter a new peril. You are in a bad spot and must ***Pay the Price***." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')

# React Under Fire
if id == 3 or userInput == "React" or userInput == "React Under Fire" or userInput == "Under Fire":
	out.append(f''' -title "**Combat Move**: React Under Fire" -desc "When you are in a bad spot and take action in a fight to avoid danger or overcome an obstacle, envision your approach and roll. If you are... \n - In pursuit, fleeing, dodging, getting back into position, or taking cover: Roll +edge \n - Remaining stalwart against fear or temptation: Roll +heart \n - Blocking or diverting with force, or taking the hit: Roll +iron \n - Moving into hiding or creating a distraction: Roll +shadow \n - Changing the plan, finding a way out, or cleverly bypassing an obstacle: Roll +wits" ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: you succeed and are in control. Take +1 momentum." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: you avoid the worst of the danger or overcome the obstacle, but not without a cost. Make a suffer move (-1). You stay in a bad spot." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: the situation worsens. You stay in a bad spot and must ***Pay the Price***." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')

# Strike
if id == 4 or userInput == "Strike" or userInput == "strike":
	out.append(f''' -title "**Combat Move**: Strike" -desc "When you are in control and assault a foe at close quarters, roll +iron; when you attack at a distance, roll +edge." ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: mark progress twice. You dominate your foe and stay in control." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: mark progress twice, but you expose yourself to danger. You are in a bad spot." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: the fight turns against you. You are in a bad spot and must ***Pay the Price***." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')

# Clash
if id == 5 or userInput == "Clash" or userInput == "clash":
	out.append(f''' -title "**Combat Move**: Clash" -desc "When you are in a bad spot and fight back against a foe at close quarters, roll +iron; when you exchange fire at a distance, roll +edge." ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: mark progress twice. You overwhelm your foe and are in control." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: mark progress, but you are dealt a counterblow or setback. You stay in a bad spot and must ***Pay the Price***." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: your foe dominates this exchange. You stay in a bad spot and must ***Pay the Price***." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')

# Take Decisive Action
if id == 6 or userInput == "Decisive Action" or userInput == "Take Decisive Action":
	out.append(f''' -title "**Combat Move**: Take Decisive Action (Progress Move)" -desc "When you seize an objective in a fight, envision how you take decisive action. Then, roll the challenge dice and compare to your progress. If you are in control, check the result as normal. If you are in a bad spot, count a strong hit without a match as a weak hit, and a weak hit as a miss." ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: you prevail. Take +1 momentum. If any objectives remain and the fight continues, you are in control." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: you achieve your objective, but not without cost. Roll on the table below or choose one. If the fight continues, you are in a bad spot." ''')
        sroll = "1d100" 
        sdie = vroll(sroll)
        if sdie.total <= 40:
            DActionTable = "It's worse than you thought: Make a suffer move (-2)."
        elif sdie.total > 40 and sdie.total <= 52:
            DActionTable = "Victory is short-lived: A new peril or foe appears."
        elif sdie.total > 52 and sdie.total <= 64:
            DActionTable = "You face collateral damage: Something is lost, damaged, or broken."
        elif sdie.total > 64 and sdie.total <= 76:
            DActionTable = "Others pay the price: Someone else suffers the cost."
        elif sdie.total > 76 and sdie.total <= 88:
            DActionTable = "Others won't forget: You are marked for vengeance."
        elif sdie.total > 88 and sdie.total <= 100:
            DActionTable = "It gets complicated: The true nature of a foe or objective is revealed."
        else:
            DActionTable = "ERROR"
        out.append(f''' -f "Ourcome|{DActionTable}" ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: you are defeated or your objective is lost. ***Pay the Price***." ''')
    else:
        out.append(f''' -f "**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')

# Face Defeat
if id == 7 or userInput == "Defeat" or userInput == "Face Defeat":
	out.append(f''' -title "**Combat Move**: Face Defeat" -desc "When you abandon or are deprived of an objective, envision the consequence of this failure, clear the objective, and ***Pay the Price***. \n If the fight continues, you may create a new objective and give it a rank to represent the changing situation. If any objectives remain, the fight continues and you are in a bad spot." ''')

# Battle
if id == 8 or userInput == "Battle" or userInput == "battle":
	out.append(f''' -title "**Combat Move**: Battle" -desc "When you fight a battle and it happens in a blur, envision your objective and roll. If you primarily... \n - Fight at range, or using your speed and the environment to your advantage: Roll +edge. \n - Fight depending on your courage, leadership, or companions: Roll +heart. \n - Fight in close to overpower your foe: Roll +iron. \n - Fight using trickery to befuddle your foe: Roll +shadow. \n - Fight using careful tactics to outsmart your foe: Roll +wits." ''')
    if outcome == "Strong Hit":
        out.append(f''' -f "**{outcome}**: you achieve your objective unconditionally. You and any allies who joined the battle may take +2 momentum." ''')
    elif outcome == "Weak Hit":
        out.append(f''' -f "**{outcome}**: you achieve your objective, but not without cost. ***Pay the Price***." ''')
    elif outcome == "Miss":
        out.append(f''' -f "**{outcome}**: you are defeated or the objective is lost. ***Pay the Price***." ''')
    else:
        out.append(f''' -f"**ERROR**: No outcome deteremined." ''')
    if match: 
        out.append(f''' -f "***Match***: The match represents a twist in the narrative, something interesting, or a new opportunity." ''')
        
if id == 9:
        out.append(f''' -desc "*Error*: There are only 8 Combat Moves" ''')

return '\n'.join(out)

</drac2>
-footer '!CombatMoves -t "Move Type" -id # -m # -a "attribute"'