from wasp_spotify_bindings.utils.applescript import AppleScript
from wasp_spotify_bindings.utils.applescripts import *


class WaspException(Exception):
    pass


class WaspLib:
    @staticmethod
    def check_if_spotify_is_running() -> bool:
        apple_script = AppleScript(script_txt=CHECK_IF_SPOTIFY_IS_RUNNING)
        return True if apple_script.run() == "running" else False

    @staticmethod
    def warn_if_not_running(func):
        def wrapper(*args, **kwargs):
            if not WaspLib.check_if_spotify_is_running():
                raise WaspException('Spotify is not running!')
            return func(*args, **kwargs)
        return wrapper
