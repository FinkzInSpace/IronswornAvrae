embed
<drac2>
## Session Moves
a, out, BAST = argparse(&ARGS&), [''], ""

# type designator
userInput = a.last('t', ' ')
id = a.last('id', 1)
id = int(id)

# Begin a Session Table
sroll = "1d100" 
sdie = vroll(sroll)
if sdie.total < 10:
    BAST = "Flashback reveals an aspect of your background or nature."
elif sdie.total > 10 and sdie.total <= 20:
    BAST = "Flashback reveals an aspect of another character, place, or faction."
elif sdie.total > 20 and sdie.total <= 30:
    BAST = "Influential character or faction is introduced or given new detail."
elif sdie.total > 30 and sdie.total <= 40:
    BAST = "Seemingly unrelated situations are shown to be connected."
elif sdie.total > 40 and sdie.total <= 50:    
    BAST = "External factors create new danger, urgency or importance for a quest."
elif sdie.total > 50 and sdie.total <= 60:   
    BAST = "Important character is put in danger or suffers a misadventure."
elif sdie.total > 60 and sdie.total <= 70:   
    BAST = "Key location is made unsafe or becomes mired in conflict."
elif sdie.total > 70 and sdie.total <= 80:    
    BAST = "Unexpected return of an emeny or threat."
elif sdie.total > 80 and sdie.total <= 90: 
    BAST = "Peril lies ahead or lurks just out of view."
elif sdie.total > 90 and sdie.total <= 100: 
    BAST = "Unforeseen aid is on the way or within reach."
else:
    BAST = "ERROR"
    
## Begin a Session
if id == 1 or userInput == "Begin" or userInput == "Begin Session" or userInput == "Begins a Session":
   	out.append(f''' -title "**Session Move**: Begin A Session" -desc "When you begin a significant session or chapter of play, do all of the following, In addition, you may spotlight a new danger, opportunity, or insight. This can include a scene hidden from your character's perspective. If you do, envision a brief vignette (you may roll or choose on the table below for inspiration). Then, all players take +1 momentum as you return to play from the viewpoint of your characters." -f "DO| Identify or adjust flagged content and Set a Flag." -f "DO| Review or recap what happened last session." -f "DO| Set the scene by envisioning your character's current situation and intent." -f "Inspiration| {BAST}" ''')
    
# Change Your Fate
if id == 2 or userInput == "Fate" or userInput == "Change Fate" or userInput == "Change your Fate":
    out.append(f''' -title "**Session Move**: Change Your Fate" -desc "When you encounter flagged content, reject an oracle, resist a consequence, or otherwise need to shift your circumstances within the game for your comfort or enjoyment, pause and identify what needs to be changed. Choose as many options as appropriate." -f "**Reframe**: This didn't happen the way you first thought. Envision the moment from another perspective in a way that diminishes or changes the content." -f "**Refocus: This is not the most important thing happening right now. Envision how the spotlight shifts to change the focus." -f "**Replace**: This happens but with a small adjustment. Switch out an element and envision how this new detail changes the scenario." -f "**Redirect**: Adjust the trajectory to involve a helping hand. Envision how another person or party becomes involved." -f "**Reshape**: The situation changes completely. Envision what happened instead." ''')

# Set a Flag
if id == 3 or userInput == "Flag" or userInput == "Set Flag" or userInput == "Set a Flag":
    out.append(f''' -title "**Session Move**: Set A Flag" -desc "When you identify situations or topics you don't want to include, don't want to envision in detail, or otherwise may need mindfulness when approaching, that content is now flagged. When you encounter content flagged as something to approach mindfully, pause to consider or discuss its role in your story. When you come across flagged content that you would rather adjust or omit, *Change Your Fate*." ''')


# Take a Break
if id == 4 or userInput == "Break" or userInput == "Take Break" or userInput == "Take a Break":
    out.append(f''' -title "**Session Move**: Take A Break" -desc "When you resolve a progress move or complete an intense scenario, take a few deep breaths and take some time to attend to the needs of your body. Reflect on what just happened and how it made you feel. Then, choose one." -f "Move on: Continue the session. You or an ally may add +1 on the next move (not a progress move), bolstered by your reflection and past experiences." -f "Stop for now: *End a Session*." ''')    


# End a Session
if id == 5 or userInput == "End" or userInput == "End Session" or userInput == "End a Session":
    out.append(f''' -title "**Session Move**: End A Session" -desc "When you end a significant session or chapter of play, reflect on the events of the game and identify any missed opportunities to mark progress. If there is a quest, connection, or other situation you would like to give focus in your next session, make note of it and take +1 momentum." -f "If you strengthened your ties to a connection, *Develop Your Relationship*." -f "If you moved forward on a quest, *Reach a Milestone*." ''')
    
if id == 6:
    out.append(f''' -desc "*Error*: There are only 5 Session Moves" ''')

return '\n'.join(out)

</drac2>
-footer '!SessionMove -t "Move Type" -id # '