from crewai.tools import BaseTool
from typing import Type, List, Dict
from pydantic import BaseModel, Field
import csv

class ReadCSVInput(BaseModel):
    path: str = Field(..., description="Full path of the CSV file to read")

class ReadCSVTool(BaseTool):
    name: str = "readcsv_tool"
    description: str = "Reads a CSV file and returns rows as list of dictionaries."

    
    args_schema: Type[ReadCSVInput] = ReadCSVInput

    def _run(self, path: str) -> List[Dict[str, str]]:
        try:
            with open(path, mode="r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                return [dict(row) for row in reader]
        except Exception as e:
            return [{"error": f"CSV read failed: {e}"}]
