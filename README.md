# 🌍 Multi-Language Translator App

This repository contains a simple and interactive multi-language translation web app built using **Gradio** and **Hugging Face Transformers**. It translates English text into various languages using the powerful **NLLB (No Language Left Behind)** model from Facebook AI.

## 🔧 Features

- Translate English text into:
  - German 🇩🇪
  - French 🇫🇷
  - Hindi 🇮🇳
  - Romanian 🇷🇴 (and easily extendable!)
- Easy-to-use web interface with Gradio
- Uses the distilled NLLB-200 multilingual model for accurate translations

## 🧠 Model Used

- `facebook/nllb-200-distilled-600M`  
  A smaller, faster version of the original NLLB model designed for low-latency real-time inference.

## 🛠️ Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/multi-language-translator.git
cd multi-language-translator

# Install dependencies
pip install transformers torch gradio


##How to Run

python multi-language-translator.py


roject Structure
multi-language-translator.py: Main application file

lang.json: Contains language and corresponding FLORES-200 codes

📝 Notes
Translation source language is fixed to English (eng_Latn)

Target languages are fetched dynamically using FLORES codes from a JSON file

# Author
Tanmay Pendharkar
