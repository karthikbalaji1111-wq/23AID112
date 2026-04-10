# Music Player using Doubly Linked List — Clean, Structured Documentation

---

## Project Overview
This project simulates a **Music Player** using a **Doubly Linked List (DLL)**.

Each song is a node with:
- `next` → next song
- `prev` → previous song

Enables:
- Forward navigation (Next)
- Backward navigation (Previous)
- Efficient deletion of current song

---

## Why Doubly Linked List?

| Requirement              | Why DLL fits                 |
|--------------------------|------------------------------|
| Next song                | `next` pointer               |
| Previous song            | `prev` pointer               |
| Delete current song      | O(1) pointer updates         |
| No shifting like arrays  | Efficient insert/delete      |

---

## Full Code

```python
class SongNode:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None


class MusicPlayer:
    def __init__(self):
        self.head = None
        self.current = None
        self.is_playing = False

    def add_song(self, name):
        new_song = SongNode(name)

        if self.head is None:
            self.head = new_song
            self.current = new_song
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_song
            new_song.prev = temp

        print(f"Added song: {name}")

    def play(self):
        if self.current is None:
            print("Playlist is empty.")
            return
        self.is_playing = True
        print(f"Playing: {self.current.name}")

    def pause(self):
        if not self.is_playing:
            print("No song is playing.")
            return
        self.is_playing = False
        print(f"Paused: {self.current.name}")

    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.play()
        else:
            print("No next song available.")

    def prev_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            self.play()
        else:
            print("No previous song available.")

    def delete_song(self):
        if self.current is None:
            print("Playlist is empty.")
            return

        print(f"Deleted song: {self.current.name}")

        if self.current.prev:
            self.current.prev.next = self.current.next
        else:
            self.head = self.current.next

        if self.current.next:
            self.current.next.prev = self.current.prev
            self.current = self.current.next
        else:
            self.current = self.current.prev

        if self.current:
            self.play()
        else:
            print("Playlist is now empty.")

    def show_playlist(self):
        if self.head is None:
            print("Playlist is empty.")
            return

        print("\nPlaylist:")
        temp = self.head
        while temp:
            marker = "=>" if temp == self.current else "  "
            print(f"{marker} {temp.name}")
            temp = temp.next
        print()


def main():
    player = MusicPlayer()

    while True:
        print("\n1. Add Song")
        print("2. Play")
        print("3. Pause")
        print("4. Next Song")
        print("5. Previous Song")
        print("6. Delete Current Song")
        print("7. Show Playlist")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter song name: ")
            player.add_song(name)

        elif choice == "2":
            player.play()

        elif choice == "3":
            player.pause()

        elif choice == "4":
            player.next_song()

        elif choice == "5":
            player.prev_song()

        elif choice == "6":
            player.delete_song()

        elif choice == "7":
            player.show_playlist()

        elif choice == "8":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
```

---

## Function-wise Explanation

### 1. `SongNode`
```python
class SongNode:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None
```
- Represents a **single song**.
- `next` and `prev` enable **bi-directional traversal**.

---

### 2. `__init__` (MusicPlayer)
```python
self.head = None
self.current = None
self.is_playing = False
```
| Variable     | Purpose            |
|--------------|--------------------|
| head         | start of list      |
| current      | navigation control |
| is_playing   | state control      |

---

### 3. `add_song()`
- Adds a new node at the **end**.
- Traverses to last node → links new node.
- Time Complexity: **O(n)**.

```python
 def add_song(self, name):
        new_song = SongNode(name)

        if self.head is None:
            self.head = new_song
            self.current = new_song
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_song
            new_song.prev = temp

        print(f"Added song: {name}")
```

---

### 4. `play()`
- Starts playback of `current`.
- Guards against empty playlist.

```python 

    def play(self):
        if self.current is None:
            print("Playlist is empty.")
            return
        self.is_playing = True
        print(f"Playing: {self.current.name}")
```

---

### 5. `pause()`
- Toggles `is_playing` to False.
- Prevents pausing when already paused.

```python 

    def pause(self):
        if not self.is_playing:
            print("No song is playing.")
            return
        self.is_playing = False
        print(f"Paused: {self.current.name}")
```

---

### 6. `next_song()`
- Moves pointer: `current = current.next`.
- Requires `current.next` to exist.
- Time: **O(1)**.

```python
    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.play()
        else:
            print("No next song available.")
```

---

### 7. `prev_song()`
- Moves pointer backward using `prev`.
- Time: **O(1)**.

```python

    def prev_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            self.play()
        else:
            print("No previous song available.")
```
---

### 8. `delete_song()` (Critical)
Handles:
1. Middle node → reconnect links
2. Head node → shift head
3. Last node → move current backward

```python

   def delete_song(self):
        if self.current is None:
            print("Playlist is empty.")
            return

        print(f"Deleted song: {self.current.name}")

        if self.current.prev:
            self.current.prev.next = self.current.next
        else:
            self.head = self.current.next

        if self.current.next:
            self.current.next.prev = self.current.prev
            self.current = self.current.next
        else:
            self.current = self.current.prev

        if self.current:
            self.play()
        else:
            print("Playlist is now empty.")
```

---

### 9. `show_playlist()`
- Traverses from `head`.
- Highlights current song using '---->'
```python

   def show_playlist(self):
        if self.head is None:
            print("Playlist is empty.")
            return

        print("\nPlaylist:")
        temp = self.head
        while temp:
            marker = "=>" if temp == self.current else "  "
            print(f"{marker} {temp.name}")
            temp = temp.next
        print()
```

---

### 10. `main()`
- Menu-driven loop for interaction.
- Keeps program running until exit.

```python 
def main():
    player = MusicPlayer()

    while True:
        print("\n1. Add Song")
        print("2. Play")
        print("3. Pause")
        print("4. Next Song")
        print("5. Previous Song")
        print("6. Delete Current Song")
        print("7. Show Playlist")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter song name: ")
            player.add_song(name)

        elif choice == "2":
            player.play()

        elif choice == "3":
            player.pause()

        elif choice == "4":
            player.next_song()

        elif choice == "5":
            player.prev_song()

        elif choice == "6":
            player.delete_song()

        elif choice == "7":
            player.show_playlist()

        elif choice == "8":
            break

        else:
            print("Invalid choice.")
```
---

## Key Takeaways
- DLL enables **bidirectional navigation**.
- `current` pointer controls the system.
- Deletion requires careful **pointer updates**.

---

## Mastery Outcome
If you understand this fully:
- You can solve Linked List problems confidently
- You understand pointer manipulation deeply
- You can build real-world DS systems


