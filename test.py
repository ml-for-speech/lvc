from lvc import LVC, LVCAudio
import librosa
import soundfile as sf
l = LVC()
o_y, o_sr = librosa.load('orig.wav')
s_y, s_sr = librosa.load('sample.wav')
o, sr = l.infer_array(
    LVCAudio(o_y, o_sr),
    LVCAudio(s_y, s_sr),
)
sf.write('out.wav', o, sr)
# l.infer_file(
#     'orig.wav',
#     'sample.wav',
#     'target.wav',
# )