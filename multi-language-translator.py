# Use a pipeline as a high-level helper
import code
import json
from torchgen.executorch.api.types import bfloat16T
from transformers import pipeline
import torch
import gradio as gr

text_translator = pipeline("translation",
                model="facebook/nllb-200-distilled-600M", torch_dtype=torch.bfloat16)

text = "hello friends, how are you?"
translation = text_translator(text,
                              src_lang="eng_Latn",
                              tgt_lang="deu_Latn"

                             )

with open('lang.json', 'r') as file:
    lang = json.load(file)

def get_FLORES_code_from_language(lang):
    for entry in lang:
        if entry['Language'].lower() == lang.lower():
            return entry['FLORES-200 code']
    return None


def translate_text(text, destination_language):
    # text = "Hello Friends, How are you?"
    dest_code= get_FLORES_code_from_language(destination_language)
    translation = text_translator(text,
                                  src_lang="eng_Latn",
                                  tgt_lang=dest_code)
    return translation[0]["translation_text"]

gr.close_all()

# demo = gr.Interface(fn=summary, inputs="text",outputs="text")
demo = gr.Interface(fn=translate_text,
                    inputs=[gr.Textbox(label="Input text to translate",lines=6), gr.Dropdown(["German","French", "Hindi", "Romanian	"], label="Select Destination Language")],
                    outputs=[gr.Textbox(label="Translated text",lines=4)],
                    title="@GenAILearniverse Project 4: Multi language translator",
                    description="THIS APPLICATION WILL BE USED TO TRNSLATE ANY ENGLIST TEXT TO MULTIPLE LANGUAGES.")
demo.launch()