import re


class EvidenceExtractor:

    @staticmethod
    def extract(
        chunks,
        question: str,
        max_sentences: int = 15
    ):

        keywords = set(
            re.findall(
                r"\w+",
                question.lower()
            )
        )

        evidence = []

        for chunk in chunks:

            text = chunk["content"]

            sentences = re.split(
                r"[.!?\n]+",
                text
            )

            for sentence in sentences:

                sentence = sentence.strip()

                if len(sentence) < 20:
                    continue

                sentence_words = set(
                    re.findall(
                        r"\w+",
                        sentence.lower()
                    )
                )

                overlap = len(
                    keywords.intersection(
                        sentence_words
                    )
                )

                score = overlap

                if overlap > 0:

                    evidence.append(
                        (
                            score,
                            sentence,
                            chunk["source"]
                        )
                    )

        evidence.sort(
            key=lambda x: x[0],
            reverse=True
        )

        best_sentences = []

        used = set()

        for score, sentence, source in evidence:

            if sentence in used:
                continue

            used.add(sentence)

            best_sentences.append(
                f"[{source}] {sentence}"
            )

            if (
                len(best_sentences)
                >= max_sentences
            ):
                break

        if not best_sentences:

            return "\n\n".join(
                [
                    chunk["content"][:1000]
                    for chunk in chunks
                ]
            )

        return "\n".join(
            best_sentences
        )