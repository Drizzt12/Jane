import plistlib
def open():
    global tracks
    global trackNames
    fileName = "/Users/apple/Music/iTunes/iTunes Music Library.xml"
    # Read playlist
    plist = plistlib.readPlist(fileName)
    # Get tracks
    tracks = plist["Tracks"]
    # Create a track name directory
    trackNames = {}
    # iterate through the tracks
    for trackId, track in tracks.items():
        try:
          name = track["Name"]
          duration = track["Total Time"]
          play_count = track["Play Count"]
          artist = track["Artist"]
          genre = track["Genre"]
          # look for existing entries
          if name in trackNames:
            # if a name and duration match, increment the count
            # round the track length to the nearest second
            if duration//1000 == trackNames[name][0]//1000:
              count = trackNames[name][1]
              trackNames[name] = (artist, duration, play_count, count+1, genre)
          else:
            # add dictionary entry as tuple (artist, duration, play_count, count)
            trackNames[name] = (artist, duration, play_count, 1, genre)
        except:
          # ignore
          pass

#Find favorite song
def fav():
    l = []
    for name in trackNames:
        i = trackNames[name]
        if i[2] not in l:
            l.append(i[2])
        else:
            multiple = True
    num = max(l)
    for name in trackNames:
        i = trackNames[name]
        if i[2] == num:
            favsong = name
            break
    print("Your favorite song is '" + favsong + "'.")

#Print all songs
def print_all():
    for i in trackNames:
        l = trackNames[i]
        if l[4] != "Podcast":
            print("'" + i + "', by " + l[0] + ": Number of times played: " + str(l[2]) + ", Number of appearences in library: " + str(l[3]))


##################

open()
