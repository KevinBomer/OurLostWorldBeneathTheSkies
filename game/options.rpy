## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Our Lost World Beneath The Skies")

## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "0.22"

## Text that is placed on the game's about screen. To insert a blank line
## between paragraphs, write \n\n.


define gui.about = _("A Product of Sarchalen Team © 2019\nCreated for NaNoRenO 2019\n\nCredits\n\nProduction:\nKevin Bomer - Director\nSandra 'SandraMJ' Molina - Voice Director\nAble Kirby - Staff Consultant\nMonochrome - Art Coordinator\nSarchalen Team - Production\n\nCast\nKieran Flitton - Tallara\nMadeline Dorroh - Laverna\nDan Gold - Magnus\nCrystal Lee - Iris\nStan 'Stanpi' Kuschick - D'aza\nSamantha Chan - Sura\nKameron Watson - Bentis\nAngela Tran - Ellis\nKenkoy - Intercom\nAriane 'Starleeter' Marchese - Rhea\nRemi Flinterman - Ace\n\nVisual Design:\nMomoca - Character Design\nKart Prowler - Event CGs\nErezu - Environment Design\nRe.Alice - User Interface\nKenta Chiba - Logo Design\nOriginal Soundtrack:\nTimothy Adan\nDalton 'GRV' Lafond\nAble Kirby\n\nStory:\nKevin Bomer\nSakyawira\nAble Kirby\n\nSound Effects:\nBeneath The Skies is proud to use sound effects liscensed through Creative Commons including recordings by:\nheyim89yearsold*\ninspectorJ*\nkangaroovindaloo*\ntimmy_h123*\n32cheeseman32*\nqubodup*\nnextmaking**\nmicknife*\nsoundscalpel.com*\nSauron974*\nHuggy13ear*\nRICHERlandTV*\n\nand made available for public use by freesound.org under the following licenses:\n\nCC BY 3.0\nSampling+ 1.0\nAll recordings were adapted from their original format\n\nSpecial thanks to:\nTom 'PyTom' Rothamel - Renpy.org" )


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "OurLostWorldBeneathTheSkies"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"

#format for naming files so only the name has to be written in the script.
define config.voice_filename_format = "voice/{filename}.ogg"
## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "music/4_OLW_SnowPiles.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = Fade(0.3, 0.1, 0.1, color="#fff")
define config.exit_transition = Fade(0.2, 0.2, 0.2, color="#fff")


## A transition that is used after a game has been loaded.

define config.after_load_transition = pushleft


## Used when entering the main menu after the game has ended.

define config.end_game_transition = fade


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.

## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"
## Transition used between splash screen and main menu load
define config.end_splash_transition = Dissolve(.2)
## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 30


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "OurLostWorldBeneathTheSkies_Saves"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:
    ## Layers #################################################################
    ## Defines which layers exist in Renpy. All displayables must exist on a layer. Background, Middle, and Forward are custom. 

    config.layers = ['master', 'background', 'middle', 'forward', 'transient', 'screens', 'overlay']
    
    register_3d_layer('background', 'middle', 'forward')
    #These layers will be registered as 3D layers, allowing their Z axis to be affected inside the 3D Camera interface. 

    config.debug_sound = True
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.
    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpt', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = True

## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"

init -1 python hide:
        def hide(name, layer='master'):
            for l in _3d_layers:
                if renpy.showing(name, l):
                    renpy.hide(name, l)
                    break
                else:
                    renpy.hide(name, layer)

                    config.hide = hide

        def scene(layer='master'):
            renpy.scene(layer)
            for l in _3d_layers:
                renpy.scene(l)

                config.scene = scene