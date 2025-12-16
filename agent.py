import os
from .memory.trauma import TraumaMemory

class ScarAgent:
    def __init__(self):
        self.memory = TraumaMemory()
        
        # Load Prompt
        prompt_path = os.path.join(os.path.dirname(__file__), 'prompts', 'scar_kernel.md')
        with open(prompt_path, 'r') as f:
            self.base_prompt = f.read()

    def write_code(self, task: str):
        # 1. Retrieve Scars
        scars_text = self.memory.get_scars_formatted()
        
        # 2. Construct Prompt (Inject Scars)
        prompt = self.base_prompt.replace("[SCARS_INSERTED_HERE]", scars_text)
        prompt = prompt.replace("[USER_TASK]", task)
        
        # 3. Simulate LLM Call (In prod, call OpenAI here)
        # return call_llm(prompt)
        return prompt  # Returning prompt for demo visualization

    def report_failure(self, task: str, bad_code: str, error: str):
        """
        Feedback Loop: User reports a crash, Agent creates a Scar.
        """
        self.memory.add_scar(task, bad_code, error)
      
