from __future__ import division
from asciimatics.effects import BannerText, Print, Scroll ,Cycle, Stars
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys


def demo(screen):
    #empty array to save all effects
    scenes = []
    #show text
    effects = [
        Print(screen,
              FigletText("yourname",
                         font='banner3' if screen.width > 80 else 'banner'),
              screen.height//2-3,
              colour=7, bg=7 if screen.unicode_aware else 0),
    ]
    scenes.append(Scene(effects))
    #show taki.gif
    effects = [
        Print(screen,
              ColourImageFile(screen, "assets/images/taki.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height,
              speed=1),
        Scroll(screen, 2)
    ]
    scenes.append(Scene(effects))
    #show mitsuha.gif
    effects = [
        BannerText(screen,
                   ColourImageFile(screen, "assets/images/mitsuha.gif", screen.height-2,
                                   uni=screen.unicode_aware, dither=screen.unicode_aware),
                   0, 0),
    ]
    scenes.append(Scene(effects))
    #show mitshua2.gif
    effects = [
        Print(screen,
            ColourImageFile(screen, "assets/images/mitsuha2.gif",screen.height,
                            uni=screen.unicode_aware),
            screen.height,
            speed=1,),
        Scroll(screen,2)
    ]
    scenes.append(Scene(effects))
    #show both.gif
    effects = [
        Print(screen,
              ColourImageFile(screen, "assets/images/both.gif", screen.height-2,
                              uni=screen.unicode_aware,
                              dither=screen.unicode_aware),
              0,
              stop_frame=200),
    ]
    scenes.append(Scene(effects))
    #show end text
    effects = [
        Cycle(
            screen, FigletText("KimiNoNamaewa?", font="big"),
            int(screen.height/2-8)
        ),
        Cycle(
            screen, FigletText("YourName", font="small"),
            int(screen.height/2+3),
        ),
    ]
    scenes.append(Scene(effects))
    screen.play(scenes, stop_on_resize=True)


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo)
            sys.exit(0)
        except ResizeScreenError:
            pass