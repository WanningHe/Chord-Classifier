#import librosa
#import librosa.display
from base_model import generate_cqt_chromagram, plot_cqt_chromagram, plot_cqt_spectrogram
import os

# Build a path to the audio file relative to this script’s location
script_dir = os.path.dirname(__file__)
audio_path = os.path.join(script_dir, 'c-major-scale.wav')

# Load an example audio file
#audio_path = "\src\c-major-scale.wav"
#y, sr = librosa.load(audio_path, sr=22050)

# Compute CQT spectrogram
chroma, cqt_db, sr = generate_cqt_chromagram(audio_path)

# Plot the CQT chromagram and spectrogram
plot_cqt_chromagram(chroma, sr)
plot_cqt_spectrogram(cqt_db, sr)
