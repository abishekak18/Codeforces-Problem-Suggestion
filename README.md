# CF Dashboard

[![Made with Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
[![Codeforces API](https://img.shields.io/badge/API-Codeforces-red?style=flat-square)](https://codeforces.com/api/help)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

> **Personalized competitive programming problem recommendations powered by intelligent skill analysis**

An AI-driven dashboard that analyzes your Codeforces profile and recommends problems tailored to your current skill level, learning patterns, and topic expertise. Built with a futuristic neon aesthetic and cutting-edge web technologies.

![CF Dashboard Preview](assets/preview.png)

## ✨ Features

- 🎯 **Smart Problem Recommendations** - Analyzes your rating and submission history to recommend problems within your skill range (±200 rating)
- 📊 **Skill Analysis** - Visualizes your strengths across 10 different algorithmic topics with interactive radar charts
- 🏆 **Rating-Based Filtering** - Personalized difficulty band based on your current Codeforces rating
- 🔍 **Advanced Search & Filter** - Search by problem name, filter by topic, sort by difficulty or skill gain
- 💾 **Smart Caching** - Optimized with pickle-based caching to minimize API calls
- 🌐 **Real-time Data Sync** - Fetches live data from Codeforces API
- 🎨 **Neon UI Design** - Stunning cyberpunk aesthetic with smooth animations
- 📱 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile
- ⚙️ **Customizable Settings** - Adjust recommendation parameters and display preferences

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/abishekak18/Codeforces-Problem-Suggestion.git
   cd Codeforces-Problem-Suggestion
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask server**
   ```bash
   python app.py
   ```

6. **Open in browser**
   Navigate to `http://localhost:5000` in your web browser

## 📖 Usage Guide

### Basic Usage

1. **Enter Codeforces Handle**
   - Type your Codeforces handle in the top input field
   - Click "ANALYZE" or press Enter

2. **View Dashboard**
   - See your profile summary with rating and solved count
   - View personalized recommendations
   - Analyze your skill distribution via radar chart

3. **Explore Recommendations**
   - Browse problems sorted by difficulty or skill gain
   - Filter by topic tags
   - Click "SOLVE" to open problems on Codeforces

### Navigation

The dashboard has 4 main views accessible from the sidebar:

- **Dashboard** - Overview and priority recommendations
- **Recommendations** - All personalized problems with advanced filtering
- **User Profile** - Detailed statistics and skill breakdown
- **Settings** - Configure recommendations and UI preferences

### Settings

#### Recommendation Engine
- **Rating Delta** - Range of difficulty (default ±200)
- **Max Recs Per Tag** - Problems shown per topic (default 5)
- **Sort Default** - Default sorting method (Difficulty/Score)

#### Display Preferences
- **Show Problem Descriptions** - Toggle problem details
- **Scanline Effect** - Retro CRT overlay
- **Glow Animations** - Hover effects
- **Compact Mode** - Smaller cards

#### Cache & Data
- **Auto-Refresh** - Re-fetch data on analyze
- **Clear Cache** - Reset cached problems

## 📁 Project Structure

```
cf-dashboard/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── static/
│   └── index.html        # Enhanced neon UI
├── cf_problems_cache.pkl # Cached problem data (generated)
├── README.md             # This file
```

### Key Files

**app.py** - Flask application with API endpoints:
- `/api/recommend` - GET endpoint for problem recommendations
- `/api/cache/clear` - POST endpoint to clear cache

**index.html** - Frontend with:
- Neon cyberpunk UI theme
- Real-time problem card rendering
- Interactive charts and filters
- Responsive grid layouts

## 🔧 API Endpoints

### GET `/api/recommend`

Fetches personalized recommendations for a user.

**Parameters:**
- `handle` (string, required) - Codeforces user handle
- `refresh` (boolean, optional) - Force cache refresh


## 🎯 How It Works

### Recommendation Algorithm

1. **User Data Fetching**
   - Retrieves user rating from Codeforces API
   - Fetches all submissions to identify solved problems
   - Analyzes submission history to build skill map

2. **Skill Analysis**
   - Counts problems solved per tag
   - Weights each tag by user's success rate
   - Builds comprehensive skill profile

3. **Problem Scoring**
   - Calculates score for each unsolved problem
   - Score = sum of user's skill levels in problem's tags
   - Higher score = better match for user's expertise

4. **Filtering & Ranking**
   - Filters problems within rating range (±200)
   - Removes already-solved problems
   - Groups by topic tags
   - Limits to top 5 per tag to avoid overwhelming users

5. **Caching**
   - Caches full problem set in pickle file
   - Reduces API calls from 2 to 1 per user
   - Automatic refresh on user request

### Performance

- **API Calls**: 1-2 per analysis (cached)
- **Response Time**: ~200-500ms typical
- **Cache Size**: ~500KB for full problem set

## 🏗️ Tech Stack

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Advanced styling with CSS variables and animations
- **Vanilla JavaScript** - No frameworks, lightweight and fast
- **Canvas API** - For radar chart rendering

### Backend
- **Python 3.8+** - Core language
- **Flask** - Lightweight web framework
- **Requests** - HTTP client for API calls
- **Pickle** - Efficient data serialization

### APIs & Services
- **Codeforces API** - User data and problem information

## 🎨 UI/UX Features

### Design System
- **Color Palette** - Neon cyan, pink, purple, gold on dark background
- **Typography** - Orbitron (headers), Rajdhani (body), Share Tech Mono (code)
- **Animations** - Smooth transitions (0.24s cubic-bezier)
- **Responsiveness** - Mobile-first approach, breakpoints at 1024px, 768px, 480px

### Interactive Elements
- **Glassmorphism** - Semi-transparent panels with blur effects
- **Gradient Accents** - Linear gradients on borders and backgrounds
- **Glow Effects** - Neon glow on hover and active states
- **Staggered Animations** - Cards animate in sequence (0.04s per card)

## 📊 Supported Topics

The dashboard analyzes and recommends problems across these 10 topics:

- **math** - Number theory, combinatorics
- **dp** - Dynamic programming
- **greedy** - Greedy algorithms
- **graphs** - Graph algorithms (BFS, DFS, shortest path)
- **strings** - String manipulation and matching
- **binary search** - Binary search and variants
- **two pointers** - Two-pointer techniques
- **data structures** - Arrays, trees, heaps, etc.
- **bitmasks** - Bitwise operations
- **brute_force** - Brute force solutions

## 🚨 Error Handling

The application handles various error scenarios:

- **Invalid Handle** - Returns 404 with "User not found" message
- **API Errors** - Returns 400 with descriptive error message
- **Network Issues** - Displays error bar with retry option
- **Cache Issues** - Automatically recovers with fresh fetch

## 🔒 Privacy & Data

- **No Data Storage** - Application reads but doesn't store user data
- **Public API Only** - Only uses Codeforces public API
- **Session-Based** - Analysis happens in real-time, no persistence
- **No Tracking** - No analytics or tracking code

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run with debug mode
python app.py --debug

# Run tests
pytest
```
**Made with ❤️ for competitive programmers**
