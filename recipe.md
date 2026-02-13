# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user

> So that I can keep track of my music listening

> I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class MusicTracker:
    # User-facing properties:
    def __init__(self):
        # Parameters: None
        # Side effects:
        #State Attribute:
        #   music_db: list
        pass # No code here yet

    def add_music_track(self, track):
        # Parameters:
        #   track : string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        # - Saves the track to the self music_db
        # - Throws an exception if the track is not a string
        pass # No code here yet

    def get_music_list(self):
        # Returns:
        #   A list of all the music track store in the database
        # Side-effects: None
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

```python
# EXAMPLE

"""
Initally, the function returns an empty list
"""
music_tracker = MusicTracker()
music_tracker.get_music_list() # => []

"""
Given one track added to the list,
the function returns the list with the one track
"""
music_tracker = MusicTracker()
music_tracker.add_music_track("Artist: Golden days, Track: Whiteland")

music_tracker.get_music_list() # => ["Artist: Golden days, Track: Whiteland"]

"""
Given two tracks added to the list,
the function returns the list with the two tracks
"""
music_tracker = MusicTracker()
music_tracker.add_music_track("Artist: Jacob Banks, Track: Part time lover")
music_tracker.add_music_track("Artist: Hot face, Track: Bumble Been")

music_tracker.get_music_list() # => ["Artist: Jacob Banks, Track: Part time lover", "Artist: Hot face, Track: Bumble Been"]

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
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
