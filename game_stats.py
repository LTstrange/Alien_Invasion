class GameStats:
    """keep tract of game stats"""

    def __init__(self, ai_settings):
        """init stats"""
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        """初始化在游戏运行期间可能改变的统计信息"""
        self.ship_left = self.ai_settings.ship_limit

