from .APIHelper import APIHelper
from .Release import Release
from .Comments import Comments
from .ExtInfo import ExtInfo
from .Favorites import Favorites
from .NFO import NFO
from .P2P import P2P
from .Search import Search
from .User import User


class xREL(APIHelper):

    def __init__(self):
        self.Release = Release()
        self.P2P = P2P()
        self.NFO = NFO()
        self.ExtInfo = ExtInfo()
        self.Search = Search()
        self.Favorites = Favorites()
        self.Comments = Comments()
        self.User = User()
