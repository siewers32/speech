import os
from openai import OpenAI


def vat_samen(tekst):
    client = OpenAI()
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Vat de volgende tekst samen in minder dan 20 woorden: {tekst}"}],
        stream=True,
    )
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")

for i in open("spoelen.txt", "rt"):
    vat_samen(i)