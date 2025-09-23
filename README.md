# 🎓 Rate My Professor Statistics - Comprehensive Analysis Platform

<div align="center">

![Project Banner](https://img.shields.io/badge/Rate%20My%20Professor-Statistics%20Platform-blue?style=for-the-badge)
![Next.js](https://img.shields.io/badge/Next.js-15.1.7-black?style=flat-square&logo=next.js)
![React](https://img.shields.io/badge/React-19.0.0-61DAFB?style=flat-square&logo=react)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python)
![Gradio](https://img.shields.io/badge/Gradio-ML%20Interface-orange?style=flat-square)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?style=flat-square&logo=mongodb)

*A comprehensive machine learning and data analysis platform for Rate My Professor data, featuring advanced analytics, sentiment analysis, and interactive visualizations.*

</div>

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [✨ Key Features](#-key-features)
- [🏗️ Technology Stack](#️-technology-stack)
- [🔬 Research Components](#-research-components)
- [📊 Data Analysis & Machine Learning](#-data-analysis--machine-learning)
- [🖥️ Frontend Dashboard](#️-frontend-dashboard)
- [🤖 Backend & ML Services](#-backend--ml-services)
- [🚀 Getting Started](#-getting-started)
- [📁 Project Structure](#-project-structure)
- [📝 API Documentation](#-api-documentation)
- [🔄 Deployment](#-deployment)

## 🎯 Project Overview

The **Rate My Professor Statistics Platform** is a comprehensive full-stack application that provides deep insights into professor performance data from Rate My Professor. This project combines advanced data science techniques, machine learning models, and modern web technologies to deliver actionable analytics for students, educators, and researchers.

### 🎪 What Makes This Project Special

- **🔍 Big Data Processing**: Analyzing 100+ universities with millions of reviews
- **🧠 Advanced ML Pipeline**: Custom sentiment analysis, temporal modeling, and statistical inference
- **📊 Interactive Visualizations**: Real-time charts, distributions, and comparative analytics
- **🎯 Class-Level Filtering**: Granular analysis by specific courses and class mappings
- **⚡ Real-Time Performance**: Optimized for fast query processing and responsive UI
- **🔄 Scalable Architecture**: Modular design supporting easy expansion and maintenance

## ✨ Key Features

### 🔬 **Advanced Analytics Engine**
- **Temporal Analysis**: Track professor performance trends over time with rolling averages
- **Sentiment Analysis**: AI-powered sentiment scoring with normalized polarity distributions
- **Statistical Modeling**: Comprehensive statistical breakdowns with confidence intervals
- **Class Mapping**: Intelligent course grouping and filtering system
- **Tag Analysis**: Automated extraction and analysis of review themes

### 📊 **Interactive Dashboard**
- **Professor Search**: Smart search across 100+ universities with autocomplete
- **Dynamic Visualizations**: Interactive charts built with Recharts
- **Real-Time Filtering**: Class-based filtering with instant results
- **Responsive Design**: Mobile-first approach with dark/light mode support
- **Debug Tools**: Development-mode analytics for data validation

### 🤖 **Machine Learning Pipeline**
- **Custom Sentiment Models**: Fine-tuned sentiment analysis for academic reviews
- **Automated Summarization**: AI-generated professor summaries using Google Gemini
- **Pattern Recognition**: Identification of teaching style patterns and student preferences
- **Predictive Analytics**: Grade distribution predictions and difficulty assessments

## 🏗️ Technology Stack

### **Frontend Technologies**
```typescript
// Core Framework
Next.js 15.1.7 + React 19.0.0 + TypeScript

// Styling & UI
TailwindCSS + Custom CSS Variables
Responsive Design + Dark/Light Mode

// Data Visualization
Recharts (Line, Bar, Pie, Composed Charts)
Custom Chart Components

// State Management
React Hooks + Context API
Real-time Data Fetching
```

### **Backend & API**
```python
# API Layer
Next.js API Routes + REST Endpoints
Gradio ML Interface Integration

# Database
MongoDB Atlas + Optimized Queries
Redis Caching (Upstash)

# ML Pipeline
Python 3.10+ + Pandas + NumPy
Gradio 3.0+ for ML Model Serving
```

### **Machine Learning Stack**
```python
# Core ML Libraries
pandas>=1.3.0          # Data manipulation
numpy>=1.20.0           # Numerical computing
matplotlib>=3.4.0       # Data visualization
textblob>=0.15.3       # NLP and sentiment analysis

# AI & ML Services
google-genai>=1.13.0    # Google Gemini for summarization
gradio>=3.0.0          # ML model interface
requests>=2.25.0       # API communications
```

## 🔬 Research Components

### 📚 **Jupyter Notebooks**

#### **T100Dataset Analysis**
- **`Sentiment.ipynb`**: Advanced sentiment analysis pipeline processing millions of reviews
- **`ClassDivision.ipynb`**: Intelligent course mapping and classification system  
- **`LargeDataset.ipynb`**: Big data processing and optimization techniques
- **`UniversityData.ipynb`**: University-level statistical analysis and insights

#### **Data Processing Pipeline**
- **Normalization Data**: Custom normalization algorithms for consistent scoring
- **Mapping Systems**: `initial_mapping.pkl` and `revised_mapping.pkl` for course classifications
- **Statistical Models**: Advanced statistical inference and trend analysis

## 📊 Data Analysis & Machine Learning

### **🧮 Statistical Analysis Module** (`Statistics.py`)
- Mean quality and difficulty calculations
- Percentage distributions (would take again, attendance mandatory)
- Tag scoring and frequency analysis
- Comment length analytics

### **📈 Temporal Analysis** (`Continous_Temporal.py`, `Discrete_Temporal.py`)
- Continuous metrics: Quality, difficulty, and sentiment over time
- Discrete metrics: Reviews by month/year, attendance patterns
- Rolling average calculations with configurable windows
- Seasonal trend detection

### **🎯 Categorical Analysis** (`Categorical.py`)
- Rating distributions (1-5 scale analysis)
- Grade distributions with class-level breakdowns
- Tag distribution analysis with frequency mapping
- Difficulty distribution modeling

### **💭 Sentiment Analysis Pipeline** (`Sentiment.py`)
```python
# Advanced sentiment processing
def analyze_sentiment(review_text):
    blob = TextBlob(review_text)
    sentiment = blob.sentiment.polarity
    normalized = (sentiment + 1) / 2  # Normalize to [0, 1]
    return {
        'sentiment': sentiment,
        'normalized_polarity': normalized,
        'subjectivity': blob.sentiment.subjectivity
    }
```

### **📝 AI Summarization** (`Summarize.py`)
- Google Gemini integration for intelligent summaries
- Custom prompt engineering for academic context
- Multi-aspect analysis (strengths, weaknesses, teaching style)
- Automated insight generation

## 🖥️ Frontend Dashboard

### **🎨 Modern UI/UX Design**
- **Responsive Grid Layout**: CSS Grid + Flexbox for optimal layout
- **Interactive Charts**: Recharts integration with custom styling
- **Dynamic Theming**: CSS variables for consistent dark/light modes
- **Smooth Animations**: Transition effects and loading states

### **📊 Visualization Components**

#### **Time Series Analysis**
```typescript
// Interactive line charts with multiple metrics
<LineChart data={timeSeriesData}>
  <Line dataKey="avg_quality" stroke="#8884d8" />
  <Line dataKey="rolling_avg_quality" strokeDasharray="5 5" />
  <Line dataKey="avg_difficulty" stroke="#82ca9d" />
</LineChart>
```

#### **Distribution Analysis**
```typescript
// Sentiment distribution with normal curve overlay
<ComposedChart data={sentimentHistogramData}>
  <Bar dataKey="count" fill="salmon" />
  <Line dataKey="normalDist" stroke="#000" strokeDasharray="5 5" />
</ComposedChart>
```

### **🔍 Advanced Search Features**
- **University Search**: Autocomplete with 100+ institutions
- **Professor Lookup**: Smart search with fuzzy matching
- **Class Filtering**: Dynamic class selection with real-time updates
- **Cache Management**: Optimized caching for fast response times

## 🤖 Backend & ML Services

### **🔌 API Architecture**

#### **Core Endpoints**
```typescript
// Professor analysis with class filtering
GET /api/analyze-professor?professorId={id}&selectedClass={class}

// University search with pagination
GET /api/search-universities?query={term}&limit={n}

// Professor search within institution
GET /api/search-professors?universityId={id}&query={term}
```

#### **ML Model Integration**
```python
# Gradio interface for ML pipeline
def analyze_reviews(professor_id: str, window: str, selected_class: str):
    # Class filtering logic
    filtered_reviews = filter_by_class(reviews, selected_class)
    
    # Comprehensive analysis pipeline
    return {
        'Statistics': get_statistics(filtered_reviews),
        'Sentiment': analyze_sentiment(filtered_reviews),
        'Temporal': temporal_analysis(filtered_reviews),
        'Summary': generate_summary(filtered_reviews)
    }
```

## 🚀 Getting Started

### **📋 Prerequisites**
```bash
# Required software
Node.js 18+ and npm
Python 3.10+
MongoDB Atlas account
Git
```

### **⚡ Quick Setup**

#### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/RateMyProfessorStats.git
cd RateMyProfessorStats
```

#### **2. Frontend Setup**
```bash
cd RMPStatsDashboard
npm install

# Create environment file
echo "DB_USERNAME=your_mongodb_username
DB_PASSWORD=your_mongodb_password
HF_TOKEN=your_huggingface_token" > .env.local

# Start development server
npm run dev
```

#### **3. ML Pipeline Setup**
```bash
cd src/ml/models
pip install -r requirements.txt

# Test the ML pipeline
python app.py
```

#### **4. Access the Application**
- **Frontend**: `http://localhost:3000`
- **ML Interface**: `http://localhost:7860` (Gradio)

## 📁 Project Structure

```
RateMyProfessorStats/
├── 📊 RMPStatsDashboard/           # Next.js Frontend Application
│   ├── 🎨 src/
│   │   ├── app/                    # Next.js App Router
│   │   │   ├── pages/              # Page components
│   │   │   ├── api/                # API routes
│   │   │   └── components/         # Reusable components
│   │   ├── ml/models/              # ML Pipeline
│   │   │   ├── app.py              # Main Gradio interface
│   │   │   ├── Sentiment.py        # Sentiment analysis
│   │   │   ├── Statistics.py       # Statistical calculations
│   │   │   ├── Class_Mapping.py    # Course classification
│   │   │   └── Summarize.py        # AI summarization
│   │   └── lib/                    # Utility functions
│   ├── 📦 public/                  # Static assets
│   ├── 🔧 package.json             # Dependencies
│   └── ⚙️ next.config.js           # Next.js configuration
├── 📔 Notebooks/                   # Research & Analysis
│   ├── T100Dataset/                # Top 100 universities analysis
│   │   ├── Sentiment.ipynb         # Sentiment analysis research
│   │   ├── ClassDivision.ipynb     # Course mapping algorithms
│   │   ├── LargeDataset.ipynb      # Big data processing
│   │   └── normalization_data/     # Data normalization
│   ├── Dashboard/                  # Dashboard prototypes
│   └── UMassDataset/              # University-specific analysis
├── 🗃️ RMPT100Reviews/             # Raw data (100+ universities)
│   └── universities/               # University-specific datasets
└── 📋 README.md                   # This comprehensive guide
```

## 📝 API Documentation

### **🔍 Search Endpoints**

#### **University Search**
```http
GET /api/search-universities
Query Parameters:
  - query: string (university name)
  - limit: number (default: 10)

Response:
{
  "universities": [
    {
      "_id": "university_id",
      "name": "University Name",
      "state": "State",
      "professor_count": 1234
    }
  ]
}
```

#### **Professor Analysis**
```http
GET /api/analyze-professor
Query Parameters:
  - professorId: string (required)
  - rollingWindow: string (default: "3 Year Rolling Window")
  - selectedClass: string (default: "All Classes")

Response:
{
  "Statistics": { /* statistical metrics */ },
  "Sentiment": { /* sentiment analysis */ },
  "Continous_Temporal": { /* time series data */ },
  "Categorical": { /* distribution data */ },
  "Summary": { /* AI-generated summary */ },
  "Class_Mapping": { /* available classes */ }
}
```

## 🔄 Deployment

### **🚀 Production Deployment**

#### **Frontend (Vercel)**
```bash
# Automatic deployment on push to main
git push origin main

# Manual deployment
npx vercel --prod
```

#### **ML Pipeline (Hugging Face Spaces)**
```yaml
# spaces-config.yml
title: RMP Statistics ML Pipeline
emoji: 📊
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 3.0.0
app_file: app.py
python_version: 3.10
```

## 🎯 Key Achievements

### **📈 Technical Accomplishments**
- **🔢 Big Data Processing**: Successfully processed millions of reviews from 100+ universities
- **⚡ Performance Optimization**: Achieved sub-second response times for complex analytics
- **🤖 AI Integration**: Implemented Google Gemini for intelligent summarization
- **📊 Advanced Visualizations**: Created interactive charts with Recharts
- **🔄 Real-time Analytics**: Built responsive filtering and analysis pipeline

### **🔬 Research Impact**
- **📚 Comprehensive Analysis**: Developed novel approaches to professor performance analysis
- **🎯 Class-Level Insights**: Created intelligent course mapping and filtering systems
- **📈 Temporal Modeling**: Implemented rolling window analysis for trend detection
- **💭 Sentiment Analysis**: Built custom sentiment scoring for academic reviews

### **🏗️ Architecture Excellence**
- **🔧 Modular Design**: Clean separation between frontend, backend, and ML components
- **📱 Responsive UI**: Mobile-first design with dark/light mode support
- **⚡ Scalable Backend**: Optimized API routes with caching strategies
- **🤖 ML Pipeline**: Gradio-based ML serving with Hugging Face integration

## 🤝 Contributing

### **🔧 Development Guidelines**
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### 🌟 Show Your Support

If this project has been helpful to you, please consider giving it a ⭐ star!

**Made with ❤️ and lots of ☕**

*A comprehensive platform showcasing advanced data science, machine learning, and full-stack development skills*

</div>