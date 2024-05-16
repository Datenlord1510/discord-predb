from .apihelper import APIHelper
from .release import Release
from .comments import Comments
from .extinfo import ExtInfo
from .favorites import Favorites
from .nfo import NFO
from .p2p import P2P
from .search import Search
from .user import User


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
