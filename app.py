import gradio as gr
import pandas as pd
# import pandas.io.sql as sqlio
# from sqlalchemy import create_engine
# import psycopg2
# from renumics import spotlight 
from pathlib import Path
# import temppathlib
import tempfile
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def calculate_hydrophobicity(sequence):
    # 创建 ProteinAnalysis 对象
    protein = ProteinAnalysis(sequence)
    # 计算疏水性
    hydrophobicity = protein.gravy()
    return hydrophobicity

df = pd.read_csv('seq_gen.csv')


css="""
    footer{display:none !important}

    .footer_main {
        position: fixed;
        bottom: 0;
        # width: 100%;
        text-align:center;
        # background-color: #253959;
        padding: 20px;
        margin-top: 0px;
        margin-left: 0px;
        margin-right: 0px;
    }
"""

def tab1_function():
    return "Content for Tab 1"


def calc(seqs):
    seqs = seqs.split('\n')
    igt_score = [0 for s in seqs]
    hpb_score = [calculate_hydrophobicity(s) for s in seqs]

    calc_df = pd.DataFrame(data={
         "Sequence": seqs,
         "Immunogenicity": igt_score,
         "Hydrophobicity": hpb_score,
    })
    tmp = tempfile.NamedTemporaryFile()
    calc_df.to_csv(tmp.name+'.csv', index=False)
    calc_df_path = Path(tmp.name+ '.csv')

    seq_eval_d = gr.DownloadButton(value = calc_df_path, label="Download",visible=True)
    return [gr.DataFrame(
                value=calc_df,
                headers=["Sequence", "Immunogenicity", "Hydrophobicity", "solubility", "Length of CDR3", "Isoelectric Point"],
                datatype=["str", "number", "number", "number", "number", "number"],
            ),seq_eval_d ]


with gr.Blocks(css=css, theme=gr.themes.Soft()) as demo:
    gr.Markdown("# VANGUARD")
    gr.Markdown("Variational Autoencoder for Antibody Generation and Design")

    gr.Markdown(
        """
        VANGUARD &copy; 2024
        """, elem_classes= 'footer_main')

    with gr.Tabs():
        with gr.Tab("Model Introduction"):
            tab1_function()
        with gr.Tab("Generated Sequences"):
            
            download_btn = gr.DownloadButton(value = Path("seq_gen.csv"), label="Download the Dataset", size="sm")

            styler = df.style.highlight_max(subset=df.columns[-5:],color = 'lightgreen', axis = 0)
            gr.DataFrame(
                value=styler,
                interactive=False,
                wrap=True,
                column_widths=[1,10,2,2,2,2,2],
                height='500',
            )
        with gr.Tab("Sequences Evaluation"):
            seqs_input = gr.Textbox(label="Input Sequences (separated by line)", lines=2, max_lines=10, placeholder="Enter your sequences here")
            calc_btn = gr.Button("Calculate")
            df_output = gr.DataFrame(
                headers=["Sequence", "Immunogenicity", "Hydrophobicity", "solubility", "Length of CDR3", "Isoelectric Point"],
                datatype=["str", "number", "number", "number", "number", "number"],
            )
            seq_eval_d = gr.DownloadButton(label="Download", visible = False)
            
            calc_btn.click(fn=calc, inputs=[seqs_input], outputs=[df_output,seq_eval_d])


if __name__ == "__main__":
    demo.launch()
