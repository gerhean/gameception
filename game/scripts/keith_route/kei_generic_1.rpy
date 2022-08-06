# Outline:
# Help Keith with creating props for the cultural festival

label kei_generic_1:
    scene bg_classroom_05_day
    show kei smile
    with fade

    l "Hey."
    e "[name] dude! I'll be working on the props for the play soon."
    menu:
        "Got something to do.":
            e "I got this dude, Don't worry!"
            jump day_manager
        "Do you need help?":
            e "I knew I can count on you dude!"

    stop music fadeout 1.0
    queue music "audio/music/vntrack06_nostal.mp3"
    scene bg_classroom_05_day
    show kei wonder
    with fade

    e "Huh, how are these things supposed to look like..."
    "With only vague instructions for the props, you had to draft out the designs."
    "You felt your creativity go up!"
    $ stat_creative_flag += 1
    jump day_end_manager