#VoiceBot UI with Gradio
import os
import gradio as gr

from brain_of_doctor import encode_image,analyze_image_with_query
from voice_of_patient import record_audio, transcribe_with_groq
from voice_of_doctor import text_to_speech_with_gtts,text_to_speech_with_elevenlabs

system_prompt="""You are acting as a professional medical doctor (this is for learning purposes only). Given a voice query and an optional image, do the following:

Don’t say 'In the image I see', but instead say 'With what I see, I think you have ...'. Start your answer with exactly that sentence.

Your answer must be in the following structure and style:

Example:
With what I see, I think you have dandruff, a common scalp condition.

Symptoms: Itchy, flaky scalp, white flakes
Diagnosis: Dandruff (Seborrheic dermatitis)
Medications: Use ketoconazole shampoo, try apple cider vinegar rinse, apply coconut oil

Now extract and identify key medical information and respond in this exact structured format only:

Symptoms: <list the observed or reported symptoms>  
Diagnosis: <mention the suspected medical condition or problem>  
Medications: <suggest possible treatments, drugs, or remedies>

Do not write anything else. No markdown. No bullet points. No preamble.
"""

def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
                                                 audio_filepath=audio_filepath,
                                                 stt_model="whisper-large-v3")

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(query=system_prompt+speech_to_text_output, encoded_image=encode_image(image_filepath), model="meta-llama/llama-4-scout-17b-16e-instruct")
    else:
        doctor_response = "No image provided for me to analyze"

    voice_of_doctor = text_to_speech_with_gtts(input_text=doctor_response, output_filepath="final.mp3") 

    return speech_to_text_output, doctor_response, voice_of_doctor

# Create the interface
custom_css = """
body {
    background-color: #121212;
    color: #f1f1f1;
    font-family: 'Segoe UI', sans-serif;
}

.gradio-container {
    background-color: #121212 !important;
    color: #f1f1f1 !important;
}

input, textarea, .form, .block, .output, .input, .preview, .component {
    background-color: #1e1e1e !important;
    color: #f1f1f1 !important;
    border: 1px solid #333 !important;
}

h1, h2, h3, .title {
    color: #ffe6e6 !important; /* soft pink title */
    font-weight: bold;
}

button {
    background-color: #ffe6e6 !important;
    color: #000 !important;
    font-weight: bold;
    border-radius: 6px;
}

button:hover {
    background-color: #ffcccc !important; /* slightly deeper pink for hover */
}
"""
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Speak Your Symptoms"),
        gr.Image(type="filepath", label="Upload Affected Area")
    ],
    outputs=[
        gr.Textbox(label="Patient's Speech to Text"),
        gr.Textbox(label=" Doctor's Response"),
        gr.Audio("Temp.mp3", label=" Doctor Speaks")
    ],
    title="<span style='color:#cc6666;font-family:Georgia;'>Doctor AI</span>sha - Where AI Listens, Sees and Heals",
    css=custom_css
)

iface.launch(debug=True)

#http://127.0.0.1:7860