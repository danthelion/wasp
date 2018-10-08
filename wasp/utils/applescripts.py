CHECK_IF_SPOTIFY_IS_RUNNING = """
if application "Spotify" is running then
    return "1"
else
    return "0"
end if
"""

QUIT_SPOTIFY = """
tell application "Spotify"
    quit
end tell
"""

START_SPOTIFY = """
tell application "Spotify"
    activate
end tell
"""

NEXT_TRACK = """
tell application "Spotify"
    next track
end tell
"""

PREVIOUS_TRACK = """
tell application "Spotify"
    previous track
end tell
"""

PAUSE = """
tell application "Spotify"
    pause
end tell
"""

PLAY = """
tell application "Spotify"
    play
end tell
"""

PLAY_TRACK = """
tell application "Spotify"
    play track "{spotify_uri}"
end tell
"""

# Credit to https://github.com/andrehaveman/spotify-node-applescript for the following AppleScripts

GET_TRACK_METADATA = r"""
on escape_quotes(string_to_escape)
  set AppleScript's text item delimiters to the "\""
  set the item_list to every text item of string_to_escape
  set AppleScript's text item delimiters to the "\\\""
  set string_to_escape to the item_list as string
  set AppleScript's text item delimiters to ""
  return string_to_escape
end escape_quotes

tell application "Spotify"
  set ctrack to "{"
  set ctrack to ctrack & "\"artist\": \"" & my escape_quotes(current track's artist) & "\""
  set ctrack to ctrack & ",\"album\": \"" & my escape_quotes(current track's album) & "\""
  set ctrack to ctrack & ",\"disc_number\": " & current track's disc number
  set ctrack to ctrack & ",\"duration\": " & current track's duration
  set ctrack to ctrack & ",\"played_count\": " & current track's played count
  set ctrack to ctrack & ",\"track_number\": " & current track's track number
  set ctrack to ctrack & ",\"popularity\": " & current track's popularity
  set ctrack to ctrack & ",\"id\": \"" & current track's id & "\""
  set ctrack to ctrack & ",\"name\": \"" & my escape_quotes(current track's name) & "\""
  set ctrack to ctrack & ",\"album_artist\": \"" & my escape_quotes(current track's album artist) & "\""
  set ctrack to ctrack & ",\"artwork_url\": \"" & current track's artwork url & "\""
  set ctrack to ctrack & ",\"spotify_url\": \"" & current track's spotify url & "\""
  set ctrack to ctrack & "}"
end tell
"""

GET_PLAYER_STATE = r"""
tell application "Spotify"
  set cstate to "{"
  set cstate to cstate & "\"track_id\": \"" & current track's id & "\""
  set cstate to cstate & ",\"volume\": " & sound volume
  set cstate to cstate & ",\"position\": " & (player position as integer)
  set cstate to cstate & ",\"state\": \"" & player state & "\""
  set cstate to cstate & "}"

  return cstate
end tell
"""

VOLUME_UP = r"""
on min(x, y)
  if x ≤ y then
    return x
  else
    return y
  end if
end min

tell application "Spotify" to set sound volume to (my min(sound volume + 10, 100))
"""

VOLUME_DOWN = """
on max(x, y)
    if x ≤ y then
        return y
    else
        return x
    end if
end max

tell application "Spotify" to set sound volume to (my max(sound volume - 10, 0))
"""
