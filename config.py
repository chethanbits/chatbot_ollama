import os
from sqlalchemy import create_engine, text

DB_URI = "oracle+cx_oracle://sys:chethan123@localhost:1521/XE?mode=SYSDBA"
#https://<your-resource-name>.openai.azure.com/openai/deployments/<your-deployment-name>/completions?api-version=2023-03-15-preview

# Azure OpenAI Configuration
config = {
    'api-version': '2024-05-01-preview',
    'openai-endpoint': "https://fabee-v2-chat.openai.azure.com/",
    'llm-deployment-name': "azure/gpt-4o",
}

if not config['api-key']:
    raise ValueError("AZURE_OPENAI_API_KEY is missing! Set it in environment variables.")

def get_oracle_tables():
    """Fetch all tables for the connected Oracle schema."""
    engine = create_engine(DB_URI)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT table_name FROM all_tables WHERE owner = 'SYS'"))  # Change 'SYS' if needed
        tables = [row[0] for row in result]
    return tables

TABLES = get_oracle_tables()
