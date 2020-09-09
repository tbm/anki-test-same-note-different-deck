"""
Define Anki models for Swahili vocabulary
"""

import genanki

STYLE = """
.card {
  font-family: arial;
  font-size: 24px;
  text-align: center;
  color: black;
  background-color: white;
}

.cloze {
  font-weight: bold;
  color: blue;
}
"""

VOCAB_REVERSE = genanki.Model(
    4231129472,
    "TEST1 Swahili vocabulary note",
    fields=[
        {
            "name": "XSwahili",
        },
        {
            "name": "XEnglish",
        },
    ],
    templates=[
        {
            "name": "Vocabulary Card (front)",
            "qfmt": "{{XSwahili}}",
            "afmt": "{{FrontSide}}<hr id=\"answer\">{{XEnglish}}",
        },
        {
            "name": "Vocabulary Card (back)",
            "qfmt": "{{XEnglish}}",
            "afmt": "{{FrontSide}}<hr id=\"answer\">{{XSwahili}}",
        },
    ],
    css=STYLE,
)


VOCAB_REVERSE2 = genanki.Model(
    3135169473,
    "TEST2 Swahili vocabulary note",
    fields=[
        {
            "name": "Swahili",
        },
        {
            "name": "English",
        },
    ],
    templates=[
        {
            "name": "Vocabulary Card (front)",
            "qfmt": "{{XSwahili}}",
            "afmt": "{{FrontSide}}<hr id=\"answer\">{{XEnglish}}",
        },
        {
            "name": "Vocabulary Card (back)",
            "qfmt": "{{XEnglish}}",
            "afmt": "{{FrontSide}}<hr id=\"answer\">{{XSwahili}}",
        },
    ],
    css=STYLE,
)
