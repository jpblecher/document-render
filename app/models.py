from typing import List, Union, Optional, Any
from pydantic import BaseModel, Field


class RenderDocxRequest(BaseModel):
    html: str = Field(..., description="Full HTML document")
    title: str = Field(..., description="Document title (used for metadata/filename)")


class SheetDefinition(BaseModel):
    name: str = Field(..., description="Worksheet name")
    headers: List[str] = Field(..., description="Header row")
    rows: List[List[Union[str, float, int, None]]] = Field(
        ..., description="2D array of row values"
    )


class RenderXlsxRequest(BaseModel):
    title: str = Field(..., description="Workbook title / filename base")
    sheets: List[SheetDefinition] = Field(..., description="List of sheet definitions")


class RenderResponse(BaseModel):
    data: Optional[str] = Field(
        None, description="Base64-encoded file content (DOCX/XLSX)"
    )
    error: bool = Field(..., description="Indicates whether an error occurred")
    message: Optional[str] = Field(
        None, description="Human-readable message (for logs / debugging)"
    )
