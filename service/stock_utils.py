
@staticmethod
def get_per(시가총액, 당기순이익):
    return int(시가총액)/ int(당기순이익)

# 비용 대비 수익비율
@staticmethod
def get_roi(수익, 매출원가):
    return (int(수익) - int(매출원가)) / int(매출원가)
