

label chapter6:
    # "Chapter 6"
    "TIMESTAMP - ????? - SAFEHOUSE"

    scene bg fight
    play music "minesong2.mp3"

    a "\"Wake up, unit 928.\""
    a "Searing light floods 928's head as she flits open her eyes."
    a "Ears ringing, sight blurred, she attempts to make sense of her surroundings."
    a "She hears muffled, distant bangs.{w} She's sitting on a chair. {w}Blinking regulates the light, but not by much."
    a "There's something tall standing over her, but the shape isn't coming together."

    
    a "\"There you are.\""

    a "That voice."

    a "A human hand grabs her by the cheeks with a familiar roughness.{w} The figure comes into view. Its eyes pierce through the haze in 928's head."
    window hide
    show 928 right haze1 damage1
    show vogan smile
    with dissolve

    "Her commander."

    c @ pout "You went missing for quite some time! Something must be wrong with your tracker, little bird."
    c @ grimace "At first I assumed Neuman got to you first... but what do you know? {w}36 hours without reporting, and here you are, still operational. {w}With my prize in your hands, no less."
    c @ sneer "I can't say I'm disappointed... {w}Though I am curious how that tracker of yours went offline. {w}You wouldn't happen to know anything about that, would you?"

    show vogan frown
    show 928 haze3
    "928's still foggy. {w}She fails to respond to the inquiry, but she starts to sort through the words. {w}Something about her tracker...?"
    show 928 bummed
    extend " She looks up with a dazed expression."

    c @ grimace "Hm. Nothing? {w}Well. Regardless."
    show 928 haze1
    "Her commander lets go and takes a step back."
    show vogan smile
    "The expression on her face is difficult to make out, still blurry. {w}In her hand, a glass ampule shines a brilliant blue. She turns it over and studies the glow."

    c grimace "You did well to find the Stellisite tucked away in such an unusual place. {w}It gives me high hopes for your future assignments."
    c sneer "However, I must say, the manner in which this mission concluded was deeply untenable."
    show vogan frown
    show 928 haze4
    "928 furrows her brow."

    c @ sneer "You seem confused. {w}This retrieval was a failure. You failed to report your discovery. {w}You understand the ramifications of this, don't you, unit 928? Respond."
    show 928 haze1
    "928 looks down and feels something wilt inside her chest. {w}The ground starts to come into focus."

    show vogan smile
    n @ haze2 "...yes, sir."
    show 928 haze3
    "928 spots the sidearm dangling from her commander's hand."

    c pout "You know the punishment for failing a mission, 928. {w}Be grateful that we were able to clean up this mess. {w}We just had to follow the last part of your uploaded path..."
    c sneer "...and from there, well. Let's just say another little birdie said hello."
    show vogan frown
    show 928 haze1
    "928 can't get her head straight. {w}Something is wrong. Someone else should be with her. "
    show 928 bummed
    extend "Her eyes adjust, yet she finds no one around but her commander. {w}Where is–"

    c pout "Tsk, tsk. Looking for something, are we?"
    show vogan smile
    show 928 haze4
    "The sensation of a metal barrel beneath her chin draws back her attention."
    show 928 dull
    c @ sneer pinch "Listen."
    show vogan frown
    show 928 haze3
    "The commander pulls the revolver away and caresses its cylinder with her thumb."

    c sneer "Don't think I'm solely placing the blame on you.{w} I did some research on the unit you were partnered up with.{w} Not my first choice... But perhaps if we were less pressed for resources, we could have sent you with an adequate counterpart."
    c pinch "It's a miracle the thing hadn't already been reformatted. {w}I don't need it getting the chance to spread {i}behavioral malfunctions{/i}."
    show 928 haze4
    c -pinch pout "But I know you, little bird. {w}You just need a little guidance to start seeing things clearly again. {w}That's why I'll give you another chance. Whatever it talked you into doing with your tracker... {w}I'll see about repairing it, shortly."
    c grimace sweat "And we can go right back to business as usual. {w}No more stress, no more confusion. "
    
    extend creepy "All you need to do is help navigate through this... predicament."
    show 928 haze3
    "Nothing in the room is familiar to 928, save the woman reprimanding her. {w}Bangs of gunfire resound from the doorway. How long has she been out?"

    c sneer "My men are outside in the tunnels, defending our prize from Neuman-Keere, which we were so regrettably delayed in securing."
    c grimace -sweat "There is still time, however, to salvage this mission. {w}You found the stellisite. It's in our hands. {w}All that remains is extraction, a task you were built to handle."
    c frown "Listen closely. {w}You will escort me and the stellisite through this battle, back to the surface. {w}If anyone gets in our way, Neuman or Etheridge, you have my full permission to dispose of them."
    c grimace "After we have escaped, and I have delivered the stellisite to headquarters, your mission will be complete, and I will be very proud of you.{w} Understood, little bird?"
    show 928 haze1
    n "..."

    c frown sweat "Unit 928. Respond."
    show 928 haze4
    "928 gulps. Her gaze is fixed on the floor. {w}The Commander always hated when 928 looked her in the eyes."
    show 928 distress
    "It takes all her strength to fight the gravity of compliance. {w}To veer away from the mental pathways carved into her for as long as she can remember. {w}The urge to respond with an affirmative is only staved off by the thought of her absent partner."

    c anger1 "Respond, unit 928. Do not waste my time."

    "A muffled explosion shakes the room. {w}Commander's head swivels toward the door in surprise. 928 mutters."
    show vogan frown -sweat
    n @ haze3 "...{w}w-where is she...?"
    show 928 haze4 -distress
    c @ sneer "'She'?"

    "The commander raises an eyebrow."

    n @ despair "...where is 637?"

    show vogan smile
    "Her curiosity shifts to bemusement. She laughs."

    n @ yelp "What... {w}what happened–"
    show 928 haze4
    c sneer "6-3-7."
    show 928 bummed
    "The numbers drip off her tongue with disdain."

    c grimace "We found the thing making an awful deal of noise, running off with the strongbox you located.{w} I suppose it makes sense, really."
    c sneer "Find the stellisite, subvert its partner's tracking device, and take the treasure right to us.{w} A desperate bid for approval, perhaps."

    show vogan frown
    show 928 haze3 distress
    "928 shudders."

    c sneer "However, I don't tolerate the sabotage of company equipment. {w}It had to be punished. And we needed answers about the stunt it pulled with your tracker."

    show 928 alert
    "928 looks up, alarmed. {w}She needs to get to 637. {w}If they were questioning her, she should be nearby."

    c @ pout "Oh, please. Don't tell me you've grown {i}attached{/i} to the thing."
    show vogan frown
    show 928 fluster -distress
    "Commander Vogan examines 928 as she eyes the door and stirs with intent. Pathfinding. {w}The humor drains from the Commander's expression. {w}928 pauses at the distinct click of a revolver's hammer pulling back."

    c @ sneer pinch "It's worse than I thought. {w}Perhaps it's broken more than just your tracker."
    show 928 haze4
    "The commander rolls her neck and points the muzzle down towards 928."
    c @ sneer "No matter. That unit has been dealt with. {w}It won't disrupt you ever again."
    show 928 alert distress
    "The finality in her tone stuns 928. {w}A gaping, hollow feeling wells up in her core."
    show 928 haze4

    c sneer "The networks in your head may be fragmented. {w}You know, when inessential stimuli data builds up in a Canary's memory, without regular intervention, its neural capacities can begin to fray."
    c smile "Senses go haywire, logic gets tangled, and soon enough, it loses total grip on reality.{w} It starts to experience hallucinations, perceiving them as truths. Revelations, even."
    show 928 haze3
    c pout "We can only {i}pray{/i} the damage to its surroundings is minimal."
    c smile "So much uncertainty and distress, both for the unit and the company. {w}So there's only one path for a malfunctioning unit. Reformatting, or disposal."
    c creepy "But you used to be one of my best. {w}So I'll give you a chance to come back to me, little bird. I need you to prove your loyalty."
    show 928 haze4
    "Each word out of her commander's mouth dredges up an unfamiliar feeling in 928. {w}It fills the hollowness in her with a dark, roiling substance on the verge of ignition."

    c sneer "You will cast aside these thoughts of 637. {w}You {i}will{/i} assist me in returning to the surface. {w}And when this is all over, we can discuss how to mend your transgressions, understand?{w}... Respond."

    "The tips of 928's fingers tremble, but she maintains a blank face. {w}Return for what? To be made to forget everything? To be exploited until the day she breaks? {w}No. She made her choice hours ago."
    
    "A part of her knows she should hide the storm brewing in her for just a bit longer, but the commander's words dig at 928. "
    show 928 bummed
    extend "Images of a 'dealt with' 637 flash through her mind."
    # maybe need something here TODO
    show 928 mad
    show vogan anger1 sweat
    "She stares into the human's eyes, silent."

    c @ anger2 "RESPOND, UNIT 928!"

    show 928 rage
    "Enough. "
    extend "928's practiced restraint breaks. "
    show 928 combat
    nvl clear
    extend "She engages her right arm. The blade deploys, and–"
    hide 928 right
    hide vogan
    "{i}BANG!{/i}" #TODO bang
    show 928 right hurt damage2
    n "AAGH!"
    hide 928 right

    a "The round pierces the joint attaching 928's forearm. {w}Her bladed limb lashes back, dislocated and suddenly numb. {w}She reels and clutches her elbow. {w}The bullet inside her still spins, molten hot."
    a "Her mind floods with visceral, static noise."
    show vogan
    c sneer pinch "You useless fucking {i}robot{/i}."
    hide vogan
    a "928 starts to move her legs in a desperate bid to get away, barely registering the shape closing in on her face. {w}The butt of the revolver smashes straight into her forehead, snapping her head backwards."
    a "The impact splays her out onto the ground, face up. {w}The commander takes a few steps back, and reaches into a black duffel bag."
    a "The room spins as 928 lays. {w}The light dangling from the ceiling burns into her vision."
    a "The noise in her head recedes into a serene, eerie calm. {w}She pictures 637. The way she snickered. Her verbal jabs. {w}The look on her face when she took charge. Her embrace."

    a "928's vision sharpens. She props herself up on her uninjured arm."

    a "Commander Vogan lifts a shotgun out from the bag in the corner. {w}She pumps it."

    a "928 raises her left arm. {w}The panels slide open and back, readying her gun."

    a "The commander spots the motion and darts for cover. {w}She aims back at 928 with the shotgun as she moves."
    
    a "928 fires first." # bang! TODO
    show vogan
    c anger2 sweat "FUCK!"
    hide vogan
    a "The blast grazes the lower side of her torso, beneath her body armor. {w}Blood seeps into her now torn outfit. {w}It throws her balance, but she stabilizes herself just long enough to return fire."

    "{i}BOOM!{/i}" # bang! TODO

    a "The shot is off-center from 928's torso. {w}The slug tears her injured arm apart below the shoulder. {w}The joint is severed completely, as cables fray and sparks fly."
    a "Shrapnel from the blast flies into her shoulder and embeds itself in a swath of the skin on her torso. {w}The sensation is agonizing."
    a "Dampening just enough of the pain to stay stable, she reorients herself. {w}She settles on a course of action in a split second."
    

    a "928 lurches forward, staying close to the ground.{w} Her gun arm shifts back to a ready hand."

    a "The commander is up against the wall. {w}By the time she pumps the shotgun, 928 has already closed the distance. {w}Gritting her teeth, she clutches the barrel of the firearm and pushes upwards as hard as she can."
    
    hide window
    nvl clear
    show cg fight with dissolve
    $ renpy.pause()
    show graynvl
    a "It fires into the rock ceiling with another bang."

    a "The kickback finally loosens 928's grip.{w} Her commander yanks the gun to the side, rotating it away from the Canary."
    a "In an instant, 928 faces the stock of the weapon. {w}Her commander rams into her nose."
    a "The human tosses the shotgun aside and lunges at the staggered machine." #TODO decide who tosses the shotgun away.
    # a "With a reflexive grasp, 928 manages to wrest the shotgun from her control. She throws it to the other side of the room. The commander wastes no time in the opening and lunges at the staggering machine."

    a "She pins 928 to the ground and grips her left arm tight. {w}With her other hand, she unholsters her revolver."
    a "928 strains against her and thrashes her legs. {w}The commander leans in close and jabs the muzzle into 928's lower jaw. {w}She cocks it."

    a "\"...Sleep now, songbird.\""

    a "Her voice is unsteady, caught between tired breaths."

    a "Panic overrides 928's mind. {w}Electrical signals ripple through every part of her.{w} Despite the restraint on her gun arm, she charges a shot."

    a "Her mutilated upper arm shifts at the shoulder. {w}Pain surges through her as she jabs the mess of live-wiring and metal into the wound on the human's lower side."
    a "The commander screams and seizes up, losing her stability to the shock."


    a "928 rolls over beneath her opponent, and releases the charged shot into the commander's torso."
    hide cg fight
    show white
    stop music fadeout 5.0
    a "There is a flash of light. {w}The human's body ceases to function. {w}It collapses to the floor."
    hide graynvl
    window hide
    hide white with slowdissolve
    nvl clear

    window show
    a "When 928's thoughts return to her, they consist only of her partner. {w}She begins to limp towards the doorway."
    a "She needs to find 637, wherever they put her. {w}It doesn't matter what they did to her. {w}928 needs to be with her, or at least, whatever's left of her."
    a "Something starts to sting."
    show 928 right damage2 grit
    "928 keels over."

    n hurt "...uh...{w}ugh..."

    "Fluid builds in her eyes. {w}Her vision smears."

    n grit "...hahh..."
    extend hurt "nnngh...{w}s-..."
    extend despair distress "s-s-s-s-...{w}six..."

    "She whimpers. {w}Her mouth is so dry."

    show 928 alert
    "Something chimes in the back of her head." #TODO beep
    extend " It takes a beat for 928 to register it as a signal. {w}It's not from base. {w}She reads it out."

    "{i}\"tracker ping sent. response requested ;)\"{/i}"
    show 928 fluster -distress
    "928 goes silent.{w} Her mouth goes slack, and her breath pauses. {w}Catching herself, her torso suddenly begins to pound."
    nvl clear
    hide 928 right
    "Still dizzy, she gets up and dashes out of the safe-room."
    window hide

    scene bg bunks2 with slowfade

    a "Exiting the tunnels that echo with the sound of combat, the sleeping quarters are dark. {w}928 enters with her visor down, cautious.{w} Not far from the bodies, a humanoid figure sits slouched."
    a "Its arms are stretched upwards, wrists tied to a ladder on the side of the bunks.{w} It speaks in a husky, digital voice."
    window hide
    show cg rescue temp with dissolve
    $ renpy.pause()

    s "Heyyy... {w}{i}COUGH{/i}{w} ...You the stupid fuck from the heli again? {w}Thought I already spilled the details about my relationship with your mother."

    "New cuts and scratches overlap the old scars on her torso. {w}Dents line the metal on her limbs.{w} Her left eye remains swollen shut, and her nose is crooked."

    n "..."
    play music "angelsslowedB.ogg"

    "637's head hangs low, but her eyes look up as a pair of robotic legs like her own step into view."

    s "Wait... are-"


    "928 drops her combat composure and hurtles over to her partner. {w}She goes in for a kiss without slowing down. Their teeth collide."

    show 928 right damage2 alert
    show 637 left hurt damage

    s "Mmmph... Ow!"
    show 928 plead
    show 637 elated
    "They both recoil for a moment, before catching each other's eyes. {w}Wordlessly, they go for another kiss."
    show 928 smile
    s scared "928... Thank god you're okay!!!"
    show 637 bummed

    n awkward "I'm alright... Haha... {w}Just glad you're... Alive..."

    show 637 sadless

    "637 looks her in the eyes with apologetic sincerity."

    s sad "I'm glad {i}you're{/i} alive!!! {w}When I tried to get you up, you were still out cold, so I moved the stellisite outside the cache, hoping they'd quit looking for us and..."
    s hurtless "...Well basically, Vogan's a bitch."

    show 637 squint
    n @ open "Yeah... {w}about that..."
    n awkward "I neutralized her."

    s surprise "Seriously.{w} Holy shit."

    show 637 elated blush
    show 928 plead blush
    "637 blinks. {w}928 moves to start removing the bindings, but before she can lift herself up, her partner's lips press into hers, diverting her from the task. 928 shuts her eyes, and runs her hand down 637's back."
    "Eventually, they separate. {w}637 lets out a breathy whisper."

    s drool "...You're so cool."

    show 928 grit -blush
    show 637 -blush sneer
    "928 finally stands up to free her partner, but is reminded of the state of her body.{w} Weak. Damaged. Sparking from the shoulder."
    show 928 bummed
    "She swaps to her gun, and fires a shot at the chain. {w}It breaks open, scattering into links of red hot metal. {w}In the flash of light, 637 sees the damage for the first time."

    s scared "Holy shit, 928, you're missing an arm."

    n awkward "I'm sure it's no big deal.{w}Ahaha, ha..."

    show 928 grit
    "As the rush dies down, she starts to feel the weight of her body. {w}637 rises up to catch her, and props 928's functioning arm over her shoulder."

    s hurtless "I know now's not the time, but, girl. {w}You have GOT to stop brushing off injuries like this. {w}I need to repair this, {i}soon.{/i}"

    n pleadgrin "Okay,,, {w}But also... We should probably get the hell out of here."

    show 928 fluster
    show 637 sneer
    "637 snickers and smacks her on the back."

    s @ wink "Okay, tough girl. We'll fix you in a bit. {w}What's the plan {i}right now{/i}?"
    show 928 shut
    "928 replies over choppy breath."

    n @ open "We should leave the area. {w}Gotta distance ourselves from Etheridge. {w}And then from Neuman-Keere. Use the tunnels. They dunno what we know."
    show 928 smile
    s @ sincopen "Smart. Get around 'em. {w}Now let's make a breakaway before these idiots collapse themselves underground."

    "They move, before 928 stops them at the door."

    n blush awkward "...Hey. I love you."
    show 928 smile
    s sneer "I love you too, idiot."
    show 928 shine
    "She winks. Warmth runs through 928's face.{w} The two of them push forward into the fray."
    stop music fadeout 5.0

    show black with slowdissolve

    "END FINAL TRANSMISSION"
    window hide
    $ border_enabled = False
    scene cg end with slowfade
    play music "satellite.mp3"

    $ renpy.pause()

    "we dont have credits yet"
    "but mina and lena directed and wrote this"
    "lena did all the art"
    "mina did all the code"
    "yuki did the music"
    "jem did 2 cgs"
    "thank u for everyone"
    return