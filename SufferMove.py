embed
<drac2>
## Session Moves
a, out, HTable, STable, WDTable = argparse(&ARGS&), [''], "", "", ""

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


## Suffer Moves

# Lose Momentum

# Endure Harm

# Endure Stress

# Companion Takes a Hit

# Sacrifice Resources

# Withstand Damage





if id == 9:
        out.append(f''' -desc "*Error*: There are only 8 Combat Moves" ''')

return '\n'.join(out)

</drac2>
-footer '!CombatMoves -t "Move Type" -id # -m # -a "attribute"'