class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于非活动状态
        self.game_active = False

        # 在任何情况下都不应重置最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化随游戏进行可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


    def increase_score(self):
        self.score += self.ai_settings.alien_points

    def check_high_score(self, scoreboard):
        """检查是否诞生了新的最高得分"""
        if self.score >= self.high_score:
            self.high_score = self.score
            scoreboard.prep_high_score()
