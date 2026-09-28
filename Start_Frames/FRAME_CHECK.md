# Start-frame check — 2026-09-26

Run: `python3 Fixed_Assets/tools/frame_set_check.py` (px at 1920×1080; the person is excluded). Replaced files are in `_replaced_2026-09-26/`.

```
== Start_Frames/Cleopatra
  frame_cleopatra_b          vs frame_cleopatra        shift +0,+0  scale +0  luma +0.5%  colour 0.5  room 2.9  PASS
  frame_cleopatra_c          vs frame_cleopatra        shift +0,+0  scale +0  luma +0.1%  colour 0.1  room 2.7  PASS
  frame_cleopatra_d          vs frame_cleopatra        shift +0,+0  scale +0  luma +2.6%  colour 2.7  room 5.2  CHECK LUMA
  frame_cleopatra_e          vs frame_cleopatra        shift +0,+0  scale -1  luma -0.3%  colour 0.6  room 4.9  PASS
  frame_cleopatra_f          vs frame_cleopatra        shift +0,+0  scale +0  luma +0.3%  colour 0.3  room 3.1  PASS
  frame_cleopatra_g          vs frame_cleopatra        shift +0,+0  scale +0  luma -0.2%  colour 0.1  room 2.7  PASS
  frame_cleopatra_h          vs frame_cleopatra        shift +0,+0  scale +0  luma +0.2%  colour 0.3  room 2.8  PASS
  frame_cleopatra_i          vs frame_cleopatra        shift +0,+0  scale +0  luma -0.3%  colour 0.3  room 2.8  CHECK  FURNITURE right armrest top +42px, left armrest top -23px
  frame_wide_cleopatra_b     vs frame_wide_cleopatra   shift +1,+0  scale -2  luma -2.5%  colour 2.9  room 8.1  CHECK LUMA
  frame_wide_cleopatra_b_marked vs frame_wide_cleopatra_marked shift +0,+0  scale -2  luma -3.3%  colour 3.6  room 8.6  CHECK LUMA COLOUR
  frame_wide_cleopatra_c     vs frame_wide_cleopatra   shift +1,+0  scale -2  luma +0.0%  colour 1.2  room 9.1  PASS
  frame_wide_cleopatra_c_marked vs frame_wide_cleopatra_marked shift +0,+0  scale -2  luma +0.0%  colour 1.1  room 11.5  PASS
== Start_Frames/Host
  frame_host_b               vs frame_host             shift +0,+0  scale +0  luma +1.1%  colour 1.1  room 5.6  PASS
  frame_host_c               vs frame_host             shift +0,+0  scale +0  luma -1.5%  colour 1.4  room 5.6  PASS
  frame_host_d               vs frame_host             shift +2,+0  scale +3  luma -1.8%  colour 1.3  room 5.6  PASS
  frame_host_e               vs frame_host             shift +0,+0  scale -3  luma -1.3%  colour 1.6  room 5.2  PASS
  frame_host_f               vs frame_host             shift +0,+0  scale +1  luma -1.4%  colour 1.4  room 5.3  PASS
  frame_host_direct          vs frame_host             shift +0,+0  scale +0  luma +0.3%  colour 0.9  room 2.9  PASS
  frame_host_direct_b        vs frame_host_b           shift +0,+0  scale +0  luma -1.4%  colour 1.0  room 2.7  PASS
  frame_host_direct_c        vs frame_host_e           shift +0,+0  scale +0  luma -0.3%  colour 0.4  room 2.8  PASS
```
