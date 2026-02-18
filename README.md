# Financial Research Tool

A full-stack financial research platform for automated income statement extraction, deterministic financial analytics, and executive-grade Excel reporting.

---

## Overview

This project implements a structured research tool designed to process financial statement PDFs and generate:

- Cleanly extracted income statement line items
- Multi-period financial metrics
- Margin and growth analytics
- CAGR calculations
- Executive summary insights
- Professionally formatted Excel output
- Interactive dashboard visualization

The system is deterministic and avoids hallucination by relying on structured parsing and rule-based financial logic.

---

## Key Features

### Document Processing
- Upload annual / quarterly financial statement PDFs
- Deterministic text-based parsing (no open-ended chatbot)
- Structured income statement extraction
- Multi-year period detection

### Financial Intelligence
- EBITDA Margin %
- PAT Margin %
- Revenue YoY Growth %
- PAT YoY Growth %
- Revenue CAGR
- PAT CAGR
- Validation warnings

### Professional Excel Output
Three-sheet structured Excel file:

1. **Income Statement**
   - Formatted headers
   - Freeze panes
   - Number formatting
   - Clean alignment

2. **Financial Metrics**
   - Percentage formatting
   - Conditional coloring (green/red)
   - Growth intelligence

3. **Executive Summary**
   - Latest period insights
   - Margin highlights
   - Growth commentary

### Dashboard Visualization
- Clean financial metric cards
- Growth indicators
- Structured results table
- Excel download support

---

## Tech Stack

### Backend
- Flask
- pdfplumber
- openpyxl
- pandas
- Deterministic regex-based parsing
- Gunicorn (production)

### Frontend
- React (Create React App)
- Axios
- Structured component architecture
- Dashboard UI

### Deployment
- Backend hosted on Render
- Frontend hosted on Vercel

---

## Architecture

User → React Frontend (Vercel)
↓
Flask API (Render)
↓
PDF Parsing → Financial Analytics → Excel Generation


The backend handles:
- File upload
- Extraction
- Metrics computation
- Excel generation

The frontend handles:
- User interaction
- Visualization
- Dashboard display
- File download

---

## How It Works

1. User uploads PDF
2. Backend extracts text deterministically
3. Key financial line items are mapped
4. Metrics are computed:
   - Margins
   - Growth
   - CAGR
5. Structured JSON returned
6. Excel generated
7. Dashboard renders analytics

No open-ended LLM output is used in financial calculations.

---

## Deployment Instructions

### Backend (Render)

1. Connect GitHub repository
2. Set root directory to `backend`
3. Build command:


pip install -r requirements.txt

4. Start command:


gunicorn run:app


### Frontend (Vercel)

1. Import GitHub repository
2. Set root directory to `frontend`
3. Build command:


npm run build

4. Output directory:


build


---

## Environment Notes

- Free-tier hosting may introduce cold-start delays (~30 seconds)
- File upload size limited by hosting plan
- Files are stored temporarily (no persistent storage)

---

## Design Philosophy

This tool was designed as a structured research engine rather than a chatbot.

Key principles:

- Deterministic extraction
- No hallucinated financial values
- Clean mapping logic
- Analyst-friendly output
- Professional formatting
- Clear separation of concerns

---

## Folder Structure



financial-research-tool/
│
├── backend/
│ ├── app/
│ │ ├── services/
│ │ ├── routes/
│ │ └── ...
│ ├── run.py
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ ├── api/
│ │ └── styles/
│ └── package.json
│
└── README.md


---

## Future Improvements

- Consolidated vs Standalone auto-detection
- Additional financial ratios (ROCE, Interest Coverage)
- Multi-document comparison
- Trend charts
- Persistent storage layer

---

## Author

Shafiq Ahmed
Full-Stack Financial Research System
