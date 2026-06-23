"""
EmotionDetection package initializer.

This module makes the `emotion_detector` function readily available when the
package is imported:

    from emotion_detection import emotion_detector

The function itself is defined in `emotion_detection.py` and implements the
logic for detecting emotions using IBM Watson NLP services.
"""

from .emotion_detection import emotion_detector

__all__ = ["emotion_detector"]