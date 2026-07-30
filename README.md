# LangChain Structured Output

Simple, hands-on demos showing how to get **structured (typed) output** from LLMs using LangChain — with `TypedDict`, `Pydantic`, and raw `JSON Schema` — across different model providers (Google Gemini, and a local Llama model via Ollama).

## 📌 What's in this repo

| File | Description |
|---|---|
| `typeddict_demo.py` | Basic Python `TypedDict` usage (no LLM involved) — foundation for understanding typed dicts before using them with LangChain. |
| `pydantic_demo.py` | Basic `Pydantic` `BaseModel` usage (no LLM involved) — shows validation, default values, and `Optional`/`Field` before using it with `with_structured_output`. |
| `with_structured_output_typeddict.py` | Uses `model.with_structured_output()` with a `TypedDict` schema to extract structured data (e.g. review summary, sentiment, pros/cons) from an LLM. |
| `with_structured_output_pydantic.py` | Same idea, but the schema is defined using a `Pydantic` `BaseModel` — gives you validation + defaults on top of structure. |
| `with_structured_output_json.py` | Uses a raw `JSON Schema` (see `json_schema.json`) instead of Python classes to define the output structure. |
| `with_structured_output_llama.py` | Same structured-output pattern, but run against a local **Llama** model (e.g. via Ollama) instead of Gemini. |
| `json_schema.json` | The JSON Schema used by `with_structured_output_json.py`. |

## 🧠 What this project demonstrates

LangChain's `with_structured_output()` lets you force an LLM to return data in a specific shape instead of free-form text — super useful for things like:

- Extracting sentiment, summary, pros & cons from a product review
- Turning unstructured text into clean, validated Python objects
- Building reliable pipelines where downstream code expects a fixed schema

This repo compares **three ways to define that schema**:

1. **TypedDict** – lightweight, no runtime validation
2. **Pydantic** – adds validation, defaults, and type coercion
3. **JSON Schema** – provider-agnostic, useful when you don't want to write Python classes

...and shows the same pattern working with **two different model backends** (Google Gemini via API, and a local Llama model via Ollama).

## 🛠️ Tech Stack

- [Python 3.10+](https://www.python.org/)
- [LangChain](https://python.langchain.com/)
- [langchain-google-genai](https://python.langchain.com/docs/integrations/chat/google_generative_ai/) (Gemini models)
- [Pydantic](https://docs.pydantic.dev/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- Ollama (for the local Llama demo)

## 📦 Installation

```bash
# 1. Clone the repo
git clone https://github.com/nitishchauhan002/langchain-structured-output.git
cd langchain-structured-output

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate

# 3. Install dependencies
pip install langchain langchain-google-genai pydantic python-dotenv
```

> If you plan to run `with_structured_output_llama.py`, install and run [Ollama](https://ollama.com/) locally and pull the model you intend to use, e.g.:
> ```bash
> ollama pull llama3.1
> ```

## 🔑 Environment Setup

Create a `.env` file in the project root for the Gemini-based scripts:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

You can get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/).

## ▶️ Usage

Run any demo script directly:

```bash
# Plain Python typing/validation demos (no API key needed)
python typeddict_demo.py
python pydantic_demo.py

# LangChain structured output demos (needs GOOGLE_API_KEY in .env)
python with_structured_output_typeddict.py
python with_structured_output_pydantic.py
python with_structured_output_json.py

# Local Llama demo (needs Ollama running)
python with_structured_output_llama.py
```

### Example (Pydantic schema)

```python
class Review(BaseModel):
    key_themes: list[str] = Field(description="Key themes discussed in the review.")
    summary: str = Field(description="A brief summary of the review.")
    sentiment: Literal["pos", "neg", "neutral"] = Field(description="Overall sentiment.")
    pros: Optional[list[str]] = Field(default=None, description="List of pros.")
    cons: Optional[list[str]] = Field(default=None, description="List of cons.")
    name: Optional[str] = Field(default=None, description="Reviewer's name.")

structured_model = model.with_structured_output(Review)
result = structured_model.invoke(review_text)

print(result.sentiment)   # "pos"
print(result.summary)     # short summary string
```

The LLM returns a validated `Review` object instead of raw text — ready to use in your application logic.

## 📂 Project Structure

```
langchain-structured-output/
├── json_schema.json
├── pydantic_demo.py
├── typeddict_demo.py
├── with_structured_output_json.py
├── with_structured_output_llama.py
├── with_structured_output_pydantic.py
├── with_structured_output_typeddict.py
├── LICENSE
└── README.md
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🙋 Author

**Nitish Chauhan**
GitHub: [@nitishchauhan002](https://github.com/nitishchauhan002)

---

⭐ If you found this helpful for learning LangChain's structured output, consider starring the repo!
