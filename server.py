import gradio as gr

from functions import Standard, Screen


with gr.Blocks(title='GexMolGen') as demo:
    gr.Markdown("""# GexMolGen (Developed by Bunnybeibei)
    By uploading the desired gene expression values along with those used 
    for the control group in a .csv file, following the example format, 
    you can generate corresponding hit-like molecules!
    """)

    with gr.Tab("Standard"):
        with gr.Row():
            control = gr.File(label="The gene expression used for the control group")
            pert = gr.File(label="The gene expression data you desire")

        with gr.Column(scale=1, min_width=600):
            seed = gr.Slider(minimum=0, maximum=100, step=1, label="seed",
                             info="Different seeds may generate different results")
            beam_width = gr.Slider(minimum=1, maximum=100, step=1, label="beam width",
                                   info="Choose between 1 and 100")

        with gr.Row():
            button = gr.Button("Submit", variant="secondary")
            clear = gr.ClearButton(components=[control, pert, beam_width, seed], value='Clear',
                                   variant="secondary")

        with gr.Accordion("Output"):
            hit_like_smiles = gr.File(label="A CSV file containing candidate molecules")
            hit_like_figs = gr.Gallery(label="Figures showing candidate molecules")
            button.click(fn=Standard, inputs=[control, pert, beam_width, seed],
                         outputs=[hit_like_smiles, hit_like_figs])

    with gr.Tab("Screen"):
        with gr.Row():
            control = gr.File(label="The gene expression used for the control group")
            pert = gr.File(label="The gene expression data you desire")
            ref_smiles = gr.File(label='Reference molecule',
                                 info="Known inhibitor list")

        with gr.Column():
            seed = gr.Slider(minimum=0, maximum=100, step=1, label="seed",
                             info="Different seeds may generate different results")
            beam_width = gr.Slider(minimum=1, maximum=100, step=1, label="beam width",
                                   info="Choose between 1 and 100")
            method = gr.Dropdown(label="method", info="The method chosen to calculate similarity",
                                 choices=["Morgan", "MACCS", "Fraggle"])

        with gr.Row():
            button = gr.Button("Submit", variant="secondary")
            clear = gr.ClearButton(components=[control, pert, ref_smiles, method, beam_width,
                                               seed], value='Clear',
                                   variant="secondary")

        with gr.Accordion("Output"):
            hit_like_smiles = gr.File(label="A CSV file containing candidate molecules")
            hit_like_figs = gr.Gallery(label="Figures showing candidate molecules")
            button.click(fn=Screen, inputs=[control, pert, ref_smiles, method, beam_width, seed],
                         outputs=[hit_like_smiles, hit_like_figs])


if __name__ == "__main__":

    demo.launch()