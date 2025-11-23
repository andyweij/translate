import os
import logging
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from agent.bot import create_translation_chain
from agent.models import TranslationRequest, TranslationResponse

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Translation Agent", version="1.0.0")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

@app.post("/translate", response_model=TranslationResponse)
async def translate(request: TranslationRequest):
    # Log the full request details
    # Masking API key for security in logs, but showing everything else
    log_payload = request.model_dump()
    if log_payload.get("config") and log_payload["config"].get("api_key"):
        log_payload["config"]["api_key"] = "***" + log_payload["config"]["api_key"][-4:]
    
    logger.info(f"Received Translation Request: {log_payload}")

    try:
        # Create chain with dynamic config
        chain = create_translation_chain(
            api_key=request.config.api_key,
            base_url=request.config.base_url,
            model=request.config.model,
            skip_ssl_verify=request.config.skip_ssl_verify
        )
        # Execute translation
        result = chain.invoke({
            "source_lang": request.source_lang,
            "target_lang": request.target_lang,
            "text": request.text
        })
        
        return TranslationResponse(translated_text=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
