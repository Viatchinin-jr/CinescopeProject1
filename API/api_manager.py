from API.auth_api import AuthAPI
from API.user_api import UserAPI
import requests
from custom_requester.custom_requester import CustomRequester
from constants import BASE_URL

class ApiManager:
    """
    Класс для управления API-классами с единой HTTP-сессией.
    """
    def __init__(self, session):
        """
        Инициализация ApiManager.
        :param session: HTTP-сессия, используемая всеми API-классами.
        """
        self.session = session
        self.session.base_url = BASE_URL
        self.auth_api = AuthAPI(session)
        self.user_api = UserAPI(session)