import docuvault.core.cloudinary
import cloudinary.uploader
import uuid

def upload_file(file_byte:bytes , fileName : str):
    public_id = f"documents/{uuid.uuid4()}"
    result = cloudinary.uploader.upload(
        file_byte,
        public_id = public_id,
        resource_type = "raw",
        filename = fileName,
        use_filename=True,
    )
    return {
        "public_id" : result["public_id"],
        "secure_url" : result["secure_url"],
        "file_size" : result["bytes"]
    }
