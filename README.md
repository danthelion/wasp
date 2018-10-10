# WASP
Wrapper around AppleScript of Spotify in Python.

This library provides a simple wrapper around the AppleScript API
of the Spotify application on MacOS.


Developed and tested with Python 3.7

## Install
```bash
pip install wasp-spotify-bindings
```

## Test
```bash
python wasp/tests/test_wasp.py
python wasp/tests/test_applescript.py
```

## Import
```python
from wasp_spotify_bindings.core import Wasp
wasp = Wasp()
```

## API

_Get track metadata._
```python
wasp.get_track()
```

returns

```python
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
```

_Get player state._
```python
wasp.get_state()
```
returns
```python
{
    "track_id": "spotify:track:4uLU6hMCjMI75M1A2tKUQC",
    "volume": 49,
    "position": 3,  # seconds
    "state": "playing"
}
```

_Start Spotify application._
```python
wasp.start_spotify()
```

_Quit Spotify application._
```python
wasp.quit_spotify()
```

_Play next track._
```python
wasp.next_track()
```

_Play previous track._
```python
wasp.previous_track()
```

_Play current track._
```python
wasp.play()
```

_Toggle play/pause on current track._
```python
wasp.play_pause()
```

_Pause current track._
```python
wasp.pause()
```

_Set volume to [0-100]_
```python
wasp.set_volume(volume=10)
```

_Play track referred to by spotify id._
```python
wasp.play_track(spotify_uri='spotify:track:4uLU6hMCjMI75M1A2tKUQC')
```

_Play track in context of an album/playlist._
```python
wasp.play_track_in_context(
    spotify_uri='spotify:track:4uLU6hMCjMI75M1A2tKUQC',
    context='spotify:track:4uLU6hMCjMI75M1A2tKUQC'
)
```

_Increase volume by 10._
```python
wasp.volume_up()
```

_Decrease volume by 10._
```python
wasp.volume_down()
```

_Jump to position in song (seconds)._
```python
wasp.jump_to(jump_to_second=5)
```

_Check if repeat is enabled._
```python
wasp.is_repeating()
```

_Check if shuffle is enabled._
```python
wasp.is_shuffling()
```

_Set repeating to `True` or `False`._
```python
wasp.set_repeating(set_repeating=True)
```

_Set shuffling to `True` or `False`._
```python
wasp.set_shuffling(set_shuffling=True)
```

_Toggle repeat on/off._
```python
wasp.toggle_repeating()
```

_Toggle shuffle on/off._
```python
wasp.toggle_shuffling()
```

_Mute player._
```python
wasp.mute()
```

_Unmute player._
```python
wasp.unmute()
```
