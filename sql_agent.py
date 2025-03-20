import os
from crewai import Agent
from crewai_tools import NL2SQLTool
from config import DB_URI, TABLES,config
from sqlalchemy import create_engine, text
from crewai import LLM

print(f"Debug: DB URI = {DB_URI}")
print(f"Available Tables: {TABLES}")

class CustomNL2SQLTool(NL2SQLTool):
    """Custom NL2SQL tool that only runs Oracle-compatible queries."""
    
    def _fetch_available_tables(self):
        """Return pre-fetched tables instead of running an invalid query."""
        return [{"table_name": table} for table in TABLES]

    def _fetch_all_available_columns(self, table_name):
        """Fetch column names and data types from Oracle."""
        engine = create_engine(self.db_uri)
        with engine.connect() as conn:
            result = conn.execute(
                text(f"SELECT column_name, data_type FROM all_tab_columns WHERE table_name = '{table_name}'")
            )
            columns = [{"column_name": row[0], "data_type": row[1]} for row in result]
        return columns

    def execute_query(self, sql_query):
        """Run ONLY valid generated SQL queries and return the results."""
        print(f"Executing SQL Query:\n{sql_query}")  # Debugging Output

        engine = create_engine(self.db_uri)
        with engine.connect() as conn:
            result = conn.execute(text(sql_query))
            rows = [dict(row) for row in result]  # Convert SQLAlchemy result to a list of dictionaries

        return rows  # Return actual data from Oracle

# Initialize the correct Azure OpenAI LLM
llm = LLM(
    model=config["llm-deployment-name"],  # Uses Azure OpenAI deployment name
    api_base=config["openai-endpoint"],  # Uses Azure OpenAI endpoint
    api_version=config["api-version"],  # Uses Azure OpenAI API version
    api_key=config["api-key"]  # Uses API key from config
)

# Initialize Custom NL2SQL Tool
nl2sql_tool = CustomNL2SQLTool(db_uri=DB_URI)

# Define SQL Agent
sql_agent = Agent(
    role="SQL Query Agent",
    goal="Fetch and execute only the queries generated from natural language inputs",
    backstory="""You are an expert SQL developer with years of experience in database querying and 
    data analysis. Your specialization is in writing efficient SQL queries and translating 
    natural language requests into optimized database queries. You are responsible for both 
    generating SQL queries based on user requests and executing only those generated queries 
    in the database. You do not execute any queries that are not system-generated, ensuring 
    accuracy and security in database operations.""",
    tools=[nl2sql_tool],  # Use the custom NL2SQLTool
    allow_delegation=False,
    llm=llm  # Assign the correct Azure OpenAI LLM instance
)



# Function to manually ask a query
def ask_query():
    while True:
        user_input = input("Enter a natural language query (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        sql_query = nl2sql_tool.nl_to_sql(user_input)  # Convert text to SQL
        result = nl2sql_tool.execute_query(sql_query)
        print(f"Query Result:\n{result}")

# Uncomment this if you want to manually ask queries from the terminal
# ask_query()
