class ArtGallery:
    # Parameterized constructor with a default empty list for artworks
    def __init__(self, gallery_name, location, artworks=None):
        self.gallery_name = gallery_name
        self.location = location
        # Avoid mutable default argument pitfalls by initializing inside __init__
        self.artworks = artworks if artworks is not None else []
        print(f"\n[System] '{self.gallery_name}' in {self.location} has been initialized.")

    # Method to add a new artwork
    def add_artwork(self, title, artist, year, price):
        artwork = {
            "title": title,
            "artist": artist,
            "year": year,
            "price": price
        }
        self.artworks.append(artwork)
        print(f"Added '{title}' by {artist} to the collection.")

    # Method to display all artworks
    def view_artworks(self):
        print(f"\n--- {self.gallery_name} ({self.location}) Collection ---")
        if not self.artworks:
            print("The gallery collection is currently empty.")
            return

        for idx, art in enumerate(self.artworks, start=1):
            print(f"{idx}. '{art['title']}' by {art['artist']} ({art['year']}) - ${art['price']:,.2f}")

    # Method to search for an artwork by title
    def search_artwork(self, title):
        for art in self.artworks:
            if art["title"].lower() == title.lower():
                print(f"\nFound: '{art['title']}' by {art['artist']} ({art['year']}) - ${art['price']:,.2f}")
                return
        print(f"\nArtwork titled '{title}' was not found in the collection.")

    # Method to remove an artwork by title
    def remove_artwork(self, title):
        for art in self.artworks:
            if art["title"].lower() == title.lower():
                self.artworks.remove(art)
                print(f"Removed '{art['title']}' from the collection.")
                return
        print(f"Cannot remove: '{title}' was not found.")

    # Destructor to demonstrate object cleanup when deleted or program ends
    def __del__(self):
        print(f"\n[System] Closing '{self.gallery_name}'. Gallery object deleted from memory.")


def main():
    # Setup the gallery using the parameterized constructor
    name = input("Enter the Art Gallery name: ")
    location = input("Enter the Gallery location: ")
    gallery = ArtGallery(name, location)

    # Menu-driven loop
    while True:
        print("\n=== Art Gallery Collection Manager ===")
        print("1. Add Artwork")
        print("2. View All Artworks")
        print("3. Search Artwork by Title")
        print("4. Remove Artwork")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            title = input("Artwork Title: ")
            artist = input("Artist Name: ")
            year = input("Year Created: ")
            try:
                price = float(input("Estimated Value ($): "))
                gallery.add_artwork(title, artist, year, price)
            except ValueError:
                print("Invalid price. Please enter a numeric value.")

        elif choice == "2":
            gallery.view_artworks()

        elif choice == "3":
            title = input("Enter the title to search: ")
            gallery.search_artwork(title)

        elif choice == "4":
            title = input("Enter the title to remove: ")
            gallery.remove_artwork(title)

        elif choice == "5":
            print("Exiting the Art Gallery Collection Manager...")
            # Explicitly deleting the object triggers __del__ immediately
            del gallery
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()
