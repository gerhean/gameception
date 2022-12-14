# Invite two friends to rush the deadline of the game
# Only friends with r3 done can be invited
# If game cannot be done, you will game over.

default ame_ring_accept_flag = False
default eve_ring_accept_flag = False
default kei_ring_accept_flag = False

label weekend_3:
    stop music fadeout 1.0
    queue music "audio/music/vntrack20_funky.mp3"
    scene bg_room_noon
    with fade
    "It's the last weekend before the submission deadline of my game!"
    "I better call for help, and fast!"
    $ ame_ring_flag = False
    $ eve_ring_flag = False
    $ kei_ring_flag = False
    jump weekend_3_call

menu weekend_3_call:
    "Who should I call for help?"
    "Amelia" if not ame_ring_flag:
        play sound "audio/sound/phone_vib.ogg"
        "Phone" "Ring... Ring..."
        $ ame_ring_flag = True
        if stat_knowledge_flag >= 6:
            a "Yay! Thanks for inviting me!"
            $ ame_ring_accept_flag = True
        else:
            a "Thanks for calling me, but I'm stuck studying..."    
        jump weekend_3_call

    "Everlyn" if not eve_ring_flag:
        play sound "audio/sound/phone_vib.ogg"
        "Phone" "Ring... Ring..."
        if stat_understand_flag >= 6:
            a "I'll be glad to help!"
            $ eve_ring_accept_flag = True
        else:
            a "Sorry, but I'm a little busy."
        $ eve_ring_flag = True
        jump weekend_3_call

    "Keith" if not kei_ring_flag:
        play sound "audio/sound/phone_vib.ogg"
        "Phone" "Ring... Ring..."
        if stat_creative_flag >= 6:
            k "Sure man, anything to help!"
            $ kei_ring_accept_flag = True
        else:
            a "Sorry man, but there's something I need to deal with."
        $ kei_ring_flag = True
        jump weekend_3_call
    
    "I'm ready!" if ame_ring_flag and eve_ring_flag and kei_ring_flag:
        jump weekend_3_work


label weekend_3_work:
    stop music fadeout 1.0
    queue music "audio/music/vntrack04_adventure.mp3"
    scene bg_room_noon
    with fade

    if ame_ring_accept_flag:
        show ame smile_casual
        voice "ame/hey"
        a "The submission deadline is tomorrow night right?"
        a "I'm super confident I can pass the make up test on Monday anyway!"
        a "So I have come to help you!"
        a "Hurry! We don't have much time left!"
        hide ame
    if eve_ring_accept_flag:
        show eve smile_casual
        voice "eve/good_morning"
        e "This is my first time visiting a friend's house..."
        e "Since the deadline is near, I'll try to put in my best effort!"
        hide eve
    if kei_ring_accept_flag:
        show kei smile_casual
        voice "kei/whatsup"
        k "Woah, your room's pretty cool!"
        k "But there's no time to play around right?"
        k "After all, the submission deadline is tomorrow!"
        hide kei

    show screen game_progress_menu_ui
    if ame_ring_accept_flag:
        scene bg_room_noon
        show ame smile_casual
        with fade
        "As always, you are impressed by the quality of artwork which Amelia produced."
        $ creative_progress += 2 * (stat_knowledge_flag - 1)
        if creative_progress > required_progress:
            $ creative_progress = required_progress
        play sound "audio/sound/grow.ogg"
        "The art for your game is now closer to being done!"
    if eve_ring_accept_flag:
        scene bg_room_noon
        show eve smile_casual
        with fade
        "You are in awe of Everlyn's coding skills."
        $ knowledge_progress += 2 * (stat_understand_flag - 1)
        if knowledge_progress > required_progress:
            $ knowledge_progress = required_progress
        play sound "audio/sound/grow.ogg"
        "The code for your game is now closer to being done!"
    if kei_ring_accept_flag:
        scene bg_room_noon
        show kei smile_casual
        with fade
        "You are impressed by Keith's extensive knowledge on games."
        $ understand_progress += 2 * (stat_creative_flag - 1)
        if understand_progress > required_progress:
            $ understand_progress = required_progress
        play sound "audio/sound/grow.ogg"
        "You are now clearer about the design of the game!"
    scene bg_room_noon
    with fade
    call self_game_progress from _call_self_game_progress_3
    
    scene bg_room_evening_light_on
    with fade
    if eve_ring_accept_flag:
        show eve smile_casual
        e "Sorry, but I have to leave soon."
        e "There's work I need to do tommorrow as well, so I am not able to come over."
        voice "eve/goodbye"
        e "Still, best of luck to you."
        hide eve
    if kei_ring_accept_flag:
        show kei smile_casual
        k "Woah, time really passed quickly! I'll have to go off soon."
        k "Anyway, I promised to meet up with my other friends tomorrow."
        voice "kei/sorry"
        k "So I won't be able to accompany you on the last stretch."
        k "Still, good luck! You're almost there!"
        hide kei
    
    if ame_ring_accept_flag:
        jump weekend_3_night_ame
    jump weekend_3_night_alone

label weekend_3_night_ame:
    show ame smile_casual
    a "Hey, I need to prepare my own submission for the festival."
    a "So I can't help you tomorrow."
    if stat_ame_flag < 3:
        a "Anyway, I had fun today like always!"
        voice "ame/bye"
        a "Bye bye!"
        jump weekend_3_night_alone
    
    stop music fadeout 1.0
    queue music "audio/music/vntrack06_nostal.mp3"
    show ame emb_casual
    voice "ame/laugh"
    a "But if you d-don't mind, can I stay over for the night?"
    a "Just like in the old times..."
    menu:
        "Sorry...":
            l "I'm not sure how our parents will think about that..."
            show ame smile_casual
            a "You fell for it you fool!"
            a "Did you actually believe I'll be so bold to do something like this?"
            show ame sad_casual
            a "Hahaha..."
            a "Anyway, I had fun today like always!"
            voice "ame/bye"
            a "Bye bye!"
            jump weekend_3_night_alone
        "W-well, if that's what you want.":
            $ stat_ame_flag += 1
    l "I mean... It'll make me really happy if you slept over."
    l "I know the past month had been hard for you, and you still have work to do."
    l "But if you need someone to be with, I'll always be there for you."
    voice "ame/gasp"
    a "[name]!"
    a "I-it was supposed to be a joke you dummy!"
    a "But if that's what you want... Let me call Mom first."
    scene black
    with fade
    "Phone" "Ring... Ring..."
    "..."
    scene bg_room_evening_light_on
    with fade
    show ame emb_casual
    a "T-that's weird... Mom didn't oppose it at all..."
    a "I have no choice then!"
    show ame smile_casual
    a "Boot up the Switch! Whoever wins at Smash will get to sleep on the bed!"
    l "Bring it on!"

    stop music fadeout 1.0
    scene black
    with fade
    $ calendar.next()
    "There is only 1 day left until the submission deadline."

    queue music "audio/music/sunny_day_happy.ogg"
    scene bg_room_noon
    with fade
    "When I came to, I was on the floor..."
    l "Huh... Did I lose at Smash? What even happened last night..."
    "But as I tried to get up, I felt a soft weight on my arm."
    l "Amelia..."
    show ame emb_casual
    voice "ame/laugh"
    a "Ahaha! Seems like we both passed out while playing. It had been a tiring day after all."
    a "Look, the TV's still turned on."
    l "Haaa... Look what you've done, now my arm's all sore."
    show ame smile_casual
    a "Sorry..."
    a "But I truly don't regret using your arm as a pillow."
    voice "ame/laugh"
    a "AHAHAHA!"

    stop music fadeout 1.0
    queue music "audio/music/vntrack20_funky.mp3"
    scene bg_room_noon
    with fade
    n "After having breakfast and waving goodbye to Amelia, I got back to work."
    n "Having seen how hard she worked, I couldn't possibly disappoint her!"
    nvl clear
    nvl hide
    jump weekend_3_work_2

label weekend_3_night_alone:
    stop music fadeout 1.0
    scene black
    with fade
    $ calendar.next()
    "There is only 1 day left until the submission deadline."
    queue music "audio/music/vntrack20_funky.mp3"
    scene bg_room_noon
    with fade
    "It's the last day I can work on my game. Time to get serious!"
    jump weekend_3_work_2

label weekend_3_work_2:
    show screen game_progress_menu_ui
    call self_game_progress from _call_self_game_progress_4
    scene bg_room_evening_light_on
    with fade
    queue music "audio/music/vntrack06_nostal.mp3"
    if knowledge_progress == required_progress and understand_progress == required_progress and creative_progress == required_progress:
        $ game_completed_flag = True
        "The game turned out amazing!"
        "But I still felt a little nervous when I hit that submit button on the website."
        "Hopefully, it will be well recieved by the judges..."
    else:
        "The game didn't feel very finished."
        "But there is no more time left to work on it."
        "I could only submit the incomplete game, and hope for the best..."

    stop music fadeout 1.0
    scene black
    with fade
    $ calendar.next()
    "4 days left until the cultural festival begins on Friday."
    jump epilogue_0_sick