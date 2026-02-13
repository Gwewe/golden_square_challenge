class MusicTracker:
    # User-facing properties:
    def __init__(self):
        self._music_db = []

    def add_music_track(self, track):
        return self._music_db.append(track)

    def get_music_list(self):
        return  self._music_db