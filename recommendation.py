from spotify_api import SpotifyAPI

class GenreBasedRecommender:
    def __init__(self, client_id, client_secret):
        # Inicialização do recomendador por gênero utilizando a API do Spotify
        self.spotify = SpotifyAPI(client_id, client_secret)
        self.recommended_tracks = []

    def recommend_music_by_genre(self, genre):
        # Método para recomendar músicas com base no gênero musical
        recommended_tracks = self.spotify.sp.recommendations(seed_genres=[genre])
        self.recommended_tracks = recommended_tracks['tracks']
        return self.recommended_tracks

class PersonalizedRecommender:
    def __init__(self, client_id, client_secret, user_id):
        # Inicialização do recomendador personalizado utilizando a API do Spotify
        self.spotify = SpotifyAPI(client_id, client_secret)
        self.user_id = user_id

    def recommend_personalized(self):
        # Método para recomendação personalizada com base nas músicas mais ouvidas pelo usuário
        user_top_tracks = self.spotify.sp.current_user_top_tracks(limit=5)
        if user_top_tracks:
            seed_tracks = [track['id'] for track in user_top_tracks['items']]
            recommended_tracks = self.spotify.sp.recommendations(seed_tracks=seed_tracks)
            return recommended_tracks['tracks']
        else:
            return None