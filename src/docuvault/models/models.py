from datetime import datetime
from sqlmodel import Field , SQLModel , Relationship
import uuid
from docuvault.models.enums import Document_Status
class User(SQLModel , table = True):
    __tablename__ = "users"
    id : uuid.UUID = Field(primary_key=True , default_factory=uuid.uuid4)
    name : str = Field(nullable=False , index= True)
    email : str = Field(nullable=False , unique=True , index=True)
    hash_pass : str = Field(nullable=False)
    created_at : datetime = Field(default=datetime.utcnow)
    updated_at : datetime = Field(default=datetime.utcnow)
    knowledgeBase : list['KnowledgeBase'] = Relationship(back_populates="user_table" , cascade_delete=True) 

class KnowledgeBase(SQLModel , table = True):
    __tablename__ = "knowledgebase"
    id : uuid.UUID = Field(primary_key=True , default_factory=uuid.uuid4)
    user_id : uuid.UUID = Field(foreign_key="users.id",nullable=False,ondelete="CASCADE")
    created_at : datetime = Field(default=datetime.utcnow)
    updated_at : datetime = Field(default=datetime.utcnow)
    name : str = Field(nullable=False)
    description : str | None = None
    user_table:'User' = Relationship(back_populates="knowledgeBase")
    documents : list['Documents'] = Relationship(back_populates="knowledgebase_table",cascade_delete=True)

class Documents(SQLModel , table = True):
    __tablename__ = "documents"
    id : uuid.UUID = Field(primary_key=True , default_factory=uuid.uuid4)
    knowledgebase_id : uuid.UUID = Field(foreign_key="knowledgebase.id",nullable=False,ondelete="CASCADE")
    created_at : datetime = Field(default=datetime.utcnow)
    updated_at : datetime = Field(default=datetime.utcnow )
    name : str = Field(nullable=False)
    description : str | None = None
    knowledgebase_table:'KnowledgeBase' = Relationship(back_populates="documents")
    filesize :int
    url: str = Field(nullable=False)
    filetype:str = Field(nullable=False)
    status: Document_Status = Field(default=Document_Status.SUCCESS)
    public_id : str = Field(index=True)
    

    
