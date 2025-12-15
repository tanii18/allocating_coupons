import subprocess
import sys

def install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

packages = ["crewai", "gradio", "pandas", "python-dotenv"]

for pkg in packages:
    try:
        __import__(pkg.replace("-", "_"))
    except ImportError:
        install(pkg)

import gradio as gr
from allocation.main import Allocation

def run_agent():
    """
    This function runs your CrewAI agent
    when the button is clicked on the website
    """
    try:
        result = Allocation().crew().kickoff()
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Agentic Coupon Allocation System")
    gr.Markdown(
        "Click the button below to run the AI agent. "
        "The agent allocates personalized coupons to the "
        "best consumers for each merchant."
    )

    run_btn = gr.Button("Run Coupon Allocation Agent")
    output_box = gr.Textbox(label="Agent Output", lines=25)

    run_btn.click(run_agent, outputs=output_box)

demo.launch()
