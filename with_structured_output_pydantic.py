from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import Optional, Literal

load_dotenv()

# Gemini Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# Pydantic Schema
class Review(BaseModel):
    key_themes: list[str] = Field(
        description="Write down all the key themes discussed in the review in a list."
    )

    summary: str = Field(
        description="A brief summary of the review."
    )

    sentiment: Literal["pos", "neg", "neutral"] = Field(
        description="Return the sentiment as pos, neg or neutral."
    )

    pros: Optional[list[str]] = Field(
        default=None,
        description="Write down all the pros in a list."
    )

    cons: Optional[list[str]] = Field(
        default=None,
        description="Write down all the cons in a list."
    )

    name: Optional[str] = Field(
        default=None,
        description="Write the name of the reviewer."
    )


# Structured Model
structured_model = model.with_structured_output(Review)

# Review
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
# Print complete object
print(result)

print("\nReviewer Name:", result.name)
print("Sentiment:", result.sentiment)
print("Summary:", result.summary)
