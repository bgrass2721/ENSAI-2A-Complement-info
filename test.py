from lrclib import LrcLibAPI

# Crée une instance de l'API (il est recommandé de préciser un user_agent)
api = LrcLibAPI(user_agent="mon-app/1.0")

# Récupère les paroles d'une chanson
lyrics = api.get_lyrics(
    track_name="I Want to Live",
    artist_name="Borislav Slavov",
    album_name="Baldur's Gate 3 (Original Game Soundtrack)",
    duration=233,  # durée en secondes (optionnel mais recommandé)
)

# Affiche les paroles synchronisées ou non
found_lyrics = lyrics.synced_lyrics or lyrics.plain_lyrics

# Recherche des paroles
results = api.search_lyrics(track_name="Life Letters")

# Affiche les 5 premiers résultats
for result in results[:5]:
    print(f"{result.artist_name} - {result.track_name} ({result.album_name})")

# Récupère les paroles du premier résultat
lyrics = api.get_lyrics_by_id(results[0].id)
found_lyrics = lyrics.synced_lyrics or lyrics.plain_lyrics
print(found_lyrics)
print("1,2,4")