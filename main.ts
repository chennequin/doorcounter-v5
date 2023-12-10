input.onPinPressed(TouchPin.P0, function () {
    Interaction = 1
    basic.showNumber(forceMagnetique())
    basic.clearScreen()
    Interaction = 0
})
function forceMagnetique () {
    return Math.round(Math.abs(input.magneticForce(Dimension.Strength)))
}
function TutorialSecret () {
    music.playSoundEffect(music.builtinSoundEffect(soundExpression.hello), SoundExpressionPlayMode.InBackground)
    basic.showIcon(IconNames.Happy)
    basic.pause(2000)
    basic.clearScreen()
    basic.pause(1000)
    basic.showArrow(ArrowNames.West)
    basic.pause(2000)
    basic.clearScreen()
    basic.pause(1000)
    basic.showArrow(ArrowNames.East)
    basic.pause(2000)
    basic.clearScreen()
    while (!(InitSecretTerminé)) {
        if (MomentDeValiderSecret) {
            if (input.runningTime() > MomentDeValiderSecret) {
                DéfinirSecret()
            }
        }
        basic.pause(100)
    }
}
datalogger.onLogFull(function () {
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
})
function VersionFlash () {
    music.startMelody(music.builtInMelody(Melodies.JumpUp), MelodyOptions.Once)
    basic.showString("cisu")
    basic.pause(2000)
    basic.clearScreen()
}
function DéfinirSecret () {
    secret = tmp
    InitSecretTerminé = 1
    datalogger.log(
    datalogger.createCV("event", 1),
    datalogger.createCV("counter", Compteur)
    )
    basic.showIcon(IconNames.Yes)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 2112, 2095, 255, 0, 514, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
    basic.clearScreen()
    MomentDeValiderSecret = 0
    tmp = 0
}
function TutorialCalibrage () {
    music.playSoundEffect(music.builtinSoundEffect(soundExpression.hello), SoundExpressionPlayMode.InBackground)
    basic.showIcon(IconNames.Happy)
    basic.pause(2000)
    basic.clearScreen()
    basic.pause(1000)
    basic.showArrow(ArrowNames.North)
    basic.pause(2000)
    basic.clearScreen()
    while (!(CalibrageTerminé)) {
        basic.pause(500)
    }
}
function ouvrir () {
    if (LaPorteEstOuverte == 0) {
        LaPorteEstOuverte = 1
        music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
        Compteur += 1
        datalogger.log(
        datalogger.createCV("event", 3),
        datalogger.createCV("counter", Compteur)
        )
    }
}
function Animation () {
    music.startMelody(music.builtInMelody(Melodies.JumpUp), MelodyOptions.Once)
    images.iconImage(IconNames.Heart).scrollImage(1, 100)
    basic.pause(2000)
    basic.clearScreen()
}
input.onButtonPressed(Button.A, function () {
    MomentDeValiderSecret = input.runningTime() + 2000
    tmp = (tmp + 32) % 1024
})
function afficherNombre (num: number) {
    led.setBrightness(64)
    basic.showNumber(num)
    for (let index = 0; index <= 64; index++) {
        led.setBrightness(64 - 1 * index)
        basic.pause(1)
    }
    basic.pause(200)
}
function fermer () {
    if (LaPorteEstOuverte != 0) {
        datalogger.log(
        datalogger.createCV("event", 4),
        datalogger.createCV("counter", Compteur)
        )
        LaPorteEstOuverte = 0
        music.startMelody(music.builtInMelody(Melodies.PowerDown), MelodyOptions.Once)
        basic.showNumber(Compteur % 10)
        basic.pause(2000)
        basic.clearScreen()
    }
}
function compteRebour () {
    for (let index2 = 0; index2 <= 4; index2++) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 2112, 2095, 255, 0, 514, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.InBackground)
        afficherNombre(5 - index2)
    }
    basic.clearScreen()
    led.setBrightness(16)
}
input.onLogoEvent(TouchButtonEvent.LongPressed, function () {
    Interaction = 1
    music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 2112, 2095, 255, 0, 514, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.InBackground)
    basic.showNumber(Compteur)
    basic.pause(2000)
    basic.clearScreen()
    Interaction = 0
})
input.onPinPressed(TouchPin.P2, function () {
    Interaction = 1
    basic.clearScreen()
    Interaction = 0
})
function aimantNonDétecté () {
    return forceMagnetique() > ForceMagnetiqueAbs + ForceMagnetiqueVar || forceMagnetique() < ForceMagnetiqueAbs - ForceMagnetiqueVar
}
input.onButtonPressed(Button.AB, function () {
    Interaction = 1
    secret = 0
    tmp = 0
    MomentDeValiderSecret = 0
    InitSecretTerminé = 0
    TutorialSecret()
    Interaction = 0
})
function ValiderSecret () {
    if (cptSaisieInvalide >= 3) {
        basic.showIcon(IconNames.Skull)
        basic.clearScreen()
    } else if (tmp == secret) {
        cptSaisieInvalide = 0
        basic.showIcon(IconNames.Yes)
        music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 2112, 2095, 255, 0, 514, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
        basic.clearScreen()
    } else {
        cptSaisieInvalide += 1
        basic.showIcon(IconNames.No)
        music.playSoundEffect(music.createSoundEffect(WaveShape.Sawtooth, 85, 84, 255, 0, 474, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
        basic.clearScreen()
    }
    MomentDeValiderSecret = 0
    tmp = 0
}
input.onButtonPressed(Button.B, function () {
    MomentDeValiderSecret = input.runningTime() + 2000
    tmp = 32 * Math.trunc(tmp / 32) + (tmp + 1) % 32
})
function Calibrer () {
    datalogger.log(
    datalogger.createCV("event", 2),
    datalogger.createCV("counter", Compteur)
    )
    AccélérationRepos = 970
    ForceMagnetiqueAbs = 0
    for (let index = 0; index < 5; index++) {
        ForceMagnetiqueAbs += forceMagnetique()
        music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 3788, 3788, 255, 255, 50, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
        basic.pause(100)
    }
    ForceMagnetiqueAbs = Math.round(ForceMagnetiqueAbs / 5)
    ForceMagnetiqueVar = 200
    DétectionTropSensible = 1
    while (DétectionTropSensible) {
        DétectionTropSensible = 0
        for (let index = 0; index < 5; index++) {
            if (aimantNonDétecté()) {
                DétectionTropSensible = 1
            }
            control.waitMicros(200)
        }
        ForceMagnetiqueVar += 50
    }
    ForceMagnetiqueVar += 50
    music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 2112, 2095, 255, 0, 514, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
    basic.showIcon(IconNames.Yes)
    basic.pause(2000)
    basic.clearScreen()
    CalibrageTerminé = 1
}
input.onPinPressed(TouchPin.P1, function () {
    Interaction = 1
    basic.clearScreen()
    Interaction = 0
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (!(CalibrageTerminé)) {
        compteRebour()
        Calibrer()
    } else {
        Interaction = 1
        music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 2112, 2095, 255, 0, 514, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.InBackground)
        basic.showNumber(Compteur % 10)
        basic.pause(2000)
        basic.clearScreen()
        Interaction = 0
    }
})
function mouvements () {
    return input.acceleration(Dimension.Strength) > AccélérationRepos + 100 || input.acceleration(Dimension.Strength) < AccélérationRepos - 100
}
let DétectionTropSensible = 0
let AccélérationRepos = 0
let cptSaisieInvalide = 0
let ForceMagnetiqueVar = 0
let ForceMagnetiqueAbs = 0
let LaPorteEstOuverte = 0
let CalibrageTerminé = 0
let tmp = 0
let MomentDeValiderSecret = 0
let InitSecretTerminé = 0
let Interaction = 0
let secret = 0
let Compteur = 0
music.setVolume(255)
led.setBrightness(16)
datalogger.setColumnTitles("event")
datalogger.setColumnTitles("counter")
datalogger.includeTimestamp(FlashLogTimeStampFormat.Minutes)
datalogger.log(
datalogger.createCV("event", 0),
datalogger.createCV("counter", Compteur)
)
input.setAccelerometerRange(AcceleratorRange.OneG)
secret = 0
Compteur = 0
Animation()
VersionFlash()
TutorialSecret()
TutorialCalibrage()
loops.everyInterval(200, function () {
    if (!(Interaction)) {
        if (aimantNonDétecté()) {
            ouvrir()
        } else {
            fermer()
        }
        if (LaPorteEstOuverte) {
            basic.showIcon(IconNames.Angry)
        }
        if (MomentDeValiderSecret) {
            if (input.runningTime() > MomentDeValiderSecret) {
                ValiderSecret()
            }
        }
    }
})
