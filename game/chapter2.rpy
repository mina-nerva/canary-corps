label chapter2:
    

    "HELKA-112 SURFACE - CYCLE 408 - 05:15"

    scene bg surface with slowfade

    
    a """The helicraft comes to a landing on a strip of asphalt.{w}
    928 and 637 begin their final equipment checks in silence. Hatches, panels, internal machinery, all clear.

    The door opens and frigid air rushes into the cargo hold. The two soldiers stand outside, helmets obscuring their features.{w}
    637 trails behind 928 exiting the vehicle. The deep voiced soldier speaks as she passes.

    \"Hey. No trouble this time.\"

    They give 637 a push on the shoulder to emphasize the point."""
    play music "howivemissedintroslowed.ogg"
    a """Neither of the Canaries pay much attention to the other as they take in the massive, looming manufacturing facility they're being escorted towards.

    The building's crown of long-dead exhaust chimneys are framed by the low, encroaching clouds of dust that encase Helka-112's surface.
    
    Fluorescent flood lights line the exterior wall, glinting off the flurry of dust particles descending from the sky."""
    nvl clear

    show 637 left at moreright
    show 928 left
    with dissolve

    "Near the entrance, the soldiers stop and turn towards the Canaries."
    show soldiera
    show soldierb
    with dissolve

    "One holds a tablet in their hands. The other, holding a large rifle, begins to address them."
    show soldiera open
    Deep "Verify mission status prior to entry."
    show soldiera shut
    show 928 open
    nl "Sir. Canary units 928 and 637 are to chart a path for confirmation and extraction of a recently discovered Stellisite source wavelength..."
    nl "...originating from a subterranean vein approximated to be on the 9th internal layer of the Laskey Solutions mining operation."
    show 928 shut
    show 637 -squint
    show soldiera open
    Deep "Good."
    Deep "Verify mapping protocol."
    show 928 open
    show soldiera shut
    nl "Sir."
    show 928 dull
    "For a moment, 928's eyes go blank."
    show 928 process
    nl "Ping sent..." #TODO beep
    nl open "Ping received. Zero percent packet loss."
    nl "Mapping protocol active. Uploads to be committed at intervals permitting EM-storm clearance."
    show 928 shut
    show soldiera open
    Deep "Good. And you?"

    "The soldier turns to 637, who had been staring off to the distant terrain."
    show 637 squint
    "Unhurried, she meets his gaze. She doesn't say anything."
    show soldiera angry
    show soldierb frown
    "The unobscured portion of the soldier's face 637 turns sour and impatient, and he shifts the rifle in his hands."
    show soldiera shut
    show soldierb open
    "Suddenly, he lowers his guard, talking to the other Etheridge soldier on closed comms. He seems upset."
    "The other soldier taps on the screen, and explains something to him."
    show soldiera open
    show soldierb shut
    Deep "...Really?... "
    show soldiera shut
    "They nod."
    "He gives the other soldier a long look before his mic clicks back onto frequency."

    show soldiera angry2
    Deep "...Nevermind, you're clear to go."

    show soldiera shut
    "The Canaries turn to leave them, but 928 hesitates for a moment, looking at 637."
    "What was that all about?"
    show soldierb grin
    "The less talkative soldier steps towards them and{nw}"
    show 928 grit
    extend " shoves 928 hard with their palm." #TODO thump
    show soldierb shut
    show 928 bummed
    "She staggers forward."


    show soldierb open
    Squeaky "Hey. I know you're {i}her{/i} pet, or whatever?"
    show soldierb grin
    Squeaky "But don't even think about coming back empty-handed, or I'll personally mark you for decommission."

    show soldierb shut
    show 928 dullsmile
    "928 steadies herself."
    show 637 mad
    "637's eyes go wide. She glares at the soldiers as best she can through their heavy visors."

    show 928 dullgrin
    nl "Sir. Understood."

    show 928 dull
    show 637 squint
    "She starts moving again."
    hide 928 with dissolve
    "637's gaze flits back and forth between her partner and the gun in the other soldier's hands."
    
    "Finally, 637 turns to follow 928."
    stop music fadeout 5.0
    window hide
    hide 637
    hide soldiera
    hide soldierb
    with dissolve
    
    window show
    a "The two make their way toward the facility. 637 tries to get a look at 928's face, but her rigid pace doesn't give her the chance."
    a "They arrive at the bombed-out doorway and enter."

    
    show bg manufacturing with fade

    # larger textbox?
    play music "minesong1.mp3"

    a """Dozens of towering, limp robotic arms line the path that 928 and 637 take.{w}
    The cavernous building is only populated by rusted-over shipping containers, mechanized warsuits and long-abandoned vehicles.

    Pieces of dead automatons and concrete chunks litter the floor.{w}
    It's clear this facility was more recently a war zone than any hub for manufacturing."""
    # TODO bunny glitch????
    nvl clear
    window hide
    show 637 left
    show 928 right dull
    with dissolve
    window show
    s mad "Man, fuck those guys!"
    s mad "I don't understand how you can take that shit lying down."
    show 637 squint

    "637 kicks a bolt laying on the ground and sends it flying. It clangs off some nearby mech remains, sending an echo down the empty halls." # clang TODO
    "928 grimaces at the sound."

    n @ mad "I don't understand why you're so consistently abrasive."

    show 637 sneer 

    "637 cackles."

    s @ drool "Listen, those assholes might act tough, but they can't really do shit to us. They need us.{w} Pissing them off is basically free entertainment."
    show 928 bummed 
    s @ wink "You should've seen their faces in the hangar. Priceless."
    show 928 shut 
    "928 walks ahead of 637 and puts on a stern expression."
    show 637 squint 
    n @ mad "That sort of {i}fun{/i} could get you reformatted. Carrying out my function is rewarding enough."

    s hurtless "Yeah, that sounds about right."
    s scowl "It's sweet that you wanna be their pet.{w} But they don't really see you as anything more than an appliance, you know.{w} Just as replaceable."
    show 928 bummed 
    show 637 squint 
    "The jab makes 928 pause for a moment. 637 doesn't react."

    s @ hurtless "Anyways, if they {i}were{/i} going to reformat me, they would have done it already."
    s @ sneer "Etheridge is spread so thin as it stands! Besides, they've got me on a leash as much as you."

    "She taps a glowing spot on her back."

    s @ sneer "Couldn't get rid of it if I tried! Haha."
    show 637 neutral

    n open "...Speaking of your tracker. It won't fail during the mission, will it?{w} Beyond regular wear, I noticed it's been tampered with."
    show 637 bummed 
    show 928 shut

    "637 sighs."

    s hurtless "Huh. Yeah, well... Maybe it's a bit dinged up, but it's not gonna break."
    s sneer "Sturdy as hell, and, uh... You know the rules. No tracker means no report, and then, y'know."
    s @ wink "KABOOM!{w} ...Haha."

    n @ open "...The Asset Loss Protocol, you mean.{w} I don't imagine they would let you out on duty in a state where it would activate unexpectedly."

    s @ scowl "Yeah, exactly. Bad for the bottom line."

    show 637 squint 

    "There's a lull in the conversation."
    "As the two head through the deserted battlefield of a building, 928 continues to examine 637's beat-up tracker."

    n @ open "Um... Unit 637?"

    s @ mad "What."
    show 928 bummed 

    "The sharpness in 637's voice delays 928's question by a few seconds."

    n @ open "What kind of role was your previous assignment?"
    show 928 shut

    s @ sneer "Oh, all kinds of stuff. I keep getting assigned to new commanders. "
    show 637 drool
    extend "Seems everyone wants a piece of me. "
    show 637 neutral
    "928 glances at her partner."

    s @ hurtless "...What about you?"

    n @ open "Subterranean navigation has been my specialty for some time now."

    s scowl "Hm. Is that so? If we weren't out here right now, I'd have a hard time seeing that."
    s sneer "Retrieval requires adaptability. Lateral thinking.{w} Those don't seem like your strong suits, protocol nerd."
    show 637 squint

    n bummed "..."

    n @ dullgrin "Well. Commander Vogan views my previous retrieval performances as satisfactory. I'm sure you'll come to appreciate her approval as well, once we complete our descent."

    s @ hurtless "Ugh. You mean that grouchy asshole with the dark hair? Yeah, can't say I'm looking forward to reporting back to her."
    s wink "What, does she like you{nw}"
    show 928 fluster
    extend " or something?"
    show 637 squint

    n @ shock "She has–"
    show 928 bummed
    "928 clears her throat."

    n @ mad "Commander Vogan has provided me with strong, beneficial supervision and feedback for all of my missions."

    s scowl "...Wait. You're telling me she's kept you with her the {i}whole{/i} time you've been active? {w}They don't rotate you around at all?"
    show 928 fluster blush
    show 637 sneer
    "637 turns around and catches a fleeting look of embarrassment on 928's face."

    n bummed "..."

    "637 faces the path ahead and chuckles to herself."

    s @ drool "'Strong, beneficial supervision,' huh?"
    
    # larger textbox?
    window hide

    hide 928 right
    hide 637 left
    with dissolve

    window show

    a """The pair's conversation dies as they reach an overhang looking down on another quadrant of the facility.{w}
    Below, military-industrial debris is scattered across conveyor belts and shipping containers.

    The power is out, and, unlike the ground-floor, there aren't any windows to provide illumination.{w}
    637 strides ahead of 928, right towards the metal barrier rails."""

    a "928 notices the rails sink with a creak. She shouts."#TODO creak

    a "\"63–\""
    nvl clear#TODO do we need this?

    a "928 fails to finish shouting her partner's identifier.{w} The overhang collapses under the Canaries' weight and swings perpendicular to the rest of the floor."
    
    show gray overlay with dissolve

    a "928 and 637 plunge to the ground beneath."
    nvl clear

    "{i}CRASH!{/i}" #TODO crash

    s "AUGH!"

    "928 lands hard, her metal body dealing more damage to the factory equipment below than it does to her."
    #end big textbox

    show 928 right alert with dissolve
    "She gets up from the crater of debris, and pats at the equipment on her head and torso. "
    show 928 shut
    extend "Ruling out any damage, she turns to look for her companion."
    "637 lays on the ground nearby in a similar pile, eyes shut, gritting her teeth."

    n open "Unit 637."
    show 928 shut

    "637 opens her eyes."

    s "Fuck... One sec."

    "928 offers a hand."
    show 637 left hurt with dissolve
    "After a beat, 637 takes it. She stands up, swaying. "
    extend "928 attempts to inspect 637's equipment by sight."
    show 637 squint
    n @ open "You seem to be in pain, 637. Did you disable your pain dampeners?"

    s @ hurtless "Ugh... I dunno– what do you think?"

    "928 stares at her blankly."

    s @ scowl "Yes. The answer is yes."
    show 637 squint

    n @ open "Why would you do that? You should only be checking for damage {i}after{/i} an incident, not before one. It's not tactically sensible."

    
    show 637 sneer
    "Through a groan, 637 smirks at 928."

    s @ sneer "It's... none of your business... {nw}"
    show 637 hurt
    extend "ugh... {w}"
    show 637 hurtless
    extend "what I prefer..."
    show 637 squint

    n @ mad "You {i}prefer{/i} feeling the full impact of a ten-meter fall?"

    s @ hurtless "I prefer feeling something over nothing at all. Helps a girl feel more alive, y'know? "
    #show 637 wink
    extend wink "And besides. I'm a tough cookie. I can take it."
    show 637 neutral

    n @ open "I don't follow. Feeling something? Our sensors already process the required amount of physical sensory data."
    show 637 sneer
    "637 chuckles."

    s @ hurtless "Yeah, the required minimum, sure. But when you pick and choose what you're letting in, you're not really living {i}all the way{/i}, y'know?"
    show 637 squint

    n @ mad "I still don't get it. That sounds insane."
    show 928 bummed

    s @ drool "You wouldn't, unless you gave it a shot. Highly recommend trying it sometime."
    hide 928 right
    hide 637 left
    with dissolve

    a "Despite her confusion, 928 turns to continue walking.{w} 637 follows, brushing the dust off herself as she goes."

    scene bg elevator off with fade

    a "They approach a room built into the wall of the building.{w} Inside, a decrepit metal shutter blocks a rectangular platform."
    nvl clear
    show 928 right
    show 637 left
    n @ open "Elevator. No electricity."

    s @ open "So, what, we pry the doors open and drop down?" #open sprite

    n open "These doors are usually inoperable due to flipped breakers.{w} If we can locate the power station nearby, it should be easy enough to reactivate. "
    extend "And that would let us use the elevator, too. Much safer."
    show 928 shut

    s @ scowl "Buzzkill."
    s sneer "Why don't you go look for that while I start–"

    "While 637 walks toward the large mechanical door, 928 traces the power lines up the wall and around the structure.{w} Finally, her sight lands on a small box, up in the mezzanine. "

    show 637 surprise
    n @ open "Found it."

    s @ mad "Okaaaay, never mind then!"
    stop music fadeout 5.0


    scene bg breaker off with slowfade
    show 928 right
    show 637 left
    with dissolve

    "The metal staircase leading to the power supply is narrow.{w} 637 shadows 928 up the steps."

    s @ hurtless "Y'know, for someone who's been out on so many missions, you're still such a stickler for the rules.{w} You said you were deployed, what, thirteen times?"
    play music "howivemissedyou.mp3"
    n @ mad "Sixteen."
    show 928 bummed

    s @ scowl "Sixteen missions of climbing through shit and rubble.{w} I've never seen a Canary go through that much and still act like they're a brainless robot."
    extend sneer " And for what? So your favorite boss can give you some {i}feedback{/i}?"
    s "Is she {i}that{/i} good to you?"
    extend @ drool " Or, are you just that fucking desperate?"
    show 928 dull
    show 637 squint

    "They crest the stairwell into the cramped power room.{w} On the far wall, a control panel sits below a window to the greater interior of the facility."

    n "..."

    "928 strides to the controls, fiddling with various switches, not responding to 637's comments."

    s @ scowl "No, seriously, I'm super curious about what makes a girl like you tick."
    show 928 mad
    "928 turns around and faces her partner, glowering."

    n @ pissed "Okay, for starters, we're not girls!"

    show 637 drool
    "637 grins."
    show 637 sneer

    n pissed "We're not people. We're just facsimiles of people. Any human traits we have are just a means to an end."
    n "Simulated senses and self-preservation protocols are just there to make us more useful. These bodies are tools, engineered for a purpose, and I'm just trying to fulfill it."
    n grit "I'm not desperate. I'm not anything!"

    show 928 mad

    "637 steps towards her."

    s drool "Aw, that's cute."
    show 928 alert
    extend " Tell me, how exactly does {i}Vogan{/i} value such a loyal, hard-working Canary like you?"

    n fluster "Vo-"
    n pissed "C-Commander Vogan provides helpful critiques of my efficiency and issues me back into the field–"
    n shock "Ah!"
    show 928 yelp
    "Her partner shoves her. 928 lands on the control panel.{w} The abrupt force leaves her stunned. 637 leans in close."#TODO thump
    window hide

    show cg power with dissolve
    $ renpy.pause()
    window show

    s "God, you're so {i}pathetic{/i}."

    "928 blushes without knowing why.{w} She stammers out a retort."

    n "Wh–...{w} No! You– I–"

    s "Shut up. I know your type. {w}You put on a flat, vacant face while they order you around. {w}You keep the filters on around the clock, curled up in the back of your own brain."
    s "Pretending you're nothing but a drone for the higher-ups.{w} You let it all drift right by you, but you can't help hoping for an ounce of recognition, praise, thanks, anything from those shitheads."
    s "I know {i}she{/i} dangles it right in front of you. But she won't give you any.{w} Why would she? No need to thank a {i}tool{/i}."

    n "Ngh..."

    s "You poor thing."
    s "Pretend all you want, but you can't hide from me. {w}I know some part of you wants to drop the barrier, to feel {i}something{/i}, just a little bit."

    "She grabs 928 by the collar and stares her down.{w} 928 can't quite manage to look her in the eyes. She's lightheaded."
    "Their faces pull closer."

    s "{i}There{/i} it is.{w} Deep under all those layers of programming, but they still left it in you.{w} They left it in me too, sis."
    s "And if your {i}commander{/i} isn't gonna do anything about it, then maybe I'll–"
    scene bg breaker on
    stop music

    "928's hand slips, and throws the breaker."

    show 928 right alert
    show 637 left surprise
    with dissolve

    "With an audible {i}click{/i}, sterile strip lights switch on and wash out the red hue of the backup light.{w} A siren sounds in the distance. " #TODO click
    extend "Outside the booth, the whir of revived motors makes clear that the power has returned. "
    show 928 -blush
    show 637 squint
    "Despite herself, 637 whips around in surprise. 928 gets up. The room goes quiet, the tension awkward and unresolved."
    show 928 bummed
    "After a moment, 928 pierces the silence."

    n "..."
    extend @ open "The... The electromagnetic-storm is clear. We need to report our progress.{w} Including that fall we sustained."
    show 928 dull


    "637 turns and gawks at her. 928 gains back her composure in a matter of seconds."

    n @ dullgrin "We should rest and upload. Residential layers are often dangerous, and before descending we should ensure we're optimally prepared."

    s @ scowl "Uh, yeah.{w} Whatever, alright."
    window hide

    hide 637 left
    hide 928 right
    with dissolve
    
    play music "satellite.mp3"

    window show
    a """928 and 637 sit apart from each other against a wall, plugged into the newfound electricity in the facility quadrant.

    928, finishing her upload, turns to check on her partner.{w}
    637 is preoccupied, looking up and out at the room, keeping watch.{w}
    928 looks over the scene. The facility stands like a monument to the dead industry that was once inside.

    In the machinery below, she catches a set of robotic assembly arms grasping at the air.{w}
    Conveyor belts below it deliver nothing but debris, and as the arms fail to catch the mess, it piles onto the ground beneath.{w}
    Without a purpose and without someone to repair it, how long can it run?

    The two canaries sit, side-by-side.

    They still have work to do."""
    
    window hide
    stop music fadeout 5.0
    show black with dissolve

    "END TRANSMISSION 2"
    nvl clear

    $ renpy.pause()

    jump chapter3