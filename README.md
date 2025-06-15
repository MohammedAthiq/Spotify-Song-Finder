# 🎵 Spotify Song Finder (CLI)

A simple Python command-line tool that allows you to search for songs on Spotify using just a line of lyrics or a phrase.

## 🚀 Features

- 🔍 Search Spotify for songs using partial lyrics
- 📄 Returns song title, artist, and Spotify link
- 🧠 Uses Spotify API
- ⚙️ Lightweight CLI tool

## 🛠️ Requirements

- Python 3.7+
- Internet connection
- Spotify Developer credentials

## 📦 Installation

```bash
git clone https://github.com/MohammedAthiq/Spotify-Song-Finder.git
cd Spotify-Song-Finder
pip install -r requirements.txt
# 🎵 Spotify Song Finder (CLI)

A lightweight Python command-line tool that lets you find songs on Spotify using just a line of lyrics or a phrase.

---

## 📌 Features

- 🔍 Search for songs using partial lyrics or phrases
- 🎧 Returns song title, artist name, and Spotify link
- 🧠 Powered by the Spotify Web API
- ⚙️ Easy to use CLI interface
- 🔐 Securely handles API keys with `.env` file

---

## 🛠️ Requirements

- Python 3.7 or higher
- Internet connection
- Spotify Developer credentials (Client ID & Secret)

---

## 🚀 Installation & Setup

```bash
git clone https://github.com/MohammedAthiq/Spotify-Song-Finder.git
cd Spotify-Song-Finder
pip install -r requirements.txt
```

### 🔐 Create your `.env` file

Make a file called `.env` in the root directory and add:

```env
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
```

You can get your credentials from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

---

## ▶️ Example Usage

```bash
$ python main.py
Enter song lyrics: I got a feeling
🎵 Song Name: I Gotta Feeling
🎤 Artist: Black Eyed Peas
🔗 Spotify Link: https://open.spotify.com/track/xyz123
```

---

## 💡 Notes

- This project uses the **Client Credentials Flow**, so it works for search but doesn't access user-specific data like playlists or liked songs.
- Lyrics must be somewhat accurate and publicly indexed on Spotify to return good results.

---

## 🤝 Contributing

Pull requests are welcome! If you'd like to improve the tool, fix bugs, or add features, feel free to open an issue or submit a PR.

