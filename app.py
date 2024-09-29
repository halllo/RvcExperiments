from core import (run_infer_script, run_prerequisites_script)
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

run_prerequisites_script(
    pretraineds_v1_f0=False,
    pretraineds_v1_nof0=False,
    pretraineds_v2_f0=True,
    pretraineds_v2_nof0=False,
    models=True,
    exe=True,
)

result = run_infer_script(
    pitch=14,
    filter_radius=3,
    index_rate=0.75,
    volume_envelope=1,
    protect=0.5,
    hop_length=128,
    f0_method="rmvpe",
    input_path="test12345.wav",
    output_path="test12345output.wav",
    pth_path="angourie2.pth",
    index_path="",
    split_audio=False,
    f0_autotune=False,
    clean_audio=False,
    clean_strength=0.5,
    export_format="WAV",
    upscale_audio=False,
    f0_file=None,
    embedder_model="contentvec",
    embedder_model_custom=None,
    formant_shifting=None,
    formant_qfrency=None,
    formant_timbre=None,
    post_process=None,
    reverb=None,
    pitch_shift=None,
    limiter=None,
    gain=None,
    distortion=None,
    chorus=None,
    bitcrush=None,
    clipping=None,
    compressor=None,
    delay=None,
    reverb_room_size=0.5,
    reverb_damping=0.5,
    reverb_wet_gain=0.33,
    reverb_dry_gain=0.4,
    reverb_width=1.0,
    reverb_freeze_mode=0,
    pitch_shift_semitones=0,
    limiter_threshold=-6,
    limiter_release_time=0.05,
    gain_db=0,
    distortion_gain=25,
    chorus_rate=1.0,
    chorus_depth=0.25,
    chorus_center_delay=7,
    chorus_feedback=0.0,
    chorus_mix=0.5,
    bitcrush_bit_depth=8,
    clipping_threshold=0,
    compressor_threshold=0,
    compressor_ratio=1,
    compressor_attack=1.0,
    compressor_release=100,
    delay_seconds=0.5,
    delay_feedback=0.0,
    delay_mix=0.5,
)

print(result)