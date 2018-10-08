import json
import logging

from wasp.utils.applescript import AppleScript
from wasp.utils.applescripts import *
from wasp.utils.lib import WaspLib

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class SpotifySystemController:
    def __init__(self):
        self.state = None

    @WaspLib.warn_if_not_running
    def load_player_state(self):
        apple_script = AppleScript(script_txt=GET_PLAYER_STATE)
        self.state = json.loads(apple_script.run())

    @staticmethod
    def start_spotify():
        apple_script = AppleScript(script_txt=START_SPOTIFY)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def quit_spotify():
        apple_script = AppleScript(script_txt=QUIT_SPOTIFY)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def next_track():
        apple_script = AppleScript(script_txt=NEXT_TRACK)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def previous_track():
        apple_script = AppleScript(script_txt=PREVIOUS_TRACK)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def play():
        apple_script = AppleScript(script_txt=PLAY)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def pause():
        apple_script = AppleScript(script_txt=PAUSE)
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def play_track(spotify_uri: str):
        apple_script = AppleScript(script_txt=PLAY_TRACK.format(spotify_uri=spotify_uri))
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def volume_up():
        apple_script = AppleScript(script_txt=PLAY_TRACK.format(spotify_uri=VOLUME_UP))
        return apple_script.run()

    @staticmethod
    @WaspLib.warn_if_not_running
    def volume_down():
        apple_script = AppleScript(script_txt=PLAY_TRACK.format(spotify_uri=VOLUME_DOWN))
        return apple_script.run()


class WaspTrack:
    def __init__(self):
        self.metadata = None

    def __repr__(self):
        return f'Track({self.metadata})'

    def load_track_metadata(self):
        apple_script = AppleScript(script_txt=GET_TRACK_METADATA)
        self.metadata = json.loads(apple_script.run())


class Wasp:
    def __init__(self):
        self.spotify_controller: SpotifySystemController = SpotifySystemController()
        self.track: WaspTrack = WaspTrack()

    def __repr__(self):
        return f'Wasp(Track: {self.track})'

    def start_spotify(self):
        return self.spotify_controller.start_spotify()

    def quit_spotify(self):
        return self.spotify_controller.quit_spotify()

    def next_track(self):
        """
        Play the next track and refresh metadata.
        """
        self.spotify_controller.next_track()
        self.get_track()

    def previous_track(self):
        """
        Play the previous track and refresh metadata.
        """
        self.spotify_controller.previous_track()
        self.get_track()

    def play(self):
        self.spotify_controller.play()

    def pause(self):
        self.spotify_controller.pause()

    def play_track(self, spotify_uri: str):
        self.spotify_controller.play_track(spotify_uri=spotify_uri)
        self.get_track()

    def volume_up(self):
        self.spotify_controller.volume_up()

    def volume_down(self):
        self.spotify_controller.volume_down()

    def get_track(self):
        self.track.load_track_metadata()

    def get_state(self):
        self.spotify_controller.load_player_state()
