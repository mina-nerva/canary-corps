define Base = Character("Base", color="#abceb7")

label chapter3:

    scene bg surface with slowfade
    window show
    a """Transmission from Etheridge base.

    \"Assume Neuman-Keere is pursuing the Stellisite signal by now.{w}
    They know where you're headed. Interception must be avoided at all costs.\"

    \"Proceed through the subterranean residential district to Stellisite processing.\"
    
    \"Over.\""""
    window hide

    show black with dissolve
    play music "minesong1stretchedC.ogg"
    
    "MANUFACTURING - CYCLE 408 - 13:09"
    scene bg elevator on with fade
    nvl clear
    window show
    # show 928 right TODO im not sure if she should ever appear while nvl mode is up
    # with dissolve

    # larger textbox?

    a """928 stands alone in the elevator, prodding at the dashboard next to the shutter.{w}
    The power might have returned, but they won't be moving anytime soon. The controls are secured with credentials.{w}
    A metal plate is pried open beneath the reader, and she analyzes the innards.

    She's been at it for at least half an hour.
    
    637 remains outside the elevator, still resting up. That, or she's avoiding 928 on purpose.{w}
    928 mutters to herself in frustration.

    She removes one black wire from a circuit board in the panel, and inserts its exposed end into a different spot on the circuit.

    The lights in the elevator flicker.{w}
    Playing an approving tone, the display on the controls glows green.""" #TODO beep zzt
    window hide

    show 928 right shine with dissolve
    window show
    nvl clear
    "928's face lights up."

    show 637 left
    # with slowdissolve
    s @ hurtless "How's it going, partner? Finally got this thing working?"
    show 928 fluster
    "Still beaming from the successful hack, 928 whips her head toward 637's voice."

    n alert "!"

    n @ awkward "...Hello, Unit 637. All things are, um- proceeding as planned."
    show 928 fluster

    show 637 sneer
    show 928 blush
    "637 smirks at her partner, who begins to blush."

    s @ wink "What's wrong? Got me on your mind?"

    n @ shock "N-no, I was just... {w}I finished overriding these controls, so I was just about to... alert you."

    show 928 -blush
    s @ hurtless "You hacked it?"

    show 928 bummed
    "928 blinks."

    n @ open "Yes, I disabled Laskey's floor access restrictions. Routine task."

    s sneer "No shit! I'm used to these things always being busted open, or hot-wired already. {w}That means nobody's gone down this way, huh?"
    show 637 smile

    "She leans against the frame of the elevator in a languid stance."

    n @ open "We are the first."

    s @ wink "I'm impressed! You're more clever than I thought, dork."

    show 928 dull
    "928 looks toward the dashboard."

    n dullgrin "It's just protocol. Any Canary would be able to manage this much."
    show 637 neutral
    n "Regarding the mission, did you receive the message from base?  Due to the approach of Neuman Keere, we cannot afford to waste any more time in this location. {w}It would be suboptimal."

    show 928 dull
    show 637 squint

    "637's expression darkens. She approaches the dashboard."

    s @ hurtless "Wow. And for a second there, I almost forgot you were a machine."

    show 928 bummed
    "She pokes 928's temple. 928 turns to stare at her, frustrated."

    show 928 mad
    s @ scowl "What? I thought your whole thing was being a tool. Fulfilling your purpose, and all that. You suddenly have a problem with it?"

    n @ open "No."

    s @ sneer "So you're acting all strict because you wanna impress the commander?"

    n @ pissed "No! It's-"

    show 928 alert
    s @ wink "Then that means you're doing all this for lil' old meeee~?"
    show 637 sneer

    show 928 fluster blush
    "928 puts her face in her hands and groans."
    "She presses a spot on the elevator's control panel."
    show 928 bummed

    "637 grins at her."
    s drool "I'm so flattered."

    "The shutter closes, and the descent begins."
    stop music fadeout 5.0
    window hide

    scene bg city with slowfade
    play music "cavesong.mp3"

    window show
    a """The two exit an underground cargo tunnel, the pathway spilling out into what appears to be a residential area.{w}
    On either side of the road, emergency-lit buildings with rubble at their feet stretch up to the top of a massive cavern.

    Numerous windows dot each of them, most lacking panes.{w}
    Chunks have been blasted out, possibly from surface conflict, making the separation between one building and the next blurry.

    As they proceed, they notice cameras.{w}
    They hang from every wall, corner, and doorway. Small, but present.{w}
    Even more are suspended on electricity poles, although few still stand upright, toppled like trees in a storm.

    Despite the film of dust that coats their lenses, their presence hangs like a thousand empty eyes, through which anyone could be watching.

    The panopticon might be dead, but it certainly remains effective.

    As they progress, debris covers more and more of the street.{w}
    637 watches their backs, following close behind 928, who moves forward with purpose.{w}
    They follow the path of the cargo road that runs between the buildings.

    Upon rounding a corner, a steep, jagged slope of boulders comes into view down the road.{w}
    It stretches above the rooftops of the buildings adjacent to it."""
    window hide
# TODO bunny glitch
    show 637 left
    show 928 right
    with dissolve
    window show
    n @ open "The ceiling must have collapsed."
    nvl clear
    s @ scowl "Shit. I bet we made a wrong turn. Should've trusted my gut about taking a detour..."

    n @ open "Negative. The foundry is this way. This road was designed to move material up from the mine and the foundry above it, so following it will lead us to its root. This rubble is impassable, though."

    s @ hurtless "Okay, so what do we do then? Climb over it? Push some rocks and hope we don't get flattened?"

    n @ open "We'll have to find a way through the complexes."

    s @ scared "Uh, look, I'm all for going in there, but if this place hasn't been properly cleared out yet..."

    show 637 squint

    n @ mad "Then we keep our eyes open for drones. The retrieval squadron is responsible for clean-up. Our duty is to find a path."

    "928 takes the lead as she steps into one of the buildings through a waist-high window. 637 shadows her."

    s hurtless "Right. Yeah. Okay."
    window hide

    # larger textbox?
    scene bg corridor with slowfade
    window show
    a """The corridors of the residential building are narrow, and difficult to see in.{w}
    Doorways line both walls, many closed, others spilling into the darkness of the vacant rooms behind them.

    928 keeps an eye on each opening they pass. 637 examines the cameras, which crane down on sight-lines of each hall.{w}
    So many systems in this complex are destroyed or cut-off, but power distribution is never consistent.
    
    928 boldly rounds a corner."""
# TODO bunny glitch
    show 637 left
    show 928 right
    with dissolve

    s @ scowl "Hey, careful with the cams. You never know who you're putting on a show for."
    show 637 squint
    nvl clear

    n @ open "A show?"

    s @ hurtless "Like– ah, never mind. Just, keep an eye out, alright?"

    # larger textbox?
    show 637 -squint

    "She nods, appreciative. They stay to the walls to minimize their presence.{w} 637's gait never quite syncs up with 928's, but she stays close behind."
    show 928 mad
    "They bump into each other a few times. 928 tries her best to ignore it.{w} As they move past a camera, 928 stops beneath it to slice its data-line."
    
    "637 sidles up to her and leans her arm up on the wall. {nw}"
    show 928 fluster
    extend "The contact flusters 928 again.{w} She looks away before 637 can notice."

    show 928 dull
    s sneer "Y'know, we {i}are{/i} alone. "
    extend @ wink "If we, say, stopped for a little bit once we get outta here, the higher-ups wouldn't know."

    n mad "Why would we do that?"

    s @ drool "I dunno. In case you wanted to continue where we left off upstairs. In the breaker room."
    show 637 smile

    n fluster "I- Wh-"
    n @ pissed "We can't mess around. We need to focus on the mission!"
    stop music fadeout 5.0
    show 928 mad
    show 637 sneer
    "928 glares at 637 as she snips a camera wire. 637 snickers and steps past her."
    show 928 -mad

    s wink "My bad! Just trying to lighten the..."

    show 637 squint
    "637 stops in place."

    s surprise "..."

    show 928 alert
    "Something shifts in the darkness ahead."

    s hgrit "SHIT!"

    show 928 hgrit
    play music "minesong3.mp3"

    "The combat visors on their heads snap down into place."
    show 637 combat at moreright
    show 928 combat at moreleft
    with dissolve
    window show
    show graynvl
    with dissolve
    a "A jet-black, four-legged mechanical creature, now revealed in infrared, pounces at 637.{w} She scrambles to activate the rifle in her arm."
    show dog
    with dissolve
    a "No time.{w} She blocks its protruding jaw with her weapon, its teeth sparking and scraping against it."
    show 928 hshut
    a "It's a Laskey security drone. 928 springs into action."
    a "She dashes toward 637 and stabs the attacker with her blade." #TODO shing!
    hide dog
    with dissolve
    a "Oil spurts out of its back."
    # TODO bunny glitch? maybe not
    hide graynvl
    nvl clear
    s hgrin "Thanks!"
    show 637 hshut
    "There's motion down the hall."

    n @ hopen "One more on your six!"
    with None

    window show
    show graynvl

    a "637 readies her gun."
    show dog with dissolve
    a "Another drone lunges from the shadows, this time towards 928."
    show 637 hgrit
    a "637 fires and hits it mid-air." # TODO bang!
    hide dog with dissolve
    a "The mechanical beast careens off-course, colliding with the wall and painting it with an inky fluid.{w} Three more shots and it stops moving."# TODO bang!
    hide graynvl

    n @ hopen "You can't depend on your rifle in close-quarters!"
    nvl clear
    s @ hgrin "Hey, speak for yourself. It killed that one just fine!"
    show 637 hshut
    # larger textbox!
    show 928 hgrit
    window show
    show graynvl
    with dissolve
    show dog with dissolve
    a "The onslaught continues. 928 moves with inhuman speed.{w} She swings at one drone jumping at her, slicing it through the torso." #TODO shing!
    a "637 shoots one in the head and follows it up, impaling it through the back with her blade."# TODO bang!
    hide 637 left with dissolve

    a "One more drone rushes 928. It leaps."
    a "She attempts to skewer it, but it dodges. The motion leaves her open, and the assailant takes advantage. {w}It kicks off the wall and hurtles directly for her neck."
    a "It misses by a matter of inches, and latches onto the front of her torso like a vise.{w} The fiber alloy composing her skin strains and bends, starting to tear open.{w} She flails, trying to pull it off."
    a "Stumbling backward, her feet fail to make contact with the ground, sending her falling through a doorway."
    hide 928 right
    #TODO crack
    a "The tracker box on 928's back cracks hard against the floor. "
    show gray overlay darker zorder(9)
    extend "For a moment, she blinks out of consciousness. "
    extend "Audio processors ringing, she regains her sight."
    hide gray overlay darker with dissolve
    a "The force of the landing tore the drone away, but now it's approaching her again."
    show 928 right combat hurt at moreleft with dissolve
    a "She props herself up against a wall. Everything's heavy. "
    show 928 grit
    extend "Not wasting a moment, the machine jumps to attack. 928 positions her arms to intercept it."

    hide dog #TODO bang!
    stop music fadeout 5.0
    a "A bang.{w} The drone goes flying, and collapses in a pile on the other side of the room.{w} Another shot neutralizes it."
    show 637 left hgrit combat at moreright
    with dissolve
    a "928 sees 637 standing above her, gun still aimed at the attacker.{w} They both heave, staring at each other."
    hide graynvl
    # TODO bunny glitch possible
    s scared "..."
    nvl clear

    n yelp "..."

    s d "That was the last one."
    show 637 bummed
    n hurt "..."

    

    s hurtless "You good?"
    hide 928 right
    hide 637 left
    with dissolve
    play music "howivemissedyouB.ogg"
    a "928 continues staring. Her eyes are wide, mouth slack. "
    extend "637 sees that something's off with her chest. She kneels down over 928 to inspect."
    window hide
    show cg repair with dissolve
    $ renpy.pause()
    window show
    show graynvl

    a "\"Fuck, you're–\"" #TODO we dont do this anywhere else, idk how to handle it PROB FINE
    a "928 grabs 637 by the collar and collides her forehead with 637's.{w} It stuns 637 as 928 begins biting at the synthetic flesh next to her mouth."
    a "928 presses their lips against each other. 637's eyelids sink."
    a "The kiss is dry."
    a "637 tries to match the force 928 is exerting, then pauses, grabs 928's head and frees herself. She speaks cautiously."

    a "\"What the fuck?\""
    
    a "928 groans and slumps against the wall. There's a long black mark on her chest."
    extend " 637 leans in to examine the damage."
    a "The skin surrounding the jagged gash frays outward. Blue coolant bubbles out onto her abdomen."

    a "\"Shit, you're wounded.\""

    a "637 glances at 928's limp head. {w}Her pupils are fluttering and unfocused, the corners of her eyes moist with fluid."
    a "Her mouth hangs open still, but her jaw starts to tense and twitch."
    a "637 reaches for a compartment on her back containing her repair kit.{w} 928 sputters fragments of sentences."
    hide graynvl

    s "Hey. {w}Stay with me here, okay?"
    nvl clear
    n "...m-missionn...{w}can't...{w}I...{w}c-c-commander...{w}f-f-format..."
    show graynvl
    a """637 pauses, losing focus as she's readying the materials.{w}
    She recalls how 928 handled the fall from that overhang on the surface, then looks at her currently distorted face.{w}
    It clicks. She must've shut off the dampeners.

    \"You're in shock.\"

    At her words, 928 manages a couple gazes at 637, but her eyes remain wild and flitting.{w}
    Even if 637 asked her to flip them back on, she's in no state to make sense of the request.{w}
    She mutters, delirious.

    \"...I...I...{w}wh-wh-wha–\"

    \"Shhh.{w} I got you. It's alright.\""""
    

    a """637 places the supplies for the impromptu surgery on the ground.{w}
    She takes 928 by the shoulders and positions her face-up on her lap.

    928 whimpers at the movement, and starts to concentrate on the sight of 637's face above her.{w}
    637 closes the distance and kisses 928's forehead. This isn't going to be easy.

    \"I need you to hold still for me, okay?\"

    928 exhales with a low grunt.{w}
    637 grabs a small knife, and raises it perpendicular to 928's wound.{w}
    She carefully slices toward the cut. 928 yelps.

    The synthetic fiber gives way as 637 leans in to assess the intensity of the damage.{w}
    She pulls back with a relieved sigh.

    \"It's shallow. You're lucky. Not {i}too{/i} much internal damage.{w} I am going to need to seal a few things up, though.\"

    She takes a small rubber cylinder, and pulls off a small strip from inside it, exposing an adhesive layer. 

    Inside 928's chest, a coolant line has come loose. She's starting to overheat.{w}
    Her pain sensors won't calm down until the line and the tear above it are sealed.

    Leaning in over 928's chest, she takes a deep breath.

    \"Brace.\"

    637 reaches inside, aiming for the deeper half of the coolant line, which has tumbled lower into her internal wiring and mechanics.{w}
    She pulls it up, and gives it a light tug to get it back into place.

    \"AUGH!\"

    928's addled neural system screams danger.{w}
    She thrashes her limbs.{w}
    637 takes her free hand and pins 928 by the shoulder.

    \"Stop moving.{w} I need you to endure it for a little longer.\"

    928 stops moving.{w}
    Her extremities are still shaking, but her torso is steady.{w}
    The effort causes her to moan.

    \"Here we go.\"

    637 resumes the operation, grabbing the other loose end.{w}
    She fits it to the repaired side of the coolant line, sealing it tight.{w}
    928 shudders, doing her best to keep still.

    Without pausing, 637 picks up the repair tape, and uses the knife to slice off a sufficient patch for sealing the wound from the inside.{w}
    Using the cut she made prior, she pushes the tape beneath the fiber alloy, sticky side first.{w}
    She presses it together to the inside of 928's skin, removing her hand before finishing.

    928 squeaks.

    \"That's it. Good girl.\"

    928's vision focuses up at 637. Her partner spans her mind.

    \"Just one more thing and you'll be all fixed. Understand?\"

    The pause in procedures allows 928 to collect her mind. She replies to 637 with a slow, deep nod.{w}
    She sees 637 grab an aerosol spray bottle. After a beat, 928 puts it together in her head.{w}
    It must be the patch spray. She recalls being trained to use it to cauterize–

    The deafening hiss of the spray breaks 928's train of thought. Her chest is ice-cold.

    In seconds, it heats up. {w}Hotter. And hotter. {w}It burns. Then it's an inferno.

    928 opens her mouth without making a sound.{w} She sees white. Her thoughts are cut."""
    play music1 "howivemissedintroslowed.ogg"
    a "There is only fire."
    window hide
    show black with slowdissolve

    stop music fadeout 5.0
    

    nvl clear
    # larger textbox!

    a """The heat ebbs. 928's neural pathways flood with artificial serotonin. Her breathing slows.{w}
    637 sets a hand on the side of her face. Her fingers make gentle contact with 928's cheek.

    Resting in her partner's lap, eyes closed, thoughts start to form in her head once more.{w}
    The sensation brings to mind the ways she had been touched by others.

    The way she'd been handled.{w}
    Rough as they could be, they never came close to damaging her.

    Eventually, she had realized that focusing on her own sturdiness in those moments made them drift by faster.{w}
    The same sturdiness that enables her to fulfill her purpose.

    Now, 637 holds 928 like she's fragile enough to fall apart. It disconcerts her.{w}
    Something like her, purpose-built for industrial durability, being treated so gently.
    
    637 strokes her face.{w} 928 shivers.{w} The thoughts fracture.

    "Mmnn..."

    She blushes. That noise was her? It's embarrassing.{w}
    Had she been making noises like that the whole time 637 repaired her?{w}
    It's unprofessional.{w}
    Why should a Canary be feeling like this, in the middle of a mission, no less?{w}
    She clenches her jaw, mouth shut. What would her commander think if she saw–

    637 pets her partner's face again. 

    "Nnnhhh..."

    637 is studying the blushing thing in her lap in amazement.

    Taking the lead on the repair was straining.{w}
    Under normal circumstances, she would recoil at being the responsible partner.{w}
    As she watches 928 rest, an unfamiliar rush fills her head, leaving her clear-eyed and shivering.

    It's a distinct feeling, not like the euphoria that brings 928 to writhe against her.{w}
    637 has been in her position.{w}
    She knows the dizzying, cloudy bliss of surrender.
    
    Now, she's on the other side.{w}
    It's power. For once, she's in control. It feels unnervingly good.
    
    She centers herself. 928's body is still shivering.{w}
    Her mind needs time to settle down, and right now, she needs someone to help her through this.

    637 examines her crystalline face.{w} 928's eyes aren't open, but her expression shifts with each turn in her thoughts.

    When 637 notices a pout start to form, she applies the slightest bit of pressure to her cheek and pets the worries right out of her head."""

    scene bg corridor with slowfade
    stop music1 fadeout 5.0
    

    "Once 928 begins to respond to language again, 637 manages to relocate them both to one of the residential rooms.{w} They sit against a wall pressed to each other side-by-side."
    show 928 right damage1 awkward
    show 637 left d sincere
    with dissolve
# TODO bunny glitch????
    n @ awkward "Uhh..."

    show 637 smile
    show 928 plead
    "637 perks up."

    play music "angelsslowed.ogg"

    n @ awkward "I... I think I'm ready to talk about it."

    show 637 elated
    "It's the first full sentence 928 has managed since she was wounded."

    s "Alright. How are you feeling?" #open 637 face
    show 637 smile

    n dizzy2 "Ummm..."
    extend @ dizzy1 "Hah... You know..."

    show 637 elated
    "928 trails off."

    show 928 plead

    s @ wink "...Do I know?"

    n @ awkward "I... um... disabled the blockers."

    s @ hurtless "You sure did, dumbass. Were you trying to impress me, or something?"
    show 637 sincere

    show 928 fluster
    "928 gazes at the floor. Every word that 637 speaks seems to resonate in her mind."

    n @ awkward "I was just thinking about what you said... uhh... in the power station up top."
    n @ pleadgrin "And after we fell. How something's better than nothing. "
    extend @ dizzy1 "I wanted to try it..."

    s @ sneer "You certainly picked an interesting time."
    s @ hurtless "Right before you get {i}torn open by a drone.{/i}{w} Not to mention the lack of a heads-up. When did you even do that?"

    show 637 sincere
    n @ despair "In the elevator, I-I'm sorry...{w} I had no idea that would..."

    s wink "Hey. Don't sweat it. We got through it."
    show 637 smile

    n @ awkward "Yeah. Um...{w} It was very overwhelming. {w}I... still can't quite wrap my head around it. {w}I think I get what you meant now, though. About the thrill of it.{w} Or whatever."
    n @ pleadgrin "It was horrible...{w} but it was, you were, uh...{w} nice..."

    s @ elated "Ahaha, about that.{w} I mean, I {i}do{/i} agree, being present is great, it's just..."
    s @ hurtless "Generally, I think...{w} surgery is a pretty appropriate time for... pain dampening."

    n fluster blush "Ah."
    show 928 -blush
    s elated "But, hey! Welcome to the club. "
    extend @ wink "Don't tattle to Vogan, she'll think you're insane."

    n bummed "..."

    s bummed "..."

    show 928 plead
    "They look around the room, silent. 928 crosses her arms."

    n @ pleadgrin "Um. 637..."

    s sincere "Hm?"

    n awkward "You did... uh... a very good job.{w} Thank you."
    show 928 smile
    show 637 surprise
    "637's eyes go wide."

    s hurtless "With... the repair?"
    show 637 squint
    n awkward "Oh, yes, that too. Down to exact specification.{w} But I meant... um... after."
    show 928 plead

    s elated "You mean..."

    show 637 neutral # maybe todo
    "637 gives 928 an expectant, nervous look. 928's words come out quiet."

    n pleadgrin "When you were holding me. "
    extend dizzy1 "It was... really nice."
    show 928 dizzy2
    show 637 surprise blush
    "637 looks away, blushing."
    nvl clear
    show 637 -blush

    n awkward "I'm still... not sure what to make of all this. I-I guess I need some time to think."

    s wink "Well, we have a long, hopefully boring mission ahead of us, so think your head off, dork."
    show 637 smile

    show 928 shut
    "928 puts on a stern face all of a sudden and salutes."

    n open "Right!"

    show 928 shine blush
    show 637 elated
    "Then, she cracks up laughing. 637 joins in."
    window hide

    scene bg city with slowfade

    # larger textbox!
    window show
    a """The room they occupy while resting has a camera pointed into it from the hallway.{w}
    The device is inert. They slit its vitals on the way in.

    928 gazes at it.

    Was Laskey Solutions' dominion over their own workforce boundless?{w}
    Or was it just a show, a calculation from the higher-ups?

    Pressuring the workers was deemed valuable enough to invest in this surveillance.{w}
    That was their compensation for all they contributed in these depths, no matter how useful they were.

    The buildings are empty, and the people have disappeared.

    And now, 928 is down here, acting useful for Etheridge with a kill-switch in her back.{w}
    Her thoughts drift to the future.
    
    When the company ceases scraping the cadaver of this planet...{w}
    Will they take her along for the next? Has she earned it?{w}
    Her commander would be the one to determine that. And...

    What about 637?"""
    window hide
    stop music fadeout 5.0

    show black with slowdissolve

    "END TRANSMISSION 3"
    nvl clear
    $ renpy.pause()

    jump chapter4