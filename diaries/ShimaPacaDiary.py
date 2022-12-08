from diaries.AbstractDiary import AbstractDiary


class ShimaPacaDiary(AbstractDiary):
    def get_date(self):
        return "2023-01-01"

    def get_summary(self):
        return "あけおめ-"

    def get_author(self):
        return "ShimaPaca"
