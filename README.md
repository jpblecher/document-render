# Document Render Service
Small FastAPI-based microservice to render DOCX and XLSX from structured JSON.
## Run locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
Healthcheck:
	• GET http://localhost:8000/health
DOCX:
	• POST http://localhost:8000/render-docx

{
  "html": "<html><body><h1>Test</h1><p>Hello.</p></body></html>",
  "title": "Test Document"
}
XLSX:
	• POST http://localhost:8000/render-xlsx

{
  "title": "Test Workbook",
  "sheets": [
    {
      "name": "Sheet1",
      "headers": ["A", "B"],
      "rows": [
        ["x", 1],
        ["y", 2]
      ]
    }
  ]
}
Build Docker image:

docker build -t document-render-service:latest .
docker run -p 8000:8000 document-render-service:latest
![Uploading image.png…]()
