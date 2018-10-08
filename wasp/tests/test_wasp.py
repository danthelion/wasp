from wasp.core import Wasp

wasp = Wasp()

wasp.get_track()
wasp.get_state()

print(wasp.track.metadata)
print(wasp.spotify_controller.state)

wasp.volume_down()
wasp.volume_up()

