def on_pin_pressed_p0():
    global Interaction
    Interaction = 1
    basic.clear_screen()
    basic.show_number(forceMagnetique())
    Interaction = 0
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def forceMagnetique():
    return Math.round(abs(input.magnetic_force(Dimension.STRENGTH)))
def TutorialSecret():
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.hello),
        SoundExpressionPlayMode.IN_BACKGROUND)
    basic.show_icon(IconNames.HAPPY)
    basic.pause(2000)
    basic.clear_screen()
    basic.pause(1000)
    basic.show_arrow(ArrowNames.WEST)
    basic.pause(2000)
    basic.clear_screen()
    basic.pause(1000)
    basic.show_arrow(ArrowNames.EAST)
    basic.pause(2000)
    basic.clear_screen()
    while not (InitSecretTerminé):
        if MomentDeValiderSecret:
            if input.running_time() > MomentDeValiderSecret:
                DéfinirSecret()
        basic.pause(100)

def on_log_full():
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
datalogger.on_log_full(on_log_full)

def DéfinirSecret():
    global secret, InitSecretTerminé, MomentDeValiderSecret, tmp
    secret = tmp
    InitSecretTerminé = 1
    datalogger.log(datalogger.create_cv("event", 1),
        datalogger.create_cv("counter", Compteur))
    basic.show_icon(IconNames.YES)
    music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
            2112,
            2095,
            255,
            0,
            514,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LOGARITHMIC),
        SoundExpressionPlayMode.UNTIL_DONE)
    basic.clear_screen()
    MomentDeValiderSecret = 0
    tmp = 0
def TutorialCalibrage():
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.hello),
        SoundExpressionPlayMode.IN_BACKGROUND)
    basic.show_icon(IconNames.HAPPY)
    basic.pause(2000)
    basic.clear_screen()
    basic.pause(1000)
    basic.show_arrow(ArrowNames.NORTH)
    basic.pause(2000)
    basic.clear_screen()
    while not (CalibrageTerminé):
        basic.pause(500)
def ouvrir():
    global LaPorteEstOuverte, Compteur
    if LaPorteEstOuverte == 0:
        LaPorteEstOuverte = 1
        Compteur += 1
        datalogger.log(datalogger.create_cv("event", 3),
            datalogger.create_cv("counter", Compteur))
        music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
def Animation():
    music.start_melody(music.built_in_melody(Melodies.JUMP_UP), MelodyOptions.ONCE)
    images.icon_image(IconNames.HEART).scroll_image(1, 100)
    basic.pause(2000)
    basic.clear_screen()

def on_button_pressed_a():
    global MomentDeValiderSecret, tmp
    MomentDeValiderSecret = input.running_time() + 2000
    tmp = (tmp + 32) % 1024
input.on_button_pressed(Button.A, on_button_pressed_a)

def afficherNombre(num: number):
    led.set_brightness(64)
    basic.show_number(num)
    for index in range(65):
        led.set_brightness(64 - 1 * index)
        basic.pause(1)
    basic.pause(200)
def fermer():
    global LaPorteEstOuverte
    if LaPorteEstOuverte != 0:
        datalogger.log(datalogger.create_cv("event", 4),
            datalogger.create_cv("counter", Compteur))
        LaPorteEstOuverte = 0
        music.start_melody(music.built_in_melody(Melodies.POWER_DOWN),
            MelodyOptions.ONCE)
        basic.show_number(Compteur % 10)
        basic.pause(2000)
        basic.clear_screen()
def compteRebour():
    for index2 in range(5):
        music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
                2112,
                2095,
                255,
                0,
                514,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LOGARITHMIC),
            SoundExpressionPlayMode.IN_BACKGROUND)
        afficherNombre(5 - index2)
    basic.clear_screen()
    led.set_brightness(16)

def on_logo_long_pressed():
    global Interaction, Compteur
    Interaction = 1
    datalogger.log(datalogger.create_cv("event", 5),
        datalogger.create_cv("counter", Compteur))
    Compteur = 0
    music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
            2112,
            2095,
            255,
            0,
            514,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LOGARITHMIC),
        SoundExpressionPlayMode.IN_BACKGROUND)
    basic.show_number(Compteur)
    basic.pause(2000)
    basic.clear_screen()
    Interaction = 0
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_pin_pressed_p2():
    global Interaction
    Interaction = 1
    basic.clear_screen()
    basic.show_number(ForceMagnetiqueVar)
    Interaction = 0
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def aimantNonDétecté():
    return forceMagnetique() > ForceMagnetiqueAbs + ForceMagnetiqueVar or forceMagnetique() < ForceMagnetiqueAbs - ForceMagnetiqueVar

def on_button_pressed_ab():
    global Interaction, secret, tmp, MomentDeValiderSecret, InitSecretTerminé
    Interaction = 1
    secret = 0
    tmp = 0
    MomentDeValiderSecret = 0
    InitSecretTerminé = 0
    TutorialSecret()
    Interaction = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def ValiderSecret():
    global cptSaisieInvalide, MomentDeValiderSecret, tmp
    if cptSaisieInvalide >= 3:
        basic.show_icon(IconNames.SKULL)
        basic.clear_screen()
    else:
        if tmp == secret:
            cptSaisieInvalide = 0
            basic.show_icon(IconNames.YES)
            music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
                    2112,
                    2095,
                    255,
                    0,
                    514,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.LOGARITHMIC),
                SoundExpressionPlayMode.UNTIL_DONE)
            basic.clear_screen()
        else:
            cptSaisieInvalide += 1
            basic.show_icon(IconNames.NO)
            music.play_sound_effect(music.create_sound_effect(WaveShape.SAWTOOTH,
                    85,
                    84,
                    255,
                    0,
                    474,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.CURVE),
                SoundExpressionPlayMode.UNTIL_DONE)
            basic.clear_screen()
    MomentDeValiderSecret = 0
    tmp = 0

def on_button_pressed_b():
    global MomentDeValiderSecret, tmp
    MomentDeValiderSecret = input.running_time() + 2000
    tmp = 32 * int(tmp / 32) + (tmp + 1) % 32
input.on_button_pressed(Button.B, on_button_pressed_b)

def Calibrer():
    global AccélérationRepos, ForceMagnetiqueAbs, ForceMagnetiqueVar, DétectionTropSensible, CalibrageTerminé
    datalogger.log(datalogger.create_cv("event", 2),
        datalogger.create_cv("counter", Compteur))
    AccélérationRepos = 970
    ForceMagnetiqueAbs = 0
    for index3 in range(5):
        ForceMagnetiqueAbs += forceMagnetique()
        music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
                3788,
                3788,
                255,
                255,
                50,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.IN_BACKGROUND)
        basic.pause(100)
    ForceMagnetiqueAbs = Math.round(ForceMagnetiqueAbs / 5)
    ForceMagnetiqueVar = 200
    DétectionTropSensible = 1
    while DétectionTropSensible:
        DétectionTropSensible = 0
        for index4 in range(5):
            if aimantNonDétecté():
                DétectionTropSensible = 1
            control.wait_micros(200)
        ForceMagnetiqueVar += 50
    music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
            2112,
            2095,
            255,
            0,
            514,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LOGARITHMIC),
        SoundExpressionPlayMode.UNTIL_DONE)
    basic.show_icon(IconNames.YES)
    basic.pause(2000)
    basic.clear_screen()
    CalibrageTerminé = 1

def on_pin_pressed_p1():
    global Interaction
    Interaction = 1
    basic.clear_screen()
    basic.show_number(ForceMagnetiqueAbs)
    Interaction = 0
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_logo_pressed():
    global Interaction
    if not (CalibrageTerminé):
        compteRebour()
        Calibrer()
    else:
        Interaction = 1
        music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
                2112,
                2095,
                255,
                0,
                514,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LOGARITHMIC),
            SoundExpressionPlayMode.IN_BACKGROUND)
        basic.show_number(Compteur)
        basic.pause(2000)
        basic.clear_screen()
        Interaction = 0
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def mouvements():
    return input.acceleration(Dimension.STRENGTH) > AccélérationRepos + 100 or input.acceleration(Dimension.STRENGTH) < AccélérationRepos - 100
DétectionTropSensible = 0
AccélérationRepos = 0
cptSaisieInvalide = 0
ForceMagnetiqueAbs = 0
ForceMagnetiqueVar = 0
LaPorteEstOuverte = 0
CalibrageTerminé = 0
tmp = 0
MomentDeValiderSecret = 0
InitSecretTerminé = 0
Interaction = 0
secret = 0
Compteur = 0
music.set_volume(32)
led.set_brightness(16)
pins.touch_set_mode(TouchTarget.P0, TouchTargetMode.CAPACITIVE)
datalogger.set_column_titles("event")
datalogger.set_column_titles("counter")
datalogger.include_timestamp(FlashLogTimeStampFormat.MINUTES)
datalogger.log(datalogger.create_cv("event", 0),
    datalogger.create_cv("counter", Compteur))
input.set_accelerometer_range(AcceleratorRange.ONE_G)
secret = 0
Compteur = 0
Animation()
TutorialSecret()
TutorialCalibrage()

def on_every_interval():
    if not (Interaction):
        if aimantNonDétecté():
            ouvrir()
        else:
            fermer()
        if LaPorteEstOuverte:
            basic.show_icon(IconNames.ANGRY)
        if MomentDeValiderSecret:
            if input.running_time() > MomentDeValiderSecret:
                ValiderSecret()
loops.every_interval(200, on_every_interval)
