from lib.music_tracker import MusicTracker

"""
Initally, the function returns an empty list
"""
def test_initially_returns_an_empty_list():
    music_tracker = MusicTracker()
    assert music_tracker.get_music_list()  == []


"""
Given one track added to the list,
the function returns the list with the one track
"""
def test_one_track_added_returns_the_track():
    music_tracker = MusicTracker()
    music_tracker.add_music_track("Artist: Golden days, Track: Whiteland")

    assert music_tracker.get_music_list() == ["Artist: Golden days, Track: Whiteland"]

"""
Given two tracks added to the list,
the function returns the list with the two tracks
"""
music_tracker = MusicTracker()
music_tracker.add_music_track("Artist: Jacob Banks, Track: Part time lover")
music_tracker.add_music_track("Artist: Hot face, Track: Bumble Been")

assert music_tracker.get_music_list() == ["Artist: Jacob Banks, Track: Part time lover", "Artist: Hot face, Track: Bumble Been"]

"""
Given three tracks added to the list,
the function returns the list with the three tracks
"""
music_tracker = MusicTracker()

music_tracker.add_music_track("Artist: Golden days, Track: Whiteland")
music_tracker.add_music_track("Artist: Jacob Banks, Track: Part time lover")
music_tracker.add_music_track("Artist: Hot face, Track: Bumble Been")

music_tracker.get_music_list() # => ["Artist: Golden days, Track: Whiteland", "Artist: Jacob Banks, Track: Part time lover", "Artist: Hot face, Track: Bumble Been"]


"""
When the track is not string
Throws an exception "The track must be a string"
"""
music_tracker = MusicTracker()

music_tracker.add_music_track(1)
# => Throws an exception "The track must be a string"