# Join grades — written by chain_frames.py. Apply in the edit; do not hand-tune.

Each chained clip is levelled to the last frame of the clip it continues: one per-channel gain, applied to the WHOLE chained clip. Only same-camera joins need it; a cut to the other camera hides a few percent.

| clip | continues | shift at the join | ffmpeg filter for the chained clip |
|---|---|---|---|
| `P1_003` | `P1_002` | 4.8% | `colorchannelmixer=rr=0.995:gg=1.005:bb=1.048` |
| `P1_010` | `P1_008` | 4.3% | `colorchannelmixer=rr=0.994:gg=1.003:bb=1.043` |
| `P1_012` | `P1_010` | 4.4% | `colorchannelmixer=rr=0.991:gg=1.004:bb=1.044` |
| `P1_024` | `P1_022` | 4.1% | `colorchannelmixer=rr=0.993:gg=1.003:bb=1.041` |
| `P1_026` | `P1_024` | 4.5% | `colorchannelmixer=rr=0.992:gg=1.005:bb=1.045` |
| `P1_035` | `P1_033` | 4.3% | `colorchannelmixer=rr=0.994:gg=1.003:bb=1.043` |
| `P1_038` | `P1_037` | 5.4% | `colorchannelmixer=rr=1.031:gg=1.029:bb=1.054` |
| `P1_045` | `P1_044` | 6.6% | `colorchannelmixer=rr=1.040:gg=1.037:bb=1.066` |
| `P1_047` | `P1_046` | 4.2% | `colorchannelmixer=rr=0.993:gg=1.003:bb=1.042` |
| `P1_049` | `P1_047` | 7.2% | `colorchannelmixer=rr=1.072:gg=1.068:bb=1.038` |
| `P1_053` | `P1_052` | 4.2% | `colorchannelmixer=rr=0.993:gg=1.003:bb=1.042` |
| `P1_055` | `P1_053` | 4.5% | `colorchannelmixer=rr=0.991:gg=1.005:bb=1.045` |
| `P1_060` | `P1_058` | 5.6% | `colorchannelmixer=rr=1.033:gg=1.031:bb=1.056` |
| `P1_062` | `P1_060` | 5.8% | `colorchannelmixer=rr=1.032:gg=1.032:bb=1.058` |
| `P1_072` | `P1_071` | 6.9% | `colorchannelmixer=rr=1.037:gg=1.037:bb=1.069` |
| `P1_080` | `P1_078` | 5.5% | `colorchannelmixer=rr=1.033:gg=1.031:bb=1.055` |
| `P1_088` | `P1_087` | 4.4% | `colorchannelmixer=rr=0.995:gg=1.004:bb=1.044` |
| `P1_091` | `P1_090` | 5.6% | `colorchannelmixer=rr=1.032:gg=1.031:bb=1.056` |
| `P1_093` | `P1_091` | 5.8% | `colorchannelmixer=rr=1.031:gg=1.031:bb=1.058` |
| `P1_099` | `P1_098` | 5.7% | `colorchannelmixer=rr=1.034:gg=1.031:bb=1.057` |
| `P1_101` | `P1_099` | 5.7% | `colorchannelmixer=rr=1.033:gg=1.032:bb=1.057` |
| `P1_109` | `P1_108` | 5.5% | `colorchannelmixer=rr=1.032:gg=1.030:bb=1.055` |
| `P1_111` | `P1_109` | 5.7% | `colorchannelmixer=rr=1.031:gg=1.031:bb=1.057` |
| `P1_115` | `P1_113` | 5.7% | `colorchannelmixer=rr=1.033:gg=1.031:bb=1.057` |
| `P1_117` | `P1_115` | 5.8% | `colorchannelmixer=rr=1.032:gg=1.031:bb=1.058` |
| `P1_121` | `P1_120` | 5.2% | `colorchannelmixer=rr=1.031:gg=1.029:bb=1.052` |
| `P1_129` | `P1_128` | 6.7% | `colorchannelmixer=rr=1.038:gg=1.038:bb=1.067` |
