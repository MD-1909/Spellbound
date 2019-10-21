# The script of the game goes in this file.

#This is to define the splashscreen which is displayed at the start of the game before displaying the main menu.
image splash1 = "logo.jpg"
image splash2 = "title.jpg"
label splashscreen:
    play music "music/Disclaimer.mp3"
    scene black
    with Pause(0.5)
    show splash1 with dissolve
    with Pause(3)
    show splash2 with dissolve
    with Pause(1)
    "{b}{size=+5}DISCLAIMER{/size}{/b}{p=1}This is a work of fiction. Any likeness to any person living or dead is purely coincidental."
    "This is an original game. In case of re-distribution, credits to the developer must be given."
    "Unauthorised re-distribution is not permitted."
    "Credits for art assets are mentioned in the 'About' section of the Main Menu"
    "The developer will not be held liable for any misuse of this software."
    "Have Fun!"
    with Pause(1)
    return

#Setting the timer for timed menus
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.042), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

init:
    $ timer_range = 0
    $ timer_jump = 0

#Declaring characters used by this game. The color argument colorizes the name of the character.
define ws = Character("WhytShadow", who_color="#696969")
define a = Character("Angie", who_color="#ff3333")
define m = Character("Medea", what_font="type9.ttf", who_color="#fa0202")
define g = Character("Gerald", who_color="#6596e8")
define e = Character("Eliza", who_color="#75dbaa")
define c1 = Character("Chris", who_color="#ffff00")
define l1 = Character("Luna", who_color="#c42f9f")
define u = Character("Unknown", who_color="#ffffff")
define mid = Character(None,
                            what_size=20,
                            what_outlines=[(3, "#000000", 0, 0)],
                            what_layout="subtitle",
                            what_xalign=0.5,
                            what_text_align=0.5,
                            window_background=None,
                            window_yminimum=0,
                            window_xfill=False,
                            window_xalign=0.5,
                            window_yalign=0.5)
define narr = Character(None, kind = nvl)

#Defining aliases to all the sprites for future ease
#male_dark_hair
image cang = im.Scale("sprites/male_dark/md_angry.png", 325, 520)
image cann = im.Scale("sprites/male_dark/md_annoyed.png", 325, 520)
image capo = im.Scale("sprites/male_dark/md_apologetic.png", 325, 520)
image ccon = im.Scale("sprites/male_dark/md_concerned.png", 325, 520)
image chap1 = im.Scale("sprites/male_dark/md_happy1.png", 325, 520)
image chap2 = im.Scale("sprites/male_dark/md_happy2.png", 325, 520)
image cneu = im.Scale("sprites/male_dark/md_neutral.png", 325, 520)
image csad = im.Scale("sprites/male_dark/md_sad.png", 325, 520)
image csly1 = im.Scale("sprites/male_dark/md_sly1.png", 325, 520)
image csly2 = im.Scale("sprites/male_dark/md_sly2.png", 325, 520)
image cpow = im.Scale("sprites/male_dark/md_power.png", 325, 520)
image ccry = im.Scale("sprites/male_dark/md_cry.png", 325, 520)
#female_dark_hair
image lang = im.Scale("sprites/female_dark/fd_angry.png", 300, 550)
image lann1 = im.Scale("sprites/female_dark/fd_annoyed1.png", 300, 550)
image lann2 = im.Scale("sprites/female_dark/fd_annoyed2.png", 300, 550)
image lhap1 = im.Scale("sprites/female_dark/fd_happy1.png", 300, 550)
image lhap2 = im.Scale("sprites/female_dark/fd_happy2.png", 300, 550)
image lneu1 = im.Scale("sprites/female_dark/fd_neutral1.png", 300, 550)
image lneu2 = im.Scale("sprites/female_dark/fd_neutral2.png", 300, 550)
image lneu3 = im.Scale("sprites/female_dark/fd_neutral3.png", 300, 550)
image lsad1 = im.Scale("sprites/female_dark/fd_sad1.png", 300, 550)
image lsad2 = im.Scale("sprites/female_dark/fd_sad2.png", 300, 550)
#male_mage
image gang = im.Scale("sprites/male_mage/mm_angry.png", 450, 500)
image gcur = im.Scale("sprites/male_mage/mm_curious.png", 450, 500)
image ghap = im.Scale("sprites/male_mage/mm_happy.png", 450, 500)
image gneu1 = im.Scale("sprites/male_mage/mm_neutral1.png", 450, 500)
image gneu2 = im.Scale("sprites/male_mage/mm_neutral2.png", 450, 500)
image gsad1 = im.Scale("sprites/male_mage/mm_sad1.png", 450, 500)
image gsad2 = im.Scale("sprites/male_mage/mm_sad2.png", 450, 500)
image gsly = im.Scale("sprites/male_mage/mm_sly.png", 450, 500)
image gsor = im.Scale("sprites/male_mage/mm_sorry.png", 450, 500)
image gsus = im.Scale("sprites/male_mage/mm_suspicious.png", 450, 500)
#female_mage
image eang1 = im.Scale("sprites/female_mage/fm_angry1.png", 500, 600)
image eang2 = im.Scale("sprites/female_mage/fm_angry2.png", 500, 600)
image ehap1 = im.Scale("sprites/female_mage/fm_happy1.png", 500, 600)
image ehap2 = im.Scale("sprites/female_mage/fm_happy2.png", 500, 600)
image eneu1 = im.Scale("sprites/female_mage/fm_neutral1.png", 500, 600)
image eneu2 = im.Scale("sprites/female_mage/fm_neutral2.png", 500, 600)
image erel = im.Scale("sprites/female_mage/fm_relieved.png", 500, 600)
image esad1 = im.Scale("sprites/female_mage/fm_sad1.png", 500, 600)
image esad2 = im.Scale("sprites/female_mage/fm_sad2.png", 500, 600)
image esmi = im.Scale("sprites/female_mage/fm_smirk.png", 500, 600)
image esus1 = im.Scale("sprites/female_mage/fm_suspicious1.png", 500, 600)
image esus2 = im.Scale("sprites/female_mage/fm_suspicious2.png", 500, 600)
#female_pink_hair
image aang1 = im.Scale("sprites/female_pink/fp_angry1.png", 400, 500)
image aang2 = im.Scale("sprites/female_pink/fp_angry2.png", 400, 500)
image aann1 = im.Scale("sprites/female_pink/fp_annoyed1.png", 400, 500)
image aann2 = im.Scale("sprites/female_pink/fp_annoyed2.png", 400, 500)
image ahap1 = im.Scale("sprites/female_pink/fp_happy1.png", 400, 500)
image ahap2 = im.Scale("sprites/female_pink/fp_happy2.png", 400, 500)
image ahap3 = im.Scale("sprites/female_pink/fp_happy3.png", 400, 500)
image ahap4 = im.Scale("sprites/female_pink/fp_happy4.png", 400, 500)
image aneu1 = im.Scale("sprites/female_pink/fp_neutral1.png", 400, 500)
image aneu2 = im.Scale("sprites/female_pink/fp_neutral2.png", 400, 500)
image asad1 = im.Scale("sprites/female_pink/fp_sad1.png", 400, 500)
image asad2 = im.Scale("sprites/female_pink/fp_sad2.png", 400, 500)
image asad3 = im.Scale("sprites/female_pink/fp_sad3.png", 400, 500)
#female_pink_hair_evil
image mang1 = im.Scale("sprites/female_pink/fpe_angry1.png", 400, 500)
image mang2 = im.Scale("sprites/female_pink/fpe_angry2.png", 400, 500)
image mann1 = im.Scale("sprites/female_pink/fpe_annoyed1.png", 400, 500)
image mann2 = im.Scale("sprites/female_pink/fpe_annoyed2.png", 400, 500)
image mhap1 = im.Scale("sprites/female_pink/fpe_happy1.png", 400, 500)
image mhap2 = im.Scale("sprites/female_pink/fpe_happy2.png", 400, 500)
image mhap3 = im.Scale("sprites/female_pink/fpe_happy3.png", 400, 500)
image mhap4 = im.Scale("sprites/female_pink/fpe_happy4.png", 400, 500)
image mneu1 = im.Scale("sprites/female_pink/fpe_neutral1.png", 400, 500)
image mneu2 = im.Scale("sprites/female_pink/fpe_neutral2.png", 400, 500)
image msad1 = im.Scale("sprites/female_pink/fpe_sad1.png", 400, 500)
image msad2 = im.Scale("sprites/female_pink/fpe_sad2.png", 400, 500)
image msad3 = im.Scale("sprites/female_pink/fpe_sad3.png", 400, 500)

#Defining aliases to backgrounds for future ease
image black = "bg/black.jpg"
image white = "bg/white.jpg"
image grey = "bg/grey.jpg"
image red = "bg/red.jpg"
image blood = "bg/blood.png"
image grave =  "bg/grave.jpg"
image beach1 = "bg/beach1.jpg"
image beach2 = "bg/beach2.jpg"
image beach3 = "bg/beach3.jpg"
image park = "bg/park.jpg"
image path1 = "bg/path1.jpg"
image path2 = "bg/path2.jpg"
image path3 = "bg/path3.jpg"
image road1 = "bg/road1.jpg"
image road2 = "bg/road2.jpg"
image mroom1 = "bg/room11.jpg"
image mroom2 = "bg/room12.jpg"
image mroom3 = "bg/room13.jpg"
image froom = "bg/room2.jpg"
image kitchen = "bg/kitchen.jpg"
image door = "bg/doorway.jpg"
image village = "bg/village1.jpg"
image square1 = "bg/village21.jpg"
image square2 = "bg/village22.jpg"
image square3 = "bg/village23.jpg"

#Defining aliases to music and sound effects for future ease
#music (*use fadeout 1*)
define audio.battle1 = "music/Battle1.ogg"
define audio.battle2 = "music/Battle2.ogg"
define audio.battle3 = "music/Battle3.ogg"
define audio.beach1 = "music/Beach1.mp3"
define audio.beach2 = "music/Beach2.mp3"
define audio.caught1 = "music/Caught1.wav"
define audio.caught2 = "music/Caught2.ogg"
define audio.confront = "music/Confrontation.mp3"
define audio.death = "music/Death.mp3"
define audio.defeat = "music/Defeat.ogg"
define audio.end = "music/End.mp3"
define audio.endbad = "music/EndBad.mp3"
define audio.endhome = "music/HomeEnd.mp3"
define audio.farewell = "music/Farewell.mp3"
define audio.finalhit = "music/FinalHit.ogg"
define audio.hero = "music/Hero.mp3"
define audio.nar = "music/Narration.mp3"
define audio.path = "music/Path.ogg"
define audio.plan = "music/Planning.mp3"
define audio.reveal = "music/Reveal.ogg"
define audio.sly = "music/Sly.mp3"
define audio.start1 = "music/Start1.mp3"
define audio.start2 = "music/Start2.mp3"
define audio.susp = "music/Suspense.mp3"
define audio.village1 = "music/VillageEnd1.mp3"
define audio.village2 = "music/VillageEnd2.mp3"
#sound
define audio.atk1 = "sounds/Attack1.mp3"
define audio.atk2 = "sounds/Attack2.mp3"
define audio.aura= "sounds/Aura.mp3"
define audio.bite = "sounds/Bite.mp3"
define audio.bleed = "sounds/Bleed.mp3"
define audio.dmg1 = "sounds/Damage1.mp3"
define audio.dmg2 = "sounds/Damage2.mp3"
define audio.door = "sounds/Door.mp3"
define audio.glass = "sounds/Glass.mp3"
define audio.go1 = "sounds/Gameover1.mp3"
define audio.go2 = "sounds/Gameover2.mp3"
define audio.knock = "sounds/Knock.mp3"
define audio.magic = "sounds/Magic.mp3"
define audio.scream= "sounds/Scream.mp3"
define audio.slash= "sounds/Slash.mp3"
define audio.suck= "sounds/Suck.mp3"
define audio.tele = "sounds/Teleport.mp3"

# The game starts here.
label start:
    stop music #Stops the music that was playing at the main menu.
    scene black with dissolve #Shows a background. This uses a placeholder by default,
    ws "Hello there! Thank you for deciding to play this game."
    ws "It is my pleasure to present to you, Spellbound."
    ws "Just a few tips before we begin..."
    ws "Save frequently. Use the mousewheel to scrollback in case you missed something."
    ws "Press H to hide the textbox. Press ESC to enter the menu."
    ws "And most importantly, make wise choices. Some of them have consequences."
    ws "For more keyboard and mouse shortcuts, refer to the 'Help' section of the Main Menu"
    ws "This game has quite a few sound effects and cool background tracks, so turn up your device volume or just plug in some headphones!"
    ws "That's all from my side."
    ws "{b}{size=+10}ENJOY!{/size}{/b}"

    show cneu at right:
        zoom 0.7
    show lneu1 at left:
        zoom 0.7

    "Do you want to play as the boy or the girl?"
    menu:           #Presents player with a choice.
        "Boy":
            jump boy_name

        "Girl":
            jump girl_name

label boy_name:
    hide lneu1
    hide cneu
    show chap1 at center with dissolve:
        zoom 1
    "Enter your name, leave blank for default ({i}Chris{/i})"
    python:
        mname = renpy.input(_("What's your name?"))
        mname = mname.strip() or "Chris"
    define c = Character("[mname]", who_color="#ffff00")
    jump boy_start

label girl_name:
    hide cneu
    hide lneu1
    show lhap1 at center with dissolve:
        zoom 1
    "Enter your name, leave blank for default ({i}Luna{/i})"
    python:
        fname = renpy.input(_("What's your name?"))
        fname = fname.strip() or "Luna"
    define l = Character("[fname]", who_color="#ff00ff")
    jump girl_start

label gameover:
    stop sound
    show image("credits.jpg")
    play music end
    mid ""

return # This ends the game.
