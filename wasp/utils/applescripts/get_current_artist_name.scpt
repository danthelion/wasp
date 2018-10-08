tell application "Spotify"
    set currentArtist to artist of current track as string
    return currentArtist
end tell