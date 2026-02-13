from lib.music_tracker import MusicTracker
import pytest

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
def test_two_track_added_returns_both_tracks():
    music_tracker = MusicTracker()
    
    music_tracker.add_music_track("Artist: Jacob Banks, Track: Part time lover")
    music_tracker.add_music_track("Artist: Hot face, Track: Bumble Been")

    assert music_tracker.get_music_list() == ["Artist: Jacob Banks, Track: Part time lover", "Artist: Hot face, Track: Bumble Been"]



"""
Given three tracks added to the list,
the function returns the list with the three tracks
"""
def test_three_track_added_returns_all_three_tracks():

    music_tracker = MusicTracker()

    music_tracker.add_music_track("Artist: Golden days, Track: Whiteland")
    music_tracker.add_music_track("Artist: Jacob Banks, Track: Part time lover")
    music_tracker.add_music_track("Artist: Hot face, Track: Bumble Been")

    assert music_tracker.get_music_list() == ["Artist: Golden days, Track: Whiteland", "Artist: Jacob Banks, Track: Part time lover", "Artist: Hot face, Track: Bumble Been"]


"""
When the track is not string
Throws an exception "The track must be a string"
"""
def test_add_non_valid_track_throws_error():

    music_tracker = MusicTracker()
    with pytest.raises(TypeError) as error:
        music_tracker.add_music_track(1)
    
    assert str(error.value) == "The track must be a string"
