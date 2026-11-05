"""Spoken texts in German and English, chosen by the locale of the Alexa request."""

MESSAGES = {
    'de': {
        'ready': 'Bereit! Sag zum Beispiel: spiele Musik von Coldplay.',
        'unsupported': 'Dieses Gerät wird nicht unterstützt.',
        'help': 'Du kannst sagen: spiele Musik von Coldplay, spiele das Album Parachutes, spiele den Song Yellow von Coldplay, spiele zufällige Musik, oder weiter, zurück, pause. Zum Beenden sag stopp.',
        'artist_not_found': 'Ich habe {artist} in der Sammlung nicht gefunden.',
        'playing_artist': 'Ich spiele Musik von {artist}.',
        'album_by_not_found': 'Ich habe das Album {album} von {artist} nicht gefunden.',
        'playing_album_by': 'Ich spiele {album} von {artist}.',
        'album_not_found': 'Ich habe das Album {album} nicht gefunden.',
        'playing_album': 'Ich spiele {album}.',
        'song_not_found': 'Ich habe den Song {song} von {artist} nicht gefunden.',
        'playing_song': 'Ich spiele {song} von {artist}.',
        'playlist_not_found': 'Ich habe die Playlist {playlist} nicht gefunden.',
        'playing_playlist': 'Ich spiele die Playlist {playlist}.',
        'genre_not_found': 'Ich habe keine Lieder im Stil {genre} gefunden.',
        'playing_genre': 'Ich spiele {genre}.',
        'no_songs': 'Ich habe keine Lieder in der Sammlung gefunden.',
        'playing_random': 'Ich spiele zufällige Musik.',
        'no_favourites': 'Du hast noch keine Lieblingslieder markiert.',
        'playing_favourites': 'Ich spiele deine Lieblingslieder.',
        'now_playing': 'Das ist {title} von {artist}, vom Album {album}.',
        'sorry': 'Entschuldigung, das habe ich nicht verstanden. Sag es bitte noch einmal.',
    },
    'en': {
        'ready': 'Ready! Say for example: play music by Coldplay.',
        'unsupported': 'This device is not supported.',
        'help': 'You can say: play music by Coldplay, play the album Parachutes, play the song Yellow by Coldplay, play random music, or next, previous, pause. Say stop to end.',
        'artist_not_found': "I couldn't find {artist} in the collection.",
        'playing_artist': 'Playing music by {artist}.',
        'album_by_not_found': "I couldn't find an album called {album} by {artist} in the collection.",
        'playing_album_by': 'Playing {album} by {artist}.',
        'album_not_found': "I couldn't find the album {album} in the collection.",
        'playing_album': 'Playing {album}.',
        'song_not_found': "I couldn't find a song called {song} by {artist} in the collection.",
        'playing_song': 'Playing {song} by {artist}.',
        'playlist_not_found': "I couldn't find the playlist {playlist} in the collection.",
        'playing_playlist': 'Playing playlist {playlist}.',
        'genre_not_found': "I couldn't find any {genre} songs in the collection.",
        'playing_genre': 'Playing {genre} music.',
        'no_songs': "I couldn't find any songs in the collection.",
        'playing_random': 'Playing random music.',
        'no_favourites': "You don't have any favourite songs in the collection.",
        'playing_favourites': 'Playing your favourite tracks.',
        'now_playing': 'This is {title} by {artist}, from the album {album}.',
        'sorry': "Sorry, I didn't get that. Can you please say it again?",
    },
}


def language_of(handler_input) -> str:
    """'de' or 'en' from the request locale (anything else falls back to English)."""
    try:
        locale = handler_input.request_envelope.request.locale or ''
    except AttributeError:
        locale = ''
    return 'de' if locale.lower().startswith('de') else 'en'


def tr(handler_input, key: str, **values) -> str:
    """The text for `key` in the request's language, with {placeholders} filled."""
    return MESSAGES[language_of(handler_input)][key].format(**values)
