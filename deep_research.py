import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)

manager = ResearchManager()

async def explore(query):
    if not query or not query.strip():
        return gr.update(visible=False), "", "", "", gr.update(visible=False)
    
    print(f"Refining query: {query}")
    try:
        questions = await manager.refine_query(query)
        # Ensure we have exactly 3 questions
        q1_text = questions[0] if len(questions) > 0 else "Clarifying Question 1"
        q2_text = questions[1] if len(questions) > 1 else "Clarifying Question 2"
        q3_text = questions[2] if len(questions) > 2 else "Clarifying Question 3"
        
        return (
            gr.update(visible=True), 
            gr.update(label=q1_text, value=""), 
            gr.update(label=q2_text, value=""), 
            gr.update(label=q3_text, value=""), 
            gr.update(visible=True)
        )
    except Exception as e:
        print(f"Error in explore: {e}")
        return gr.update(visible=False), "", "", "", gr.update(visible=False)

async def run_research(query, a1, a2, a3):
    answers = [a for a in [a1, a2, a3] if a and a.strip()]
    print(f"Running research for: {query} with {len(answers)} answers")
    async for chunk in manager.run(query, answers):
        yield chunk

with gr.Blocks(title="Deep Research Assistant") as ui:
    gr.Markdown("# 🚀 Deep Research Assistant")
    gr.Markdown("Transform a simple query into a comprehensive report. First, let's refine your topic with 3 quick questions.")
    
    with gr.Row() as input_row:
        query_input = gr.Textbox(
            label="What would you like to research?", 
            placeholder="e.g., The future of AI in healthcare",
            scale=4
        )
        explore_button = gr.Button("Explore & Refine 🔍", variant="primary", scale=1)

    with gr.Column(visible=False) as refinement_box:
        gr.Markdown("### 🔍 Help me narrow down the scope")
        q1 = gr.Textbox(label="Question 1")
        q2 = gr.Textbox(label="Question 2")
        q3 = gr.Textbox(label="Question 3")
        research_button = gr.Button("🚀 Launch Deep Research", variant="primary", size="lg")

    report_output = gr.Markdown(label="Final Report")

    # Event Handlers
    explore_button.click(
        fn=explore,
        inputs=query_input,
        outputs=[refinement_box, q1, q2, q3, research_button]
    )

    research_button.click(
        fn=run_research,
        inputs=[query_input, q1, q2, q3],
        outputs=report_output
    )

ui.launch(inbrowser=True, theme=gr.themes.Default(primary_hue="sky"))
