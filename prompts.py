# Prompt templates for each variant

ZERO_SHOT = """
{base_prompt}
"""

FEW_SHOT = """
{base_prompt}

Here are a few examples:
{examples}

Now, apply the same logic to the input above.
"""

CHAIN_OF_THOUGHT = """
{base_prompt}

Think step by step:
1. Break down the problem
2. Reason through each part
3. Come to a conclusion

Provide your reasoning and final answer.
"""

ROLE_BASED = """
You are an expert {role}.

{base_prompt}

Respond in the style and depth appropriate for a {role}.
"""

STRUCTURED_OUTPUT = """
{base_prompt}

Please provide your response in the following structured format:
- Summary: [brief summary]
- Key Points: [3-5 bullet points]
- Action Items: [if applicable]
"""

REVERSE_PROMPTING = """
Instead of {base_prompt}, think about what the opposite would be.
Then use that contrast to answer the original question better.

Original: {base_prompt}

First, explain the opposite perspective, then provide your answer.
"""

SOCRATIC = """
{base_prompt}

Use the Socratic method to explore this question:
1. Start by asking clarifying questions
2. Break the problem into smaller parts
3. Guide toward deeper understanding
4. Provide a comprehensive answer
"""

def get_prompt_variants(base_prompt, use_case="general", examples=""):
    """Generate 7 prompt variants based on base prompt"""
    variants = {
        "Zero-Shot": ZERO_SHOT.format(base_prompt=base_prompt),
        "Few-Shot": FEW_SHOT.format(base_prompt=base_prompt, examples=examples or "[Example 1]\n[Example 2]\n[Example 3]"),
        "Chain-of-Thought": CHAIN_OF_THOUGHT.format(base_prompt=base_prompt),
        "Role-Based": ROLE_BASED.format(
            role="subject matter expert" if use_case == "general" else use_case,
            base_prompt=base_prompt
        ),
        "Structured Output": STRUCTURED_OUTPUT.format(base_prompt=base_prompt),
        "Reverse Prompting": REVERSE_PROMPTING.format(base_prompt=base_prompt),
        "Socratic Method": SOCRATIC.format(base_prompt=base_prompt),
    }
    return variants


def build_comparison_prompt(variants_dict, test_input):
    """Build prompts with test input for comparison"""
    comparison = {}
    for name, variant in variants_dict.items():
        comparison[name] = f"{variant}\n\nTest Input: {test_input}"
    return comparison