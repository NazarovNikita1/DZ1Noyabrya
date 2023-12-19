from collections import Counter

class NERStats:
    def __init__(self, document, ner_extractor):
        self.document = document
        self.ner_extractor = ner_extractor
        self.ner_entities = []

    def analyze_entities(self):
        self.ner_entities = self.ner_extractor.extract_entities(self.document)

    def display_most_common_entities(self, n):
        if not self.ner_entities:
            print("Run analyze_entities first.")
            return

        #словарь
        entity_counter = Counter(self.ner_entities)

        most_common_entities = entity_counter.most_common(n)
        print(f"Top {n} Most Common Named Entities:")
        for entity, count in most_common_entities:
            print(f"{entity}: {count}")

# Пример использования:
class NERExtractor:
    def extract_entities(self, document):
        pass

# Создаем экземпляр NERStats
document = "Те, кто водят хороводы — хороводоводы. Те, кто изучают творчество хороводоводов — хороводоводоведы. Те, кто любят читать хороводоводоведов — хороводоводоведофилы. Те, кто ненавидит хороводоводоведофилов — хороводоводоведофилофобы."
ner_extractor = NERExtractor()
ner_stats = NERStats(document, ner_extractor)

ner_stats.analyze_entities()

#отображение 3 самых частотных именованных сущностей
ner_stats.display_most_common_entities(3)
