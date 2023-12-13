# RMAX Spot - Sistema de Recomendação de Música com Spotify API

Este é um projeto de recomendação de música que utiliza a API do Spotify para recomendar músicas com base em gêneros musicais fornecidos pelo usuário.

## Configuração do Ambiente

### Pré-requisitos
- Python 3.x instalado
- Conta de desenvolvedor no Spotify Developer Dashboard

### Configuração do Spotify API
Antes de executar o projeto, insira seu `client_id` e `client_secret` diretamente no arquivo `main.py`:

```python
# main.py
client_id = 'SEU_CLIENT_ID'
client_secret = 'SEU_CLIENT_SECRET'
```

## Executando o projeto

Para iniciar o projeto, execute o arquivo `main.py`:

```bash
python main.py
```

Isso abrirá a interface gráfica onde você pode inserir gêneros musicais para receber recomendações.

## Funcionalidades
- **Recomendação por Gênero:** Insira um gênero musical para receber recomendações de músicas desse gênero.
- **Detalhes da Música:** Visualize detalhes de uma música recomendada.
- **Adicionar à Seleção:** Adicione músicas à lista de músicas selecionadas.
