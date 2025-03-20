from crewai import Task
from sql_agent import sql_agent

# Define the SQL retrieval task
sql_task = Task(
    description="Retrieve relevant information from the database",
    agent=sql_agent,
    expected_output="A JSON response containing structured data retrieved from the database.",
    action=lambda: sql_agent.tools[0].execute_query("SELECT * FROM employees")  # Example query
)

# Define the report generation task
report_task = Task(
    description="Generate a report based on the extracted SQL data",
    agent=sql_agent,
    expected_output="A summary of SQL query results.",
)
