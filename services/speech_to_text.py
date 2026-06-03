from faster_whisper import WhisperModel
whisper_model=WhisperModel('small',device='cpu',compute_type='int8')

def transcribe_audio(audio_path):
    segments,info=whisper_model.transcribe(audio_path,beam_size=5)
    transcribed_text=" ".join([segment.text for segment in segments])
    return transcribed_text,info.language
    
