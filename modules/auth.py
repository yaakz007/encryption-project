#Funções de login e cadastro dos usuários
from modules import utils 
from time import sleep
from pathlib import Path
import json

BASE_DIR = Path(__file__).parent.parent
LOG_FILE = BASE_DIR / 'data' / 'logs.json'


