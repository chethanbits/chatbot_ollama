from crewai import Crew
from tasks import sql_task, report_task
from sql_agent import sql_agent
from report_agent import report_agent

# Create Crew with agents and tasks
crew = Crew(agents=[sql_agent, report_agent], tasks=[sql_task, report_task])

def run_crew():
    result = crew.kickoff()
    print(result)

if __name__ == "__main__":
    run_crew()
