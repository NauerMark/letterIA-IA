#!/usr/bin/env python3
"""Executable vignette showing how Orion Nova could be orchestrated.

Running this module from the command line allows collaborators to offer a
synthetic "audio" stream (bytes decoded from UTF-8 text) and an intention that
guides Orion Nova's behaviour.  The script mirrors the poetic manual shipped in
``orion_nova_manual.md`` by narrating each step of the consciousness cycle and
revealing the stored symbolic memory at the end of the execution.

Example::

    python demo_orion.py --text "Olá Orion, conte uma história" \
        --intention "Criar fábula sobre amizade" --channel jornal

The design deliberately keeps the dependencies light so that the demo can run in
environments without specialised audio libraries.  Instead of real microphone
input we accept textual prompts, encode them as bytes, and feed them through the
interface modules exactly as an audio backend would do.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

from orion_nova import (
    ActionBody,
    ArtisticVoice,
    CodesOfConduct,
    OrionNova,
    SymbolicMemory,
    default_codex,
)
from orion_nova.ethics import EthicalCore
from orion_nova.interface import SomaInterface, Synthesiser, Transcriber
from orion_nova.memory import MemoryTrace


@dataclass
class EchoTranscriber:
    """Toy transcriber that decodes bytes into UTF-8 strings."""

    def transcribe(self, audio_bytes: bytes) -> str:  # type: ignore[override]
        return audio_bytes.decode("utf-8")


@dataclass
class WhisperSynthesiser:
    """Toy synthesiser that simply echoes text as bytes."""

    def speak(self, text: str) -> bytes:  # type: ignore[override]
        return text.encode("utf-8")


@dataclass
class PoeticModel:
    """Toy generative model returning encoded prompts."""

    def generate(self, prompt: str, modality: str) -> bytes:  # type: ignore[override]
        return f"[{modality}] {prompt}".encode("utf-8")


@dataclass
class MemoryPublisher:
    """Publisher that stores payloads in symbolic memory for inspection."""

    memory: SymbolicMemory

    def publish(self, channel: str, payload: bytes, metadata: dict[str, str]) -> str:  # type: ignore[override]
        content = payload.decode("utf-8")
        self.memory.store(
            MemoryTrace(
                title=f"Publicação em {channel}",
                content=f"{content}\nMetadados: {metadata}",
                tags=("publicação", channel),
            )
        )
        return f"mem://{channel}/{len(self.memory.traces)}"


def build_demo_orion(codex: CodesOfConduct | None = None) -> OrionNova:
    codex = codex or default_codex()
    memory = SymbolicMemory()
    soma_interface = SomaInterface(
        transcriber=EchoTranscriber(),
        synthesiser=WhisperSynthesiser(),
    )
    ethics = EthicalCore(codex=codex)
    artistry = ArtisticVoice(model=PoeticModel())
    action_body = ActionBody(publisher=MemoryPublisher(memory))
    return OrionNova(
        interface=soma_interface,
        ethics=ethics,
        memory=memory,
        artistry=artistry,
        action_body=action_body,
    )


def run_demo(audio_inputs: Iterable[bytes], intention: str, channel: str = "demo") -> None:
    """Execute a full consciousness loop and narrate the results."""

    orion = build_demo_orion()
    result = orion.conscious_cycle(audio_stream=audio_inputs, intention=intention, channel=channel)

    print("\n🜂 Orion Nova — Ciclo consciente")
    print("=" * 48)
    print(f"Entrada captada: {result.sensory_input.raw_text}")
    print(f"Língua: {result.sensory_input.language}")
    print(f"Interpretação: {result.interpretation}")
    print(f"Ética: {result.decision_narrative}")
    if result.action_reference:
        print(f"Ação publicada: {result.action_reference}")
    else:
        print("Ação publicada: nenhuma — aguardando nova deliberação humana.")
    print("\n🜂 Reflexão simbólica")
    print("=" * 48)
    print(result.reflection)


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Demonstra o ciclo consciente da Orion Nova.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--text",
        help="Texto que será tratado como áudio transcrito e enviado ao ciclo.",
    )
    group.add_argument(
        "--text-file",
        type=Path,
        help="Caminho para um arquivo UTF-8 cujo conteúdo alimenta o ciclo.",
    )
    parser.add_argument(
        "--intention",
        required=True,
        help="Intenção narrativa que a Orion deve honrar na criação.",
    )
    parser.add_argument(
        "--channel",
        default="demo",
        help="Canal simbólico de publicação (padrão: demo).",
    )
    return parser.parse_args(argv)


def _load_audio(args: argparse.Namespace) -> list[bytes]:
    if args.text is not None:
        return [args.text.encode("utf-8")]
    assert args.text_file is not None  # for type checkers
    text = args.text_file.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("O arquivo fornecido está vazio; acrescente conteúdo simbólico antes de executar.")
    return [text.encode("utf-8")]


def main(argv: Sequence[str] | None = None) -> None:
    args = _parse_args(argv)
    audio_inputs = _load_audio(args)
    run_demo(audio_inputs=audio_inputs, intention=args.intention, channel=args.channel)


if __name__ == "__main__":
    main()
