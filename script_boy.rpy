label boy_start:

label sceneb1:
    hide chap1
    scene mroom1 with dissolve
    play music start1
    show cneu at center:
        zoom 0.75
    narr "You are an average cheerful, happy-go-lucky guy."
    narr "You have an extreme love for video games and most of your time is spent in front of your computer."
    narr "You have a twin sister, more on that later."
    narr "You don't exactly have any special skills that set you apart from others."
    narr "However, you have noticed since you were young..."
    narr "That in times of extreme anger, you have been able to tap into some unknown pool of energy."
    narr "With full access to this arcane energy, you have been able to perform some insane feats."
    narr "You have no idea why this happens nor can you explain this phenomenon."
    narr "Nobody other than your sister knows about this."
    narr "There is one catch though...It is insanely difficult to get you angry enough to unleash your powers."
    ws "Now isn't that convenient..."
    narr "That's all you need to know for now. Let's start with the story."
    nvl clear
    c "{i}*Yawn* How long did I sleep for?{/i}"
    hide cneu
    show chap1 at center:
        zoom 0.75
    c "{i}Doesn't really matter, it's my birthday today... I can sleep for as long as I want!{/i}"
    hide chap1
    show ccon at center:
        zoom 0.75
    c "{i}Crap! Birthday! I really hope Luna isn't awake yet. I'd better check.{/i}"
    hide ccon
    show black with dissolve
    hide mroom1
    show ccon at left:
        zoom 0.75
    play sound knock
    "Knock Knock"
    "..."
    play sound knock
    "Knock Knock"
    "..."
    c "Luna?"
    c "{i}No response, I guess she is still asleep. Phew, crisis averted.{/i}"
    play sound dmg2
    "BANG!" with hpunch
    "The door flew open with a loud bang and smacked you in the face."
    hide ccon
    show cann at left:
        zoom 0.75
    c "What the hell Luna!?"
    show froom with dissolve
    show lann1 at right:
        zoom 0.75
    narr "This is your twin sister, Luna. She is quick-tempered, but deep down she is a really caring person."
    narr "Nobody can match her wit and very few have managed to hold their own in a fight with her."
    narr "She will go to any lengths to defend the people she loves and will always fight for what is right."
    narr "You two have been inseparable ever since your parents died in a car crash, leaving you in the care of your kind neighbour. More on that later."
    narr "You both share a really cool birthdate...\n 1st Jan 2001. Basically 01/01/01"
    narr "Let's get back to the situation at hand..."
    nvl clear
    hide cann
    show cann at left:
        zoom 0.75
    l1 "You tell me! It's our 18th birthday and you decide to sleep in today of all days?"
    l1 "I had so many plans for us! Now we can't do any of them!"
    hide cann
    show capo at left:
        zoom 0.75
    c "I'm really sorry Luna. Truly, I am... I just didn't feel like getting up so early."
    c "We still have a lot of time, it's not thaaaaat late."
    hide lann1
    show lann2 at right:
        zoom 0.75
    l1 "Humph! I don't want to talk to you."
    c "Oh, come on... Don't be like that! I said I'm sorry."
    l1 "Sorry won't fix anything. You made me sad on my birthday."
    hide capo
    show csly1 at left:
        zoom 0.75
    c "Hey! It's my birthday too. Don't I matter?"
    a "KIDDOS! COME DOWN IF YOU BOTH ARE AWAKE... BREAKFAST IS READY!"
    hide csly1
    show cneu at left:
        zoom 0.75
    c "Coming Angie!"
    hide lann2
    show lneu1 at right:
        zoom 0.75
    l1 "We will be down in a moment!"
    l1 "I haven't forgiven you yet."
    c "Seriously? Come on, don't be like that!"
    hide lneu1
    hide cneu
    show kitchen with dissolve
    hide froom
    show aneu1 at center:
        zoom 0.75
    narr "This is Mrs. Lewis, or as she likes you to call her, Angie. Angie lives alone, having lost her husband in the army."
    narr "She has taken care of you ever since your parents died. She has never let you feel their loss and loves you like her own kids."
    narr "You both are extremely grateful for all that she has done."
    nvl clear
    hide aneu1
    show ahap4 at center:
        zoom 0.75
    show chap1 at left:
        zoom 0.75
    show lhap1 at right:
        zoom 0.75
    l1 "Good Morning Angie!"
    c "Morning!"
    a "There you are my sweetlings! Did you sleep well?"
    l1 "Some of us slept a little {i}too{/i} well..."
    a "That's nice to hear."
    a "Help me set the table, you two..."
    menu:
        "Help Angie":
            jump sceneb2

        "Sorry, I don't work in real life, let alone in a game.":
            ws "Well, then I sure as hell won't put you through all the trouble of playing this game..."
            jump gameover


label sceneb2:
    "You all set the table and start eating your breakfast..."
    a "So, any plans for your birthday?"
    a "After all, it's a big deal... You both are offically adults now."
    l1 "Aww...We will always be your little ones."
    l1 "I had made lots of plans but this idiot got up late."
    c "It wasn't late! She wanted to go cycling at 5 in the morning."
    a "Oh, it's fine Luna. Your brother must get very tired after all the late-night gaming he does."
    hide chap1
    show chap2 at left:
        zoom 0.75
    c "Huh? I don't do that...You must be mistaken..."
    hide lhap1
    show lang at right:
        zoom 0.75
    l1 "Don't act all innocent now. We all know how much you love those stupid games of yours."
    c "They're not stupid! They're works of art."
    l1 "Sure! What kind of art involves sneaking around and shooting people?"
    c "That's not the only type of games I play!"
    l1 "Well that's all I see you playing all the time!"
    a "Now, now. Don't squabble."
    a "Why don't you both finish your breakfast and go down to the beach? It's lovely this time of the year."
    hide lang
    show lhap1 at right:
        zoom 0.75
    l1 "That's a fantastic idea! Thanks Angie, you're the best."
    a "Run along now! Come home before 9 if you decide to go somewhere else after visiting the beach."
    c "Sure thing! Bye!"
    l1 "Bye Angie, take care."
    a "Bye kiddos."


label sceneb3:
    hide lhap1
    hide ahap4
    hide chap2
    show black with dissolve
    play music start2
    hide kitchen
    "After a few minutes..."
    show door with dissolve
    show chap1 at left:
        zoom 0.75
    show lhap1 at right:
        zoom 0.75
    l1 "Have you taken everything?"
    c "Sunscreen? Check. Towels? Check. Portable charger? Check. Snacks? Check. Extra cash? Check."
    c "Yeah, I guess we have all we need."
    l1 "Take the charger out. If we carry it then you will spend most of your time gaming on your phone."
    c "Aww come on! It's for emergencies."
    l1 "Take it out or I'm going alone."
    c "Fine...I'll go keep it."
    hide lhap1
    hide chap1
    show mroom1 with dissolve
    play music sly
    show csly1 at center:
        zoom 0.75
    hide door
    c "{i}Should I hide the charger and take it along anyway?{/i}"
    menu:
        "Take it.":
            $charger_flag = True
            c "{i}I guess it's smarter to carry it along."
            c "{i}Luna won't notice..."
            c "{i}Hopefully..."

        "Leave it.":
            $charger_flag = False
            c "{i}Better do as she says..."
            c "{i}Don't want to piss her off anymore."

    c "{i}Done. Let's get back to Luna."
    hide csly1
    show door with dissolve
    play music start2
    hide mroom1
    show chap1 at left:
        zoom 0.75
    c "I'm ready."
    show lhap1 at right:
        zoom 0.75
    l1 "Great. Let's go! Sunny beach, here we come!"
    hide lhap1
    hide chap1
    show black with dissolve
    hide door


label sceneb4:
    play music beach1
    "At the beach..."
    show beach1 with dissolve
    show chap1 at left:
        zoom 0.75
    show lhap1 at right:
        zoom 0.75
    l1 "Angie was right, it's perfect! Just the right amount of sunlight, not a lot of crowd and overall a beautiful day!"
    c "Let's find a good place to put down our towels."
    l1 "That seems like a nice spot. It is quite shady and close to the ice-cream stall."
    c "Let's go then."
    "You two spend most of your morning swimming and eating ice-creams."
    "As afternoon comes, you open the lunch that Angie has thoughtfully packed for you."
    "After lunch..."
    play music beach2
    l1 "I guess we should head back now."
    c "Ugh. I don't feel like going home so soon. Isn't there any other place we could go to?"
    l1 "Well, a friend of mine mentioned that there is a secluded path which leads to the park behind the highschool"
    l1 "But nobody knows where it starts from. If you want we could check it out. If it gets too dark we can always just retrace our steps."
    c "Sounds like a plan. Let's go!"
    l1 "Wait, I'll keep some of our stuff behind in the beach lockers. No point in lugging everything along with us."
    c "Good call... Hurry up."
    hide lhap1
    hide chap1
    show black with dissolve
    hide beach1
    show park with dissolve
    show csly1 at left:
        zoom 0.75
    show lneu3 at right:
        zoom 0.75
    c "Huh, would you look at that. There is a path hidden behind this swing-set."
    l1 "I can't believe we never noticed this before."
    c "Probably because we weren't looking for it earlier. Who cares! This is kind of exciting."
    l1 "Let's go then. I'm right behind you."
    hide csly1
    hide lneu3


label sceneb5:
    show path1 with dissolve
    hide park
    play music path
    show cneu at left:
        zoom 0.75
    show lneu1 at right:
        zoom 0.75
    c "Some part of me wants to believe that there is something really cool at the other end, like an abandoned fortress or something, but I don't wanna get my hopes up."
    l1 "Of course you would want something like that. This isn't one of your games [c]. Grow up."
    c "You're always such a spoilsport."
    l1 "I'm a realist."
    c "Is that another word for annoying and dumb?"
    l1 "Let's just walk. I cannot tolerate your idiocy for another minute."
    "After walking for about an hour."
    show path2 with dissolve
    hide cneu
    hide lneu1
    hide path 1
    show lneu3 at right:
        zoom 0.75
    show csly2 at left:
        zoom 0.75
    c "We have been walking for over an hour now and this path shows no sign of ending..."
    l1 "Let me check our location on my phone."
    l1 "..."
    hide lneu3
    show lang at right:
        zoom 0.75
    l1 "Dammit, no battery left."
    c "Same. We can't charge it either. I told you that we should have carried the power bank along with us."
    l1 "Dont take me on a guilt trip now!"
    if charger_flag:
        c "I sneaked it along with us anyway. Guess it paid off huh?"
        l1 "I should be angry with you but I'll let it slide since it might just get us out of this predicament..."
        c "..."
        c "There, it's on."
        c "..."
        l1 "Any luck?"
        c "..."
        c "Nope. No network. You try."
        l1 "Same. Guess we're stranded."
        jump sceneb6
    else:
        c "I guess we're stranded then."
        jump sceneb6


label sceneb6:
    l1 "Least we can do is keep walking."
    c "Yeah. Let's go."
    "A few minutes later..."
    c "I think we have been walking in circles."
    l1 "Stop assuming the worst everytime."
    c "That's your job."
    l1 "Hush! I think the path is getting wider."
    c "You mean we are nearing the end?"
    l1 "I think so, yeah."
    c "Let's keep moving then..."
    hide lang
    hide csly2
    show road1 with dissolve
    hide path2
    show csly2 at left:
        zoom 0.75
    show lneu3 at right:
        zoom 0.75
    c "Finally! We did it!"
    l1 "This looks like an old village. What is it doing so close to the city?"
    c "Most importantly, how has nobody stumbled upon it like we have?"
    l1 "I don't know, but standing around won't answer any of your questions. Let's start exploring."
    show village22 with dissolve
    hide csly2
    hide lneu3
    hide road1
    play music village2
    show cneu at left:
        zoom 0.75
    show lneu1 at right:
        zoom 0.75
    l1 "Looks pretty abandoned to me."
    c "Judging by the dilapidated buildings and untended fields, nobody has set foot here in years."
    l1 "Makes it all the more easier to poke around without the fear of tresspassing."
    c "True. Let's split up."
    l1 "Fine by me. We'll meet back here in sometime."
    c "Holler if you find anything cool."
    l1 "Will do."


label sceneb7:
    hide cneu
    hide lneu1
    play music plan
    show csly1 at center:
        zoom 0.75
    c "{i}Where should I look around?{/i}"

default chosen_menu_choicesb1 = []
label menub1:
    menu:
        set chosen_menu_choicesb1

        "Choose a place to look around"

        "Tavern":
            jump tavern

        "Village Square":
            jump villagesquare

        "Blacksmith Workshop":
            jump blacksmith

    menu:
        "Choose a place to look around"
        "Farmhouse":
            jump farm


label tavern:
    c "I guess this must have been the local tavern..."
    c "Should I go in?"
    menu:
        "Yes":
            jump enterb

        "No":
            jump denterb

    label enterb:
        c "How should I enter?"
        menu:
            "Through the door":
                c "HNNNGGGGGH! I think its blocked by something really heavy..."
                c "Looks like the window is the only way."
                jump taverninterior

            "Break the window and enter":
                jump taverninterior

        label taverninterior:
            c "The window seems breakable enough."
            c "Just need a good stone."
            c "..."
            c "There, this should do just fine."
            c "..."
            play sound glass
            "CRASH!"
            "The window explodes into hundreds of splinters."
            c "Done and dusted."
            c "Let's see what secrets you hide."
            c "..."
            c "Hmmm. Too dark to see anything."
            c "I think I have a torch with me."
            c "There!"
            c "OH! So the roof has fallen in. That's what was blocking the door."
            c "Other than that, just a normal tavern, nothing much to see."
            c "There's a large layer of dust over everything."
            c "Looks like nobody has been in here for years."
            c "Let's go somewhere else."
        jump menub1

    label denterb:
        c "Yeah. I guess I won't find anything worth my time."
        jump menub1


label villagesquare:
    c "This seems to be the village square."
    c "I mean what else could a large empty ground with a raised platform be?"
    hide csly1
    show chap1 at center:
        zoom 0.75
    c "What if this was a sparring arena?"
    c "Or maybe all the criminals were beheaded here."
    c "Damn. That would be so cool!"
    c "Well, guess I'll never know."
    c "Let's go somewhere else now. Nothing left to see here."
    hide chap1
    show csly1 at center:
        zoom 0.75
    jump menub1


label blacksmith:
    hide csly1
    show chap1 at center:
        zoom 0.75
    c "Awesome! A real, live smithy!"
    c "Imagine all the swords, maces and shields that must have been forged here."
    c "I wonder if there might be a sword lying around..."
    c "I could take it back as a memento of this day!"
    c "I should take a look around."
    default chosen_menu_choicesb2 = []
    label menub2:
        menu:
            set chosen_menu_choicesb2
            c "Where should I look?"

            "Behind the counter":
                c "Just various tools."
                c "Hammers, nails, chisels... The usual stuff you would expect to find."
                c "Nothing of value..."
                jump menub2

            "On the anvil":
                hide chap1
                show cann at center:
                    zoom 0.75
                c "Why did I think this would work?"
                c "It's an anvil. That's it."
                c "{i}{size=-5}Stupid developer{/size}{/i}"
                ws "Silence! I don't pay you to mock me! I could delete you with one click."
                c "Huh! Did I hear someone?"
                c "..."
                c "Probably just my imagination."
                hide cann
                show chap1 at center:
                    zoom 0.75
                jump menub2

            "Inside the barrels":
                c "The lid seems heavy..."
                c "HHNNNNGGGH! Almost there... Just a little more..."
                play sound dmg2
                c "There!"
                hide chap1
                show cang at center:
                    zoom 0.75
                c "Empty! ARE YOU SERIOUS?!"
                c "Damn it."
                c "All that effort for nothing."
                "The rest of the barrels turn out to be equally empty."
                hide cang
                show chap1 at center:
                    zoom 0.75
                jump menub2

    label menu3:
        menu:
            c "Where should I look?"
            "Inside the furnace":
                c "Jackpot! That looks like the hilt of a sword!"
                c "Crap! It's heavy..."
                hide chap1
                show csad at center:
                    zoom 0.75
                c "You have got to be kidding me..."
                c "It's just a hilt."
                c "Why would someone make just a hilt."
                c "I bet this is someone's idea of a cruel joke."
                c "They're probably laughing somewhere."
                ws "HAHAHAHAHAHA"
                c "I HOPE YOU ARE HAPPY!!!"
                ws "Extremely..."
                c "It's better than nothing I guess."
                c "Let's go somewhere else now."
                hide csad
                show csly1 at center:
                    zoom 0.75
        jump menub1


label farm:
    c "Wow, this is one big farmhouse!"
    c "It feels more like a mansion than a farmhouse."
    c "I should look around and see if I can find something that can give us an idea about this village."
    c "Hmm. That looks like a grave."
    hide csly1
    show capo at center with hpunch:
        zoom 0.75
    c "Are my eyes deceiving me?"
    c "This can't be real..."
    c "No way!"
    c "This has to be some messed up coincidence..."
    c "But how???"
    c "LUNA!!!"
    c "LUNAAAAAA!!!"
    c "Dammit, where is she?"
    c "..."
    "As all this is taking place, the sun has already started to set..."


label sceneb8:
    show village23
    play music confront
    c "It's dark already... Where is Luna?"
    c "LUNAAA!"
    hide capo
    show cneu at left:
        zoom 0.75
    show lang at right:
        zoom 0.75
    l1 "What is it [c]?"
    l1 "Why are you shouting like you have been possessed?"
    c "Did you find anything?"
    hide lang
    show lann1 at right:
        zoom 0.75
    l1 "No Luck... Just abandoned buildings and a dumb prank note... What about you?"
    c "I wandered around for a bit. I finally came upon this farmhouse..."
    c "It seemed normal until I saw this grave. That's why I shouted for you."
    l1 "What does it say?"
    c "See for yourself..."
    l1 "..."
    l1 "Are you pranking me?"
    c "NO! I have nothing to do with this! I swear."
    l1 "Who else would write my name on this gravestone?"
    c "Your name? What do you mean?"
    l1 "Didn't you call me here because its my name on the gravestone?"
    c "NO! I called you because I saw my name on the gravestone!"
    l1 "This makes no sense!"
    l1 "Are you telling me that you don't see my name engraved here?"
    c "No! I see my name."
    l1 "This is honestly freaking me out now!"
    c "So apparently we can only see our own name engraved on this headstone. That is crazy!"
    l1 "OH MY GOD! Did you see the dates?"
    c "No, I didn't go further than my name. Why? What does it say?"
    l1 "Born 01/01/01"
    c "Our birth date. So what?"
    l1 "Died 01/01/19" with hpunch
    c "That's today. But we're both alive and breathing. That makes no sense."
    l1 "I honestly have no idea what to make of this..."
    c "Hey, can you feel this headstone vibrating? A very low humming vibration but its there."
    l1 "Huh, let me see."
    play sound magic
    show white with Dissolve(0.3)
    hide white
    l1 "Whoa! What was that!"
    c "OH DEAR! Looks like we caused something bad to happen."
    l1 "The farmhouse is glowing from within!"
    c "This does not bode well for us."


label sceneb9:
    play music caught2
    play sound tele
    show white with Dissolve(0.4)
    hide white
    show gang at right:
        xpos 0.6
        zoom 0.75
    pause(1.5)
    play sound tele
    show white with Dissolve(0.4)
    hide white
    show eang1 at left:
        xpos 0.45
        zoom 0.75
    u "{b}Who dares awaken us from our slumber?{/b}"
    u "{b}Prepare to be obliterated for your insolence!{/b}"
    show lang at right:
        zoom 0.75
    show csad at left:
        zoom 0.75
    l1 "Please tell me this is an extremely well-thought out prank."
    l1 "You can show yourselves now. Ha Ha you got us. OOOO we're so scared. Look at me I'm shivering."
    u "SILENCE!"
    u "You shall speak only when we give you permission to do so."
    l1 "Ha! No one tells me what to do! Especially not some freaks in funny medieval robes."
    l1 "Where did you buy those rags? I hope you didn't pay too much for them because they suck!"
    c "Luna. Please be quiet. I think they're really powerful mages."
    l1 "Pah! Mages? Don't make me laugh. They're just terrible actors hired by my friends to prank me on my birthday."
    u "So you think we are actors huh?"
    u "Well can an actor do this?"
    play sound magic
    hide village23
    hide gang
    hide eang1
    hide lang
    show village23
    show gang at right:
        xpos 0.6
        zoom 0.75
    show eang1 at left:
        xpos 0.45
        zoom 0.75
    show lang at right:
        zoom 0.75
    show cann:
        zoom 0.75
        rotate_pad False
        xalign 0.0 yalign 0.0
        rotate 0
        linear 4.0 rotate 360
        repeat
    c "AAAAH! WHAT THE HELL!!!!! PUT ME DOWN PUT ME DOWN PUT ME DOWN!"
    u "Only if this arrogant companion of yours gets down on her knees and apologises."
    u "She must learn her place."
    l1 "HOLY MOLY! You guys can really do magic! What is happening! This is like a dream!"
    c "Luna please apologise to them! Hurry or I'm gonna throw up any minute now!"
    l1 "{i}Damn it! Looks like I have no choice. I would never bow down to anyone but I have to save [c]!{/i}"
    hide lang
    show lang at right:
        ypos 1.25
        zoom 0.75
    l1 "Okay okay. I am sorry for my behaviour. I did not realise the extent of your powers. Please forgive me and put my brother down."
    u "Very well. Do not repeat this mistake, or it will be the last thing you do."
    hide lang
    show lang at right:
        zoom 0.75
    play sound magic
    hide cann
    show cang at left:
        zoom 0.75
    c "Whew! I thought I was a goner for sure."
    l1 "Who are you really?"
    u "I am Gerald, Leader of the Seven Spectres..."
    u "And I am Eliza, Second-in-Command to Gerald and his ever-faithful companion."
    g "We were and are the most powerful mages in the entire history of mankind."
    e "Amongst the righteous mages to be precise."
    hide gang
    show gsad1 at right:
        xpos 0.6
        zoom 0.75
    hide eang1
    show esad1 at left:
        xpos 0.45
        zoom 0.75
    g "Or what's left of them."
    hide village23
    hide gsad1
    hide esad1
    hide cang
    hide lang
    show village22
    show village23
    hide village22
    show lang at right:
        zoom 0.75
    show cneu at left:
        zoom 0.75
    hide cneu
    show cneu at left:
        zoom 0.75
    show gsad1 at right:
        xpos 0.6
        zoom 0.75
    show esad1 at left:
        xpos 0.45
        zoom 0.75
    l1 "What do you mean?"
    hide gsad1
    show gang at right:
        xpos 0.6
        zoom 0.75
    hide esad1
    show eang1 at left:
        xpos 0.45
        zoom 0.75
    g "Enough with the questions."
    e "We are not answerable to you mere mortals."
    g "Nor have we forgotten that you were the ones to rouse us before our time of awakening."
    e "For which you must be punished."
    g "However we are just."
    e "So we will grant you leave to explain yourselves."
    g "Before our judgement is cast upon you."
    e "So speak, mortal."


label sceneb10:
    hide gang
    show gneu1 at right:
        xpos 0.6
        zoom 0.75
    hide eang1
    show eneu1 at left:
        xpos 0.45
        zoom 0.75
    c "We did not mean to awaken you. We don't even know what caused all this to happen!"
    l1 "Calm down, bro... Let me explain."
    "Luna explained everything to them..."
    "Right from the time they left the beach till the time they came upon the gravestone..."
    l1 "So that's what happened..."
    hide gneu1
    show gsus at right:
        xpos 0.6
        zoom 0.75
    hide eneu1
    show esus1 at left:
        xpos 0.45
        zoom 0.75
    g "So you mean to say that you both can only see your own name on this gravestone?"
    e "And it is your birthdate on this gravestone?"
    c "Yes. That seems to be the case!"
    g "Eliza, does this mean what I think it does?"
    e "It would seem that way Gerald..."
    hide gsus
    show ghap at right:
        xpos 0.6
        zoom 0.75
    hide esus1
    show ehap1 at left:
        xpos 0.45
        zoom 0.75
    g "In that case, it was fate that brought you here."
    e "We were destined to be awakened by your hands."
    hide ghap
    show gsor at right:
        xpos 0.6
        zoom 0.75
    g "Thus we apologise for our behaviour."
    e "We hope you will not hold this against us for we have need of your powers."
    l1 "Powers? What do you mean?"
    c "We are perfectly normal people, unlike you..."
    hide lang
    show lneu1 at right:
        zoom 0.75
    g "That's what you think."
    e "Reality is often more than we perceive it to be."
    c "What are you implying?"
    hide gsor
    show ghap at right:
        xpos 0.6
        zoom 0.75
    g "For you to understand, we will have to tell you a tale..."
    e "One that is filled with death and despair..."
    g "Yet promises a future filled with hope..."
    e "So are you ready?"
    g "Listen closely..."
    play music village1
    show grey with dissolve
    narr "This tale is from a time when magic was still prevalent."
    narr "The ability to use magic was bestowed upon a chosen few at birth."
    narr "These lucky few were sent to the Magician's Guild where they would learn the skills necessary for them to become mages."
    narr "I was one of them and so was Eliza."
    narr "Humans and mages lived in harmony, and they lived under the joint rule of a human queen and a mage king."
    narr "We belonged to the village of Arandur, the largest and most famous magical settlement."
    narr "It was ruled over by King Hrothgar and his wife Queen Illisna."
    narr "They were just and wise, and our King was the most powerful mage in the world at that time."
    narr "Everything was going smoothly and life was pleasant."
    narr "However, peace cannot exist forever, for chaos reigns supreme..."
    play music nar
    narr "One female mage by the name of Medea was not satisified with the extent of her powers."
    narr "She wanted to go beyond her limits, become more powerful than the Mage King himself."
    narr "Thus she hid herself away from the world and began to meddle in magic unspoken of."
    narr "Nobody knew of her intentions at first... but as time passed, her powers began to grow immensely."
    narr "It was impossible to keep your powers hidden beyond a certain limit, for the Mage King had a group of magicians called the Seven Spectres."
    narr "The king himself presided over it."
    narr "They were assigned the task of ensuring that peace is maintained and dealing with any conflicts that may arise."
    narr "Along with this, they kept a track of everyone's powers and warned the kingdom if anyone gave signs of losing control..."
    narr "I had the good fortune of finding myself accepted into the ranks of the Spectres."
    narr "It was there that I met Eliza and together we began to slowly rise amongst the ranks of the Spectres."
    narr "We proved ourselves in various situations and managed to build a reputation as the most promising mages."
    narr "Thus, when the time came for the King to decide who would succeed him as Leader of the Spectres, he chose me."
    narr "And of course, Eliza was selected as second in command."
    narr "Coming back to Medea... When the Spectres learnt of her secretive training, they rushed to confront her."
    narr "Meanwhile, the two of us were tasked with assisting the king to guard the people from the potential threat."
    narr "As we made our way to the palace, we saw bright flashes of light from the general direction of Medea's lair."
    narr "This meant that Medea had refused to comply with the Spectres and that they were in the middle of a fight."
    narr "We spoke a silent prayer for our brothers and sisters amongst the Spectres and hastened towards the palace."
    narr "We informed the king of the recent developments and began placing enchantments around the palace with his help."
    narr "We then waited for news, either good or bad..."
    narr "As minutes turned to hours, our fear for the worst began to grow."
    narr "The king began pacing his chambers... The trepidation in the room was palpable."
    narr "As we waited, Eliza pulled out an Ancient Tome that she carried everywhere she went."
    narr "It was a compilation of every unique and powerful spell she had come across during her studies..."
    narr "She pored over it with an intensity I had never seen before. Perhaps she had understood the delicacy of the situation more than I had."
    play music battle3
    narr "Suddenly, one of the palace walls blasted inwards violently. We rushed to the king's side and braced ourselves for another attack."
    narr "Out of the smoke and rubble, a figure began to slowly approach us."
    narr "Our fears were confirmed when we realised it was Medea..."
    narr "From her belt, hung the heads of our 4 fallen comrades, fresh blood dripping from where their necks had been..."
    narr "For a moment we stood there transfixed. The Spectres were a force to be reckoned with..."
    narr "Yet Medea had gotten the better of 4 of them at the same time."
    narr "Our instincts took over and we prepared to counter whatever she might throw at us."
    narr "Medea had an inhuman look to her, we found ourselves unable to look at her for long without a cold fear gripping at our hearts."
    narr "Whatever she had done to achieve this power, it had taken away more than it had given."
    narr "I realised that it was of utmost importance to rid the world of her, even if it meant destroying myself in the process."
    narr "I looked over at Eliza and realised that she was thinking the same thing."
    narr "We nodded to each other and thus a silent pact was formed between us."
    narr "Without any indication whatsoever, we rushed at Medea and began throwing volleys of spells at her."
    narr "She countered them like we were nothing but pesky flies in her way."
    narr "We gave it our all but it was futile, the extent of her powers was slowly becoming more and more obvious to us."
    narr "Without even glancing our way, she kept blocking our attacks and walked towards the king."
    narr "It was clear that he was her only target."
    narr "When she got as close as she needed to, she flicked us away with a snap of her fingers."
    narr "We slammed into the wall and lay there panting, tired out from our over-exertion..."
    narr "She rushed into the king and he just barely managed to stand his ground."
    narr "They fought like nothing we had ever seen before."
    narr "King Hrothgar proved to be as powerful as the legends told."
    narr "Unfortunately, it was visible that we were on the losing end."
    narr "Inspite of his best efforts, the king was slowly getting pushed back."
    narr "Medea was stronger than him. She had actually managed to rise above his power."
    narr "We had to do something and we had to do it fast. I looked over to Eliza in hopes that she had some sort of plan."
    narr "All I saw was one lonesome tear rolling down her face..."
    narr "She walked over to me, her eyes closed, and held out her hand."
    narr "I grabbed ahold of it and then I felt nothing..."
    narr "It was as though she was absorbing every ounce of energy that I had, every fiber of my being."
    narr "I trusted her and did not resist..."
    narr "With all that energy coursing through her, she cast an immeasurably powerful spell."
    narr "It struck Medea but she did not falter. Instead, she just turned and smiled triumphantly."
    narr "Evidently, we had lost."
    narr "Or so we thought..."
    narr "In that brief moment of respite, the king was able to teleport himself to our side."
    narr "He looked at us with pride in his eyes and mouthed the words 'Thank You'."
    narr "With this final act, he scarificed himself and transformed into a giant mass of pure energy."
    narr "This globular apparition enveloped Eliza and all of a sudden, her spell seemed to be working."
    narr "Medea's smile waned. She seemed concerned..."
    narr "There was a large flash of light and then all was silent."
    narr "I floated in nothingness, I could not feel anything."
    narr "I let the warmth and darkness swallow me."
    play music farewell
    narr "Finally, I awoke to the sound of someone calling my name."
    narr "It was Eliza. She had transported us to this tiny village where we are right now."
    narr "She explained what she had done... It was brutal, but it was the only way..."
    narr "She had cast a prophecy spell. One that can overcome the strongest of magical forces."
    narr "With this prophecy, she had trapped Medea into a human body."
    narr "The closest human she could find..."
    narr "Queen Illisna."
    narr "The phrophecy would bind Medea to her human body until she would consume the blood of twins."
    narr "Not just any twins, but twins that were born on the day that this prophecy was cast."
    narr "And the twins needed to come of age for this spell to be broken."
    narr "Every year, on that fateful day, Medea would get back a fraction of her powers, for her magic could not be contained."
    narr "Until then, magic would be gone from this world."
    narr "With this spell, Eliza had managed to save the world from Medea, though not forever."
    narr "With heavy hearts, we realised that we needed to destroy ourselves lest Medea find us and use our energy to regain her powers."
    narr "So we entombed ourselves to this gravestone in hopes that the day shall never come when such twins are born."
    nvl clear


label sceneb11:
    hide grey with dissolve
    hide ghap
    show gsad1 at right:
        xpos 0.6
        zoom 0.75
    hide ehap1
    show esad1 at left:
        xpos 0.45
        zoom 0.75
    hide lneu
    show lsad1 at right:
        zoom 0.75
    hide cneu
    show csad at left:
        zoom 0.75
    hide csad
    show csad at left:
        zoom 0.75
    c "That's terrible."
    g "I warned you that it is a tale filled with despair."
    e "The truth is always cruel. There is no running away from that."
    l1 "I find it hard to digest that such things could have happened in the past and we had no clue."
    g "We have no reason to lie to you."
    hide gsad1
    show gneu2 at right:
        xpos 0.6
        zoom 0.75
    hide esad1
    show eneu2 at left:
        xpos 0.45
        zoom 0.75
    hide lsad1
    show lneu3 at right:
        zoom 0.75
    hide csad
    show csly2 at left:
        zoom 0.75
    hide csly2
    show csly2 at left:
        zoom 0.75
    e "I am sure you have a lot of questions from us. Ask us whatever comes to your mind."
    default chosen_menu_choicesb3 = []
    label menub3:
        menu:
            set chosen_menu_choicesb3

            "What should I ask?"

            "Is Medea still in our world?":
                g "Unfortunately yes."
                e "There is only one way to get rid of her..."
                g "That is by attacking her after she has consumed your blood and is in the process of shedding her human shell."
                e "She will be most vulnerable at that moment."
                jump menub3

            "If Medea is so weak now, why can't you defeat her?":
                g "Medea may be weak, but she still has remanants of her dark magic."
                e "She can absorb our powers if we get anywhere near her and then there will be no stopping her."
                jump menub3

            "Are we the twins from your prophecy?":
                g "We suspect so. Your united touch caused the gravestone to release us."
                e "We had laid a spell that would preserve our being until the prophetic twins came along."
                g "This is the reason why you could see your birthdate and name on the stone."
                jump menub3

            "What about the date of death on this tombstone?":
                g "The date is today, yet you both are alive."
                e "This means that in a few hours, Medea will find you and consume you, thus fulfilling the prophecy."
                jump menub3

            "What if we don't believe you?":
                g "You need our help to rid the world of Medea."
                e "And we need your help in distracting her."
                g "Neither can do anything without the other."
                e "So if you turn away and leave, then nothing can save this world from Medea's wrath."
                jump menub3

            "I have no more questions.":
                jump sceneb12


label sceneb12:
    play music caught1
    hide gneu2
    show gcur at right:
        xpos 0.6
        zoom 0.75
    hide eneu2
    show eneu1 at left:
        xpos 0.45
        zoom 0.75
    hide csly2
    show cneu at left:
        zoom 0.75
    hide cneu
    show cneu at left:
        zoom 0.75
    g "Very well then. Since we're all on the same page now, let us get down to the business of defeating Medea."
    e "We do not know what she looks like. She may have gained enough of her powers back to have disguised herself."
    g "We cannot stay with you lest she detect our presence."
    e "She must not suspect that you are aware of the prophecy."
    g "Therefore, we shall teach you a spell."
    e "Utter the spell once Medea has successfully ingested blood from both of you..."
    g "You shall have to use your wits to ensure that she extracts your blood without killing you."
    e "Are you ready?"
    default chosen_menu_choicesb4 = []
    label menub4:
        menu:
            set chosen_menu_choicesb4

            "Yes":
                jump sceneb13

            "Yes":
                jump sceneb13

            "No":
                ws "You don't have much of a choice here..."
                ws "I mean, what else can you do?"
                ws "If you decline, the game won't move forward."
                ws "I hope you understand."
                menu:
                    "Okay yeah. I understand that I have no say in this matter...":
                        jump menub4

                    "I SAID NO!":
                        return

            "Yes":
                jump sceneb13

            "Yes":
                jump sceneb13


label sceneb13:
    g "Let's hasten. We probably don't have much time."
    e "Pay close attention to the incantation. Inscribe it upon your minds..."
    g "The spell goes like this..."
    mid "SENNIEN DE ZAR HVATA {w} \n KWAYAN MAYAKA LESNORA {w} \n UMARNA LITA HUNNEN"
    g "Did you get that?"
    e "{b}It is of utmost importance that you remember it perfectly.{/b}"
    ws "{i}Don't cheat, kids...{/i}"
    menu:
        "I got it":
            jump sceneb14

        "Please repeat it":
            mid "SENNIEN DE ZAR HVATA {w} \n KWAYAN MAYAKA LESNORA {w} \n UMARNA LITA HUNNEN"
            jump sceneb14


label sceneb14:
    hide gcur
    show ghap at right:
        xpos 0.6
        zoom 0.75
    hide eneu1
    show ehap1 at left:
        xpos 0.45
        zoom 0.75
    hide lneu3
    show lhap1 at right:
        zoom 0.75
    hide cneu
    show chap1 at left:
        zoom 0.75
    hide chap1
    show chap1 at left:
        zoom 0.75
    g "I hope you are ready for what lies ahead..."
    e "We realise all this is too much to take in."
    g "And we know that is a lot to ask of you."
    e "But the fate of the world lies in your hands now."
    g "May the spirit of The Seven Spectres be with you."
    e "Good Luck little ones."
    show road2 with dissolve
    play music path
    hide village23
    hide gcur
    hide eneu1
    hide lhap1
    show lann1 at right:
        zoom 0.75
    hide lann1
    show lann1 at right:
        zoom 0.75
    hide chap1
    show cann at left:
        zoom 0.75
    c "Pretty insane birthday huh?"
    l1 "What makes you say so?"
    c "I mean mages, magic, evil witches and stuff..."
    l1 "Jeez, why can you never understand sarcasm?"
    c "Maybe you suck at being sarcastic."
    l1 "Maybe I let Medea suck your blood."
    c "I prefer not to think of that..."
    show path3 with dissolve
    hide road2
    hide lann1
    hide cann
    show cann at left:
        zoom 0.75
    show lann1 at right:
        zoom 0.75
    c "Have you thought about how we are going to distract Medea?"
    l1 "Not really..."
    c "I mean, we need to be alive even after she drinks our blood, in order to say the spell."
    l1 "I am aware of that."
    c "So? Any ideas?"
    l1 "We will cross that bridge when we get to it..."
    c "Not a good strategy for the given situation but okay..."
    l1 "Also, in case you forgot, we need to go to the beach before going home to grab all our stuff."
    c "Right, right... Walk faster then."
    show beach3 with dissolve
    play music confront
    hide path3
    hide cann1
    hide lann1
    show lang at right:
        zoom 0.75
    show cang at left:
        zoom 0.75
    c "Did you get it?"
    l1 "Yeah, it's all here, let's get back home..."
label sceneb15:
    show ahap3 at center:
        zoom 0.75
    a "Oh thank god! I found you guys..."
    l1 "Angie? What are you doing here?"
    hide ahap3
    show asad3 at center:
        zoom 0.75
    a "I got worried about you kids."
    hide asad3
    show asad2 at center:
        zoom 0.75
    a "I waited for so long but there was no sign of you two, so I decided to come looking for you..."
    c "But you never come out so late at night!"
    a "I had no option, even your phones were not reachable..."
    l1 "Sorry for making you worry!"
    hide asad2
    show ahap4 at center:
        zoom 0.75
    a "Nonsene! I am just glad that you both are safe and sound."
    c "You should have waited at home, we would have returned as usual."
    hide cang
    hide lang
    show lann1 at right:
        zoom 0.75
    show csly1 at left:
        zoom 0.75
    l1 "Yes! It's not like you to worry so much about us!"
    a "I have always worried about your safety. What are you talking about?"
    c "You have, but never to this extent."
    l1 "Not that we mind, it's just kind of unusual that's all."
    a "The two of you are just overthinking! You kids have had a long day and must be exhausted."
    a "Let's get back home so that you can go to sleep."
    c "Umm...Okay."
    "As the three of you start making your way back home, Luna visibly slowed down a little."
    "You realise that she wants you to do the same..."
    "Luna waits for Angie to move a little out of earshot before whispering to you..."
    hide ahap4
    l1 "Something just does't feel right."
    c "Relax...Its been a pretty insane day. I am just as on edge as you are."
    l1 "No, think about it! Angie is behaving so weirdly."
    c "She was just worried about us, she really cares for us."
    l1 "Do you think she is Medea?"
    c "Are you kidding me? No way. I can't believe you would even think of that."
    l1 "Please just consider the possibility atleast! It's literally a matter of life and death!"
    c "I really don't want to think about it."
    l1 "Please please please! Atleast for my sake!"
    c "Ugh. Fine... Let me think..."
    menu:
        "I really don't see any chance of her being Medea...":
            jump endb1

        "I think you may be right. We should be careful...":
            jump sceneb16


label sceneb16:
    c "I think maybe you are right. We should be careful..."
    l1 "I am glad that we both are on the same page..."
    l1 "What do you think our next step should be?"
    c "I think the best thing to do would be to confront her here and now..."
    c "If we reach home, she might have some traps or something set up for us..."
    c "And on top of that, the beach is open enough for Gerald and Eliza to fight her comfortably and without any chance of witnesses."
    l1 "I guess that makes sense."
    c "Are you ready?"
    l1 "I never will be, but we don't have much of a choice."
    c "Quite literally do or die..."
    hide csly1
    hide lann1
    show lhap2 at right:
        zoom 0.75
    show chap2 at left:
        zoom 0.75
    l1 "Heh. I just want you to know, whether we make it out of this in one piece or not...I really love you bro!"
    c "Bad time to get all sappy...but yeah, I love you too sis."
    l1 "Let's do this!"
    c "Yes! Here goes nothing."
    l1 "[c]."
    c "Yeah?"
    l1 "Don't die."
    c "I'll try my best. Same goes for you."
    l1 "Time to end this!"
    play music reveal
    "You both pick up your pace and catch up with Angie."
    show ahap4 at center:
        zoom 0.75
    c "Angie! We have a question for you!"
    a "Oh, sure. What is it?"
    l1 "Have you heard the name Medea?"
    hide ahap4
    show aang1 at center:
        zoom 0.75
    a "No, I have never heard that name. Why do you ask?"
    l1 "Because we know for a fact that she is going to come after us and suck out all our blood..."
    a "That all sounds very fantastical. Have you kids been taking some drugs?"
    c "You can cut the act Angie. We know that you are Medea."
    hide aang1
    show ahap3 at center:
        zoom 0.75
    a "What are you both saying? Medea, blood, prophecy. It makes no sense."
    l1 "We never said anything about a prophecy!"
    c "Why would you say that of all things unless you are Medea?"
    a "Come on kiddos, let's just go home."
    hide chap2
    hide lhap2
    show lang at right:
        zoom 0.75
    show cang at left:
        zoom 0.75
    c "NO WE ARE NOT GOING ANYWHERE WITH YOU!"
    l1 "I cannot believe that you have lied to us for 13 whole years."
    c "You are an evil, selfish human."
    a "HAHAHAHAHAHAHA! Thats's the thing my dear [c]... I am not a human..."
    play sound magic
    show white with Dissolve(0.42)
    pause(0.5)
    hide white
    hide ahap3
    show mhap2 at center:
        zoom 0.75
    play music battle1


label sceneb17:
    m "I am the most powerful being to have ever walked the face of this measly planet..." with vpunch
    m "And today is the day that I return to my true form and watch this world crumble under my might!"
    m "Isn't this all so exciting?"
    c "!!!"
    l1 "Did you see her eyes? They turned red!"
    c "And her voice... It hurts my ears. It's like someone is scratching the inside of my head with a nail."
    l1 "She is extremely powerful, I can feel an immense amount of energy emanating from her."
    c "And this isn't even her final form! We need to be extremely cautious!"
    hide mhap2
    show mang1 at center:
        zoom 0.75
    m "Stop whispering, it is of no use. I can hear everything you are saying..."
    m "Bow down to your queen!"
    c "I think we should comply for now..."
    l1 "Ugh, I don't like this but I have to agree."
    hide lang
    show lang at right:
        ypos 1.25
        zoom 0.75
    hide cang
    show cang at left:
        ypos 1.25
        zoom 0.75
    hide mang1
    show mhap2 at center:
        zoom 0.75
    m "Look at you two, cowering on the ground just like your weakling parents..."
    c "What do you mean?"
    m "What do you think I mean? I killed your parents once I was able to confirm that you two were the twins I needed."
    l1 "You mean they didn't die in a car crash?"
    m "HAHAHAHAHAHAHA! Of course not... That was what it looked like because I made it so!"
    m "I spent years finding the right pair of twins and then when I finally found you two, I knew that I had to keep you close to me."
    m "So I purchased your neighbour's house. He was very compliant... especially after he had no eyes..."
    m "And then all I had to do was orchestrate a simple car accident and Voila! The twins are in my hands."
    m "Finally the wait is over. It is time for me to shed this vile human carcass."
    c "Do you have to kill us? I don't want to die."
    m "I don't need to kill you, but it would be fun to watch you both squirm and flop around like fishes out of water."
    m "And as it is, I have no use of either of you..."
    l1 "Well then [c], I guess we won't get to see her final form and judge if it really is as magnificient as she claims it to be..."
    c "That's a shame. Can't be helped now."
    l1 "Do what you must, witch."
    hide mhap2
    show mhap3 at center:
        zoom 0.75
    m "You desire to lay your unworthy eyes upon my final form?"
    m "Very well, I shall grant your last wish."
    m "It is time to feast upon your succulent heart-fluid!"
    m "I haven't been so excited in centuries since I saw Hrothgar falter under my gaze..."
    m "Come closer maggots... Give me your blood."
    stop music


label sceneb18:
    "Medea moved closer to Luna and bit her arm..."
    play sound bite
    pause(2.0)
    l1 "AAAAGHHHH!"
    "Medea slowly starting intaking Luna's blood, swallowing gratitiously."
    play sound suck
    pause(8.0)
    c "Are you okay Luna?"
    m "She will live. It's nothing."
    m "Your turn now boy."
    "Medea performed the same biting action on you as she had done on Luna."
    play sound bite
    pause(2.0)
    c "Damn it that hurts."
    m "Itsh shuposshed to."
    play sound suck
    pause(8.0)
    m "AH! That feels so good..."
    play music caught2
    m "I can feel your blood moving around my body. It is working its magic."
    m "HAHAHAHAHAHA! The moment has come! No more shall I be spellbound to this flesh prison!"
    play sound magic
    show white
    pause(0.5)
    hide white
    hide mhap3
    show mhap2 at center:
        zoom 0.75
        xzoom .75 yzoom 1.25
        linear 1.0 xzoom 1.25 yzoom .75
        linear 1.0 xzoom .75 yzoom 1.25
        repeat
    hide cang
    hide lang
    show lang at right:
        zoom 0.75
    show cang at left:
        zoom 0.75
    l1 "[c], this is our chance! She is transforming. Cast the spell..."
    c "Okay. I hope I remember it correctly..."
    ws "{i}{b}Get ready to think fast and click fast!"
    $ spellb_score = 0
    label quiz1b:
        $ time = 7
        $ timer_range = 7
        $ timer_jump = 'quiz2b'
        show screen countdown
        menu:
            "SENIEN DE ZAR HVATA":
                jump quiz2b

            "SENNIEN DE ZAR HVATA":
                $ spellb_score += 1
                jump quiz2b

            "SENNIEN DE ZAR HVAATA":
                jump quiz2b

    label quiz2b:
        $ time = 7
        $ timer_range = 7
        $ timer_jump = 'quiz3b'
        show screen countdown
        menu:
            "KWAYAN MAYAKA LESNORA":
                $ spellb_score += 1
                jump quiz3b

            "KWAYANN MAYAKA LESNORA":
                jump quiz3b

            "KWAYAN MAYAKA LASNORA":
                jump quiz3b

    label quiz3b:
        $ time = 7
        $ timer_range = 7
        $ timer_jump = 'decisionb'
        show screen countdown
        menu:
            "UMARNA LETA HUNNEN":
                jump decisionb

            "UMARNA LITA HUNEN":
                jump decisionb

            "UMARNA LITA HUNNEN":
                $ spellb_score += 1
                jump decisionb

label decisionb:
    $ time = 0.42
    $ timer_range = 0
    if spellb_score == 3:
        jump sceneb19
    else:
        jump endb2


label sceneb19:
    c "I hope those were the right words..."
    l1 "We'll find out soon enough."
    play music finalhit
    play sound tele
    show white with Dissolve(0.4)
    hide white
    show gsly at right:
        xpos 0.6
        zoom 0.75
    pause(1.5)
    play sound tele
    show white with Dissolve(0.4)
    hide white
    show esmi at left:
        xpos 0.45
        zoom 0.75
    g "Well done, younglings."
    e "We knew you would succeed."
    g "We shall take over from here."
    e "Medea's reign comes to an end now..."
    hide cang
    hide lang
    hide gsly
    hide esmi
    show gang at left:
        zoom 0.75
    show eang1 at right:
        zoom 0.75
    play music battle2
    hide mhap2
    show mang2 at center:
        zoom 0.75
    m "YOU! YOU TWO ARE STILL ALIVE?"
    m "YOU STUPID, STUPID, GOOD-FOR-NOTHING WITCH! You shall pay for imprisoning me in this body..."
    e "We will see about that. Gerald...?"
    g "..."
    play sound atk1
    show white
    pause(0.18)
    hide white
    m "AHHH! Stop that!" with hpunch
    g "Do you feel the pain you have inflicted on others?"
    e "Do you understand the suffering you have caused?"
    hide mang2
    hide gang
    hide eang1
    show beach2
    hide beach3
    show beach3
    hide beach2
    show gang at left:
        zoom 0.75
    show eang1 at right:
        zoom 0.75
    show mhap3 at center:
        zoom 0.75
    m "HAHAHAHAHAHA! I do not care! I have almost transformed back to my original form."
    m "There is nothing you can do to stop me!"
    g "Hit her with all you've got Eliza!"
    play sound atk1
    show white
    pause(0.18)
    hide white
    mid "" with hpunch
    play sound atk2
    show white
    pause(0.18)
    hide white
    mid "" with hpunch
    play sound atk1
    show white
    pause(0.18)
    hide white
    mid "" with hpunch
    play sound atk2
    show white
    pause(0.18)
    hide white
    mid "" with hpunch
    play sound atk1
    show white
    pause(0.18)
    hide white
    mid "" with hpunch
    play sound atk2
    show white
    pause(0.18)
    hide white
    mid "" with hpunch
    hide gang
    hide eang1
    show gsad1 at left:
        zoom 0.75
    show esad1 at right:
        zoom 0.75
    g "It's not enough!"
    e "We need to hit her with more energy!"
    g "Hurry!!! She is almost free of her body!"
    m "BWAHAHAHAHA! All you do is futile! I am unstoppable."
    m "All of you will die soon..."
    m "You will soon be reunited with your stupid, worthless parents!"
    hide esad1
    show esad1 at left:
        xpos 0.1
        zoom 0.75
    show cang at right:
        zoom 0.75


label sceneb20:
    c "HOW DARE YOU CALL THEM WORTHLESS!"
    c "THEY WERE BRAVE AND AMAZING. UNLIKE YOU, YOU COWARDLY BITCH!"
    c "I SWEAR I WILL KILL YOU WITH MY OWN HANDS IF ITS THE LAST THING I DO!!!"
    play music hero
    hide cang
    play sound aura
    show white
    pause(0.69)
    hide white
    show cpow at right:
        zoom 0.75
    hide mhap3
    show mann2 at center:
        zoom 0.75
    hide gsad1
    show gsly at left:
        zoom 0.75
    hide esad1
    show esmi at left:
        xpos 0.1
        zoom 0.75
    c "SAY YOUR PRAYERS!"
    play sound dmg1
    mid "" with hpunch
    play sound dmg2
    mid "" with hpunch
    play sound dmg1
    mid "" with hpunch
    play sound dmg2
    mid "" with hpunch
    play sound dmg1
    mid "" with hpunch
    play sound dmg2
    mid "" with hpunch
    play sound dmg1
    mid "" with hpunch
    play sound dmg2
    mid "" with hpunch
    play sound dmg1
    mid "" with hpunch
    m "What is this power? How? This can't be!"
    g "Keep at it [c], you actually made her bleed..."
    e "We will keep hitting her with spells as well!"
    play sound dmg1
    mid "" with hpunch
    play sound atk1
    show white
    pause(0.18)
    hide white
    mid "" with hpunch
    play sound dmg2
    mid "" with hpunch
    play sound atk2
    show white
    pause(0.18)
    hide white
    mid "" with hpunch
    play sound dmg1
    mid "" with hpunch
    play sound atk1
    show white
    pause(0.18)
    hide white
    mid "" with hpunch
    play sound dmg2
    mid "" with hpunch
    play sound atk2
    show white
    pause(0.18)
    hide white
    mid "" with hpunch
    play music susp
    m "NOOOOO!"
    m "I cannot lose at the hands of a mere mortal like you!"
    m "{b}{size=+9}I AM MEDEA{/b}" with vpunch
    m "THE STRONEST BEING ON THIS PLANET."
    m "THIS IS NOT HOW IT ENDS..."
    m "THIS IS NOT..."
    m "{size=-3}HOW..."
    m "{size=-5}IT..."
    m "{size=-7}ENDS..."
    hide mann2 with Dissolve(3.6)
    jump endb3


label endb1:
    hide csly1
    show capo at left:
        zoom 0.75
    c "I really don't see any chance of her being Medea..."
    hide lann1
    show lsad1 at right:
        zoom 0.75
    l1 "Okay, I guess I am just being sceptical."
    c "Let's catch up with Angie before she feels something is wrong..."
    show ahap4 at center:
        zoom 0.75
    "The three of you make your way home."
    show doorway
    hide beach3
    hide ahap4
    hide capo
    hide lsad1
    show ahap4 at center:
        zoom 0.75
    a "You kids go wash yourselves, and I will give you something to eat."
    show ccon at right:
        zoom 0.75
    c "Can we just go to sleep, please? We are terribly tired."
    a "Oh of course. You both are adults now, you may do as you please."
    a "If you need anything, just come to my bedroom."
    c "Okay Angie, goodnight."
    hide black
    hide lneu1
    hide ghap
    hide path1
    hide cann
    hide ehap1
    show black
    hide doorway
    hide ahap4
    hide ccon
    "You and Luna retired to your rooms and fell asleep within minutes."
    "Inspite of all your plans to stay awake and on the lookout for any signs of Medea, fatigue overtook your resolution."
    show mroom3
    play music susp
    show cneu at center:
        zoom 0.75
    c "Dammit, I fell asleep. Hopefully Luna was able to stay awake and keep a watch."
    c "What time is it anyway?"
    c "..."
    c "It's almost midnight..."
    c "WAIT! WHY THE HELL IS MY WINDOW GLOWING?" with hpunch
    c "This is not good..."
    c "I should check on Luna..."
    play sound scream
    l1 "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"
    hide cneu
    show ccon at center:
        zoom 0.75
    c "Crap! LUNA! I'm coming..."
    play sound tele
    show white
    pause(0.5)
    hide white
    show mhap2 at right:
        zoom 0.75
    m "You are not going anywhere..."
    hide ccon
    hide ccon
    show csly2 at left:
        zoom 0.75
    c "Angie?! What the hell is going on?"
    m "HAHAHAHAHAHA! There is no Angie... There never was. Just good old Medea."
    m "You probably don't understand what I am saying..."
    m "Doesn't matter, your life will be over in a matter of seconds anyway."
    c "MEDEA?! You're Medea? OH MY GOD!!!"
    c "Luna was right!"
    c "WHERE IS LUNA! WHAT HAVE YOU DONE TO HER?"
    m "Luna is fine. Just suffering from a little hole in her neck situation. Nothing major."
    hide csly2
    play music endbad
    show ccry at left:
        zoom 0.75
    c "You killed her? You actually killed her?"
    c "YOU MONSTER!" with hpunch
    c "Why? Why? Why?"
    c "It's all my fault, I should have listened to Luna."
    c "{size=-9}It's all over... We failed."
    m "HAHAHAHAHAHA... Atleast you aren't completely stupid."
    m "It's almost poetic. Everyone in this family died at my hands."
    c "YOU?! YOU KILLED OUR PARENTS?"
    m "Of course. I had to ensure that you wouldn't get out of my grasp."
    m "I spent years finding the right pair of twins and then when I finally found you two, I knew that I had to keep you close to me."
    m "So I purchased your neighbour's house. He was very compliant... especially after he had no eyes..."
    m "And then all I had to do was orchestrate a simple car accident and Voila! The twins are in my hands."
    m "Isn't it brilliant?"
    m "And now it is finally time for me to shed this human carcass of mine..."
    m "Night Night [c]!"
    stop music
    play sound slash
    c "AGH!" with hpunch
    show blood:
        alpha 0.9
    hide ccry with Dissolve(1.0)
    hide mroom3
    play sound bleed
    pause(3.0)
    play sound suck
    hide mhap2
    show mhap3 at center:
        zoom 0.75
    m "AT LONG LAST!"
    m "I..."
    m "AM..."
    m "{b}{size=+9}FREE!"
    hide mhap3
    hide blood
    show red
    play sound go1
    "Medea, finally free of her human prison, wreaked havoc on the entire planet."
    "Nobody could lay a finger on her, and pretty soon, Earth became a living hell..."
    "The End."

    ws "This was ending 1 of 3."
    ws "Replay the game if you want to explore other potential ways that this could have ended..."
    hide red
    jump gameover


label endb2:
    c "..."
    c "Why is nothing happening?"
    l1 "You messed up. That wasn't the right incantation."
    hide path1
    hide cann
    hide ehap1
    hide black
    hide ghap
    hide lneu1
    c "Crap. You try..."
    l1 "Okay..."
    l1 "SENNIEN DE ZAR HVATA"
    l1 "KWAYAN MAYAKA LES..."
    stop music
    play sound slash
    pause(2.0)
    play sound bleed
    hide lang with Dissolve(0.69)
    c "WHAT...?"
    hide mhap2
    show mhap3 at right:
        zoom 0.75
    m "Did you seriously think that I would let you summon those good-for nothing mages?"
    hide cang
    show ccry at left:
        zoom 0.75
    play music battle2
    c "Luna? LUNA? TALK TO ME LUNA! SAY SOMETHING!"
    m "AWW! Don't cry [c]... She is dead... Nothing can be done now."
    m "She is gone to your parents, and very soon, so shall you."
    c "{size=-3}Lu...na...noooo..."
    m "It's almost poetic. Everyone in this family died at my hands."
    m "And now it is finally time for me to shed this human carcass of mine..."
    hide ccry
    show cann at left:
        zoom 0.75
    c "{size=-7}You bitch..."
    m "Huh? What was that?"
    c "I said..."
    c "{b}{size=+7}YOU BITCH!" with vpunch
    c "You will pay for this. I will avenge everyone."
    c "I. WILL. KILL. YOU."
    m "Don't make me laugh, what can you possibly do to me, a weak mortal like y..."
    hide mhap3
    show mhap3 at left:
        zoom 0.75
    play music hero
    hide cann
    play sound aura
    show white
    pause(0.69)
    hide white
    show cpow at right:
        zoom 0.75
    c "Let me show you what I can do."
    hide mhap3
    show mneu2 at left:
        zoom 0.75
    m "Come at me, nothing can defeat me."
    c "You asked for it!"
    play sound dmg1
    mid "" with hpunch
    play sound dmg2
    mid "" with vpunch
    play sound dmg1
    mid "" with hpunch
    play sound dmg2
    mid "" with vpunch
    play sound dmg1
    mid "" with hpunch
    play sound dmg2
    mid "" with vpunch
    play sound dmg1
    mid "" with hpunch
    play sound dmg2
    mid "" with vpunch
    play sound dmg1
    mid "" with hpunch
    hide mneu2
    show msad3 at left:
        zoom 0.75
    m "What is this power? How? This can't be!"
    c "That's right, you monster. How does it feel to be on the receiving end of pain for once?"
    m "NONONONONOONONONONONONONONONONONO! This is not supposed to happen!"
    c "SHUT UP!"
    play sound dmg1
    mid "" with hpunch
    play sound dmg2
    mid "" with vpunch
    play sound dmg1
    mid "" with hpunch
    play sound dmg2
    mid "" with vpunch
    hide msad3
    show mann2 at left:
        zoom 0.75
    m "Please stop! It actually hurts. What is this immense power? Why cannot I sense its source?"
    c "I will not stop till you cease to exist"
    play sound dmg1
    mid "" with hpunch
    play sound dmg2
    mid "" with vpunch
    play sound dmg1
    mid "" with hpunch
    play sound dmg2
    mid "" with vpunch
    m "AGHHHH! STOPPPPP!!!"
    m "I cannot lose at the hands of a mere mortal like you!"
    m "{b}{size=+9}I AM MEDEA{/b}" with vpunch
    m "THE STRONEST BEING ON THIS PLANET."
    m "THIS IS NOT HOW IT ENDS..."
    m "THIS IS NOT..."
    m "{size=-3}HOW..."
    m "{size=-5}IT..."
    m "{size=-7}ENDS..."
    hide mann2 with Dissolve(3.6)
    c "Where did she go?"
    c "Is it over?"
    c "Finally..."
    play music death
    hide cpow
    show ccry at center:
        zoom 0.75
    c "Oh Luna!"
    c "This is all so wrong."
    c "Just one twin left alive. It goes against nature."
    c "You promised me you wouldn't die!!!"
    c "Sigh. Nothing can be done now."
    c "I guess I should go home and bury her..."
    hide ccry
    show black with dissolve
    hide beach3
    ""
    "The next day, after digging a modest grave behind their house, you return to the ancient village where all this began."
    show village1 with dissolve
    hide black
    show csad at center:
        zoom 0.75
    c "I cannot summon Gerald and Eliza without Luna..."
    c "I really need to talk to them though."
    c "..."
    c "Woah! I can see Luna's name on the gravestone."
    c "Does this mean it is finally over?"
    play sound tele
    show white with Dissolve(0.4)
    hide white
    show gsad1 at right:
        zoom 0.75
    pause(1.5)
    play sound tele
    show white with Dissolve(0.4)
    hide white
    show esad2 at left:
        zoom 0.75
    g "Yes it does. The prophecy has been fulfilled..."
    c "Gerald! Eliza! How did you guys know I was here?"
    e "We can feel the magic permeating through the air."
    g "We know of your tragic loss."
    e "You have our deepest apologies."
    g "This was not supposed to be the way things happened."
    e "Alas, even magic cannot turn back time, so nothing can be done."
    g "You must move on and live your life holding on to her memories."
    e "It's not fair, but life never is."
    g "Live knowing that you killed Medea with your own hands, a feat no man has ever been able to do."
    c "But, where did I get that power from, I never understood it no matter how hard I tried."
    g "After Eliza's spell, everybody lost the ability to use magic."
    e "Magic was gone from the world, in a way."
    g "However, the prophecy linked your existence to Medea's and thereby, magic flowed through your veins."
    e "We think that you were directly using energy that you siphoned off Medea, basically weakening her to strengthen yourself."
    g "Which is why your attacks were so successful."
    e "Now that the prophecy has been fulfilled, magic will forever leave this world, never to be seen again."
    c "And what about you two?"
    g "We will vanish as well, for our existence is impossible without magic."
    e "You will lose your powers as well, and this village will cease to exist..."
    c "So, I guess this is it then?"
    g "Yes, young one. This is farewell."
    e "May fortune forever be in your favour, and may the tides of luck always be behind your back."
    c "Goodbye."
    hide gsad1 with Dissolve(1.0)
    hide esad2 with Dissolve(1.0)
    stop music
    play sound go2
    show grave with dissolve
    hide village1
    hide csad
    "Thus, you went on living, never forgetting the day you got a new life, yet lost everything."
    "It wasn't the ending you had in mind, but it was better than dying..."
    "The End."

    ws "This was ending 2 of 3."
    ws "Replay the game if you want to explore other potential ways that this could have ended..."
    hide grave
    jump gameover

label endb3:
    c "Where did she go?"
    g "I think that's the end of it..."
    e "I cannot feel her presence anymore."
    hide cpow
    hide esmi
    hide gsly
    show gsor at right:
        xpos 0.6
        zoom 0.75
    show erel at left:
        xpos 0.45
        zoom 0.75
    show lhap2 at right:
        zoom 0.75
    show chap2 at left:
        zoom 0.75
    l1 "Did we win?"
    c "Yes we did!"
    g "All thanks to you two."
    play music nar
    e "You have done what no man was ever able to do, defeat Medea herself."
    g "You are brave and diligent kids, and we are proud to have met you both."
    c "But, where did I get that power from, I never understood it no matter how hard I tried."
    g "After Eliza's spell, everybody lost the ability to use magic."
    e "Magic was gone from the world, in a way."
    g "However, the prophecy linked your existence to Medea's and thereby, magic flowed through your veins."
    e "We think that you were directly using energy that you siphoned off Medea, basically weakening her to strengthen yourself."
    g "Which is why your attacks were so successful."
    e "Now that the prophecy has been fulfilled, magic will forever leave this world, never to be seen again."
    l1 "And the tombstone? What will happen to its engraving?"
    g "Why dont you come along with us and take a look?"
    show village1 with dissolve
    hide path1
    hide cann
    hide mhap2
    hide ehap1
    hide black
    hide ghap
    hide lneu1
    hide beach3
    hide chap2
    hide erel
    hide gsor
    hide lhap2
    show ghap at right:
        xpos 0.6
        zoom 0.75
    show ehap2 at left:
        xpos 0.45
        zoom 0.75
    show lhap2 at right:
        zoom 0.75
    show chap2 at left:
        zoom 0.75
    c "WOW! It says Medea now!"
    g "Thus proving the prophecy has been fulfilled."
    e "You are now free of its binding."
    g "No more are you spellbound..."
    e "This world will finally prosper without the evil shadow of Medea cast upon it."
    c "And what about you two?"
    g "We will vanish as well, for our existence is impossible without magic."
    e "You will lose your powers as well, and the village will cease to exist..."
    c "So, I guess this is it then?"
    g "Yes, young ones. This is farewell."
    e "May fortune forever be in your favour, and may the tides of luck always be behind your back."
    c "Goodbye."
    l1 "Goodbye Gerald and Eliza, thank you for everything."
    hide ghap with Dissolve(1.0)
    hide ehap2 with Dissolve(1.0)
    ""
    show mroom1 with dissolve
    play music endhome
    hide village1
    hide lhap2
    hide chap2
    show chap1 at left:
        zoom 0.75
    show lhap1 at right:
        zoom 0.75
    c "You have no idea how relieved I am to put all of that behind us."
    l1 "It feels like I aged decades in that one night."
    c "How's your arm?"
    l1 "Healing, nothing major. What about you?"
    c "Completely healed! When I powered up, it somehow fixed my arm as well!"
    l1 "It sucks that you lost your powers."
    c "That is a sacrifice I am willing to give in exchange for being alive and kicking."
    l1 "True. And [c]?"
    c "Hm?"
    l1 "Thanks for not dying. I don't know what I would have done if I would have lost you."
    c "The feeling is mutual sis."
    l1 "What now?"
    c "First we sleep and then we eat. I don't want to plan any further than that..."
    l1 "Sounds like a plan!"
    show mroom2 with dissolve
    hide mroom1
    hide chap1
    hide lhap1
    "Everything was back to normal. Both Luna and you had been through a lot..."
    "But you still had each other and your entire lives to look forward to."
    "That's all that mattered."
    "The End."

    ws "This was ending 3 of 3."
    ws "Replay the game if you want to explore other potential ways that this could have ended..."
    hide mroom2
    jump gameover
