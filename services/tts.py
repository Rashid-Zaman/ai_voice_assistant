import numpy as np
from kokoro import KPipeline
import soundfile as sf

def text_to_speech(text, detected_lang):

    if detected_lang in ["hi", "ur"]:
        lang_code = "h"
    else:
        lang_code = "a"

    pipeline = KPipeline(lang_code=lang_code)

    generator = pipeline(
        text,
        voice="af_heart",
        speed=1
    )

    audio_chunks = []

    for _, _, audio in generator:
        audio_chunks.append(audio)

    full_audio = np.concatenate(audio_chunks)

    output_file = "audio/output.wav"

    sf.write(
        output_file,
        full_audio,
        24000
    )

    return output_file