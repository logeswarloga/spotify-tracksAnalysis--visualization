
# 🎧 Spotify Track Data Importer and Visualizer

This project is a Python-based application that performs the following tasks using the Spotify Web API and MySQL:

1. Extracts and visualizes metadata for a single Spotify track.
2. Stores the metadata into a MySQL database.
3. Processes multiple Spotify tracks from a CSV file and inserts the data into MySQL.

---

## 📁 Project Structure

```
spotify-track-project/
├── spotify.py           # Handles single track extraction, MySQL insertion, and visualization
├── sp_mysql.py      # Connects to MySQL and inserts single track metadata
├── tracks.csvt.py       # Reads multiple track URLs from a CSV file and inserts into MySQL
├── tracks.csv           # CSV file containing multiple Spotify track URLs (one per line)
├── spodify_trackdata.csv # Output CSV for single track data
├── README.md            # Project documentation
```

---

## 🚀 Features

- ✅ Fetch track metadata from Spotify (Track Name, Artist, Album, Popularity, Duration)
- ✅ Visualize track popularity and duration using matplotlib
- ✅ Insert metadata into MySQL
- ✅ Handle both single and multiple track URLs

---

## ⚙️ Requirements

Install required packages:

```bash
pip install spotipy mysql-connector-python matplotlib pandas
```

---

## 🛠️ Setup Instructions

### 1. Spotify Developer Setup

- Visit [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
- Create an app to get your `client_id` and `client_secret`
- Use those credentials in all Python scripts where authentication is required.

### 2. MySQL Database Setup

- Create a MySQL database named `spotify`
- Run the following SQL to create the table:

```sql
CREATE TABLE track_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_min FLOAT
);
```

---

## 🧪 File Descriptions

### `spotify.py`
- Extracts metadata from a **single Spotify track URL**
- Displays metadata in terminal
- Saves metadata to a CSV file (`spodify_trackdata.csv`)
- Visualizes `Popularity` and `Duration` using `matplotlib`
- Optionally inserts the data into MySQL

### `mysql_single.py`
- Focuses on connecting to MySQL and inserting one track's metadata
- Simple and clean version for testing DB integration

### `bulk_import.py`
- Reads Spotify track URLs from a file `tracks.csv`
- Processes each URL and extracts track metadata
- Inserts all records into MySQL in a loop
- Skips invalid or broken URLs with error messages

---

## 📂 Example CSV (tracks.csv)

```
https://open.spotify.com/track/003vvx7Niy0yvhvHt4a68B
https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b
https://open.spotify.com/track/6habFhsOp2NvshLv26DqMb
```

---

## 📌 Notes

- Ensure MySQL server is running and credentials in the scripts match your database.
- If your track data does not appear in MySQL, check:
  - If the track URL is valid
  - If the SQL table exists and matches the schema
  - If `cursor.commit()` is called after insertion

---

## 👨‍💻 Author

Built by **Logeswar** for practical use of Spotify APIs, database integration, and data visualization.

---

