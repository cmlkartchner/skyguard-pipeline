from __future__ import annotations

import logging
import os

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import typing

from shared.util import get_production_path, resolve_mapped_path

from ..baseclass import DCC
from env import Executables

log = logging.getLogger(__name__)


class HoudiniDCC(DCC):
    """Houdini DCC class"""

    def __init__(
        self,
        is_python_shell: bool = False,
    ) -> None:
        this_path = Path(__file__).resolve()
        pipe_path = this_path.parents[2]

        env_vars: typing.Mapping[str, int | str | None] | None
        env_vars = {
            "DCC": str(this_path.parent.name),
            # Backup directory
            "HOUDINI_BACKUP_DIR": "./.backup",
            # Dump the core on crash to help debugging
            "HOUDINI_COREDUMP": 1,
            # Compiled Houdini files debug
            "HOUDINI_DSO_ERROR": 2 if log.isEnabledFor(logging.DEBUG) else None,
            # Max backup files
            "HOUDINI_MAX_BACKUP_FILES": 20,
            # Prevent user envs from overriding existing values
            "HOUDINI_NO_ENV_FILE_OVERRIDES": 1,
            # Disable start page splash
            "HOUDINI_NO_START_PAGE_SPLASH": 1,
            # Configure additional HDA locations outside of the pipeline
            "HOUDINI_OTLSCAN_PATH": os.pathsep.join(
                [
                    str(p)
                    for p in resolve_mapped_path(
                        get_production_path() / "hda"
                    ).iterdir()
                ]
                + ["&"]
            ),
            # Package loading debug logging
            "HOUDINI_PACKAGE_VERBOSE": 1 if log.isEnabledFor(logging.DEBUG) else None,
            # Splash file
            "HOUDINI_SPLASH_FILE": str(pipe_path / "lib/splash/dunginisplash19.5.png"),
            # Project-specific preference overrides
            "HSITE": str(resolve_mapped_path(this_path.parent / "hsite")),
            # Job directory
            "JOB": str(resolve_mapped_path(get_production_path())),
            # Pass log level defined on commandline
            "PIPE_LOG_LEVEL": log.getEffectiveLevel(),
            "PIPE_PATH": str(pipe_path),
            # Add pipe modules to Pyton path
            "PYTHONPATH": os.pathsep.join(
                [
                    str(pipe_path),
                ]
            ),
        }

        launch_command = ""
        if is_python_shell:
            launch_command = str(Executables.hython)
        else:
            launch_command = str(Executables.houdini)

        launch_args: list[str] = [] if is_python_shell else ["-foreground"]

        super().__init__(launch_command, launch_args, env_vars)
