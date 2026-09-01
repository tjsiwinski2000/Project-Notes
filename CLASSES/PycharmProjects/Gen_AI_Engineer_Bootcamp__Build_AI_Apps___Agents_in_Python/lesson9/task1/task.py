from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from typing import List

load_dotenv()


class Recipe(BaseModel):
    name: str = Field(description="Name of the recipe")
    description: str = Field(description="Brief description of the recipe")
    prep_time: str = Field(description="Estimated preparation time of the recipe")


class Response(BaseModel):
    """A single recipe"""
    ingredients: List[str] = Field(description="List of main ingredients")
    recipes: List[Recipe] = Field(description="List of 3 recipe suggestions")


# TODO: Change model_provider to "google_genai"
model = init_chat_model("gemini-3-flash-preview", model_provider="openai")

# TODO: Change Recipe to Response
structured_model = model.with_structured_output(Recipe)

system_prompt = """
You are a helpful chef. Identify the main ingredients. Suggest 3 recipes based on those ingredients.
"""

message = [{"role": "system", "content": system_prompt},
           {"role": "user", "content": "I have chicken, garlic, and lemon."}]

response = structured_model.invoke(message)
print(response.model_dump())
