import json
import os

class TraumaMemory:
    """
    Implements Loop 10: Persistent Scars.
    """
    def __init__(self, scar_file="scars.json"):
        self.scar_file = scar_file
        self.scars = self._load_scars()

    def _load_scars(self):
        if not os.path.exists(self.scar_file):
            return []
        with open(self.scar_file, 'r') as f:
            return json.load(f)

    def add_scar(self, task: str, bad_code: str, error_msg: str):
        """
        Etches a new failure into memory.
        """
        new_scar = {
            "context": task,
            "failed_approach": bad_code[:50] + "...", # Truncate for brevity
            "error": error_msg,
            "lesson": f"Avoid doing X when trying to {task}" # In prod, LLM generates this lesson
        }
        self.scars.append(new_scar)
        self._save_scars()
        print(f"   ⚡ SCAR FORMED: {error_msg}")

    def _save_scars(self):
        with open(self.scar_file, 'w') as f:
            json.dump(self.scars, f, indent=2)

    def get_scars_formatted(self):
        if not self.scars:
            return "No scars detected. Proceed with caution."
        
        text = ""
        for i, s in enumerate(self.scars):
            text += f"{i+1}. WHEN '{s['context']}': {s['error']}\n"
        return text
      
