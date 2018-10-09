from time import sleep

from wasp_spotify_bindings.core import Wasp
from wasp_spotify_bindings.utils.lib import WaspLib


def test_open_spotify(wasp: Wasp) -> None:
    wasp.start_spotify()
    sleep(3)
    assert WaspLib.check_if_spotify_is_running()


def test_start_track_from_uri(wasp: Wasp, spotify_uri: str) -> None:
    wasp.play_track(spotify_uri=spotify_uri)
    track = wasp.get_track()
    sleep(2)
    assert track['artist'] == 'Rick Astley'


def set_volume_to(wasp: Wasp, volume: int) -> None:
    wasp.set_volume(volume=volume)
    state = wasp.get_state()
    assert state['volume'] == 49


def mute(wasp: Wasp) -> None:
    wasp.mute()
    state = wasp.get_state()
    assert state['volume'] == 0


def unmute(wasp: Wasp) -> None:
    wasp.unmute()
    state = wasp.get_state()
    assert state['volume'] == 48


def jump_to_second(wasp: Wasp, target: int) -> None:
    wasp.jump_to(jump_to_second=target)
    assert wasp.get_state()['position'] == 40


def main():
    if WaspLib.check_if_spotify_is_running():
        exit('Close Spotify before running the tests!')

    wasp = Wasp()

    test_open_spotify(wasp=wasp)
    test_start_track_from_uri(wasp=wasp, spotify_uri='spotify:track:4uLU6hMCjMI75M1A2tKUQC')
    set_volume_to(wasp=wasp, volume=50)
    jump_to_second(wasp=wasp, target=40)
    mute(wasp=wasp)
    unmute(wasp=wasp)


if __name__ == '__main__':
    main()
