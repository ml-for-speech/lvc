# LVC

Unofficial package for LVC-VC (zero-shot voice conversion) by Wonjune Kang, Mark Hasegawa-Johnson, Deb Roy.

## Installation

```
pip install lvc
```

## Usage

You can either convert files or convert arrays.

### Convert Files

```python
from lvc import LVC, LVCAudio
l = LVC()

l.infer_file(
    'orig.wav',
    'sample.wav',
    'target.wav',
)
```

### Convert Arrays

```python
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
```

## License

MIT