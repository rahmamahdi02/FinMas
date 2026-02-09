# Financial Intelligence through Robust Multi-agents 🤖💰

A sophisticated multiagent finance system that leverages AI and machine learning to collect, analyze, and provide insights on financial data from multiple sources. This system integrates news, social media, SEC filings, and market data to create a comprehensive financial intelligence platform.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 🌟 Features

### 📊 Data Collection Agents
- **Financial News**: Real-time news from multiple sources (CNBC, Yahoo Finance, Reuters, etc.)
- **Social Media**: Sentiment analysis from Twitter, Reddit, StockTwits
- **SEC Filings**: Automated collection and processing of SEC documents
- **Market Data**: Real-time and historical stock data via multiple APIs
- **Earnings Calls**: Transcripts and analysis of earnings calls

### 🧠 AI-Powered Analysis
- **Sentiment Analysis**: Advanced NLP for market sentiment detection
- **Entity Recognition**: Automatic extraction of companies, people, and financial terms
- **Trend Analysis**: Pattern recognition in financial data
- **Risk Assessment**: AI-driven risk evaluation

### 🔄 Multiagent Architecture
- **Data Collection Agent**: Orchestrates data gathering from multiple sources
- **Analysis Agent**: Processes and analyzes collected data
- **Notification Agent**: Alerts and reporting system
- **Trading Insights Agent**: Generates actionable trading insights

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Git
- API keys for various financial data sources

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vedantbarbhaya/Finance-Agent-System.git
   cd Finance-Agent-System
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. **Run the system**
   ```bash
   python src/main.py
   ```

## 🔧 Configuration

### API Keys Required

Create a `.env` file in the root directory with the following keys:

```env
# Financial Data APIs
FINNHUB_API_KEY=your_finnhub_key
OPENBB_PAT=your_openbb_token
SEC_API_KEY=your_sec_api_key

# Social Media APIs
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret

# AI/ML APIs
OPENAI_API_KEY=your_openai_key
LANGSMITH_API_KEY=your_langsmith_key

# Database (Optional)
QDRANT_CLUSTER_KEY=your_qdrant_key
```

### Getting API Keys

1. **Finnhub**: [Sign up at Finnhub.io](https://finnhub.io/dashboard)
2. **OpenBB**: [Get token from OpenBB](https://my.openbb.co/)
3. **SEC API**: [Register at SEC-API.io](https://sec-api.io/)
4. **Reddit**: [Create app at Reddit](https://www.reddit.com/prefs/apps)
5. **OpenAI**: [Get API key from OpenAI](https://platform.openai.com/api-keys)

## 📁 Project Structure

```
Finance-Agent-System/
├── src/
│   ├── Agents/
│   │   └── DatacollectionAgent.py    # Main data collection agent
│   ├── data_sources/
│   │   ├── finnlp_utils.py           # FinNLP integration utilities
│   │   ├── finnhub_utils.py          # Finnhub API integration
│   │   ├── yfinance_utils.py         # Yahoo Finance integration
│   │   ├── reddit_utils.py           # Reddit data collection
│   │   ├── sec_utils.py              # SEC filings processing
│   │   └── fmp_utils.py              # Financial Modeling Prep API
│   ├── config.py                     # Configuration management
│   ├── utils.py                      # Utility functions
│   └── main.py                       # Main application entry point
├── tests/                            # Test files
├── output/                           # Generated reports and data
├── requirements.txt                  # Python dependencies
├── setup.py                          # Package setup
├── .env.example                      # Environment variables template
├── .gitignore                        # Git ignore rules
└── README.md                         # This file
```

## 🎯 Usage Examples

### Basic Data Collection

```python
from src.Agents.DatacollectionAgent import DataCollectionAgent

# Initialize the agent
agent = DataCollectionAgent(finhub_api_key="your_key")

# Fetch stock data
data = agent.fetch_data("AAPL", "yfinance", "2023-01-01", "2023-12-31")
print(data.head())

# Perform sentiment analysis
result = agent.execute_task(
    query="What is the sentiment of recent stock performance?",
    symbol="AAPL",
    source="yfinance"
)
```

### News Collection with FinNLP

```python
from src.data_sources.finnlp_utils import FinNLPUtils

# Initialize FinNLP utilities
finnlp = FinNLPUtils()

# Collect CNBC news
news_data = finnlp.cnbc_news_download(
    keyword="tesla",
    rounds=3,
    save_path="tesla_news.csv"
)

# Collect Finnhub news for specific stock
stock_news = finnlp.finnhub_news_download(
    start_date="2024-01-01",
    end_date="2024-01-31",
    stock="AAPL",
    save_path="aapl_news.csv"
)
```

### Social Media Sentiment Analysis

```python
from src.data_sources.reddit_utils import RedditCollector

# Collect Reddit posts
reddit = RedditCollector()
posts = reddit.collect_posts(
    subreddit="wallstreetbets",
    limit=100,
    keywords=["AAPL", "Tesla"]
)
```

## 🔍 Data Sources

### Financial News
- **CNBC**: Real-time financial news
- **Yahoo Finance**: Market news and analysis
- **Reuters**: Global financial news
- **Sina Finance**: Chinese financial news
- **Eastmoney**: Chinese market data

### Social Media
- **Reddit**: r/wallstreetbets, r/investing, r/stocks
- **Twitter/X**: Financial influencers and market sentiment
- **StockTwits**: Stock-specific social sentiment

### Official Data
- **SEC Filings**: 10-K, 10-Q, 8-K forms
- **Earnings Calls**: Transcripts and analysis
- **Company Announcements**: Official press releases

### Market Data
- **Real-time Prices**: Multiple exchange data
- **Historical Data**: Years of historical market data
- **Options Data**: Options chains and Greeks
- **Crypto Data**: Cryptocurrency market data

## 🤖 Agent Architecture

### Data Collection Agent
- Orchestrates data collection from multiple sources
- Handles rate limiting and API management
- Normalizes data from different sources
- Implements retry logic and error handling

### Analysis Agent (Coming Soon)
- Performs sentiment analysis on collected data
- Generates trading signals
- Risk assessment and portfolio analysis
- Market trend identification

### Notification Agent (Coming Soon)
- Real-time alerts for significant market events
- Email and SMS notifications
- Custom alert conditions
- Portfolio monitoring

## 📊 Output Formats

The system supports multiple output formats:
- **CSV**: For data analysis and Excel integration
- **JSON**: For API consumption and web applications
- **Parquet**: For big data processing
- **Database**: Direct database storage (PostgreSQL, MongoDB)

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_data_collection.py

# Run with coverage
python -m pytest tests/ --cov=src/
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This software is for educational and research purposes only. It is not intended as financial advice. Always consult with qualified financial professionals before making investment decisions. The authors are not responsible for any financial losses incurred through the use of this software.

## 🙏 Acknowledgments

- [FinNLP](https://github.com/AI4Finance-Foundation/FinNLP) - Financial NLP library
- [AI4Finance Foundation](https://github.com/AI4Finance-Foundation) - Open source financial AI tools
- [yfinance](https://github.com/ranaroussi/yfinance) - Yahoo Finance API
- [PRAW](https://github.com/praw-dev/praw) - Python Reddit API Wrapper
