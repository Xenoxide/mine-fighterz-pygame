import pygame
from pygame import mixer

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init() #turn all of pygame on.
pygame.mixer.init()

def loadAssets(): 
    backdropNames = [
        'arcade.png', #0
        'death1.png',
        'grey1.png',
        'grey4.png',
        'overworldday.png',
        'secretkitchen.png',
        'black.png',
        'death2.png',
        'grey2.png',
        'loading1.png',
        'overworldnight.png',
        'startscreen.png',
        'cave.png',
        'grey0.png',
        'grey3.png',
        'loading2.png',
        'piratecat.png',
        'volcano.png' #17
    ]

    sprites_misc = [
        'arcade.png', #0
        'arcadebowl.png',
        'arcaderock.png',
        'blank.png',
        'chestclosed.png',
        'chestopen.png',
        'godown.png',
        'painting.png',
        'playbutton.png' #8
    ]
    sprites_othercharacters = [
        'apple.png', #9
        'badapple.png',
        'boss1.png',
        'boss2.png',
        'chezletter1.png',
        'chezletter2.png',
        'piratecat.png' #15
    ]
    sprites_player = [
        'eatleft1.png', #16
        'eatleft2.png',
        'eatright1.png',
        'eatright2.png',
        'left.png',
        'pickaxeleft1.png',
        'pickaxeleft2.png',
        'pickaxeright1.png',
        'pickaxeright2.png',
        'right.png',
        'sleepleft.png',
        'sleepright.png',
        'surprised.png',
        'walkietalkie.png',
        'yeahleft.png',
        'yeahright.png' #31
    ]
    sprites_ray = [
        'neutral.png', #32
        'sad.png',
        'smile.png',
        'surprised.png',
        'sword.png' #36
    ]
    sprites_text = [
        'hunger.png', #37
        'jeffporg.png',
        'minefighterz.png',
        'minefighterzred.png',
        'quickattack.png',
        'spicygum.png' #42
    ]
    sprites_toddler = [
        'angry.png', #43
        'left.png',
        'right.png'
    ]
    sound_names = [
        'music/backbeat.wav', #0
        'music/epicmusic.wav',
        'music/ifeelsoalive.wav',
        'music/introtheme.wav',
        'music/overworldtheme.wav',
        'music/sadpiano.wav', #5
        'sfx/belltoll.wav', #6
        'sfx/bigpop.wav',
        'sfx/boing.wav',
        'sfx/cricket.wav',
        'sfx/electrobeat.wav',
        'sfx/electrobeat2.wav',
        'sfx/electrobeat3.wav',
        'sfx/electrobeat4.wav',
        'sfx/groovydrums1.wav',
        'sfx/groovydrums2.wav',
        'sfx/groovydrums3.wav',
        'sfx/groovydrums4.wav',
        'sfx/melodic.wav',
        'sfx/pop.wav',
        'sfx/scream.wav',
        'sfx/snap.wav',
        'sfx/ufo.wav',
        'sfx/woop.wav' #23
    ]

    backdrops = []
    for backdrop in backdropNames:
        backdrops.append(pygame.image.load('assets/backdrops/' + backdrop))

    sprites = []
    for sprite in sprites_misc:
        sprites.append(pygame.image.load('assets/sprites/misc/' + sprite))
    for sprite in sprites_othercharacters:
        sprites.append(pygame.image.load('assets/sprites/othercharacters/' + sprite))
    for sprite in sprites_player:
        sprites.append(pygame.image.load('assets/sprites/player/' + sprite))
    for sprite in sprites_ray:
        sprites.append(pygame.image.load('assets/sprites/ray/' + sprite))
    for sprite in sprites_text:
        sprites.append(pygame.image.load('assets/sprites/text/' + sprite))
    for sprite in sprites_toddler:
        sprites.append(pygame.image.load('assets/sprites/toddler/' + sprite))

    #sounds = []
    #for sound in sound_names:
    #    sounds.append(pygame.mixer.music.load('assets/sound/' + sound))
    return (backdrops, sprites)

