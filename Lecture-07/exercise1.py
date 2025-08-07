survey_result = [
    ["Python","javaScript","C++"],
    ["Python","javaScript","C#"],
    ["Python","java"],
    ["Python","C++","JavaScript"],
    ["Python","javaScript","C++","Java"],
]
languages_set = [set(languages) for languages in survey_result]
print(languages_set)

choices_set = [set(p) for p in survey_result]
common_languages = set.intersection(*choices_set)
print("1. Languages chosen by all participants:", common_languages)

all_languages = set.union(*languages_set)
unique_languages = len(all_languages)
print("3.The number of unique languages mentioned:", unique_languages)