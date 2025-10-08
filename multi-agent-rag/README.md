# Multi-Agent RAG System (Demo Skeleton)\n\nGenerated: 2025-10-07 09:19:16\n

## Expanded features added
- FAISS-backed RAG ingestion and retrieval (backend/agents/faiss_store.py)
- PDF ingestion and chunking utilities (backend/utils/pdf_utils.py)
- Embedding wrapper using sentence-transformers (backend/utils/embeddings.py)
- LLM client placeholders with retry/backoff (backend/utils/llm_client.py)
- Dockerfile and docker-compose for local deployment
- GitHub Actions CI workflow and unit tests

## How to run locally
1. Create a virtualenv and install dependencies:

```
python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

2. Create faiss index directory and uploads dir:
```
mkdir faiss_index uploads
```

3. Run the Flask app (development):
```
$env:FLASK_APP="backend\app.py"
flask run

```

Or build with Docker:
```
docker build -t multi-agent-rag:dev .
docker run -p 7860:7860 --env-file .env.example multi-agent-rag:dev
```

## Pushing to GitHub
1. Create a new repo on GitHub.
2. Push the local folder:
```
git init
git add .
git commit -m "Initial multi-agent rag skeleton"
git branch -M main
git remote add origin <YOUR_GIT_REMOTE>
git push -u origin main
```
 

## How TO Activate The Virtual Environment
Step 1: Make sure Python is installed

Check version:

python --version


or sometimes:

python3 --version

🔹 Step 2: Create a new virtual environment

In your project folder, run:

On Windows
python -m venv venv

On Linux / macOS
python3 -m venv venv

🔹 Step 3: Activate the venv
Windows (PowerShell / CMD):
.\venv\Scripts\activate

Linux / macOS:
source venv/bin/activate


✅ You’ll see (venv) at the start of your terminal prompt → means it’s active.

🔹 Step 4: Install packages inside venv

Once activated, install packages using pip:

pip install flask requests numpy


They’ll install only inside this venv, not globally.

🔹 Step 5: Deactivate when done
deactivate

 
## Try these commands to run the project:- 
 1) python -m backend.app
 2) cd backend
 3) python app.py
