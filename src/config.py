"""
Configuration management for Finance Agent System.

This module handles all environment variables and configuration settings
for the multiagent finance system.
"""

import os
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class to manage environment variables and settings."""
    
    def __init__(self):
        """Initialize configuration with default values."""
        self.environment = self.get_env_variable('ENVIRONMENT', 'development')
        self.debug = self.get_env_variable('DEBUG', 'false').lower() == 'true'
        self.log_level = self.get_env_variable('LOG_LEVEL', 'INFO')
        
    @staticmethod
    def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
        """
        Get an environment variable.
        
        Args:
            key (str): The name of the environment variable
            default: The default value if the environment variable is not found
            
        Returns:
            The value of the environment variable or the default value
        """
        return os.getenv(key, default)
    
    @staticmethod
    def get_bool_env_variable(key: str, default: bool = False) -> bool:
        """
        Get a boolean environment variable.
        
        Args:
            key (str): The name of the environment variable
            default (bool): The default value if the environment variable is not found
            
        Returns:
            Boolean value of the environment variable
        """
        value = os.getenv(key, str(default)).lower()
        return value in ('true', '1', 'yes', 'on')
    
    @staticmethod
    def get_int_env_variable(key: str, default: int = 0) -> int:
        """
        Get an integer environment variable.
        
        Args:
            key (str): The name of the environment variable
            default (int): The default value if the environment variable is not found
            
        Returns:
            Integer value of the environment variable
        """
        try:
            return int(os.getenv(key, str(default)))
        except ValueError:
            return default
    
    # Financial Data API Keys
    @staticmethod
    def get_finnhub_api_key() -> Optional[str]:
        """Get Finnhub API key."""
        return Config.get_env_variable('FINNHUB_API_KEY')
    
    @staticmethod
    def get_openbb_token() -> Optional[str]:
        """Get OpenBB platform token."""
        return Config.get_env_variable('OPENBB_PAT')
    
    @staticmethod
    def get_sec_api_key() -> Optional[str]:
        """Get SEC API key."""
        return Config.get_env_variable('SEC_API_KEY')
    
    @staticmethod
    def get_fmp_api_key() -> Optional[str]:
        """Get Financial Modeling Prep API key."""
        return Config.get_env_variable('FMP_API_KEY')
    
    # Social Media API Keys
    @staticmethod
    def get_reddit_client_id() -> Optional[str]:
        """Get Reddit client ID."""
        return Config.get_env_variable('REDDIT_CLIENT_ID')
    
    @staticmethod
    def get_reddit_client_secret() -> Optional[str]:
        """Get Reddit client secret."""
        return Config.get_env_variable('REDDIT_CLIENT_SECRET')
    
    @staticmethod
    def get_reddit_user_agent() -> str:
        """Get Reddit user agent."""
        return Config.get_env_variable('REDDIT_USER_AGENT', 'Finance-Agent-System/1.0')
    
    @staticmethod
    def get_twitter_bearer_token() -> Optional[str]:
        """Get Twitter bearer token."""
        return Config.get_env_variable('TWITTER_BEARER_TOKEN')
    
    # AI/ML API Keys
    @staticmethod
    def get_openai_api_key() -> Optional[str]:
        """Get OpenAI API key."""
        return Config.get_env_variable('OPENAI_API_KEY')
    
    @staticmethod
    def get_langsmith_api_key() -> Optional[str]:
        """Get LangSmith API key."""
        return Config.get_env_variable('LANGSMITH_API_KEY')
    
    @staticmethod
    def get_huggingface_api_key() -> Optional[str]:
        """Get Hugging Face API key."""
        return Config.get_env_variable('HUGGINGFACE_API_KEY')
    
    # Database Configuration
    @staticmethod
    def get_database_url() -> Optional[str]:
        """Get database URL."""
        return Config.get_env_variable('DATABASE_URL')
    
    @staticmethod
    def get_mongodb_uri() -> Optional[str]:
        """Get MongoDB URI."""
        return Config.get_env_variable('MONGODB_URI')
    
    @staticmethod
    def get_qdrant_cluster_key() -> Optional[str]:
        """Get Qdrant cluster key."""
        return Config.get_env_variable('QDRANT_CLUSTER_KEY')
    
    @staticmethod
    def get_qdrant_url() -> Optional[str]:
        """Get Qdrant URL."""
        return Config.get_env_variable('QDRANT_URL')
    
    # Application Settings
    @staticmethod
    def get_data_dir() -> str:
        """Get data directory path."""
        return Config.get_env_variable('DATA_DIR', './output')
    
    @staticmethod
    def is_cache_enabled() -> bool:
        """Check if caching is enabled."""
        return Config.get_bool_env_variable('CACHE_ENABLED', True)
    
    @staticmethod
    def get_cache_ttl() -> int:
        """Get cache TTL in seconds."""
        return Config.get_int_env_variable('CACHE_TTL', 3600)
    
    @staticmethod
    def is_rate_limit_enabled() -> bool:
        """Check if rate limiting is enabled."""
        return Config.get_bool_env_variable('RATE_LIMIT_ENABLED', True)
    
    @staticmethod
    def get_max_requests_per_minute() -> int:
        """Get maximum requests per minute."""
        return Config.get_int_env_variable('MAX_REQUESTS_PER_MINUTE', 60)
    
    # Notification Settings
    @staticmethod
    def get_smtp_server() -> Optional[str]:
        """Get SMTP server."""
        return Config.get_env_variable('SMTP_SERVER')
    
    @staticmethod
    def get_smtp_port() -> int:
        """Get SMTP port."""
        return Config.get_int_env_variable('SMTP_PORT', 587)
    
    @staticmethod
    def get_email_username() -> Optional[str]:
        """Get email username."""
        return Config.get_env_variable('EMAIL_USERNAME')
    
    @staticmethod
    def get_email_password() -> Optional[str]:
        """Get email password."""
        return Config.get_env_variable('EMAIL_PASSWORD')
    
    @staticmethod
    def get_slack_webhook_url() -> Optional[str]:
        """Get Slack webhook URL."""
        return Config.get_env_variable('SLACK_WEBHOOK_URL')
    
    # Security Settings
    @staticmethod
    def get_secret_key() -> Optional[str]:
        """Get secret key."""
        return Config.get_env_variable('SECRET_KEY')
    
    @staticmethod
    def get_jwt_secret_key() -> Optional[str]:
        """Get JWT secret key."""
        return Config.get_env_variable('JWT_SECRET_KEY')
    
    @staticmethod
    def get_jwt_expiration_hours() -> int:
        """Get JWT expiration hours."""
        return Config.get_int_env_variable('JWT_EXPIRATION_HOURS', 24)
    
    # Proxy Settings
    @staticmethod
    def get_http_proxy() -> Optional[str]:
        """Get HTTP proxy."""
        return Config.get_env_variable('HTTP_PROXY')
    
    @staticmethod
    def get_https_proxy() -> Optional[str]:
        """Get HTTPS proxy."""
        return Config.get_env_variable('HTTPS_PROXY')
    
    @staticmethod
    def is_ssl_verify_disabled() -> bool:
        """Check if SSL verification is disabled."""
        return Config.get_bool_env_variable('DISABLE_SSL_VERIFY', False)
    
    def get_all_config(self) -> Dict[str, Any]:
        """
        Get all configuration as a dictionary (excluding sensitive data).
        
        Returns:
            Dictionary with all non-sensitive configuration values
        """
        return {
            'environment': self.environment,
            'debug': self.debug,
            'log_level': self.log_level,
            'data_dir': self.get_data_dir(),
            'cache_enabled': self.is_cache_enabled(),
            'cache_ttl': self.get_cache_ttl(),
            'rate_limit_enabled': self.is_rate_limit_enabled(),
            'max_requests_per_minute': self.get_max_requests_per_minute(),
            'ssl_verify_disabled': self.is_ssl_verify_disabled(),
        }
    
    def validate_required_keys(self, required_keys: list) -> Dict[str, bool]:
        """
        Validate that required API keys are present.
        
        Args:
            required_keys: List of required environment variable names
            
        Returns:
            Dictionary mapping key names to whether they are present
        """
        validation_results = {}
        for key in required_keys:
            validation_results[key] = bool(self.get_env_variable(key))
        return validation_results 