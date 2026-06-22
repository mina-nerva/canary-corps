label chapter4:
    "TIMESTAMP" # TODO

    # larger textbox
    scene bg processing with slowfade
    window show
    show graynvl
    with dissolve
    play music "minesong1stretchedB.ogg"
    a """Orange light emanates from the end of the railway tunnel connecting the residential district with the foundry.{w}
    The two Canaries see a concrete station platform come into view, along with piles of train parts and stone debris that blanket the rails ahead.

    Without words, the pair climb up and around the cars.{w}
    Specks of molten dust float in the air all around them.{w}
    The platform overlooks the processing complex. 928 peers into the distance.

    Broad catwalks draw squares above the intestines that once processed Helka-112's Stellisite.{w}
    928 attempts to derive the path taken by the mineral in the facility, but it proves futile.

    The place has long been stewing in its own heat.{w}
    With no one to keep the temperature regulated, the pipes and machinery have melted into new, useless forms.{w}
    Whether unassisted humans could have ever survived down here without specialized equipment is an open question.

    Now, it's left only for the Canaries.

    928 glances at 637, then back at the scenery.{w}
    The station platform they stand on is elevated meters above the catwalks proper.{w}
    A lack of rails in a spot indicates where stairs would have connected them. Navigating across might be tricky."""
    hide graynvl
    window hide
    with dissolve

    show 928 right damage1
    show 637 left
    with dissolve
# TODO bunny glitch
    n @ open "Maybe we could look for a–"

    hide 637 left with dissolve
    "Sudden, quick footsteps on the platform snatch 928's attention. "
    show 928 alert
    extend "Then, she sees 637 sprinting full-speed at the gap in the railing."

    n shock "WHAT ARE YOU DOING?!"
    show 928 alert

    "637 launches off the platform near the edge. {w}928 gapes at her airborne figure as it sails through the air towards the catwalk, finally landing with a smooth roll."#TODO thump?
    "637 gets up and shakes herself off. {w}She holds her hands like a megaphone towards 928."
    
    s "Huh?! What'd you say?"
    show 928 fluster
    "928 shouts back at her."

    n @ shock "That was so reckless!"

    "637 laughs."

    s "Was it? I've made scarier jumps!"

    show 928 mad
    "928 clicks her tongue."

    n @ pissed "You're crazy!"

    "637 smirks and props herself up on the catwalk's railing."
    nvl clear
    s "How 'bout you come over and say that to my face, dweeb!"
    
    show 928 grit
    "928 huffs."
    show 928 mad
    extend " Strictly speaking, protocol dictates to play it safe and assemble a safe path across with a cable or scrap metal. "
    show 928 bummed
    extend "If 637 made it, though..."

    n pissed "Alright!"

    show 928 shut
    "She stands back toward the rails. Deep breath. She takes off running, and leaps off the platform."
    hide 928 right with dissolve
    window hide

    window show
    show graynvl
    with dissolve
    a "928 flails her arms as she hurtles through the air. The fear fluttering through her slows the moment down to an excruciating length."
    a "She barely registers the platform appearing beneath her, securing her safety. {w}Her feet smack onto the catwalk with a rattle. {w}Brought to her senses, 928 attempts to redirect the impact of the landing with a roll, like 637, but she's a touch too late."#TODO thump!
    a "Her legs buckle, and she tilts forward."
    hide graynvl
# TODO bunny glitch
    show 928 right yelp damage1
    show 637 left
    s sneer "Woah!"
    show 637 smile
    show 928 grit
    "637 kneels to catch her, killing her momentum.{w} Shock from the impact and the subsequent relief of solid ground causes 928 to lose her balance. {w}She clings to 637. "
    show 637 sneer
    extend "Then, 637 cackles."

    show 928 fluster
    s @ wink "Smooth."

    show 928 mad
    "928 snaps out of it, pulling away as she recalls her indignation."

    n @ pissed "I- Wh-"
    n @ pissed "It's not my fault I stumbled. {w}I did a good enough job. {w}And for what it's worth, we're not supposed to be taking risks like that anyways!"

    "They stand up. 928 steps away from 637, pouting."

    s sneer "Wait, really?{w} I thought you'd have no problem with that, Miss Perfect-Record! {w}Is there some rule that says 'no jumping over small gaps?'"
    show 637 smile
    n pissed blush "YES!"
    show 928 mad
    show 637 sneer
    "637 snickers at her and backs away."
    nvl clear
    show 928 -blush
    s @ hurtless "Damn..."

    s wink "You really are a dweeb!"
    hide 637 left with dissolve
    "She sticks her tongue out at 928, and takes off onwards."
    hide 928 right with dissolve
    "928, exasperated, follows after."
    window hide
    # larger textbox
    
    window show
    show graynvl
    with dissolve
    a """They continue walking the metal path deeper into the sweltering complex.

    Distant walls are lined with colossal, metal fans.{w}
    They sit idle, beginning to lose their shape in the sheer, stagnant heat.

    Surveillance here is minimal in comparison to the residential district.{w}
    No wall-mounted cameras in sight, only a sparse number of hovering drones on autopilot, making the same rounds, over and over.

    637 has been taking pot shots at them for the last few minutes. 928 keeps up a brisk pace, ignoring her.{w}
    637 spots one gliding perpendicular to their trajectory in the distance.
    
    She grabs 928's shoulder."""
    hide graynvl
    window hide
    with dissolve

    show 928 right damage1
    show 637 left smile
    with dissolve
# TODO bunny glitch
    s @ sneer "Come onnnnn. Humor me. You try one."

    n @ open "No."

    s @ drool "Don't tell me you've never taken practice shots before."

    n @ mad "Yes, of course I have. {w}Right now, I'm trying to focus on navigation.{w} If you have nothing better to do, then I suggest you just neutralize it yourself."

    s sneer "Ouch! "
    extend hurtless "Well, navigating's all well and good, but you {i}are{/i} falling behind, y'know. {w}As it stands we're 8-2."
    show 637 smile

    show 928 bummed
    "928 blinks."

    n @ mad "...What?"

    s @ drool "Drone kills, girl! You haven't kept track?"

    n @ open "Wh– {w}You're keeping track? "
    extend @ mad "I... don't see how that would have any benefit for the mission."
    show 928 shut
    show 637 squint
    "637 rolls her eyes."

    s scowl "C'mon, loosen up! You were so chill after the repair. What happened to that?"
    s hurtless "It's not like racking up some drone kills is gonna {i}harm{/i} the mission. {w}Where's your competitive spirit?"

    show 637 wink
    "637 winks."
    show 637 smile

    n bummed "..."

    s @ scowl "Damn. You're so stubborn!"
    s @ squint "..."
    s @ sneer "I'm starting to think you just can't aim."

    show 928 alert
    "928 stops."

    n mad "I can aim. {w}Of course I can aim. Our combat capabilities are built into us."

    s @ hurtless "Yeah... I don't know if I see it. "
    extend @ drool "Maybe your little commander friend pulled some strings for you, and you've been getting by with just your blade."

    "928 scowls at her insinuation. {w}She glares at 637, then at the drone plodding through the air."

    s @ wink "Hey, I'm giving you a chance to prove me wrong!"

    n @ pissed "I- Ugh... {w}You know what, fine."

    show 637 smile
    show 928 hshut
    "She readies her weapon arm, and the gun folds out and into position. {w}Her eyes narrow, tracking the drone's linear path.{w} She fires." #TODO bang!
    "The body of the drone sparks, and crumples. {w}It drops into the glowing oblivion, propellers still whirring."
    show 928 smile
    show 637 neutral
    "928 gives 637 a smug look and tilts her head. {w}637 touches her chin in blank contemplation."
    s "..."
    show 928 plead

    "The silence begins to erode 928's satisfied expression into uncertain anticipation."

    show 928 fluster
    s @ hurtless "Wow. Now we're 8-3, huh? {w}Still a pretty steep gap. {w}You probably just got lucky, let's be real."

    n pissed "What?!"
    show 928 mad


    "637 ignores her and looks out to the distance, where another drone drifts along the sweltering air."
    show 928 bummed
    s sneer "Oh, look! Another one."

    "She closes one eye and aims her arm in its direction."

    s drool "Guess I'll go ahead and secure my lead–"

    show 928 shut
    show 637 surprise
    "A bang interrupts her, and the machine she was eyeing bursts open and scatters. {w}637 looks at 928, who lowers her arm, billowing smoke. {w}928 is turned away from her."#TODO bang!

    n @ mad "8-4. {w}Let's get going."
    show 637 elated
    hide 928 right with dissolve
    window show
    "928 strides forwards."
    hide 637 left with dissolve
    window show
    "637 bites her lip, then starts to catch up."
    
    scene bg processing with fade

    "{i}Bang.{/i}"
    show 928 right damage1
    n @ open "That's 12-8, my lead."

    show 637 left hurt
    "She turns to her partner, who staggers toward her on the catwalk, panting. {w}637 holds herself up by the railing. 928 comes to lean next to her."
    show 928 smile

    s hurtless "...Hah. Fuck... {w}I guess you {i}are{/i} a decent shot."
    show 637 smile

    "637 gathers herself and holds out her hand to 928."

    s @ wink "Good game. You proved me wrong!"

    show 928 shine
    "928 beams and shakes her partner's hand."

    show 928 smile
    s @ sneer "See? It's not so bad to take a little time to yourself, is it?"
    stop music fadeout 5.0

    show 928 shut
    "The two of them rest, gazing over the rails into the mechanical abyss. {w}928 furrows her brow and mumbles under her breath."

    n bummed "...Agh, what am I doing...?"

    s neutral "Hm?"

    "928 buries her face in her hands and groans."

    n despair "I don't know. Something's wrong with me. {w}That was... {i}fun{/i}, but it feels like there's something clawing at the inside of my chest. {w}I feel it every time I catch myself not thinking about the..."

    show 928 bummed
    "637 leans over on the rails beside her."
    

    s @ hurtless "The mission, right?"

    "928 nods."

    n @ despair "I'm just- All of THIS, it's so... new. {w}Before, it seemed so simple. I could just focus on the task at hand. {w}But, now I'm messing around and killing time..."

    "She shakes her head."

    n @ despair "I don't know how to make sense of it. {w}Is it scarier that I'm going off track, or that I don't want it to stop? "
    extend @ yelp "Am I bugged? Or-"
    n @ grit "Aghh!!!"
    play music "howivemissedintroslowed.ogg"
    show 637 sincere

    "She puts her face in her hands. It's too much. 637 taps the rail with her fingers, chuckling to herself."

    s hurtless "I gave it a lot of thought myself. Back when I was 'fresh', like you. {w}Had a guy on my ass telling me what to do, where to go... And I did it."
    s bummed "You don't just wanna stop being useful to Etheridge when the alternative is... y'know."

    "She points a finger at her own head and mimes a gunshot."

    s @ hurtless "But after I saw enough Canaries killed in action, killed in base, reformatted... {w}I kinda stopped giving a shit.{w} So I started wondering, it's pretty fucked that they'd make us aware of death as a concept, right?"

    s @ scowl "You look at the drones we shoot out here, and they've got as much of a problem being killed as a toaster does being unplugged from an outlet. {w}But we're different."
    show 637 sincere
    "928 hazards a look towards her."

    n @ open "You mean self-preservation instinct. For navigation and survival."

    s hurtless "Right, yeah. {w}But again, if it's just an instinct for self-preservation, someone at Etheridge fucked up.{w} Made us a {i}little{/i} too human."
    s @ scowl "'Cause {i}I{/i} don't just wanna {i}self-preserve{/i}... I wanna {i}live{/i}, right???{w} But nah, they need us somewhere between a brain-dead tool and an intelligent soldier.{w} So you end up with threats, reformatting, decommissioning..."
    show 637 sincere

    "928 stares at the ground, wide-eyed."

    n @ open "But the commander appreciates me."
    show 928 shut
    show 637 sadless
    "637 sighs."

    s scowl "She might appreciate what you {i}do{/i}. {w}What you {i}are{/i}. "
    show 928 dull
    extend hurtless "Sure, you might be the most reliable tool on her shelf. {w}Sure she'll drop you some validating words, keep you thinking you're almost good enough to be a person in her eyes."
    s "But only enough to keep you desperate for more. {w}And then it's, what, back to the locker, right?"

    show 637 sincere
    n bummed "..."

    s hurtless "Me, personally? I'm done trying to be something I'm not. {w}There's no point playing pretend, because they've made up their minds about us. {w}Might as well embrace what we are."
    s sneer "We're cunning, sturdy, dangerous things. {w}Not human. But {i}very{/i} alive."
    s open "I dunno what Etheridge will do with us when they're done scraping the bottom of this barrel for all it's worth. {w}But if they're gonna try and take me out, I'm not just going to let myself die as a tool."
    show 637 sincere
    show 928 alert
    "928 swallows."
    

    n open "I think... {w}I don't want to be just a tool either."
    n despair "But, then, even if I {i}do{/i} feel that way... What can we even do about that? {w}We have to carry out our assignment. If we don't, then..."
    show 928 bummed
    show 637 elated
    "637 grins."
    show 928 shut
    s sincopen "Yeah, they've got us pinned pretty tight.{w} We're still kicking, though. And finding ways to be a little happy.{w} That's what really matters."
    show 637 sincere

    show 928 smile
    "637 moves her hand against 928's."


    n @ awkward "...Um.{w} What {i}did{/i} you do to your tracker?"
    show 928 shut

    show 637 bummed
    "637 sighs.{w} She turns away, gazing at nothing in particular."

    s @ sadless "I, uh..."
    s hurtless "Look. A few deployments ago, I decided I had enough, and made a plan. {w}Figured Laskey's shit would be enough to bust it open but, turns out, not the case."
    show 928 alert

    s open "I split off from my partner and spent an hour or so messing with the thing... {w}I only messed up the long range tracker, and my movement systems."
    s scowl "Not being able to do anything about it, I waited for the protocol to kill me. {w}A soldier found me first."

    show 637 sneer
    "637 lets out a short, dry chuckle."
    show 928 shut
    s sincopen "So, I went back to base with a busted up tracker. "
    extend open "You can imagine the reaction that got."

    show 637 bummed
    show 928 bummed
    "928 recalls the scene in the hangar."

    n @ open "Oh... Yeah."
    show 928 shut

    s @ hurtless "Between you and me, 928? {w}I still want out. But there's not really anywhere to go. And after this...{w} Well, I get the feeling Etheridge won't be keeping me around much longer."
    
    s @ open "They'll still have a use for you, though, so...{w} That's something."
    show 637 neutral
    n @ open "Don't say that. {w}We are both here on this mission. They need us both."
    show 928 bummed

    s bummed "..."
    s @ hurtless "Yeah. You're right.{w} Sorry."

    show 637 sincere
    "637 steps away from the rails and stretches out her shoulders."

    s @ wink "Guess we better get moving again, no?"

    n @ open "Uh... Yeah."
    stop music fadeout 5.0
    show 928 shut


    scene bg blastdoor with slowfade
    show 928 right alert damage1
    show 637 left sincere
    with dissolve
    "928 pauses."
    nvl clear
    n open "There it is."
    hide 928 right
    hide 637 left
    show graynvl
    with dissolve

    a "The elevated catwalk ends, leading into an alcove in the face of the wall."
    a "At the back of the space, a large blast door reading 'QUARRY F6' bars the way to the mineshafts proper."
    a "Adjacent to it, a small security building labeled sits, seemingly unoccupied."
    a "A vague impression of a control panel is visible through the blurry, tempered glass windows that face the door."
    hide graynvl
    show 928 right damage1
    show 637 left
    with dissolve

    play music "minesong2slowed.ogg"

# TODO bunny glitch
    n @ open "If we can get into that security room, we could open the barrier."

    s @ sneer "Are you going to, uh, hack it open or something?"
    show 637 neutral

    n @ open "Not from out here, I'm not."
    show 637 smile

    "928 brings her hand to her chin, thinking through the problem."

    s @ hurtless "Yeah, much as I was a fan of the 'pry the door open' plan earlier? This one's too big."

    n @ smile "..." #smile

    s @ sneer "What about that window? I bet we could break in through there."

    "637 strides toward the rail closest to the window."

    n @ open "It's a security booth. That's reinforced glass. {w}For security."

    "637 pauses."

    s @ surprise "...Ah."

    "928 sighs and gazes upwards. {w}Another giant, dead fan is positioned above the checkpoint."

    n awkward "Hypothetically, that room's ventilation could be accessible through..."

    "She points to the fan."
    nvl clear
    n open "...there."
    show 928 shut

    s squint "..."
    extend sneer "!"
    show 928 smile

    s drool "Sounds fun. I'll get my grapple ready."
    window hide


    scene bg office with fade
    window show
    # a "{i}CLANG!{/i}" #TODO clang!
    

    a "928 and 637 drop through the ceiling of the security booth through the vent."
    a "They kneel upon landing, weapons at the ready, scanning the unfamiliar room."
    a "The vent was intact when they found it. {w}The only way a threat could have entered the room would be an alternate security door. {w}However, both entrances appear untampered."
    show 928 right damage1 hshut
    show 637 left hgrin
    with dissolve
    # TODO bunny glitch
    s @ hgrin "Looks clear to me!"

    n @ hopen "Affirmative."

    show 928 shut
    show 637 smile
    "The room is a mess. A contrast from the barren residential complexes that housed workers above."
    "Personal belongings are strewn across desks. {w}Abandoned outerwear lies on chairs. {w}Dishes, cups, cans, and paper waste cover the cubicle desks, as well as the gate control table."

    s @ scowl "Wow, what a wreck. I suppose these guys had to clear out quickly. {w}That, or they just lived like this."

    show 637 sneer
    "637 walks over to a desk chair and takes a seat.{w} She lifts up a white mug with the Laskey Solutions logo printed on it. {w}Dark residue lines the bottom. {w}She scoffs and reclines in the cushioned chair, kicking her legs up onto the desk."

    s @ sincopen "Ahh. Sure beats sitting on the floor. {w}We could stand to take a rest here, honestly."

    show 928 dull
    show 637 smile
    "928 stares at the glazed window that faces the processing facility. {w}The fiery light filtering in gives the room an orange tinge."

    s @ open "But I guess we gotta find a way to open that door first, right?{w} 928?"

    show 928 alert
    "Hearing her name, 928 snaps away from it and looks to 637."

    n awkward "Oh, yeah! "
    extend open "Agreed."

    show 928 shut
    s @ hurtless "How about I have a look around here, and you do some crazy hacker shit on that computer."

    n @ shine "Pff. "
    extend smile "Okay. I'll see what I can do."


    "928 approaches the control table and takes a look over the array of computer monitors that cover its surface. {w}They display power usage data and camera feeds, though they're filled with static."
    "A keyboard sits next to a screen which prompts for credentials.{w} She blows the dust off of its surface."
    hide 928 right with dissolve

    show 637 squint
    "637 rifles through more items from the cubicle desks.{w} Playing cards, napkins, pencils, quite a few crushed aluminum cans."
    "Beneath a piece of notebook paper, she spots a card labeled 'SECURITY.'{w} Turning it over, the back reads 'LEVEL FIVE ACCESS.'"

    s sneer "Wow. Laskey sure knew how to pick their security staff. {w}So responsible."

    show 637 smile
    "She grabs the key and checks on 928's progress."
    show 637 squint
    "637 finds her kneeling under the desk.{w} Her head and hands are hidden behind the tangle of wires spilling out from the partially dismantled computers."

    s @ hurtless "928?"

    stop music fadeout 5.0

    n "Ah!"
    show 637 neutral
    n "{cps=80}I was seeing what I could manage for a manual override, since we don't have any credentials. What was that about stopping here? We could go a bit longer without a recharge, but this might take a while.{/cps}{nw}"
    show 637 smile
    n "{cps=90}Not sure though, I still have to see what I'm working with in terms of the circuitry under the card reader... There are a bunch of camera feeds that lead here, but I don't think those will be much help.{/cps}{nw}"
    show 637 elated
    n "{cps=100}I'll go ahead and cut them off before we leave. Oh, and since we have a way to proceed we might as well rest–{/cps}{nw}"

    # note: make above segment scroll fast in the text box to indicate rambling

    s @ hurtless "Hey, nerd. Look here."
    show 637 smile
    "It takes 928 a moment to free herself from the nest of cables she's caught in."
    show 928 right fluster damage1 at moredown
    with dissolve
    "Finally, her head pops out from under the desk. {w}Still on her knees, she spots the access key that 637 holds out to her and takes it."

    s @ wink "Level five! We're good to go."
    hide 928 right
    show 928 right damage1 shine
    with dissolve
    "Excitement dawns on 928's face."

    n @ pleadgrin "Wait, where did you even-!?"
    show 928 smile

    s @ sincopen "Dug for buried treasure."

    "928 giggles and takes the card, still staring at it in disbelief."
    
    "She looks up at the card reader, then back down at the tangle she'd been working on. "
    show 928 bummed
    extend "637 spots a grimace on her face."

    s @ hurtless "Oh, that card's no good?"
    show 637 sincere
    n @ fluster "No, no. The card's almost certainly fine, I just- "
    extend @ awkward"Ah, never mind."

    s @ sneer "Bummed your little wire-game got cut short?"

    n @ awkward "Uh, no, no, it's fine. {w}This works better."

    s @ open "Come on, 928.{w} Be real with me. "
    extend @ sincopen "What's the matter?"

    play music "angelsslowed.ogg"

    show 928 plead
    "Flustered, 928 extricates herself from beneath the desk. {w}She stands, gazing at her feet, and hands the card back to 637."

    n @ awkward "I just... um... {w}We've been at it for a while. If that opens the gate for us right away, then, well..."

    show 637 neutral
    "637 turns the card in her hand."

    s @ open "We'd have to keep moving instead of stopping in here to recharge?"

    n @ pleadgrin "Well, yeah. {w}We need to make an upload sometime, and it's quiet in here, and I thought it'd be nice to stop for a bit. "
    extend @ awkward "So we can... uh... y'know. {w}Have a moment."

    s @ hurtless "You mean, take an actual break? And not push forward?"

    n @ pleadgrin "Y-yeah.{w} I mean, we made plenty of good headway, and I {i}could{/i} just say I had to spend more time rewiring things, if anyone asks."
    # n @ pleadgrin "Y-yeah, I mean, we made plenty of good headway, and it's not like I can't say I {i}didn't{/i} need to spend a lot more time in here rewiring things..." #TODO

    s @ drool "What's going on with you, 928? {w}Your mind should be on the mission, not on breaks!"
    s @ sneer "What would our benevolent overlords think if you misallocated, like, {i}one whole hour.{/i} {w}That's time you could spend enriching the company!"

    n @ shine blush "...pffft. {w}Cut it out..."
    show 928 smile

    s @ sincopen "Okay, okay. So, we {i}didn't{/i} find the card. {w}Oops! Guess that means we've got a lot of time to kill in here. {w}Together.{w} Alone."

    n pleadgrin "Y-yeah. {w}Um. Okay. {w}Haha."

    show 637 sneer
    show 928 fluster
    "637 leans towards her with a smug grin on her face."
    
    s @ drool "So. What'cha wanna do?"
    show 928 dizzy2
    extend " Make out or something?"

    show 928 dizzy3
    show 637 smile
    "928 turns beet red."

    n @ dizzy4 "..."

    s @ drool "Oh my god, you're so easy! {w}Haha."

    show 928 shine blush
    show 637 elated
    "928 grabs 637's right hand. They both snicker."

    s sincopen "It's all over your face. {w}Come on. Fess up."
    show 637 sincere
    show 928 plead -blush
    "928 looks down to the floor."


    s @ sincopen "Look, there's no shame in it. {w}Talk to me, 928. What do you want?"

    n @ pleadgrin "Okay. Um.{w} I think I want to be close with you."

    s @ sneer "Yeah?"

    n @ pleadgrin "And I've been thinking about what happened earlier. {w}In... um... the residential district. {w}I don't know... i-it's kind of embarrassing. {w}Um... I just..."

    "637 raises an eyebrow."

    s @ hurtless "...Go on."

    n pleadgrin "Okay. Look. {w}I don't know if it's the way you talk, the way you act, the way you smile..."
    n dizzy1 "But the more I'm with you, I keep finding myself more and more drawn in.{w} It makes no sense. I have half a mind to tell you off, but..."

    show 928 dizzy2
    s @ wink "But?"

    n @ dizzy1 "I can't stop thinking about, uhm.{w} When you repaired me... the s-spray... and how you held me after...{w} And I liked kissing you..."
    show 637 elated
    "The silence is unbroken by 637. {w}She lets the stammering thing in front of her continue at its own pace."

    n @ dizzy1 "I just... I keep replaying it in my head. {w}I try to shake it, but I can't really stop thinking about it..."

    show 928 dizzy3
    show 637 sneer
    "637 snickers."

    s @ sincopen "Is that so?"

    show 637 elated
    n pleadgrin "Y-yeah! It was intense. {w}It hurt a lot, of course, but that aside, uh, w-what confuses me is, even though I shut off my dampeners..."
    n "It wasn't like regular pain? {w}Maybe it was nice because it was {i}you{/i} doing it... {w}But when I was lying there, and you helped me recover..."
    n dizzy1 "It felt nice to lose track of everything else in the fog of it all? {w}I was helpless, but you were holding me, and I just..."
    n despair "Aagh. Never mind. {w}There must be some wires crossed in my head or something."

    show 928 plead
    show 637 sincere
    "637 sets her hand on 928's cheek."

    s @ sincopen "Hey, look. {w}If I'm being honest, I got a rush from it too."
    s @ hurtless "To be clear, I obviously didn't like seeing you having a giant gash on your chest, but..."
    s sincopen "Being in control, taking care of you, watching you squirm... "
    extend @ sneer "Wow."

    show 928 blush fluster
    show 637 blush bummed
    "They both have a moment of quiet, too flustered to speak."

    s @ blush hurtless "...That doesn't make me a fucked up bitch, right?"
    show 637 neutral
    show 928 shine

    n "No, haha... I don't think so."
    n awkward "In fact, I think I'd actually like to be like that again... If you'd wanna try."

    show 928 plead
    s @ open "Try it again? Like, me take control?"
    

    "928 nods, eyes still toward the ground."

    s @ hurtless "Shit, okay... Since you asked so nicely..."

    show 928 alert
    "She leans in close and wraps a hand around the back of 928's head, splaying her fingers in her partner's hair."

    s sneer "You know something, 928? {w}I thought you were such a square at first. So focused on the mission. Making your commander happy."
    s @ drool "Now look at you. {w}All messed up by me."

    show 928 fluster blush
    "The sound of her voice sends shivers up 928's spine. {w}637 bears a sharp grin."

    show 928 plead

    s @ drool "Really, I should be the one in charge of you, not her.{w} Don't you think?"

    show 928 despair
    "The fingers in 928's hair tighten into a grip. Her blush intensifies. She nods."

    show 928 plead
    s @ hurtless "Look at me."
    show 637 squint

    "928 draws her gaze to 637's face. They're so close."

    s @ hurtless "You need a break, and so do I. {w}We're gonna take some time for ourselves, and I'm gonna take good care of you.{w} We can take it slow. You just let me know if I'm on the right track. {w}Okay?"
    show 637 neutral

    n @ pleadgrin "Yeah..."

    s sneer "Good. {w}Now, I'm gonna mess you up a bit more."

    "Her eyes drop down to 928's torso."

    show 928 fluster
    s @ drool "I think I wanna punch you in the stomach... Then maybe drop you to the floor. {w}Sound good?"

    n dizzy1 "...W-Wow. {w}Um, yeah."

    show 928 dizzy2
    "928's eyes shut tight. She nods hard. {w}637 grabs her by the chin to stop her."

    s @ hurtless "I need you to say it, though. You gotta ask for it."

    n despair "...p-please..."

    show 928 alert
    "637 lets go of her chin. 928's eyes go wide."
    show 928 plead

    s scowl "No.{w} The whole thing. Say what you want me to do."
    show 637 sneer
    nvl clear

    n pleadgrin "Nnnh... I want you to punch me in the-"
    n hurt "AH!"
    window hide
    hide 637 left
    hide 928 right
    with dissolve
    window show
    a "637's fist lands in the center of 928's abdomen with a thump.{w} Not enough to damage the fragile thing in front of her. {w}But more than enough to make an impact."

    a "The threads composing 928's thoughts snap in an instant. {w}Her vision fills with noise, and she drops to her knees."
    a "The blow radiates from her lower torso, searing and hollow. {w}Her throat tightens. {w}Panic blots her mind as she gasps for air she doesn't need."
    a "She nearly collapses, but 637 quickly moves to help stabilize her, easing her down until she settles on her knees. {w}Grabbing her by the headgear, 637 brings her partner's head close to her lower torso. {w}She strokes 928's hair."

    a "\"God, you're cute down there. That position looks good on you... {w}How's it feeling?\""

    a "The phantom choking feeling subsides, but the words in 928's head are all jumbled. {w}Still, she attempts an answer."

    a "\"...Mmmnn...{w}Hahhhah...\""

    a "637 sees a wide, crooked smile forming on 928's face."

    a "\"...Good...hhhnnn...\""

    a "\"Atta girl~\""

    a "She kisses her on the lips, and the two of them tumble down onto the floor."

    window hide
    nvl clear
    show gray overlay with dissolve
    window show
    with dissolve
    stop music fadeout 5.0

    a "Before long, the Canaries will have to enter the mineshafts proper, and approach the end of their search."
    a "For now, though, the keycard lies on the back of an office chair. Its lanyard dangling aimlessly."
    a "The mission can probably wait a few hours."
    window hide
    

    show black with slowdissolve

    "END TRANSMISSION 4"
    $ renpy.pause()

    jump chapter5