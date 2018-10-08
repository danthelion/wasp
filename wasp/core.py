import logging
from pathlib import Path

from wasp.utils.applescript import AppleScript

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

APPLESCRIPTS_DIR = Path(__file__).parent / 'utils' / 'applescripts'


class WaspException(Exception):
    pass


class SpotifySystemController:
    def __init__(self):
        self.is_spotify_running: bool = False
        self.check_if_spotify_is_running()

    def check_if_spotify_is_running(self):
        apple_script = AppleScript.from_file(script_path=APPLESCRIPTS_DIR / 'check_if_spotify_is_running.scpt')
        self.is_spotify_running = True if apple_script.run() == "1" else False

    def start_spotify(self):
        apple_script = AppleScript.from_file(script_path=APPLESCRIPTS_DIR / 'start_spotify.scpt')
        if not self.is_spotify_running:
            res = apple_script.run()
            self.is_spotify_running = True
            return res

    def stop_spotify(self):
        apple_script = AppleScript.from_file(script_path=APPLESCRIPTS_DIR / 'stop_spotify.scpt')
        if self.is_spotify_running:
            res = apple_script.run()
            self.is_spotify_running = False
            return res


class WaspSong:
    def __init__(self):
        self.track_name = None

    def __repr__(self):
        return f'Song({self.track_name})'

    def get_track_name(self):
        apple_script = AppleScript.from_file(script_path=APPLESCRIPTS_DIR / 'get_current_track_name.scpt')
        self.track_name = apple_script.run()
        return self.track_name


class WaspArtist:
    def __init__(self):
        self.artist_name = None

    def __repr__(self):
        return f'Artist({self.artist_name})'

    def get_artist_name(self):
        apple_script = AppleScript.from_file(script_path=APPLESCRIPTS_DIR / 'get_current_artist_name.scpt')
        self.artist_name = apple_script.run()
        return self.artist_name


class Wasp:
    def __init__(self):
        self.spotify_controller: SpotifySystemController = SpotifySystemController()
        self.current_track: WaspSong = WaspSong()
        self.current_artist: WaspArtist = WaspArtist()

    def __repr__(self):
        return f'Wasp(Artist: {self.current_artist} Track: {self.current_track})'

    def start_spotify(self):
        return self.spotify_controller.start_spotify()

    def stop_spotify(self):
        return self.spotify_controller.stop_spotify()

    def is_spotify_running(self):
        return self.spotify_controller.is_spotify_running

    def _warn_if_not_running(self):
        if not self.is_spotify_running():
            raise WaspException('Spotify is not running!')

    def load_track_metadata(self):
        self.get_current_track_name()

    def load_artist_metadata(self):
        self.get_current_artist_name()

    def get_current_track_name(self):
        self._warn_if_not_running()
        return self.current_track.get_track_name()

    def get_current_artist_name(self):
        self._warn_if_not_running()
        return self.current_artist.get_artist_name()

    def poll(self):
        # TODO threading, wait for all.
        self.load_track_metadata()
        self.load_artist_metadata()
