#!/usr/bin/env python3
"""
Finance Agent System - Main Entry Point

A sophisticated multiagent finance system that leverages AI and machine learning 
to collect, analyze, and provide insights on financial data from multiple sources.
"""

import asyncio
import logging
import sys
from pathlib import Path
from typing import Optional

# Add src to path for imports
sys.path.append(str(Path(__file__).parent))

from config import Config
from Agents.DatacollectionAgent import DataCollectionAgent
from data_sources.finnlp_utils import FinNLPUtils

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('finance_agent.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


class FinanceAgentSystem:
    """Main Finance Agent System orchestrator."""
    
    def __init__(self):
        """Initialize the Finance Agent System."""
        self.config = Config()
        self.data_collection_agent: Optional[DataCollectionAgent] = None
        self.finnlp_utils: Optional[FinNLPUtils] = None
        
        # Validate required API keys
        self._validate_configuration()
        
    def _validate_configuration(self) -> None:
        """Validate that required API keys are present."""
        required_keys = ['FINNHUB_API_KEY']
        missing_keys = []
        
        for key in required_keys:
            if not self.config.get_env_variable(key):
                missing_keys.append(key)
        
        if missing_keys:
            logger.warning(f"Missing API keys: {missing_keys}")
            logger.warning("Some features may not work without proper API keys.")
            logger.info("Please check your .env file and add the missing keys.")
    
    def initialize_agents(self) -> None:
        """Initialize all agents."""
        try:
            # Initialize Data Collection Agent
            finnhub_key = self.config.get_env_variable('FINNHUB_API_KEY')
            if finnhub_key:
                self.data_collection_agent = DataCollectionAgent(finnhub_key)
                logger.info("Data Collection Agent initialized successfully")
            else:
                logger.warning("Data Collection Agent not initialized - missing FINNHUB_API_KEY")
            
            # Initialize FinNLP utilities
            self.finnlp_utils = FinNLPUtils()
            logger.info("FinNLP utilities initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing agents: {e}")
            raise
    
    async def run_data_collection_demo(self) -> None:
        """Run a demonstration of data collection capabilities."""
        logger.info("Starting data collection demonstration...")
        
        try:
            if self.data_collection_agent:
                # Fetch sample stock data
                logger.info("Fetching AAPL stock data...")
                stock_data = self.data_collection_agent.fetch_data(
                    symbol="AAPL",
                    source="yfinance",
                    start_date="2024-01-01",
                    end_date="2024-01-31"
                )
                
                if stock_data is not None and not stock_data.empty:
                    logger.info(f"Successfully fetched {len(stock_data)} records for AAPL")
                    logger.info(f"Data columns: {list(stock_data.columns)}")
                    logger.info(f"Date range: {stock_data.index.min()} to {stock_data.index.max()}")
                else:
                    logger.warning("No stock data retrieved")
            
            if self.finnlp_utils:
                # Collect news data
                logger.info("Collecting news data...")
                try:
                    news_data = self.finnlp_utils.cnbc_news_download(
                        keyword="AAPL",
                        rounds=1,
                        save_path="output/aapl_news_demo.csv"
                    )
                    
                    if not news_data.empty:
                        logger.info(f"Successfully collected {len(news_data)} news articles")
                    else:
                        logger.warning("No news data collected")
                        
                except Exception as e:
                    logger.error(f"Error collecting news data: {e}")
                    logger.info("This might be due to network issues or API limitations")
        
        except Exception as e:
            logger.error(f"Error in data collection demo: {e}")
    
    async def run_sentiment_analysis_demo(self) -> None:
        """Run a demonstration of sentiment analysis capabilities."""
        logger.info("Starting sentiment analysis demonstration...")
        
        try:
            if self.data_collection_agent:
                # Perform sentiment analysis
                result = self.data_collection_agent.execute_task(
                    query="What is the sentiment of recent stock performance?",
                    symbol="AAPL",
                    source="yfinance",
                    start_date="2024-01-01",
                    end_date="2024-01-31"
                )
                
                logger.info("Sentiment analysis completed")
                logger.info(f"Result type: {type(result)}")
                
                if hasattr(result, 'shape'):
                    logger.info(f"Result shape: {result.shape}")
        
        except Exception as e:
            logger.error(f"Error in sentiment analysis demo: {e}")
    
    async def run(self) -> None:
        """Run the main Finance Agent System."""
        logger.info("🤖💰 Starting Finance Agent System...")
        
        try:
            # Initialize agents
            self.initialize_agents()
            
            # Create output directory
            Path("output").mkdir(exist_ok=True)
            
            # Run demonstrations
            await self.run_data_collection_demo()
            await self.run_sentiment_analysis_demo()
            
            logger.info("✅ Finance Agent System completed successfully!")
            
        except KeyboardInterrupt:
            logger.info("System interrupted by user")
        except Exception as e:
            logger.error(f"System error: {e}")
            raise


async def main() -> None:
    """Main entry point for the Finance Agent System."""
    try:
        system = FinanceAgentSystem()
        await system.run()
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    print("🤖💰 Finance Agent System")
    print("=" * 50)
    print("A sophisticated multiagent finance system")
    print("for data collection and analysis")
    print("=" * 50)
    
    asyncio.run(main()) 