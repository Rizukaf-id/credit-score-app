#!/bin/bash

# run backend (FastAPI) di background
uvicorn src.main:app --host 0.0.0.0 --port 8000 &

# run frontend (Streamlit) di foreground
streamlit run src/dashboard.py --server.port 8501 --server.address 0.0.0.0