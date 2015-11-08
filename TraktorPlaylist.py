def main():
	# List to be filled with tuples of track names and artists
	tracks = list()

	# Fill tracks list
	with open("Radio.html") as f:
		trackPart = None
		trackName = ""
		for line in f:
			if "<tr>" in line:
				trackPart = 0
			elif trackPart == 0:
				trackPart = 1
			elif trackPart == 1:
				trackName = line.strip()
				trackName = trackName[4:-5]
				trackPart = 2
			elif trackPart == 2:
				trackArtist = line.strip()
				trackArtist = trackArtist[4:-5]
				tracks.append((trackName,trackArtist))
				trackPart = None

	# Write tracks to text file
	with open("Tracklist.txt", "w") as f:
		for track in tracks:
			f.write(track[0] + " - " + track[1] + '\n')


if __name__ == "__main__":
    main()