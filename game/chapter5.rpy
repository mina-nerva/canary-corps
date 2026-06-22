label chapter5:
    "Chapter 5"
    "TIMESTAMP"
    scene bg tunnels1 with fade
    nvl clear
    window show
    show graynvl with dissolve
    play music "cavesongslowed.ogg"
    a """After opening the blast doors, the Canaries take a long, vertical lift down into the mineshafts proper.

    The air grows colder, the earthen walls more claustrophobic. {w}Upon reaching the bottom, they step off of the lift.

    The tunnel sprawls straight ahead. Smaller passages on the sides branch out and twist into unknown paths. {w}Even with their visors, the end is out of sight.
    
    928 and 637 walk side-by-side along the rails in the center of the mineshaft.{w} The ground adjacent to the rails is composed of loose rock; remnants of the explosions that opened the path.

    The signal is close. {w}It's only a matter of time until they pinpoint it, but reaching it is another question entirely.

    They search the subterranean pathways in total silence.{w} 928 loses track of how many times they've looped back over their path.

    Every junction that should bring them closer to the Stellisite frequency ends up overshooting it. {w}The depth is correct, they can be certain of that, but navigational systems only work so well underground.
    
    637 scrubs through the map in her internal memory. She can't seem to bring up anything that sticks out.

    928's mind couldn't be further from the mission.
    
    She sifts through what 637 told her about their trackers.{w} The Asset Loss Protocol.{w} Running away from Etheridge. {w}For all of 637's defiance, escape seemed a sore subject for her.
    
    For 928, the notion was novel. {w}She knew of past Canaries attempting to gain their freedom, though she'd never entertained that notion for herself.{w} Too dangerous.
    
    It only led to reformatting, and why would she want anything beyond her station? {w}The only things she kept in mind were her commander and whatever assignment she had for her.
    
    Now, however...

    928 gazes towards 637. The blinking spot on her back with the beat-up casing.
    
    Defying Etheridge would mean independence. {w}The likelihood of pursuit seems low, considering Neuman-Keere's encroachment.
    
    The question is, then: what about the Asset Loss Protocol? {w}How can they stay alive without the permission of Etheridge?
    
    928 pictures a time-bomb ticking away in her own head. In 637's head.{w} What keeps them from reaching zero?
    
    For 928, it's a long-distance, encrypted ping response. {w}But 637's tracker was broken, right?

    Without the resources to fix it properly, {i}how is it still functional?{/i}"""
    hide graynvl
    show 637 left squint
    show 928 right damage1
    with dissolve
    "637 suddenly breaks her out of her train of thought, pulling close to her in a hushed but urgent tone."

    s @ scowl "Fuck, what's that noise? Do you hear that?"

    "928 goes still and listens. There's a low rumble ahead."

    n @ open "I do."

    "The rumble continues. The rails vibrate beneath 928's feet."

    n @ open "It's getting closer."

    s @ scowl "Shit. Is it Neuman Keere? {w}You think they got in here first?"

    n @ open "It's possible. Get your weapons ready."

    # show 928 combat # probably dont do this actually TODO
    # show 637 combat
    "A dot of light appears far down the rails. {w}928 and 637 rush to the wall of the mineshaft, crouching and aiming."

    "The source comes into view as a large, rectangular vehicle. {w}The top is jagged, overflowing with what appears to be the same slag beneath their feet."
    "There aren't any passengers."

    n @ open "It's... just a mine cart."

    s @ drool "Thought we were gonna have to start a tally on human kills for a sec."

    show 637 smile
    show 928 dull
    n "..."

    "The rumbling fades as the cart proceeds down its obsolete path. {w}The Canaries brush themselves off and step back onto the rails."

    s @ sincopen "I can't believe those are still running! Maybe we should've hitched a ride."

    show 637 neutral
    n "..."

    s @ hurtless "Hey, you good?{w} Was the 'human tally' joke too much?"

    show 928 smile
    "928 shakes her head."
    show 637 smile

    n @ awkward "...I've been thinking about your tracker."

    s @ wink "Aw, I'm flattered!"

    show 928 shut
    "928 rolls her eyes."

    n open "What I've been contemplating is...{w} If the long-distance component is no longer active, how does your validation process work? {w}There's no other component that could communicate all the way to the surface."
    n "And, clearly the Asset Loss Protocol hasn't..."

    show 928 fluster
    show 637 bummed
    "928 clears her throat."

    show 637 neutral
    n awkward "What I mean to say is: There must be some way your tracker receives the response, even down here."
    show 637 sincere
    n open "If we assume my tracker is the only thing on us that can reach the base...{w} then it's possible the signal you receive runs through mine. Like a close-range proxy."

    show 928 smile
    s @ scowl "...Woah.{w} That... seems like a security risk, right? Neuman could just capture both of us."

    n @ open "No, no. We're both on a leash. Because of me. {w}They'd still know exactly where we went, and the Asset Loss Protocol would terminate us both."
    show 928 shut
    s @ hurtless "Okay... {w}So what does that have to do with anything, right now?"

    n @ open "It means the encrypted responses we receive don't have to come {i}directly{/i} from Etheridge.{w} I'm definitely uploading both of our map updates... {w}But I'm only receiving one set of encrypted codes."
    n @ awkward "If I'm right about what that means, we might be able to exploit that... with some modifications."

    show 928 smile
    show 637 surprise

    "637 stares at her partner, eyes wide in disbelief."

    s scared "Shit, are you serious? You're saying we could go off the grid?!"

    show 637 neutral
    show 928 shut
    "928 looks at her and nods intently."

    s @ hurtless "Don't play me. I know you're techy, but... {w}You seriously think we could hack {i}ourselves..?{/i}"

    show 928 smile

    "An odd smile appears on 928's face."

    n @ shine "I could certainly try...? After all, we're {i}basically{/i} just computers, more or less."

    s sneer "Pff... {w}Ok, well, I can't say I've seen a computer that blushes like you."

    n shock blush "H-Hey!!!"
    show 928 fluster
    "637 laughs."

    show 928 -blush
    s sincopen "In all seriousness though, how do we do that?"
    show 637 sincere
    n @ open "We'd need a direct connection between us. Chances are we'd be out for hours. {w}And it'd be extremely obvious if we messed up and our trackers went offline..."

    show 928 bummed
    show 637 bummed
    "She looks down at the ground, and 637 grimaces."
    show 928 shut
    nvl clear
    s hurtless "Yeaaaah... I'm not too eager for either of us to be a heap of burning scrap."
    s open "Let's just, uh, keep going for now."
    window hide

    scene bg tunnels2 with fade

    # nvl
    a "They come to a junction in the tunnel."
    a "There's a distant, dim glow down the path to the left.{w} Following the light, the Canaries are silent. {w}They listen for movement, but all they can hear is each other's."
    a "The end of the rails come into view."
    a "They find themselves in a large circular alcove.{w} Brittle, rusty power-tools are scattered on the floor. {w}A haphazard mound of equipment sits off to the side of the rails against the wall."
    a "On the far end, mounted tube lights demarcate a narrow passageway."
    show 928 right damage1
    show 637 left

    "928 breaks the silence with a whisper."

    n @ open "The signal is close. This might be our destination."

    s @ sneer "I'll head in first."
    nvl clear
    show 928 hshut
    show 637 hgrin
    "She lowers her visor. 928 follows suit."
    scene bg bunks with fade
    
    window show
    a "They stay close to the wall, passing through mechanical door into long-abandoned living quarters."
    a "It's crowded with capsule bunk beds, each stacked three high. {w}Most of the thin mattresses are in a sorry state, with sheets torn to shreds or crumpled."
    a "928 and 637 step in, weapons still raised. {w}Checking between each bunk, all they find is assorted trinkets and personal affects from whoever once lived here."
    window hide
    
    show 928 right hshut damage1
    show 637 left hshut
    with dissolve
    window show
    "As 637 finishes clearing the corners, she spots something."
    

    s sneer "Woah. 928, you gotta see this."

    show 928 alert
    "928 looks over, and jumps."
    "At the wall opposite to the entrance, a still figure slumps beneath a flickering fluorescent light.{w} Next to it, two more figures lay on their sides."
    n @ shock "Oh my god."

    "The body on the wall is dressed in a standard Laskey miner uniform. {w}A bright orange vest, stained near the ribs with a brown-red color. On the ground near its left hand is a rusted knife."
    show 928 fluster
    "Spots of shriveled flesh cling around its gaping jaw.{w} 928 gazes at its empty eye sockets. She wonders how synthetic flesh decays.{w} She pictures 637's face..."

    show 928 grit
    "She turns away from the corpse and grabs her mouth."

    s @ sincopen  "Damn, you alright? Never seen a dead guy before?"
    show 637 smile

    n yelp "It's... {w}ugh! I'm fine!"
    show 928 bummed

    "637 crouches to examine the other two bodies lying on the ground.{w} They both wear security outfits. Bullet-proof vests slump against their now-hollow torsos."
    "The larger corpse's hand still clutches a pistol laying nearby. {w}Near their necks, the floor is coated with dried blood."
    show 637 squint
    "637 spots a crumpled piece of paper wedged in the smaller one's back pocket.{w} She grabs it and turns to 928."
    show 928 shut
    s @ open "See what's up with this. I'm gonna keep checking their pockets."

    "637 unfurls the slip of paper and hands it to 928."
    "At the top, the word 'SMUGGLERS' is scrawled out and underlined.{w} Below, various worker identification numbers are listed, some crossed out."
    show 928 fluster
    "She glances at the miner's vest. The ID on it matches with one at the bottom of the list. {w}She swallows."

    n open "The guards were interrogating them. {w}They had a list of workers suspected to be smugglers."
    show 928 shut
    s @ scowl "Sheesh, what were they smuggling?"

    n @ open "Not sure... {w}Probably something valuable, if they died over it."

    show 928 bummed
    "If they went through with escaping Etheridge, her and 637's numbers might end up on a similar list. "
    show 928 shut
    extend "She watches as 637 sticks her hand into the miner's pants pocket. "
    show 637 surprise
    show 928 alert
    extend "She pauses."

    s sneer "Oh, shit. {w}No way!!!"

    "From the pocket, she slips out a small glass vial containing a sliver of glowing blue crystal, turning it in her hand. {w}928 stares at it, fascinated. 637 chuckles."
    "A Stellisite shard."

    s wink "Well. There it is, I guess. Problem solved!"
    show 637 squint
    "She squints at the small, glowing blue crystal fragment."
    show 928 shut
    s @ mad "This is seriously all they sent us down for?!"
    s @ scowl "Damn... They really {i}are{/i} desperate."

    show 637 neutral

    "637 hands it to 928. {w}It warms her hand. Pinpricks of static run through her fingertips. {w}Even a fragment this small holds an unbelievable amount of power."

    n @ open "I agree... This is too small to warrant us being sent down here. {w}And the signal couldn't just be for this tiny little thing.{w} The detected deposit was nowhere near this size, and Etheridge's scans are accurate."
    n @ open "That being said: {w}If this many people were, uh, {i}interrogated{/i} about the smuggling operation... It's entirely possible that there could be a central stash."

    s @ hurtless "Huh. I guess that makes sense? Seen guys die over less, though."

    "637 stands up."

    s @ open "But, one way or another, that's all these folks had on 'em. {w}So let's keep looking."
    show 637 smile
    "637 scans around the eerie living quarters."

    s @ open "How close is the signal, then?"

    n @ open "Exact locations are unreliable, this deep...{w} But we should be right next to it. Or very close, at least."

    s @ hurtless "...You know what, come with me."

    n @ awkward "Um, what?"

    "928 turns to see 637 already walking to leave. {w}She looks back at her, and waves a beckoning hand."
    nvl clear
    s @ wink "Just hear me out! I've got an idea."

    hide 637 left
    hide 928 right
    with dissolve
    show bg tunnels2 with dissolve

    a "928 follows 637 out of the sleeping quarters back into the tunnels."


    a "They wind around a passage or two, past where the rails stop. {w}They stop in a dead end packed with mining machinery."
    show bg junk with dissolve
    a "The old equipment and vehicles are coated in a thin layer of dust.{w} Many seem too damaged or stripped to function."
    a "The pair wrote it off as a wrong turn before, but one small detail catches 637's eye."
    show 637 left smile
    show 928 right damage1
    with dissolve
    "She leans on a massive boulder on the side of the cavern, beside the rusted frame of an industrial power suit."

    s @ sincopen "You've been through one of these mines before, no? Ever seen Laskey store equipment like this?"

    n @ open "Yes. Less haphazardly though...{w} Are you suggesting the workers could have hidden the Stellisite {i}inside of these machines?{/i} {w}That hardly seems like a sound idea. Pretty obvious place to look."

    s @ hurtless "Yup.{w} And if I were a smart little mine worker, trying to keep things from security, I'd wanna give them a serious runaround. {w}Make 'em miss the forest for the trees."
    s sneer "Which is what brings me to this baby, right here."

    "She knocks on the frame of the power suit."

    s sincopen "You're techy. {w}Notice anything about this guy?"
    show 637 sincere

    n @ open "Aside from superficial damage, it appears there are few parts of this lifter that would fail to operate if replaced... {w}What are you trying to say?"

    s @ sneer "Girl. We're in a scrap heap. Full of easy to miss used parts. And this thing lifts rock. {w}Who needs to hide stuff in a machine when you can have a machine hide stuff for you?"

    "She gets up, braces herself against the side of the boulder, and shoves with all of her strength. {w}It shifts ever so slightly."

    nvl clear
    "With the combined effort of two mechanical bodies, they shove the boulder off to the side."
    "It sends a shockwave of dust through the room. Through it, a shadow becomes visible on the uncovered wall."
    "A low, square opening reveals itself. The Canaries enter."
    stop music fadeout 5.0
    window hide
    scene black with dissolve
    
    # 928 positions herself to peek into it."

    # n "...I can't see where it leads. Do you think... this is it?"

    # show 637 sneer
    # "She looks up at her partner, who responds with a satisfied grin."

    # n "Um. Do you want me to go first, or...?"
    # hide 637 left
    # "637 drops to her hands and knees alongside 928."

    # s "Nah. I got this."

    # "..."

    # s "Ugh, finally!"
    

    a "928 cranes her neck and spots shreds of light past her partner's figure. With every step, the roof slopes upwards. {w}The end comes into view and the partners finally manage to stand."

    a "A make-shift plank door is illuminated from behind. There's no doorknob."
    a "637 pushes it with her hand. {w}It doesn't open, but it creaks. {w}637 motions 928 to stand back."


    a "Before 928 can respond, 637 smashes her shoulder into the center plank with all her weight."
    scene bg cache
    play music "minesong2slowed.ogg"
    a "The door gives way. 637 stumbles, catches herself on the doorway, then turns to smirk at 928."

    a "The room is lit by a bulb hanging on a wire overhead. {w}On one wall, rows of wooden supply crates hold mining equipment sharpened into weapons and makeshift firearms."
    a "In a corner sits a pile of explosives with tangled electrical wires protruding."
    a "Whatever plans the workers had for these supplies have long expired, dashed by the corporate scavengers that put Laskey's operation down."
    a "The rebels and their opposition are gone from this place. {w}Neither had the chance to capitalize on these supplies."
    a "In the far end of the room, a collapsed wall covers a lead storage container with rubble and dust."

    show 928 right damage1
    show 637 left smile
    with dissolve
    
    "637 steps to the center of the room."

    show 637 left sincere
    show 928 right damage1 smile

    s @ sincopen "Wow, would you look at that... Sure is cozy in here."

    n @ awkward "I don't know if cozy is the right word."

    s @ wink "Well. The bombs might be a bit much."
    show 637 smile
    "While 637 scrutinizes the crates of make-shift weaponry, 928 moves toward the collapsed wall."
    "Wiping away the debris from the storage container, she notices a crack in the top compartment. {w}It holds a small, aluminum box with a handle."
    show 928 alert
    "928 opens it and gasps. 637 turns to face her."
    show 928 fluster
    s hurtless "Hey, what's-"
    show 637 surprise
    "Her eyes go wide. {w}The contents of the box gleam a familiar teal across 928's face."
    show 637 squint
    "The reason for every security system and killer automaton down here. {w}The impetus for all the blood that's been spilled.{w} The potential leverage for Laskey's underclass. {w}The entire purpose of the Canaries, what they were built to retrieve."
    "The box overflows with Stellisite crystals."

    n @ shock "Holy shit."
    show 637 elated
    show 928 smile
    "As 637 approaches her, 928 starts to smile, eyes wide."
    "They accomplished what they had set out for. At least, the hard part. {w}For the moment, she's overjoyed, filled with the ecstasy of fulfilling her purpose."
    "Another job well done."
    show 637 sincere
    "637 puts her hands on her hips, and sighs in exhaustion."


    n shut "..."

    s neutral "..."

    s @ hurtless "Well, I guess that's it then!"

    n bummed  "..."
    extend @ awkward "Yeah!"

    s bummed "..."
    nvl clear
    n open "Well... I suppose it's time to upload our final route...{w} We should recharge before we proceed with retrieval. "
    extend awkward "With the pressure from Neuman-Keere, Etheridge won't be long to reach us. "
    extend dullgrin "And then we can return to base..."
    
    show graynvl
    hide 928 right
    hide 637 left
    with dissolve
    a "Something snags 928's words, staring at the box in her hands. Her commander's promises loom heavy in her mind."
    
    a "Her chest pangs, as she imagines receiving approval for fulfilling her purpose. She's performed her function. In return she will be reminded of her value."
    
    a "But then she remembers what comes after."
    a "Countless hours in the storage unit on standby, surrounded by other dormant machines. {w}Attempting to empty herself of all thoughts in order to accelerate the time."
    a "Trying to stave off the cold envy threatening to overtake her. {w}Not envy towards the humans, but the equipment resting nearby, unburdened by sentience."
    a "A gun doesn't have to think. {w}It does what it's built for. And when it fails, it's not scolded. It's repaired."
    a "That's what the commander demands of her. She just can't seem to give it."

    a "637 moves closer. 928 observes her."
    a "The scars on her face that run along the bridge of her nose, partly hidden by unkempt locks of hair. {w}The scratches and imperfections dotting the surface of her torso, evidence of injuries she's sustained and mended numerous times."
    a "Her metallic hands that held her gently, forcefully, always with care."
    a "928 looks deep into her eyes, trembling."

    stop music fadeout 2.0

    a "There is no electro-magnetic interference. {w}928 and 637 are expected to report within the next few hours. {w}Once they do, Etheridge will know they found the Stellisite."
    hide graynvl
    show 928 right damage1 bummed
    show 637 left bummed

    "They continue to lock eyes. 928 shuts the box."

    n despair "637, I..."

    "She pauses. 637 is silent."

    n @ yelp "...I don't want to go back."
    play music "howivemissedintroslowed.ogg"

    show 637 sadless
    "637 puts her hands on 928's face and presses her forehead to hers. The box is set aside.{w} 637 wraps her arms around her. 928 leans into the hug, relaxing into her partner, calming herself."
    show 637 bummed
    show 928 bummed
    "After a moment, they pull back from the embrace."
    
    s @ sad "To be entirely honest with you... {w}I don't want us to go back either."
    s @ sadless "But I don't know where we'd go. {w}Or if it'd work out, like you said earlier. {w}I trust you with this, but it's kind of a long shot, right?"

    n open "It might be. {w}But I think it's worth the try. For both of us."
    show 928 shut
    s hurtless "Okay. So what's the plan, then?"
    nvl clear
    show 637 bummed
    n @ open "...Let me think."
    hide 928 right
    hide 637 left
    show graynvl
    with dissolve
    window show
    
    a "928 flies through the possibilities in her head. {w}637 proves that Canaries don't need direct communication with Etheridge."
    a "Canaries' transmitters are capable of encrypting, decrypting, and forwarding the ping response to each other.{w} The encrypted key she receives on upload is only for her, which means that 637's must be coming from 928 herself."
    a "And if one Canary can give another a key..."
    hide graynvl
    show 928 right shut damage1
    show 637 left bummed

    n @ open "...A feedback loop.{w} If we made a feedback loop, and our trackers kept passing the packets back to each other, connected at short-distance...{w} I could break my long distance tracker off from reaching Etheridge. Like yours."
    n @ open "And we'd be..."

    show 637 scared
    "637 stares at her."

    n @ awkward "...We would be untrackable."

    s bummed "..."

    n shut "..."

    s @ hurtless "Okay, so, assuming we do this...{w} {i}How{/i} do we pull it off? {w}You said before we'd need a {i}direct connection{/i}."


    "928 looks down."

    n @ awkward "I... have an idea, but-"

    s @ wink "What, it's risky?{w} Well, you know me. Famously risk-averse."

    show 637 sneer
    "She sneers."

    s "Spit it out, dork."

    show 637 smile
    "928 smiles a little, then shifts and looks around the room."

    n @ open "If we want to connect our trackers, we would need to reboot them at the same time, and link them, so our keys are mapped to each other. {w}The only way I can think of doing that, without any outside help, is... well."
    n @ open "Directly connecting our neural interfaces and modifying each other while we're both still powered on."
    nvl clear
    s @ scared "...Th-that's... {w}Um. Wow."
    s @ hurtless "So, we'll be in each other's heads?"

    
    "928 nods."

    s @ drool "Freaky. Let's do it."
    stop music fadeout 5.0
    window hide
    scene bg cache with fade
    window show
    show graynvl
    with dissolve
    a "They shut the door."
    
    a "928 and 637 sit side-by-side. A tangle of repurposed wires protrudes from the back of 928's neck beneath an unscrewed panel."
    a "She holds the exposed end of the wire in her hand. 637 is turned away, holding her hair in a bunch off to the side."
    a "The same access panel is there on her own neck, waiting for a connection."
    hide graynvl
    show 637 left sincere
    show 928 right damage1
    with dissolve
    # bunny glitch
    n @ open "Okay. Remember, our first priority is to connect our trackers.{w} Find the root where we store the keys."

    s @ hurtless "Right, okay."

    n @ open "Then, you copy them over. {w}And we disable the connection to Etheridge."

    s @ drool "Yeah! Fuck 'em!"

    "928 sighs."

    n @ awkward "I... can't even begin to guess what this will feel like. {w}There might be an urge to push the connection out, so we'll need to stay focused."
    n @ open "We might be unconscious for a while. {w}If we succeed though, it shouldn't matter."

    s @ sincopen "No 'if's. Let's do this."

    n @ awkward "...I love you."
    show 928 smile
    show 637 elated
    "637 turns around, surprised."

    s sincopen "I love you too, dork."
    s sneer "Now come on. Plug me in."
    show 637 smile

    "928 slots the exposed copper into the back of 637's neck and presses the panel down to hold it in."
    "There's a shock."
    show 928 process
    nvl clear
    s process "Nnngh..."

    hide 928 right
    hide 637 left
    with dissolve
    show graynvl
    a "928 feels a tingle. {w}She's never heard 637 make a sound like that before."
    a "She gazes at 637's back. Everything's still. {w}928's vision is fixed on her partner."
    show bg cache d1 with dissolve
    # hide 637 left
    # show 637 distort
    a "Then, she notices the lines."
    play music "angelsinthesnowB.ogg"
    a "They emanate outward from the edges of 637's figure, all parallel. {w}She's splitting apart. It's dizzying.{w} 928 feels herself swaying."
    a "With every motion, her vision unravels. {w}Then, it jumps back to normal, as if she hadn't moved at all. It disorients her.{w} She's spinning, losing track of where she is. {w}Her head hasn't moved an inch."
    show bg cache d2 with dissolve
    # show 637 b2 h2
    a "She feels herself fall forward.{w} Gravity draws her toward 637, but she can't reach her. The fall is continuous."
    a "928 gets the sensation that she's phasing through her partner, and then through the ground beneath."
    show bg cache d3 with dissolve
    a "But she can't catch her bearings before the cycle repeats itself and she's back where she started. {w}She attempts to speak."
    show 928 right process damage1
    n "lohzxcuoi1asdrfi9asdrf8asdrf8idasrfpiodfsaujdskjrfkuikjp;kdjwrplk;we;lksdf;kjlsdflkjdfsjklsjkdlfjkldrkjlsdfjlksdfljkrfjkslapjklp;rfljkp;kljp;fwskjlrwejmnhurewjmhnugrfjmhnurdwe"
    hide 928 right
    a "928 doesn't understand her own voice. {w}Did she even make a sound?"
    a "She falls and falls. Something must be wrong. {w}She can't place what it is. {w}Maybe, if she just closes her eyes..."
    hide graynvl
    scene white with dissolve
    

    a "928 sees white."
    $ border_enabled = False
    show mentalbg with dissolve

    #show mental
    
    a """The free fall continues, but now 928 finds herself in a void. {w}There is no up or down.{w} It envelops her and dissolves her discomfort.

    Spinning and falling become the same thing; a perpetual, directionless motion going nowhere and everywhere."""

    show mental with slowdissolve
    
    a """She attempts to perceive her own form. It's not quite what she recalled. {w}Her limbs billow outward.{w} At times, they seem soft and flowing, others, firm and powerful.

    With no point of reference, her size becomes uncertain. {w}She separates from herself and views her body from multiple angles.

    She looks at the scar on her chest. {w}Her identification number, though she doesn't recognize the digits. {w}The components she carried on her back come into view. {w}Her tracker is blinking a million times a second, in all possible colors.
    
    Her breathing slows. {w}Everything she held inside of her comes into view, orbiting around her like a sprawling tree of data.{w} She spots her own head, eyes closed, somewhere in the parade of nodes.

    She feels lonely here, surrounded by herself.

    The branches coalesce into a figure.

    It's another her. {w}She feels herself in two different places at once. {w}Duplicated senses, communicating in sync with each other. {w}They start to move in unison. Steady, smooth motions mirroring each other.
    
    Everything unfocuses. {w}The figure comes back into view as 637.{w} The split vision unifies.

    She faces away from 928, but her presence is immeasurable in the void. {w}Her sense of time and space is anchored by her partner. {w}Suddenly, she finds herself surrounded.

    A thought crosses her mind. {w}There was something they needed to do.

    928 gathers herself and closes the distance to 637. {w}The edges of their figures are ribbons coiling around each other.

    She attempts to perceive the form 637. {w}A swarm of parts conceal the shape. {w}928 manifests her own limbs to reach out towards them. {w}Numerous hands brush against each other.

    Then, 928 sees her.

    637's body is all sharp edges.{w} Each angle glimmers with an iridescent sheen.{w} Fluid ripples around the edges of her eyes.

    A timid hand reaches toward the jagged thing, but the contact slices it open. {w}Both the limb and 637 recoil. 637 shrinks away from 928, and a vast plane forms between them.

    The cut on 928's hand emits loose capillaries of light.{w} Old scars appear to her as fresh sensations, and she recalls everything that's touched her in the past.

    Attacks by violent animals. Harsh coaxes from captors. {w}The new wound spreads further into her body. {w}Defensiveness clouds her mind, but a thought reappears.

    There's something they need to do.

    928's limbs transform into fractals. {w}They flow outward against the plane, branching out around 637. They envelop her.

    637 folds against herself, seeming microscopic in comparison.{w} Her eyes glint as they peek at the form surrounding her.

    928 collapses a swath of limbs to make contact with 637's serrated exterior. {w}Every point slices 928 open anew. The cuts leave the limbs soft and stringy, but 928 doesn't pull away.{w} More and more parts of her embrace 637.

    They split into a loose web of fragments that push themselves further into her edges.{w} 637 witnesses with wide eyes. {w}There's a violence in the fracturing, but 928's affection seeps out of her lacerations.

    It warms her. {w}The sharp points begin to wear down. {w}Her guard lowers.{w} For an eternity, she has sharpened herself. {w}Now, she wonders why the points were raised in the first place.

    As 928 continues to permeate her, the habit starts to seem obsolete.

    637 unfolds. {w}The tatters of 928's extremities drape across her. {w}Their eyes meet. {w}928 closes the distance and begins to meld into 637. {w}Gaps between every molecule and cell that compose them grow wider. {w}Their borders dissolve into a single form, face, body, limbs all overlapping.

    928 moves her arms, or 637's arms, into their body.{w} They sink into soft, permeable flesh. {w}Their gentle hands navigate through their organs. {w}Some are firm and coarse, others are delicate and slick.

    One hand grasps something supple and singing. {w}Her tracker. {w}The other hand finds a second one, damaged and fraying. {w}Slowly, they push them closer to each other.

    They are incomplete, desperate for an answer.

    Finally, the trackers meet.{w} There's a high-pitched noise. {w}She presses the trackers into each other. {w}The sound grows louder. They click into place.

    The chiral patterns of their encrypted keys merge, singing each other's song like sheet music as they spin in unison. {w}There is a call and a response."""

    #TODO BEEEP!!!

    a """Synchronicity.

    Long-distance contact disabled.

    She doesn't understand the words, but they bring her a sense of satisfaction.{w} Freeing arms from its insides, the merged form embraces itself and drifts off to somewhere unknown..."""
    window hide

    stop music fadeout 5.0
    show black with Dissolve(5)

    "END TRANSMISSION 5"
    nvl clear
    $ border_enabled = True
    $ renpy.pause()

    jump chapter6