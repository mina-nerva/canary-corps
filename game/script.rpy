# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("928", color="#f07575", image = "928", namebox_style = "namebox_left", callback = name_callback, cb_name = "928")
define nl = Character("928", color="#f07575", image = "928", namebox_style = "namebox_right", callback = name_callback, cb_name = "928")
define na = Character(kind = nvl, callback = name_callback, cb_name = "928")
define s = Character("637", color="#ffc75f", image = "637", namebox_style = "namebox_right", callback = name_callback, cb_name = "637")
define sa = Character(kind = nvl, callback = name_callback, cb_name = "637")

define Deep = Character("Soldier", color="#abceb7", image="soldiera", namebox_style="namebox_s", who_size = 40, callback = name_callback, cb_name = "soldiera")
define Squeaky = Character("Soldier", color="#c7baa2", image="soldierb", namebox_style="namebox_s", who_size = 40, callback = name_callback, cb_name = "soldierb")

define c = Character("Commander", color="#d42929", image="vogan", namebox_style = "namebox_long", who_size = 37, callback = name_callback, cb_name = "vogan")
define cq = Character("???", color="#d42929", image="vogan", namebox_style="namebox_right", callback = name_callback, cb_name = "vogan")

define a = Character(kind = nvl, callback = name_callback, cb_name = None)
define narrator = Character(callback = name_callback, cb_name = None)

layeredimage 928 right:
    at sprite_highlight('928')
    zoom 0.4
    pos (0.25, 1.1)

    group base:
        attribute d default
        attribute damage1
        attribute damage2
        attribute combat

    group head:
        attribute shut default
        attribute open
        attribute mad
        attribute pissed
        attribute dullgrin
        attribute awkward
        attribute dull
        attribute fluster
        attribute dullsmile
        attribute smile
        attribute shine
        attribute grit
        attribute yelp
        attribute hurt
        attribute plead
        attribute pleadgrin
        attribute bummed
        attribute despair
        attribute alert
        attribute shock
        attribute dizzy1
        attribute dizzy2
        attribute dizzy3
        attribute dizzy4
        attribute process
        attribute hopen
        attribute hshut
        attribute hgrit
        attribute rage
        attribute haze1
        attribute haze2
        attribute haze3
        attribute haze4
    
    group fx:
        attribute blush
        attribute distress

layeredimage 928 left:
    at sprite_highlight('928')

    zoom 0.4
    pos (0.63, 1.1)

    attribute base default

    group head:
        attribute shut default
        attribute open
        attribute process
        attribute dull
        attribute grit
        attribute bummed
        attribute dullsmile
        attribute dullgrin

transform moreright:
    xalign 0.5
    xanchor -0.5
    yalign 0.0
    yanchor -0.1

transform moreleft:
    xalign 0.5
    xanchor 1.5
    yalign 0.0
    yanchor -0.1

transform moredown:
    xalign 0.5
    xanchor 1.175
    yalign 0.0
    yanchor -0.3

layeredimage 637 left:
    at sprite_highlight('637')
    zoom 0.4
    pos (0.75, 1.1)

    group base:
        attribute d default
        attribute combat

    group head:
        attribute neutral default
        attribute mad
        attribute scowl
        attribute wink
        attribute smile
        attribute elated
        attribute hurt
        attribute hurtless
        attribute bummed
        attribute sad
        attribute sadless
        attribute sneer
        attribute drool
        attribute scared
        attribute surprise
        attribute sincere
        attribute squint
        attribute process
        attribute open
        attribute sincopen
        attribute hopen
        attribute hshut
        attribute hgrit
        attribute hgrin
    attribute damage
    attribute blush

layeredimage dog:
    zoom 0.4
    pos (0.5, 1.15)

    attribute base default
# layeredimage 637 distort:
#     pos (0.75, 1.1)

#     group base:
#         attribute b1 default
#         attribute b2
#         attribute b3
    
#     group head:
#         attribute h1 default
#         attribute h2
#         attribute h3

layeredimage soldierb:
    at sprite_highlight('soldierb')
    zoom 0.4
    pos (0.20, 1.10)
    group face:
        attribute frown
        attribute grin
        attribute open
        attribute shut default

layeredimage soldiera:
    at sprite_highlight('soldiera')
    zoom 0.4
    pos (0.40, 1.05)
    group face:
        attribute angry
        attribute angry2
        attribute grin
        attribute open
        attribute shut default

layeredimage vogan:
    at sprite_highlight('vogan')
    zoom 0.4
    pos (0.67, 1.0)
    attribute body default

    group head:
        attribute anger1
        attribute anger2
        attribute frown default
        attribute grimace
        attribute pout
        attribute smile
        attribute sneer
        attribute creepy
    
    group fx:
        attribute sweat
        attribute pinch
        attribute null default null

image mental:
    "images/@2.5/mental1.png"
    pause 0.7
    "images/@2.5/mental2.png"
    pause 0.7
    "images/@2.5/mental3.png"
    pause 0.7
    repeat

image mentalbg:
    "images/m1.jpg"
    pause 0.05
    "images/m2.jpg"
    pause 0.05
    "images/m3.jpg"
    pause 0.05
    "images/m4.jpg"
    pause 0.05
    "images/m5.jpg"
    pause 0.05
    repeat
# The game starts here.


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    jump chapter1

    show 928 right
    "928"
    n dizzy1 "dizzy"
    n dizzy2 "aaa"
    n dizzy3 "aaaaa"
    n dizzy4 "aAAAAAAAA"
    n process damage1 "aioseimoasdimo"
    n damage2 "fuck, my arm"
    show 637 left
    s "asdasd"
    s squint "iisdiaosd"
    s damage "aosdooa owch"
    s -damage "ok all better"

    scene bg transport
    with slowfade

    "a gay ass machine sits in a stupid vehicle"
    "it looks like this btw:"

    show 928 right dull
    with slowdissolve

    n "..."

    "theres a sound outside."

    v1 "fuck"
    v2 "you"

    s "i boned your gay mom, fuck da troops-YOWCH!!!!"

    show cg boot temp # TODO

    "why is she like this?"

    hide cg boot temp # TODO

    "she landed on her face"

    show 928 right alert

    s "damn! wth!!"

    show 928 right shut

    show 637 left sneer
    with slowdissolve

    "weird girl gets up"

    show 637 left wink
    show 928 bummed

    s "sup cutie"

    show 637 neutral
    show 928 open
    n "uh hi im a gay nerd"

    show 637 sneer
    show 928 shut
    s "i can tell"

    show 637 neutral
    show 928 open
    n "mom's very proud of me"

    show 637 scowl
    show 928 dull
    s "i hate your mom"

    show 637 sneer
    s "wanna see a trick?"
    
    "she does a trick"

    show 637 wink
    show 928 dullsmile
    s "pretty sick, right?"

    show 928 dullgrin
    show 637 neutral
    n "sure."

    show 928 dull
    show 637 sneer
    s "lets spy on boys."

    show 928 mad
    n "wtf no"

    show 637 drool
    s "cmon dork"

    show 928 fluster
    n "eep!"

    show gray overlay
    with slowdissolve

    v1 "i have negative feelings towards the lgbt community."

    v2 "same lol"

    v1 "these dumb robots better do their dumb job right or im gonna go away"

    v2 "its ok bro im sure nothing bad will happen in a cave today"

    v2 "also i think robots should kill themselves"

    v1 "AMEn!!!!!!!!!!!!!!!!!!!!!!"

    hide gray overlay
    with slowdissolve

    show 928 dull
    show 637 sneer
    s "wow they think we're sisters"

    show 637 drool
    s "#weird"

    n "..."

    "END CHAPTA 1"

    scene bg surface
    with slowfade

    show soldiera
    show soldierb
    show 928 right
    show 637 left
    with slowdissolve

    "wow its cramped out here huh"

    show soldierb open
    v1 "go get some rocks ladys"

    show soldiera angry2
    show soldierb grin
    v2 "yeah!"

    show soldiera angry
    show 928 open
    n "ok"

    show 928 shut
    show 637 mad
    s "..."

    show 928 blush
    show soldierb open
    v1 "go away queers"

    scene bg manufacturing

    show 637 left 
    show 928 right open

    n "yapyapyapyap"

    show 928 shut
    show 637 scowl
    s "yapyapyapyap wwowwww i felll off a cliff time to go turn on the power"

    show 637 mad
    show 928 mad
    s "youre really stupid nerd"

    show 928 pissed
    n ">:(((( im not"

    show 637 sneer
    s "oh yeah?"

    show 928 shock
    n "eep!"

    show cg power temp

    "she pushes her down and shit"

    n "staaaahp i admit it!!!! im stupid!!! uncle uncle uncle"

    s "hah!"

    "emd of totally real demo"


    # This ends the game.

    return
