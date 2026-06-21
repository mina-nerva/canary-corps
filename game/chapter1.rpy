define Digital = Character("???", color="#ffc75f", namebox_style="namebox_right", callback=name_callback, cb_name = "???")
define Voice = Character("Voice", color="#abceb7", namebox_style="namebox_v", who_size = 40)
define Other = Character("Other Voice", color="#c7baa2", namebox_style="namebox_ov", who_size = 40)

define Soldier = Character("Soldier", color="#abceb7", namebox_style="namebox_s", who_size = 40)

define slowfade = Fade(1.0, 1.0, 1.0)
define slowdissolve = Dissolve(1.0)

label chapter1:
    # "Chapter 1"
    "ETHERIDGE ASSET EXPORT - CYCLE 408 - 00:47"
    play music "minesong1stretchedA.ogg"

    scene bg transport with slowdissolve

    "The cargo hold of the military helicraft is dimly lit. Among the shaded figures of cargo and weapons, a humanoid machine waits, buckled in for takeoff."

    show 928 right dull with slowdissolve
    
    "It gazes at a supply crate strapped to the floor."
    n "..."
    "Human voices chatter through the radio."

    Voice "Yep. Yeah. It's on board already."
    Voice "The other one's giving us trouble, but we'll have it ready shortly. You know how these things can be."
    Other "Fuckin' Canaries, man."

    "{i}Click.{/i}" #TODO click
    "The chatter cuts."
    show 928 shut
    "Outside the vehicle, a door rattles, boots shuffle, and shouting voices fill the air. The machine labeled “928” looks toward the door, now alert."

    Voice "Move along!"
    Other "Open up the door. I'll hold it in place."

    "A husky, digital voice laughs."

    Digital "What, am I heavy? Sorry the company gave me such a fat ass– OW!" #TODO thump

    "A heavy thud is punctuated by the hiss and whine of servos opening the back of the helicraft."
    "The scene outside floods in."
    
    show cg boot with dissolve
    window hide
    $ renpy.pause()

    window show
    "A group of uniformed soldiers stand over a machine laying prone, the same model as 928."
    "One has their boot planted on the machine's head, while the other, knee digging into her back, forces her arms up. She locks eyes with 928, wearing a wicked grin."

    Soldier "Get up!"

    "The machine tries to catch her balance as the soldiers haul her up by the arms. "

    hide cg boot

    "The soldiers haphazardly shove her through the vehicle's door, and she lands face-down with a grunt." #TODO thump

    Soldier "Have a nice trip."

    "The soldiers step off the loading platform. The cargo door rises, reducing the outside light to a sliver before it locks shut."
    
    show 637 left sneer with slowdissolve
    "The other machine, still laying on the floor, looks up towards 928."


    show 637 wink
    s "Hey, new girl. What was {i}their{/i} fuckin' problem, huh?"

    show 637 sneer
    "637 sneers, props her back up against a nearby supply crate, and settles on the floor."
    show 928 dull
    "928 gives her an empty stare."
    show 637 surprise
    "The engine jolts to life, nearly knocking 637 over, but she catches herself on the crate's straps."

    show 928 open
    show 637 smile
    n "You aren't buckled in."

    show 928 dull
    show 637 open
    s "Really? I didn't notice."

    show 637 smile
    "She lifts herself up and takes a wide-legged seat on the crate."
    
    show 637 sneer
    s "So, what, you're my new partner, then?"

    show 637 smile
    show 928 open
    n "I am Canary Unit 928, assigned to extraction on Helka-112 for Etheridge United Companies."

    show 637 neutral
    show 928 dull
    "637 blinks."

    show 637 scowl
    s "Yeah, duh. We're on the same job. On the same heli. What's with the formal opening?"

    show 928 open
    show 637 neutral
    n "It's standard protocol."

    show 928 shut
    s @ sincopen "Ah, right. New blood. How many times you been deployed so far?"

    show 637 smile
    show 928 open
    n "Sixteen."

    show 928 shut
    show 637 sneer
    s "No shit, really? And hardly a scratch, 'cept your face. Pretty good."

    show 928 dullsmile
    n "I always complete missions as ordered. Commander Vogan values my performance."

    show 637 scowl
    s "Yeah. I'm sure she does."

    show 637 neutral
    "637's sneer fades into a dull scowl. She glances around the cramped vehicle."

    show 928 open
    n "...Your prior actions indicate an unstable persona. You {i}are{/i} aware force would not be necessary if you complied, correct?"

    show 928 dull
    "928's expression remains blank. 637 sighs, back to looking at her."

    show 637 scowl
    s "Oh, and here I was thinking those guys beat the shit out of me 'cause I'm so pretty.{w} I bet that observational skill will come in {i}real{/i} handy on this mission."
    show 637 squint
    show 928 dullsmile
    "A vacant, polite smile takes shape on 928's face."

    show 928 dullgrin
    n "Glad to hear you're considering cooperative action during this expedition.{w} It would be regrettable to cause undesirable outcomes in the field."

    show 928 dullsmile
    s scowl "You're a real bundle of joy, aren't ya?"

    show 637 neutral
    show 928 bummed
    "637 stands up and cracks her knuckles."

    show 637 drool
    s "I'm bored. Let's listen in on those dorks up front."

    show 928 bummed
    show 637 sneer
    n "What?"

    show 928 bummed
    "Her brow furrows. 637 leans towards her, holding herself up by the wall above 928's head."

    s "C'mon, we have nothing better to do."

    show 928 bummed
    show 637 smile
    n "We should remain on standby until we arrive at our–"

    show 637 wink
    s "Tch! Think about it like, maybe they're talking about this job. This is just, I dunno, {i}retrieving vital information{/i} for the mission or whatever."

    show 928 open
    show 637 smile
    n "I'm certain if it was vital information, we would be briefed properly..."

    show 928 bummed
    "Glancing around the drab, cluttered hold they're confined in, she trails off and looks down."

    n "..."

    show 637 sneer
    "637 lets out a slight snicker."

    s "You're curious, aren't you? What do you even know about this job?"

    show 928 mad
    "637's new partner glares at her."

    show 928 open
    n "We are on a pathfinding expedition to assist in the extraction of a recently discovered Stellisite signal detected in–{nw}"

    show 928 mad
    show 637 hurtless
    s "Yeayeayea. I know that much. C'mon."

    show 928 bummed
    show 637 neutral
    "She taps 928's shoulder and moves towards the far end of the vehicle, near the drivers."

    show 637 sneer
    s "Trust me, these dweebs say the most entertai– I mean, most {i}mission vital{/i} shit."
    show 637 wink
    s "Humor me."

    show 928 bummed
    show 637 sneer
    "928 stares at 637, unenthused. She'll put up with it for now."
    show 637 neutral
    window hide
    show gray overlay darker zorder(9) with dissolve
    # possibly replace this with big textbox
    window show
    a """Through the wall, one voice is deep, the other squeaky. 928 recognizes them as the soldiers that handled 637.

    \"...I mean, Christ, you couldn't pay me to go in there first. Deposits just get deeper and deeper.{w}
    First it's the warehouses, then the plant... at some point it's gotta stop being worth it, right? Even with Canaries, they've been pulling up less and less.\"

    \"Shut up, man. A gram of Stellisite's worth more than every organ in your extended family. We won't be done here till the place is picked clean.{w}
    Just be thankful you aren't a Canary down there getting beheaded by a Laskey drone.\"

    \"Point taken.\"

    \"I just hope those two things do their job right. Neumann's set to make another push in the east mines soon. If they malfunction, it's our asses.\"

    \"Fuck, I hate dealing with them. Can you believe the way that thing was talking back to me earlier?{w}
    And the other one just freaks me out. All it does is stand there, silently staring. I don't know if it's {i}worse{/i}, but it gives me the creeps.\"

    \"If you ask me, the mouthy one is toward the end of its rope. Management won't decommission them unless they're {i}really{/i} defective, though.{w}
    Fuckers are penny-pinching so hard that they'll still send fragmented Canaries on missions.{w}
    Who knows, maybe {i}it'll put itself down{/i} in front of its sister. Save us a bullet or two.\""""
    show 637 scared
    a "Laughter."
    # TODO bunny glitch????
    nvl clear
    hide gray overlay darker

    show 928 dull
    
    n "..."
    show 637 neutral

    "928 gazes at a supply crate on the floor. 637 shakes her head and leans closer."

    show 637 sneer
    s "Aww, they think we're sisters."
    show 637 drool
    s "Heheh... hot."

    show 928 bummed
    show 637 sneer
    "928 squints at her partner."

    show 928 mad
    n "...You still aren't buckled in."
    stop music fadeout 5.0
    show black with dissolve

    "END TRANSMISSION 1"

    $ renpy.pause()

    jump chapter2