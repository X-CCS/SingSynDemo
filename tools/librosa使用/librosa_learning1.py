# -*- coding:utf-8 -*-
# /usr/bin/python
'''
@Author  :  X-CCS 
@Describe:  
@Evn     :  
@Date    :  2021-08-04  17:19
'''
# Feature extraction example
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load the example clip
filename = "a.wav"

# 数值化和采样率
y, sr = librosa.load(filename)
print("y",y,"\nsr",sr)

# 傅里叶变换
D = np.abs(librosa.stft(y))
print("D",D)

#使用左对齐的帧，而不是居中的帧
D_left = np.abs(librosa.stft(y, center=False))
librosa.display.specshow(librosa.amplitude_to_db(D,ref=np.max),y_axis='log', x_axis='time')
plt.title('Power spectrogram')
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()
plt.show()
plt.savefig("./power_spe.png")


# 输出wav文件
librosa.output.write_wav("./aa.wav",y,sr)

# 获取采样率
sr = librosa.get_samplerate(filename)
print("sr",sr)

# 获取采样率
sr = librosa.get_samplerate(filename)
print("sr", sr)

# 获取时长
# duration = librosa.get_duration([y,sr])
# print('duration',duration)

# 转化为mono格式
y = librosa.to_mono(y)
print("mono_y",y,"\nmono_sr",sr)

orig_sr = sr
target_sr = 44000
y = librosa.resample(y,orig_sr, target_sr)
print("resample_y",y,"\nresample_sr",sr)

# Set the hop length; at 22050 Hz, 512 samples ~= 23ms
hop_length = 512

# Separate harmonics and percussives into two waveforms
# y_harmonic:谐波（音调）和 y_percussive:打击（瞬态）部分
y_harmonic, y_percussive = librosa.effects.hpss(y)
print('y_harmonic',y_harmonic, '\ny_percussive',y_percussive)

# Beat track on the percussive signal
tempo, beat_frames = librosa.beat.beat_track(y=y_percussive,sr=sr)
print('tempo',tempo,'\nbeat_frames',beat_frames)

# Compute MFCC features from the raw signal
mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=13)
print('mfcc',mfcc)

# And the first-order differences (delta features)
mfcc_delta = librosa.feature.delta(mfcc)
print('mfcc_delta',mfcc_delta)

# 在节拍事件之间堆叠和同步
# 这一次，我们将使用平均值（默认值）而不是中位数
beat_mfcc_delta = librosa.util.sync(np.vstack([mfcc, mfcc_delta]),beat_frames)
print('beat_mfcc_delta',beat_mfcc_delta)

# 根据谐波信号计算色度特征
chromagram = librosa.feature.chroma_cqt(y=y_harmonic,sr=sr)
print('chromagram',chromagram)

# 在节拍事件之间聚合色度特征
# 我们将在节拍帧之间使用每个特征的中值
beat_chroma = librosa.util.sync(chromagram,beat_frames,aggregate=np.median)
print('beat_chroma',beat_chroma)

# 所有节拍同步功能堆叠在一起
beat_features = np.vstack([beat_chroma, beat_mfcc_delta])
print('beat_features',beat_features)