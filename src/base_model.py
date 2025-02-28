import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def generate_cqt_chromagram(audio, sr=None, mono=True):  
    #Load the audio file
    y, sr = librosa.load(audio, sr=sr, mono=mono)

    #Compute the CQT absolute amplitudes
    cqt = np.abs(librosa.cqt(y=y, sr=sr, hop_length=512, n_bins=7*12)) #7 octaves, 12 bins per octave
    cqt_db = librosa.amplitude_to_db(cqt, ref=np.max)

    #Compute the chromagram from the CQT
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr, hop_length=512)

    return chroma, cqt_db, sr

def plot_cqt_chromagram(chroma, sr):
    plt.figure(figsize=(12, 4))
    librosa.display.specshow(chroma, sr=sr, x_axis='time', y_axis='chroma', vmin=0, vmax=1)
    plt.title('Chromagram')
    plt.colorbar()
    plt.tight_layout()
    plt.show()

def plot_cqt_spectrogram(cqt_db, sr):
    plt.figure(figsize=(12, 4)) #or 10, 4
    librosa.display.specshow(cqt_db, sr=sr, x_axis='time', y_axis='cqt_hz')
    plt.title('CQT')
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()
    plt.show()

