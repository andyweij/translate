from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import httpx

def create_translation_chain(api_key: str, base_url: str | None, model: str, skip_ssl_verify: bool = False):
    """Creates a translation chain with dynamic configuration."""
    
    # Configure HTTP Client
    http_client = None
    if skip_ssl_verify:
        http_client = httpx.Client(verify=False)

    # Initialize LLM with dynamic config
    llm = ChatOpenAI(
        api_key=api_key,
        base_url=base_url,
        model_kwargs={"model": model}, # Force 'model' field in payload
        streaming=True, # Handle text/event-stream responses
        temperature=0.3,
        http_client=http_client
    )

    # Define translation prompt
    system_prompt = """You are a highly skilled professional translator with expertise in many languages.
Your task is to translate the following text from {source_lang} to {target_lang}.

Guidelines:
1. Maintain the original tone, style, and meaning of the source text.
2. If the text contains technical terms, use the standard equivalents in the target language.
3. Ensure the translation reads naturally and fluently in the target language.
4. Do not add any explanations, notes, or conversational fillers. Output ONLY the translated text.
5. If the source text is a code snippet or technical command, keep it unchanged unless it contains comments that need translation.

Translate accurately and professionally."""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "{text}")
    ])

    # Create chain
    chain = prompt | llm | StrOutputParser()
    
    return chain
