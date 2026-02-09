# Contributing to Finance Agent System

Thank you for your interest in contributing to the Finance Agent System! We welcome contributions from the community and are pleased to have you join us.

## 🤝 How to Contribute

### Reporting Issues

1. **Check existing issues** first to avoid duplicates
2. **Use the issue template** when creating new issues
3. **Provide detailed information** including:
   - Steps to reproduce the issue
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Error messages and stack traces

### Suggesting Features

1. **Open a feature request** issue first to discuss the idea
2. **Explain the use case** and why it would be valuable
3. **Consider the scope** - start with smaller, focused features

### Code Contributions

#### Setting Up Development Environment

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/Finance-Agent-System.git
   cd Finance-Agent-System
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -e .  # Install in development mode
   ```

5. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

#### Making Changes

1. **Create a new branch** for your feature/fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our coding standards
3. **Write tests** for new functionality
4. **Run tests** to ensure everything works:
   ```bash
   python -m pytest tests/
   ```

5. **Update documentation** if needed

#### Code Style Guidelines

- **Follow PEP 8** Python style guidelines
- **Use type hints** where appropriate
- **Write docstrings** for all functions and classes
- **Keep functions small** and focused
- **Use meaningful variable names**
- **Add comments** for complex logic

#### Example Code Style

```python
from typing import List, Optional
import pandas as pd

def fetch_stock_data(
    symbol: str, 
    start_date: str, 
    end_date: str,
    source: str = "yfinance"
) -> Optional[pd.DataFrame]:
    """
    Fetch stock data for a given symbol and date range.
    
    Args:
        symbol: Stock symbol (e.g., 'AAPL')
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        source: Data source to use
        
    Returns:
        DataFrame with stock data or None if failed
        
    Raises:
        ValueError: If date format is invalid
    """
    # Implementation here
    pass
```

#### Testing Guidelines

- **Write unit tests** for all new functions
- **Use pytest** as the testing framework
- **Mock external API calls** in tests
- **Test edge cases** and error conditions
- **Aim for >80% code coverage**

Example test:
```python
import pytest
from unittest.mock import patch
from src.agents.DatacollectionAgent import DataCollectionAgent

def test_fetch_data_success():
    """Test successful data fetching."""
    agent = DataCollectionAgent("test_key")
    
    with patch('yfinance.Ticker') as mock_ticker:
        # Mock the API response
        mock_ticker.return_value.history.return_value = mock_data
        
        result = agent.fetch_data("AAPL", "yfinance", "2023-01-01", "2023-12-31")
        
        assert result is not None
        assert len(result) > 0
```

#### Submitting Pull Requests

1. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** on GitHub with:
   - Clear title and description
   - Reference to related issues
   - List of changes made
   - Screenshots if UI changes

3. **Respond to feedback** and make requested changes
4. **Ensure CI passes** before requesting review

## 📋 Development Guidelines

### Project Structure

- `src/` - Main source code
- `tests/` - Test files
- `docs/` - Documentation
- `examples/` - Usage examples
- `scripts/` - Utility scripts

### API Design Principles

- **Consistency** - Similar functions should work similarly
- **Simplicity** - Keep interfaces simple and intuitive
- **Flexibility** - Allow customization without complexity
- **Error Handling** - Provide clear error messages

### Documentation

- **Update README.md** for significant changes
- **Add docstrings** to all public functions
- **Include examples** in documentation
- **Keep docs up to date** with code changes

## 🔒 Security Guidelines

- **Never commit API keys** or sensitive data
- **Use environment variables** for configuration
- **Validate all inputs** to prevent injection attacks
- **Follow security best practices** for financial data

## 🐛 Bug Reports

When reporting bugs, please include:

- **Python version** and operating system
- **Package versions** (`pip freeze`)
- **Minimal code example** that reproduces the issue
- **Full error traceback**
- **Expected vs actual behavior**

## 💡 Feature Requests

For feature requests, please:

- **Explain the use case** clearly
- **Provide examples** of how it would be used
- **Consider implementation complexity**
- **Discuss alternatives** you've considered

## 📞 Getting Help

- **GitHub Issues** - For bugs and feature requests
- **GitHub Discussions** - For questions and general discussion
- **Email** - vedant.barbhaya@example.com for private matters

## 🏆 Recognition

Contributors will be:
- **Listed in CONTRIBUTORS.md**
- **Mentioned in release notes**
- **Given credit in documentation**

## 📜 Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.

### Our Standards

- **Be respectful** and inclusive
- **Welcome newcomers** and help them learn
- **Focus on constructive feedback**
- **Respect different viewpoints**
- **Show empathy** towards other community members

Thank you for contributing to Finance Agent System! 🚀 