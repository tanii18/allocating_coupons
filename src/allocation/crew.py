from __future__ import annotations
from typing import List

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, task, crew, tool
from crewai.agents.agent_builder.base_agent import BaseAgent


from .tools.readcsv_tool import ReadCSVTool
from .tools.allocate_coupon_tool import AllocateCouponTool


@CrewBase
class Allocation:
    """Allocation crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # ----------------------------
    # Register tools for the agent
    # ----------------------------
    @tool
    def read_csv(self):
        return ReadCSVTool()
    

    @tool
    def allocate_coupon(self):
        return AllocateCouponTool()
        


    # ----------------------------
    # Define agent from YAML
    # ----------------------------
    @agent
    def coupon_allocator(self) -> Agent:
        return Agent(
            config=self.agents_config["coupon_allocator"],  # type: ignore[index]
            verbose=True,
        )

    # ----------------------------
    # Define task from YAML
    # ----------------------------
    @task
    def allocate_coupon_task(self) -> Task:
        return Task(
            config=self.tasks_config["allocate_coupon_task"],  # type: ignore[index]
        )

    # ----------------------------
    # Build the full crew
    # ----------------------------
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,     # auto-created from @agent
            tasks=self.tasks,       # auto-created from @task
            process=Process.sequential,
            verbose=True,
        )
