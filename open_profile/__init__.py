# Copyright: 2023 - mizmu
# License: AGPLv3+

from aqt import mw
from aqt.gui_hooks import *


def showProfileManager() -> None:
    if len(mw.pm.profiles()) > 1:
        aqt.AnkiQt.unloadProfile(mw, mw.showProfileManager)


main_window_did_init.append(showProfileManager)

