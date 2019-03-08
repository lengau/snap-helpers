from typing import (
    Mapping,
    Optional,
)

from ._conf import SnapConfig
from ._ctl import SnapCtl
from ._env import SnapEnviron
from ._path import SnapPaths


class EnvironProperty:
    """Wrapper to get properties from a :class:`SanpEnviron` instance."""

    def __init__(self, name: str):
        self.name = name

    def __get__(self, instance, owner):
        return getattr(instance.environ, self.name)


class Snap:
    """Top-level wrapper for a Snap."""

    config: SnapConfig
    ctl: SnapCtl
    environ: SnapEnviron
    paths: SnapPaths

    def __init__(self, environ: Optional[Mapping[str, str]] = None):
        self.ctl = SnapCtl(environ=environ)
        self.config = SnapConfig(snapctl=self.ctl)
        self.environ = SnapEnviron(environ=environ)
        self.paths = SnapPaths(environ=environ)

    name = EnvironProperty('NAME')
    instance_name = EnvironProperty('INSTANCE_NAME')
    version = EnvironProperty('VERSION')
    revision = EnvironProperty('REVISION')
