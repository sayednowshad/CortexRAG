class EvidenceExtractor:

    @staticmethod
    def extract(
        chunks,
        question: str,
        max_sentences: int = 10
    ):

        keywords = set(
            question.lower().split()
        )

        evidence = []

        for chunk in chunks:

            text = chunk["content"]

            sentences = text.split(".")

            for sentence in sentences:

                sentence = sentence.strip()

                if not sentence:

                    continue

                score = 0

                sentence_words = set(
                    sentence.lower().split()
                )

                overlap = len(
                    keywords.intersection(
                        sentence_words
                    )
                )

                score += overlap

                evidence.append(
                    (
                        score,
                        sentence,
                        chunk["source"]
                    )
                )

        evidence.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        best_sentences = []

        used = set()

        for score, sentence, source in evidence:

            if sentence in used:

                continue

            used.add(sentence)

            best_sentences.append(
                sentence
            )

            if (
                len(best_sentences)
                >= max_sentences
            ):
                break

        return "\n".join(
            best_sentences
        )