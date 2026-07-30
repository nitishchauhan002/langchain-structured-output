from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

# Gemini Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# Schema
class Review(TypedDict):
    key_themes: Annotated[
        list[str],
        "Write down all the key themes discussed in the review in a list."
    ]

    summary: Annotated[
        str,
        "A brief summary of the review."
    ]

    sentiment: Annotated[
        Literal["pos", "neg", "neutral"],
        "Return the sentiment of the review as pos, neg or neutral."
    ]

    pros: Annotated[
        Optional[list[str]],
        "Write down all the pros in a list."
    ]

    cons: Annotated[
        Optional[list[str]],
        "Write down all the cons in a list."
    ]

    name: Annotated[
        Optional[str],
        "Write the name of the reviewer."
    ]


# Structured Output Model
structured_model = model.with_structured_output(Review)

# Review Text
review = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse!

The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos.

The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often.

What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light.

Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use.

Also, Samsung’s One UI still comes with bloatware.

The $1300 price tag is also a hard pill to swallow.

Pros:
- Insanely powerful processor
- Stunning 200MP camera
- Long battery life
- S-Pen support

Review by Nitish Singh
"""

# Invoke
result = structured_model.invoke(review)

print("\nStructured Output:\n")
print(result)

print("\nReviewer Name:", result["name"])