from pydantic import BaseModel, Field
from typing import Optional

class LLMConfig(BaseModel):
    api_key: str = Field(..., description="OpenAI API Key")
    base_url: Optional[str] = Field(None, description="Base URL for the LLM provider (e.g. for Ollama)")
    model: str = Field("gpt-3.5-turbo", description="Model name to use")
    skip_ssl_verify: bool = Field(False, description="Whether to skip SSL verification (useful for self-signed certs)")

class TranslationRequest(BaseModel):
    text: str
    source_lang: str = "auto"
    target_lang: str
    config: LLMConfig

class TranslationResponse(BaseModel):
    translated_text: str
