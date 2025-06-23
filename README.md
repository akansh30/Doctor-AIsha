# Doctor AIsha

Doctor AIsha is a multimodal voice assistant that simulates a doctor-patient interaction using voice and image input. It integrates speech recognition, vision models, large language models, and text-to-speech synthesis to provide an end-to-end medical consultation experience through a voice bot interface.
![Screenshot 2025-06-21 153634](https://github.com/user-attachments/assets/f792884e-cbf4-4bb7-883d-4ebd94d5244f)

## Project Layout

### Phase 1 – Setup the Brain of the Doctor (Multimodal LLM)
- Configure GROQ API key
- Convert the uploaded image into the required format
- Send both image and transcribed query to a Multimodal LLM for diagnosis

### Phase 2 – Setup Voice of the Patient
- Record patient's voice using microphone (FFmpeg & PyAudio)
- Convert speech to text using a STT model like Whisper

### Phase 3 – Setup Voice of the Doctor
- Convert LLM text output into speech using gTTS or ElevenLabs
- Output a playable audio file for the user

### Phase 4 – Setup the VoiceBot UI
- UI built with Gradio for:
  - Speaking symptoms
  - Uploading affected area images
  - Hearing the AI doctor's voice response

## Technologies Used

- **GROQ API** – for running LLMs (like LLaMA)
- **Whisper** – for speech-to-text
- **Meta multimodal models** – for vision+text-based diagnosis
- **gTTS / ElevenLabs** – for text-to-speech synthesis
- **Gradio** – for building the frontend interface
- **PyAudio & FFmpeg** – for capturing and handling audio


### Voice + Image Based Diagnosis Interface
![Screenshot 2025-06-20 142614](https://github.com/user-attachments/assets/13543a6f-b1cf-4bdc-a7e9-b4b7d77ff69b)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/akansh30/Doctor-AIsha.git
cd Doctor-AIsha
```
### Setup Environment and install req
```bash
python -m venv venv
source venv/Scripts/activate #windows
pip install -r requirements.txt
```
### Create a .env file
```bash
GROQ_API_KEY=your_groq_key_here
ELEVENLABS_API_KEY=your_elevenlabs_key_here
```

