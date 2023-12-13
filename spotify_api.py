import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyAPI:
    def __init__(self, client_id, client_secret):
        # Inicialização da API do Spotify com as credenciais do cliente
        self.__client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=self.__client_credentials_manager)

    def get_track_details(self, track_id):
        # Método para obter detalhes de uma música pelo seu ID
        track_info = self.sp.track(track_id)
        return track_info

    def add_tracks_to_playlist(self, user_id, playlist_id, track_ids):
        # Método para adicionar múltiplas músicas a uma playlist do usuário
        self.sp.user_playlist_add_tracks(user_id, playlist_id, track_ids)
        return f"Músicas adicionadas à playlist {playlist_id}"

    def search_track(self, track_name):
        # Método para buscar uma música por nome
        results = self.sp.search(q=track_name, limit=1)
        if results['tracks']['items']:
            return results['tracks']['items'][0]
        else:
            return None

    def list_user_playlists(self, user_id):
        # Método para listar as playlists do usuário
        playlists = self.sp.user_playlists(user_id)
        if playlists:
            for playlist in playlists['items']:
                print(f"{playlist['name']} - {playlist['id']}")
        else:
            print("Nenhuma playlist encontrada.")