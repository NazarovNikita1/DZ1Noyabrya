def jaccard_similarity(sentence1, sentence2):
    #токенизируем
    words1 = set(sentence1.lower().split())
    words2 = set(sentence2.lower().split())

    #пересечение токенов
    intersection = len(words1.intersection(words2))

    #коэф жаккара
    union = len(words1) + len(words2) - intersection
    if union == 0:
        #на ноль не делим
        return 0
    else:
        similarity = intersection / union
        return similarity

#пример
sentence1 = "Wes Anderson is a decent director"
sentence2 = "But Martin Scorcese surpasses Wes as a director"
result = jaccard_similarity(sentence1, sentence2)
print(result)

