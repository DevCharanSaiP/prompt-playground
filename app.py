import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import gradio as gr
import json

from prompts import get_prompt_variants, build_comparison_prompt
from style import CSS

# ---- Load token and set up client ----
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

client = InferenceClient(
    "meta-llama/Meta-Llama-3-8B-Instruct",
    token=HF_TOKEN,
)

# ---- Core functions ----
def generate_variants(base_prompt, use_case, examples, test_input):
    """Generate all 7 prompt variants and test them"""
    if not base_prompt.strip():
        return "Please provide a base prompt.", "", ""

    # Generate 7 variants
    variants = get_prompt_variants(base_prompt, use_case, examples)
    
    # Test each variant
    results = {}
    for variant_name, variant_prompt in variants.items():
        full_prompt = f"{variant_prompt}\n\nTest Input: {test_input}"
        
        messages = [{"role": "user", "content": full_prompt}]
        
        try:
            response = client.chat_completion(
                messages=messages,
                max_tokens=300,
                temperature=0.8,
            )
            results[variant_name] = response.choices[0].message["content"].strip()
        except Exception as e:
            results[variant_name] = f"Error: {str(e)}"
    
    # Build output markdown for variants
    variants_md = "## 📊 7 Prompt Variants\n\n"
    for i, (name, output) in enumerate(results.items(), 1):
        variants_md += f"### {i}. {name}\n"
        variants_md += f"``````\n\n"
    
    # Build comparison table
    comparison_md = "## 📈 Performance Comparison\n\n"
    comparison_md += "| Variant | Use Case | Complexity | Best For |\n"
    comparison_md += "|---------|----------|-----------|----------|\n"
    
    use_cases_map = {
        "Zero-Shot": "Direct answers | Low | Quick responses |",
        "Few-Shot": "Learning from examples | Medium | Consistent formats |",
        "Chain-of-Thought": "Complex reasoning | High | Deep analysis |",
        "Role-Based": "Specialized expertise | Medium | Domain-specific answers |",
        "Structured Output": "Organized responses | Medium | Data extraction |",
        "Reverse Prompting": "Creative thinking | High | Problem-solving |",
        "Socratic Method": "Learning & exploration | High | Educational content |",
    }
    
    for variant_name in results.keys():
        if variant_name in use_cases_map:
            comparison_md += f"| {variant_name} | {use_cases_map[variant_name]} |\n"
    
    # Auto-optimized version
    optimized = f"""## 🚀 Auto-Optimized Version

Based on your use case (**{use_case}**), here's the recommended optimized prompt:
{get_prompt_variants(base_prompt, use_case, examples)['Chain-of-Thought']}

Test Input: {test_input}

**Why this works:**
- Combines structured thinking with clarity
- Encourages step-by-step reasoning
- Easy to iterate and refine
"""
    
    return variants_md, comparison_md, optimized


# ---- Gradio UI ----
with gr.Blocks() as demo:
    gr.HTML(
        CSS
        + """
        <div id="title-wrap">
          <h1>⚗️ Prompt Engineering Playground</h1>
          <p>Write a prompt. Generate 7 variants. Compare. Optimize. Copy & Share.</p>
        </div>
        """
    )

    with gr.Column(elem_classes=["panel"]):
        gr.Markdown("### Step 1: Define Your Base Prompt")
        
        base_prompt = gr.Textbox(
            label="Base Prompt",
            placeholder="Describe the task you want to accomplish...",
            lines=4,
        )

        with gr.Row():
            use_case = gr.Dropdown(
                ["General", "Code generation", "Creative writing", "Data analysis", 
                 "Customer support", "Education", "Research", "Brainstorming"],
                label="Use Case",
                value="General",
            )
            examples = gr.Textbox(
                label="Examples (for Few-Shot, optional)",
                placeholder="Provide 2-3 examples separated by line breaks...",
                lines=3,
            )

        test_input = gr.Textbox(
            label="Test Input",
            placeholder="Input to test all variants against...",
            lines=2,
        )

        generate_button = gr.Button("⚡ Generate & Compare 7 Variants", variant="primary")

    # Output sections
    with gr.Column(elem_classes=["panel"]):
        variants_output = gr.Markdown(
            label="Prompt Variants",
            elem_classes=["variant-output"],
            value="Your 7 prompt variants will appear here."
        )

        comparison_output = gr.Markdown(
            label="Performance Comparison",
            elem_classes=["comparison-table"],
            value="Comparison table will appear here."
        )

        optimized_output = gr.Markdown(
            label="Auto-Optimized Version",
            elem_classes=["variant-output"],
            value="Optimized prompt will appear here."
        )

    generate_button.click(
        fn=generate_variants,
        inputs=[base_prompt, use_case, examples, test_input],
        outputs=[variants_output, comparison_output, optimized_output],
    )


if __name__ == "__main__":
    demo.launch()