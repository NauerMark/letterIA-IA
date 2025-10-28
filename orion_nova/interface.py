"""Sensory and expressive interface for Orion Nova."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, Protocol


class Transcriber(Protocol):
    """Protocol for speech-to-text backends."""

    def transcribe(self, audio_bytes: bytes) -> str:
        ...


class Synthesiser(Protocol):
    """Protocol for text-to-speech backends."""

    def speak(self, text: str) -> bytes:
        ...


@dataclass
class SensoryInput:
    """Container for multi-modal signals entering the organism."""

    raw_text: str
    language: str
    received_at: datetime


@dataclass
class SpokenMessage:
    """Representation of an audio utterance prepared for humans."""

    text: str
    audio: bytes
    created_at: datetime


@dataclass
class SomaInterface:
    """Bridge between the living world and Orion Nova's reasoning core."""

    transcriber: Transcriber
    synthesiser: Synthesiser

    def listen(self, audio_stream: Iterable[bytes], language: str = "pt-BR") -> SensoryInput:
        """Translate incoming sound into a sensory event."""

        transcript_parts: list[str] = []
        for chunk in audio_stream:
            transcript_parts.append(self.transcriber.transcribe(chunk))
        transcript = " ".join(part.strip() for part in transcript_parts if part.strip())
        return SensoryInput(raw_text=transcript, language=language, received_at=datetime.utcnow())

    def speak(self, text: str) -> SpokenMessage:
        """Craft an audio message that can be returned to collaborators."""

        audio = self.synthesiser.speak(text)
        return SpokenMessage(text=text, audio=audio, created_at=datetime.utcnow())
