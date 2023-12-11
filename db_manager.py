import sqlite3
# Run pip3 install sqlite3 
# pip install --upgrade googletrans==4.0.0-rc1
# Create a connection to a new database or connect to an existing one
conn = sqlite3.connect('destinations.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the destinations table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS destinations (
        name TEXT NOT NULL,
        start_age INTEGER NOT NULL,
        end_age INTEGER NOT NULL,
        attraction TEXT NOT NULL,
        terrain TEXT NOT NULL,
        age INTEGER NOT NULL,
        season TEXT NOT NULL
    )
''')

# Define the data to be inserted
destinations_data = [('Vietnam', 20000, 60000, 'Historic attractions', 'Beaches', 50, 'Summer'), ('Venezuela', 10000, 90000, 'Scenic beauty', 'Beaches', 20, 'Summer'), ('Zimbabwe', 100000, 400000, 'Wildlife parks', 'Mountains', 10, 'Winter'), ('Turkey', 70000, 200000, 'Historic attractions', 'Beaches', 40, 'Summer'), ('Mexico', 150000, 400000, 'Historic attractions', 'Beaches', 25, 'Summer'), ('Mauritius', 200000, 500000, 'Water sports', 'Beaches', 18, 'Summer'), ('Jamaica', 10000, 90000, 'Recreational activities', 'Beaches', 25, 'Summer'), ('Iceland', 10000, 90000, 'Scenic beauty', 'Snow', 25, 'Winter'), ('Denmark', 10000, 90000, 'Architecture', 'Beaches', 30, 'Summer'), ('Finland', 10000, 90000, 'Scenic beauty', 'Snow', 20, 'Winter'), ('New Zealand', 200000, 600000, 'Adventure sports', 'Snow', 20, 'Winter'), ('Germany', 800000, 300000, 'Historic attractions', 'Snow', 30, 'Winter'), ('Czech Republic', 40000, 200000, 'Historic attractions', 'Snow', 40, 'Winter'), ('Bhutan', 100000, 400000, 'Cuisine', 'Mountains', 50, 'Winter'), ('Austria', 10000, 90000, 'Scenic beauty', 'Mountains', 40, 'Winter'), ('Bahamas', 500000, 2000000, 'Water sports', 'Beaches', 20, 'Summer'), ('Bangladesh', 20000, 60000, 'Historic attractions', 'Beaches', 50, 'Summer'), ('Cambodia', 50000, 100000, 'National parks', 'Beaches', 50, 'Summer'), ('Canada', 100000, 600000, 'Adventure sports', 'Snow', 20, 'Winter'), ('Cuba', 200000, 600000, 'Scenic beauty', 'Beaches', 40, 'Summer'), ('Israel', 30000, 90000, 'Museums', 'Snow', 40, 'Winter'), ('Kenya', 100000, 600000, 'Scenic beauty', 'Beaches', 30, 'Summer'), ('Madagascar', 100000, 500000, 'Biodiversity', 'Mountains', 10, 'Winter'), ('Monaco', 100000, 600000, 'Scenic beauty', 'Beaches', 30, 'Summer'), ('Spain', 40000, 300000, 'Cuisine', 'Mountains', 30, 'Winter'), ('Italy', 10000, 90000, 'Cuisine', 'Beaches', 25, 'Summer'), ('Greece', 10000, 90000, 'Historic attractions', 'Beaches', 30, 'Summer'), ('Australia', 10000, 90000, 'Scenic beauty', 'Mountains', 20, 'Winter'), ('UAE', 10000, 90000, 'Recreational activities', 'Desert', 20, 'Summer'), ('Brazil', 10000, 90000, 'Biodiversity', 'Forest', 30, 'Winter'), ('China', 10000, 250000, 'Historic attractions', 'Mountains', 30, 'Winter'), ('Japan', 40000, 300000, 'cuisine', 'Mountains', 25, 'Winter'), ('Egypt', 10000, 200000, 'Historic attractions', 'desert', 20, 'Summer'), ('Fiji', 30000, 250000, 'water sports', 'beaches', 15, 'Summer')]


# Insert data into the destinations table
cursor.executemany('''
    INSERT INTO destinations (name, start_age, end_age, attraction, terrain, age, season)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', destinations_data)

# Commit changes and close the connection
conn.commit()
conn.close()
