import tkinter as tk
from tkinter import ttk
from recommendation import GenreBasedRecommender

selected_tracks = []

# Instância do GenreBasedRecommender com as credenciais do cliente
client_id = 'seu_client_id'
client_secret = 'seu_client_secret'
genre_recommender = GenreBasedRecommender(client_id, client_secret)

def recommend_music():
    # Função para recomendar músicas com base no gênero inserido pelo usuário
    genre = entry_genre.get()
    recommended_tracks = genre_recommender.recommend_music_by_genre(genre)
    display_recommendations(recommended_tracks)

def display_recommendations(recommended_tracks):
    clear_display()
    if recommended_tracks:
        canvas = tk.Canvas(root)
        frame = tk.Frame(canvas)
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        frame.bind("<Configure>", lambda event, canvas=canvas: on_frame_configure(canvas))

        for index, track in enumerate(recommended_tracks, start=1):
            label = tk.Label(frame, text=f"{index}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
            label.pack()

            details_button = tk.Button(frame, text="Detalhes", command=lambda t=track: show_details(t))
            details_button.pack()

            add_button = tk.Button(frame, text="Adicionar à Seleção", command=lambda t=track: add_to_selected(t))
            add_button.pack()

        back_button = tk.Button(root, text="Voltar", command=back_to_main)
        back_button.pack()
    else:
        label = tk.Label(root, text="Nenhuma música recomendada para esse gênero.")
        label.pack()

def clear_display():
    for widget in root.winfo_children():
        widget.destroy()

def on_frame_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def back_to_main():
    clear_display()
    # Aqui você pode chamar a função ou criar uma nova para voltar à tela principal

def display_genre_recommendation():
    clear_display()
    
    label_genre = tk.Label(root, text="Digite um gênero:")
    label_genre.pack()

    entry_genre = tk.Entry(root)
    entry_genre.pack()

    button_recommend = tk.Button(root, text="Recomendar", command=recommend_music)
    button_recommend.pack()

def back_to_main():
    clear_display()
    display_genre_recommendation()
def show_details(track):
    # Função para exibir detalhes de uma música
    details = genre_recommender.spotify.get_track_details(track['id'])
    if details:
        details_window = tk.Toplevel()
        details_window.title("Detalhes da Música")
        
        details_label = tk.Label(details_window, text=f"Detalhes da música: {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
        details_label.pack()
        
        details_info = tk.Label(details_window, text=f"Artistas: {', '.join([artist['name'] for artist in track['artists']])}\nÁlbum: {details['album']['name']}\nPopularidade: {details['popularity']}")
        details_info.pack()
    else:
        details_label = tk.Label(root, text="Detalhes não disponíveis.")
        details_label.pack()

def add_to_selected(track):
    # Função para adicionar uma música à lista de músicas selecionadas
    selected_tracks.append(track)
    label = tk.Label(root, text=f"{track['name']} foi adicionada à seleção.")
    label.pack()

# Criação e configuração da interface gráfica
root = tk.Tk()
root.title("RMAX Spot - Sistema de Recomendação de Música")

label_genre = tk.Label(root, text="Digite um gênero:")
label_genre.pack()

entry_genre = tk.Entry(root)
entry_genre.pack()

button_recommend = tk.Button(root, text="Recomendar", command=recommend_music)
button_recommend.pack()

root.mainloop()