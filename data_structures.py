__all__ = (
    'Label',
)


class Label(object):
    def __init__(self, label, probability, correct):
        self.label = label
        self.probability = probability
        self.correct = correct

    def __str__(self):
        return self.as_text
    __repr__ = __str__

    @property
    def as_text(self):
        return "{}: {:10.8f}% ({})".format(
            self.label,
            self.probability * 100.0,
            "correct" if self.correct else "incorrect"
        )

    @property
    def as_text_with_percentage_only(self):
        return "{}: {:9.6f}%".format(
            self.label,
            self.probability * 100.0,
        )

    @property
    def as_text_with_numbers_only(self):
        return "{}: {}%".format(
            self.label,
            self.probability,
        )
