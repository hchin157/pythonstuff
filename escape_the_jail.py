start = '''
You open your eyes and look around to see yourself in a dark, grimy cell.
With you are three people you never expected to be in the same room,
much less with you.
There's Justin Bieber.
Nicki Minaj.
And...Donald Trump???
One thing is clear...
You have to ESCAPE THE JAIL
You have to choose ONE of these characters to go with you
'''
print(start)
chosen="'Great! You chose me,"
oops = "Oops! "
dead = " you're dead. Better start over!"

def choose_character():
    person= input("Do you choose [Justin Bieber], [Nicki Minaj], or [Donald Trump]?")
    if person == 'Justin Bieber':
        print (chosen + " Justin Bieber'")
        chose_JB()
    elif person == 'Nicki Minaj':
        print (chosen + " Nicki Minaj'")
        chose_NM()
    elif person == 'Donald Trump':
        print (chosen + " Donald Trump'")
        chose_DT()
    else:
        print ("Who's that? Please retype answer")
        choose_character()

def chose_JB():
    action_cell= input("'Should we [smash the wall] or [steal the key]?'")
    if action_cell == 'smash the wall':
        print (oops+ "a rock fell on your head," + dead)
        choose_character()
    elif action_cell == 'steal the key':
        print("You manage to snag the key as a guard walks past.")
        print("'Great! We've stolen the key. Let's go!'")
        print("'The dungeon is so dark, and I haven't eaten anything for ages!'")
        print("'Ughhh, I can't see anything. *smashes into a wall*'")
        print("'Hey... I smell something good from my left!'")
        print("'But I hear guards too.'")
        print("'I don't hear or smell anything on the right.'")
        chose_dirJB()
    else:
        print("'What? Why would you want to do that?'")
        chose_JB()

def chose_dirJB():
    action_dir= input("Do we turn [left] or [right]?")
    if action_dir== 'right':
        print (oops + "you starved to death," + dead)
        choose_character()
    elif action_dir== 'left':
        print ("There are no lights in the cafeteria so")
        chose_speedJB()
    else:
        print("What are you talking about, there's no path there.")
        chose_dirJB

def chose_speedJB():
    action_speed= input("Should we [sneak in] to get the food or [go fast]")
    if action_speed == 'sneak in':
        print ("'Okay let's sneak in'")
        print ("'YAY we got the food'")
        chose_yesJB()
    elif action_speed == 'go fast':
        print (oops + "The guards heard you running and tackled you," + dead)
        choose_character()
    else:
        print("I don't think we can do that.")
        chose_speedJB()

def chose_yesJB():
    action_yes = input("'Hey I see a door should we go for it? [yes] or [no]")
    if action_yes == 'yes':
        print ("YAY WE'RE OUT")
        print ("You and Justin Bieber have a great life out of jail.")
        end()
    elif action_yes == 'no':
        print (oops + "You were stuck there for too long" + dead)
    else:
        print ("Huh? What did you say?")
        chose_yesJB

def end():
    print ("*****************************************")
    print ("You did it! You and your partner-in-crime safely make it to...safety.")
    print ("*****************************************")

def chose_NM():
    act_cell = input("'Should we [break the gate] or [bribe the officer]?'")
    if act_cell == 'break the gate':
        print (oops + "You broke yourself trying to break the gate," + dead)
        choose_character()
    elif act_cell == 'bribe the officer':
        print ("'Hey officer, I got something for you!'")
        print ("'I'll give you 100,000 dollars if you let us out!'")
        print ("The officer nods.")
        print ("You and Nicki Minaj follow the officer outside of the prison.")
        choose_escapeNM()
    else:
        print ("'That's not possible. We're not doing that.'")
        chose_NM()

def choose_escapeNM():
    print("'I see a moat.'")
    print("The officer leaves.")
    act_escape = input("'Should we [climb the rope] above the moat, or [swim across]?'")
    if act_escape == 'climb the rope':
        print ("'Yay! We're on the other side!")
        end()
    elif act_escape == 'swim across':
        print (oops + "You got eaten by an alligator," + dead)
        choose_character()
    else:
        print ("'There's only two ways we can get across. Your idea won't work, sorry.'")
        choose_escapeNM()

def chose_DT():
    pres_cell= input("'Should we go [through the vent] or [dig a hole] with a spoon?'")
    if pres_cell== 'dig a hole':
        print (oops +'you used a plastic spoon, and got nowhere' + dead)
        choose_character()
    elif pres_cell == 'through the vent':
        print ("'Follow me I have a hyuuge plan.'")
        print ("You follow Donald Trump into the vent, not knowing what to expect")
        print ("You hear a loud thump as Donals Trump bumps into a wall")
        print ("'Ow this wall is such a nuisance...'")
        chose_dirDT()
    else:
        print("'No thanks, I don't want to do that.'")
        chose_DT()

def chose_dirDT():
    pres_dir= input("'We can turn [left] or [right] what do you think?'")
    if pres_dir == 'left':
        print (oops + "You tripped off a security laser and got zapped" + dead)
        choose_character()
    elif pres_dir == 'right':
        print ("You see another vent and escape, and fly away.")
        end()
    else:
        print ("'No no no, I said...'")
        chose_dirDT()

choose_character()
