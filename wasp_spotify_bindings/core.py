import json
from typing import Dict, Union, Optional

from wasp_spotify_bindings.utils.applescript import AppleScript
from wasp_spotify_bindings.utils.applescripts import *
from wasp_spotify_bindings.utils.lib import WaspLib, WaspException


class Wasp:
    def __init__(self) -> None:
        self.pre_muted_volume: int = 0

    @staticmethod
    def start_spotify() -> Optional[str]:
        """
        Start the Spotify application.
        """
        apple_script: AppleScript = AppleScript(script_txt=START_SPOTIFY)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def quit_spotify() -> Optional[str]:
        apple_script: AppleScript = AppleScript(script_txt=QUIT_SPOTIFY)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def next_track() -> Optional[str]:
        apple_script = AppleScript(script_txt=NEXT_TRACK)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def previous_track() -> Optional[str]:
        apple_script = AppleScript(script_txt=PREVIOUS_TRACK)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def play() -> Optional[str]:
        apple_script = AppleScript(script_txt=PLAY)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def play_pause() -> Optional[str]:
        apple_script = AppleScript(script_txt=PLAY_PAUSE)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def pause() -> Optional[str]:
        apple_script = AppleScript(script_txt=PAUSE)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def set_volume(volume: int) -> Optional[str]:
        if not 100 >= volume >= 0:
            raise WaspException('Volume has to be in range [0-100]!')
        apple_script = AppleScript(script_txt=SET_VOLUME.format(volume=volume))
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def play_track(spotify_uri: str) -> Optional[str]:
        apple_script = AppleScript(script_txt=PLAY_TRACK.format(spotify_uri=spotify_uri))
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def play_track_in_context(spotify_uri: str, context: str) -> Optional[str]:
        apple_script = AppleScript(script_txt=PLAY_TRACK_IN_CONTEXT.format(spotify_uri=spotify_uri, context=context))
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def volume_up() -> Optional[str]:
        apple_script = AppleScript(script_txt=VOLUME_UP)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def volume_down() -> Optional[str]:
        apple_script = AppleScript(script_txt=VOLUME_DOWN)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def get_track() -> Dict[str, Union[str, int]]:
        """
        Get metadata about the current track.

        {
            'artist': 'Rick Astley',
            'album': 'Whenever You Need Somebody',
            'disc_number': 1,
            'duration': 213573,
            'played_count': 0,
            'track_number': 1,
            'popularity': 75,
            'id': 'spotify:track:4uLU6hMCjMI75M1A2tKUQC',
            'name': 'Never Gonna Give You Up',
            'album_artist':
            'Rick Astley',
            'artwork_url':
            'http://i.scdn.co/image/15ac2c9091d9b74e841b281ceb23ca8208321444',
            'spotify_url': 'spotify:track:4uLU6hMCjMI75M1A2tKUQC'
        }
        """
        apple_script = AppleScript(script_txt=GET_TRACK_METADATA)
        return json.loads(apple_script.run())

    @staticmethod
    @WaspLib.warn_if_not_running
    def jump_to(jump_to_second: int) -> Optional[str]:
        apple_script = AppleScript(script_txt=JUMP_TO.format(jump_to_second=jump_to_second))
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def is_repeating() -> Optional[str]:
        apple_script = AppleScript(script_txt=IS_REPEATING)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def is_shuffling() -> Optional[str]:
        apple_script = AppleScript(script_txt=IS_SHUFFLING)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def set_repeating(set_repeating: bool) -> Optional[str]:
        apple_script = AppleScript(script_txt=SET_REPEATING.format(set_repeating='true' if set_repeating else 'false'))
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def set_shuffling(set_shuffling: bool) -> Optional[str]:
        apple_script = AppleScript(script_txt=SET_SHUFFLING.format(set_shuffling='true' if set_shuffling else 'false'))
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def toggle_repeating() -> Optional[str]:
        apple_script = AppleScript(script_txt=TOGGLE_REPEATING)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def toggle_shuffling() -> Optional[str]:
        apple_script = AppleScript(script_txt=TOGGLE_SHUFFLING)
        return apple_script.run()

    @WaspLib.warn_if_not_running
    def mute(self):
        state = Wasp.get_state()
        self.pre_muted_volume = state['volume']
        apple_script = AppleScript(script_txt=SET_VOLUME.format(volume=0))
        return apple_script.run()

    @WaspLib.warn_if_not_running
    def unmute(self):
        apple_script = AppleScript(script_txt=SET_VOLUME.format(volume=self.pre_muted_volume))
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def get_state() -> Dict[str, Union[str, int]]:
        """
        Get current state of the Spotify player.

        {
            "track_id": "spotify:track:4uLU6hMCjMI75M1A2tKUQC",
            "volume": 49,
            "position": 3,  # seconds
            "state": "playing"
        }

        :return: Above json as a dictionary
        """
        apple_script = AppleScript(script_txt=GET_PLAYER_STATE)
        res: Optional[str] = apple_script.run()
        if res:
            return json.loads(res)
        else:
            raise WaspException('Unable to get Spotify player state!')
