from fastapi import FastAPI , UploadFile
from docuvault.service.file_extractor import pdf_extractor , text_extractor
from docuvault.service import storage_service
app = FastAPI()

ALLOWED_TYPES = ["application/pdf","text/plain","text/markdown"]
@app.post("/add/file")
async def add_file(file:UploadFile):
    content = await file.read()
    if file.content_type not in ALLOWED_TYPES:
        return {"error":"Unsupported File Type"}
    result = storage_service.upload_file(content , file.filename)
    if file.content_type == "application/pdf":
        text = pdf_extractor(content)
    else:
        text = text_extractor(content)
    
    # return {
    #     "filename":file.filename ,
    #     "content":text[:1000] if text else "Not Found",
    #     "url":result["secure_url"],
    #     "public_id":result["public_id"]
    # }

