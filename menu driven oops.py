my_playlist = Playlist("Road Trip Mix", "Pop")

while True:
    print("\n1. Add Song  2. Remove Song  3. View Playlist  4. Delete & Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        song = input("Enter song name: ")
        my_playlist.add_song(song)
    elif choice == "2":
        song = input("Enter song to remove: ")
        my_playlist.remove_song(song)
    elif choice == "3":
        my_playlist.display()
    elif choice == "4":
        del my_playlist   # destructor fires
        break
    else:
        print("Invalid choice. Enter 1, 2, 3, or 4.")