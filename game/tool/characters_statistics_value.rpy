# Statistic
default mcStat = Statistic()
default friendStat = Statistic(
    values= {
        "strength"      :   7,
        "intelligence"  :   7,
        "agility"       :   7,
    }
)
# statsSentimental
default girlSentimental = SentimentalStatistic(gender_attracted = "M", virgin = True, bisexual = False, polyamorous = False, against = False)
default friendSentimental = SentimentalStatistic(gender_attracted = "F", virgin = False, bisexual = False, polyamorous = False, against = 20,)
