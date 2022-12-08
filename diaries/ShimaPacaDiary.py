from diaries.AbstractDiary import AbstractDiary


class ShimaPacaDiary(AbstractDiary):
    def get_date(self):
        return "2022-12-08"

    def get_summary(self):
        return "眠たい"

    def get_author(self):
        return "ShimaPaca"
