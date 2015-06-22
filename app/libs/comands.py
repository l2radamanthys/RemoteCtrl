

import winamp



def wnpcmd(cmd=""):
    wnp = winamp.Winamp()
    if cmd == "play":
        wnp.play()

    if cmd == "pause":
        wnp.pause()

    if cmd == "stop":
        wnp.stop()

    elif cmd == "next":
        wnp.next()

    elif cmd == "prev":
        wnp.previous()

    elif cmd == "current-song":
        return wnp.getCurrentPlayingTitle()

    else:
        pass