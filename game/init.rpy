init:
    #Text outlines
    $ style.say_thought.outlines = [(1, "000000", 0, 0), (1, "#202020", 0, 0)]
    $ style.say_dialogue.outlines = [(1, "000000", 0, 0), (1, "#202020", 0, 0)]
    $ style.pref_label_text.outlines = [(0.2, "000000", 0, 0), (1, "#202020", 0, 0)]

    $ leftoffset = Position(xpos = .35)
    $ leftoffset2 = Position(xpos = .15)
    $ rightoffset = Position(xpos = .65)
    $ rightoffset2 = Position(xpos = .85)
    $ chaptertitlespot = Position(xanchor = 0.5, xpos = 0.8, yalign = 0.95)
    
    # Character Initialization: These lines represent all the possible sprites you can call up. 
    # When adding new sprites, this is where you define them. If you rename the files, they have to be renamed here too. 
    # The "Color" value lets you choose a six hexadecimal color code for each character's name. 

    #Main Character Definitions:
    define T = Character("TALLARA", image = "T",voice_tag = "Tallara",who_color="#ffffff",what_prefix = '', what_suffix = '')
    define I = Character("IRIS", image = "I",voice_tag = "Iris",who_color="#ffffff",what_prefix = '', what_suffix = '')
    define L = Character("LAVERNA", image = "L",voice_tag = "Laverna",who_color="#ffffff",what_prefix = '', what_suffix = '')
    define M = Character("MAGNUS", image = "M",voice_tag = "Magnus",who_color="#ffffff",what_prefix = '', what_suffix = '')
    define S = Character("SURA", image = "S",voice_tag = "Sura",who_color="#ffffff",what_prefix = '', what_suffix = '')
    define E = Character("ELLIS", image = "E",voice_tag = "Sura",who_color="#ffffff",what_prefix = '', what_suffix = '')
    define D = Character("DAZA", image = "D",voice_tag = "Daza",who_color="#ffffff",what_prefix = '', what_suffix = '')
    define B = Character("BENTIS", image = "B",voice_tag = "Bentis",who_color="#ffffff",what_prefix = '', what_suffix = '')
    
    ##These are side characters who don't have images. 
    define Ace = Character("ACE", image = "Ace",voice_tag = "Ace",who_color="#ffffff",what_prefix = '', what_suffix = '')
    define Rhea = Character("RHEA", image = "Rhea",voice_tag = "Rhea",who_color="#ffffff",what_prefix = '', what_suffix = '')
    define Intercom = Character("INTERCOM", image = "Intercom",voice_tag = "Intercom",who_color="#ffffff",what_prefix = '', what_suffix = '')
    define Canteen = Character("GALLEY SERVER", image = "Intercom",voice_tag = "Intercom",who_color="#ffffff",what_prefix = '', what_suffix = '')
    define communications = Character("COMMS OFFICER", image = "Communications",voice_tag = "Communications",who_color="#ffffff",what_prefix = '', what_suffix = '')
    #Example of a night time character tint:
    image characternight = im.MatrixColor("sprites/Kaori/Uniform/pose 1/Kaori u shocked p1.png",
                                im.matrix.saturation(0.7)*im.matrix.tint(.9,.9,1)*im.matrix.brightness(-0.05))
    #Sprites:
    #Daza sprites:
    image D normal = "sprites/daza/D normal.png"
    image D speaking = "sprites/daza/D speaking.png"
    image D thinking = "sprites/daza/D thinking.png"
    image D confident = "sprites/daza/D confident.png"
    
    #Magnus Sprites:
    #normal outfit
    image M speaking n = "sprites/magnus/M speaking n.png"
    image M sigh n = "sprites/magnus/M sigh n.png"
    image M normal n = "sprites/magnus/M normal n.png"
    image M condescending n = "sprites/magnus/M condescending n.png"
    image M cocky n = "sprites/magnus/M cocky n.png"
    image M annoyed n = "sprites/magnus/M annoyed n.png"
    image M angry n = "sprites/magnus/M angry n.png"
    #combat outfit
    image M speaking c = "sprites/magnus/M speaking c.png"
    image M sigh c = "sprites/magnus/M sigh c.png"
    image M normal c = "sprites/magnus/M normal c.png"
    image M condescending c = "sprites/magnus/M condescending c.png"
    image M cocky c = "sprites/magnus/M cocky c.png"
    image M annoyed c = "sprites/magnus/M annoyed c.png"
    image M angry c = "sprites/magnus/M angry c.png"
    
    #Laverna Sprites:
    image L annoyed c = "sprites/laverna/L annoyed c.png"
    image L cheerful c = "sprites/laverna/L cheerful c.png"
    image L flirty c = "sprites/laverna/L flirty c.png"
    image L normal c = "sprites/laverna/L normal c.png"
    image L questioning c = "sprites/laverna/L questioning c.png"
    image L sarcastic c = "sprites/laverna/L sarcastic c.png"
    image L sigh c = "sprites/laverna/L sigh c.png"
    image L speaking c = "sprites/laverna/L speaking c.png"
    image L surprised c = "sprites/laverna/L surprised c.png"
    
    image L annoyed n = "sprites/laverna/L annoyed n.png"
    image L cheerful n = "sprites/laverna/L cheerful n.png"
    image L flirty n = "sprites/laverna/L flirty n.png"
    image L normal n = "sprites/laverna/L normal n.png"
    image L questioning n = "sprites/laverna/L questioning n.png"
    image L sarcastic n = "sprites/laverna/L sarcastic n.png"
    image L sigh n = "sprites/laverna/L sigh n.png"
    image L speaking n = "sprites/laverna/L speaking n.png"
    image L surprised n = "sprites/laverna/L surprised n.png"
    
    #Bentis Sprites
    image B angry = "sprites/bentis/B angry.png"
    image B annoyed = "sprites/bentis/B annoyed.png"
    image B confident = "sprites/bentis/B confident.png"
    image B confident2 = "sprites/bentis/B confident2.png"
    image B normal = "sprites/bentis/B normal.png"
    image B speaking = "sprites/bentis/B speaking.png"
    
    #Iris Sprites
    #Normal
    image I annoyed n = "sprites/iris/I annoyed n.png"
    image I confident n = "sprites/iris/I confident n.png"
    image I cool n = "sprites/iris/I cool n.png"
    image I questioning n = "sprites/iris/I questioning n.png"
    image I sigh n = "sprites/iris/I sigh n.png"
    image I sigh2 n = "sprites/iris/I sigh2 n.png"
    image I speaking n = "sprites/iris/I speaking n.png"
    image I surprised n = "sprites/iris/I surprised n.png"
    image I pleading n = "sprites/iris/I pleading n.png"
    #combat
    image I annoyed c = "sprites/iris/I annoyed c.png"
    image I confident c = "sprites/iris/I confident c.png"
    image I cool c = "sprites/iris/I cool c.png"
    image I questioning c = "sprites/iris/I questioning c.png"
    image I sigh c = "sprites/iris/I sigh c.png"
    image I sigh2 c = "sprites/iris/I sigh2 c.png"
    image I speaking c = "sprites/iris/I speaking c.png"
    image I surprised c = "sprites/iris/I surprised c.png"
    image I pleading c = "sprites/iris/I pleading c.png"
    
    #Ellis sprites
    image E cheerful = "sprites/ellis/E cheerful.png"
    image E angry = "sprites/ellis/E angry.png"
    image E observing = "sprites/ellis/E observing.png"
    image E speaking = "sprites/ellis/E speaking.png"
    
    
    #Sura sprites
    image S neutral = "sprites/sura/S neutral.png"
    image S acknowledging = "sprites/sura/S acknowledging.png"
    image S psychic = "sprites/sura/S psychic.png"
    image S salute = "sprites/sura/S salute.png"
    image S speaking = "sprites/sura/S speaking.png"
    
    #define channel for environment sound
    $renpy.music.register_channel("env", mixer="sfx", loop=True, stop_on_mute=True, tight=False, buffer_queue=True, movie=False)
    #music initialization:
    define audio.Sugawara = "music/SugawaraKS.mp3"


    #Background initialization:
    image white = "backgrounds/white.png"
    image menubg = "backgrounds/menubg.png"
    image trainingroom = "backgrounds/trainingroom.png"
    image deploymentdeck:
        "backgrounds/deploymentdeck.png"
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1)*SaturationMatrix(.5)*BrightnessMatrix(0.0)*HueMatrix(20) blur 0
    image flankerberth:
        "backgrounds/flankerberth.png"
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1)*SaturationMatrix(.5)*BrightnessMatrix(0.0)*HueMatrix(10) blur 0
    image commandcenter: 
        "backgrounds/commandcenter.png"
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.2)*SaturationMatrix(.8)*BrightnessMatrix(0.1)*HueMatrix(20) blur 0
    image hallway: 
        "backgrounds/hallway.png"
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1)*SaturationMatrix(.5)*BrightnessMatrix(0.0)*HueMatrix(0) blur 0
    image sky night = "backgrounds/sky night.png"
    image sky = "backgrounds/sky.png"
    image blizzard = "backgrounds/blizzard.png"
    image bridge:
        "backgrounds/bridge.png"
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1)*SaturationMatrix(.5)*BrightnessMatrix(0.0)*HueMatrix(0) blur 0
    image diving = "backgrounds/diving.png"
    image vineyard = "backgrounds/vineyard.jpg"
    image igdrilbuilding = "backgrounds/igdrilbuilding.jpg"
    image igdril = "backgrounds/igdril.png"
    image insigli = "backgrounds/insigli.png"
    image fyrir = "backgrounds/fyrir.png"
    image road = "backgrounds/road.png"
    image messhall:
        "backgrounds/messhall.png"
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1)*SaturationMatrix(.5)*BrightnessMatrix(0.0)*HueMatrix(20) blur 0
    

    #Logo Initialization:
    image logo = "logo.png"
    image illusoryworldlogo = "illusoryworldlogo.png"
    
    #CG Initialization:
    image CGmushrooms = "images/cgs/CG mushrooms.png"
    image CGskydiving = "images/cgs/CG skydiving.png"
    image CGwraith = "images/cgs/CG wraith.png"
    #Some prefedined transforms:
    transform xflip:
     xzoom -1

    transform logodissolve:
        linear 1.0 zoom 1.0 ,
        ypos .6

    transform fromRight:
        subpixel True
        alpha 0.0 xalign 1.0 xanchor 0.0
        parallel:
            easein 1.0 alpha 1.0
        parallel:
            easein 1.0 xalign 0.5
        on hide:            
            alpha 1 zoom 1 xanchor 0.5 yanchor 0.5
            block:
                linear 0.1 zoom 1.1
                linear 0.5 zoom 0
                
    transform bounce:
        yoffset 15
        easein .10 yoffset 0
        easeout .175 yoffset 15

##Side image transform
transform same_transform(old, new):
    old
    new with Dissolve(0.1, alpha=True)

define config.side_image_same_transform = same_transform


define config.say_attribute_transition = Dissolve(.2)

label splashscreen:
    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
        
            _preferences.volumes['music'] *= .3
            _preferences.volumes['voice'] *= .8
            _preferences.volumes['sfx'] *= .75
    $ renpy.music.play(config.main_menu_music)
    scene menubg:
        xanchor .5 yanchor .5
        xpos .5 ypos .5
        zoom 1.2
        easein 4 zoom 1.3
    show illusoryworldlogo at center with Dissolve(1):
        subpixel True
        zoom .9
        yanchor .5
        ypos .5
        easeout 4 zoom 1
        parallel:
            ease 2 alpha 0
    $ renpy.pause(2, hard=True)
    hide illusoryworldlogo with Dissolve(1.0)
    return