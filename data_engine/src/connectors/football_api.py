import requests
import os
import json
import sys

sys.path.append('/app/src') 
from utils.logger import setup_logger

class FootballAPI:
    def __init__(self):
        # 1. Iniciamos el Logger
        self.logger = setup_logger("FootballAPI_Connector", "ingestion.log")

        # Instanciamos variables de entorno y configuración
        self.api_key = os.getenv("FOOTBALL_API_KEY")
        self.base_url = "https://v3.football.api-sports.io/"
        
        if not self.api_key:
            self.logger.critical("No se encontró la variable FOOTBALL_API_KEY en el entorno.")
            raise ValueError("Error: No se encontró la variable FOOTBALL_API_KEY")

        self.headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': self.api_key
        }
    
    def save_json(self, data, path, filename):
        # Guardar datos JSON en el sistema de archivos
        try:
            os.makedirs(path, exist_ok=True)
            full_path = os.path.join(path, filename)
            
            with open(full_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            
            self.logger.info(f"Archivo guardado en: {full_path}")
            
        except Exception as e:
            self.logger.error(f"Error al intentar guardar el archivo {filename}: {e}")

    # Funciones para interactuar con la API
    
    def get_data(self, endpoint, params=None):
        # Función para realizar una petición GET a la API
        url = f"{self.base_url}{endpoint}"
        
        self.logger.info(f"Solicitud a: {endpoint} [ Parametros: {params} ]")

        # Realizamos la petición
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            
            self.logger.error(f"Error de conexión con API Football: {e}")
            return None

    #Función para obtener ligas 
    def get_leagues(self, season):
        endpoint = "leagues"
        params = {"season": season}
        
        data = self.get_data(endpoint, params)
        if data:
            return data.get("response", [])
        return []
    
    #Función para obtener fixtures
    def get_fixtures(self, league_id, season):
        endpoint = "fixtures"
        params = {"league": league_id, "season": season}
        
        data = self.get_data(endpoint, params)
        if data:
            return data.get("response", [])
        return []
    
    def get_teams_information(self, team_id, season):
        endpoint = "teams"
        params = {"id": team_id, "season": season}
        
        data = self.get_data(endpoint, params)
        if data:
            return data.get("response", [])
        return []
    
    def get_teams_statistics(self, team_id, league_id, season):
        endpoint = "teams/statistics"
        params = {"team": team_id, "league": league_id, "season": season}
        
        data = self.get_data(endpoint, params)
        if data:
            return data.get("response", [])
        return []
    
    def get_squads(self, team_id):
        endpoint = "players/squads"
        params = {"team": team_id}
        
        data = self.get_data(endpoint, params)
        if data:
            return data.get("response", [])
        return []
    
    def get_players_statistics(self, player_id, season, team_id):
        endpoint = "players"
        params = {"id": player_id, "season": season, "team": team_id}
        
        data = self.get_data(endpoint, params)
        if data:
            return data.get("response", [])
        return []
    
    def get_standings(self, league_id, season):
        endpoint = "standings"
        params = {"league": league_id, "season": season}
        
        data = self.get_data(endpoint, params)
        if data:
            return data.get("response", [])
        return []