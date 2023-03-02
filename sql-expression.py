from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# Execute the instructions from our localhost db ("Chinook").
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# Create variable for "Artist" table.
artist_table = Table(
    "Artist", meta,
    Column("ArtistID", Integer, primary_key=True),
    Column("Name", String)
)

# Create variable for "Album" table.
album_table = Table(
    "Album", meta,
    Column("AlbumID", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistID", Integer, ForeignKey("artist_table.ArtistID"))
)

# Create variable for "Track" table.
track_table = Table(
    "Track", meta,
    Column("TrackID", Integer, primary_key=True),
    Column("Name", String),
    Column("ArtistID", Integer, ForeignKey("album_table.ArtistID")),
    Column("MediaTypeID", Integer, primary_key=False),
    Column("GenreID", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)

)

# Make the connection
with db.connect() as connection:

    # Query 1 Select all from the artists table
    select_query = artist_table.select()

    results = connection.execute(select_query)
    for result in results:
        print(result)
