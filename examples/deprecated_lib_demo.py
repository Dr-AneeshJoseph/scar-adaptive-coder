from scar.agent import ScarAgent

agent = ScarAgent()
task = "Calculate the mean of a list using numpy."

print("--- ATTEMPT 1: Naive Execution ---")
# 1. Agent tries to write code (Hypothetically generates bad code)
code_v1 = "import numpy; print(numpy.mean_val([1,2,3]))" # 'mean_val' doesn't exist
print(f"Agent generated: {code_v1}")

# 2. Execution Fails
error = "AttributeError: module 'numpy' has no attribute 'mean_val'"
print(f"Execution Error: {error}")

# 3. Form the Scar
agent.report_failure(task, code_v1, error)

print("\n--- ATTEMPT 2: Adaptive Execution ---")
# 4. Agent tries again. This time, the Prompt INCLUDES the Scar.
final_prompt = agent.write_code(task)

print("GENERATED PROMPT FOR LLM:")
print(final_prompt)

# EXPECTED OUTPUT in Prompt:
# THE SCAR LIST:
# 1. WHEN 'Calculate mean...': AttributeError: ... no attribute 'mean_val'
#
# The LLM sees this and thinks: "Okay, don't use mean_val. Use mean."

