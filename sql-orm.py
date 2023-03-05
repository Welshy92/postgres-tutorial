from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Executing instructions from the chinnok database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# Create class-based model for the Artist table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer(), primary_key=True)
    Name = Column(String)


# Create class-based model for the Album table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# Create class-based model for the Track table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# Create a new instance of sessionmaker, then point it to our engine (db)
Session = sessionmaker(db)
# Open the session by calling the Session subclass defined above
session = Session()

# Create the database using the declaritive_base subclass
base.metadata.create_all(db)


# Query 1 Select all from the artist table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 Select names from the artist table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 Find the artist name Queen only
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 Find the artistID of 51
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 Select albums with the AritstID of 51
albums = session.query(Album).filter_by(ArtistId=51)
for album in albums:
    print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 Filter composer of queen from the tracks class
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | ")
