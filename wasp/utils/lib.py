from wasp.utils.applescript import AppleScript
from wasp.utils.applescripts import *


class WaspException(Exception):
    pass


class WaspLib:
    @staticmethod
    def check_if_spotify_is_running():
        apple_script = AppleScript(script_txt=CHECK_IF_SPOTIFY_IS_RUNNING)
        return True if apple_script.run() == "1" else False

    @staticmethod
    def warn_if_not_running(func):
        def wrapper(*args, **kwargs):
            if not WaspLib.check_if_spotify_is_running():
                raise WaspException('Spotify is not running!')
            func(*args, **kwargs)

        return wrapper
