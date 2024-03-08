"""
Calsh of Clans API - ClansFilter models
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class ClansFilter:
    name: Optional[str] = None
    warFrequency: Optional[str] = None
    locationId: Optional[int] = None
    minMembers: Optional[int] = None
    maxMembers: Optional[int] = None
    minClanPoints: Optional[int] = None
    maxClanLevel: Optional[int] = None
    limit: Optional[int] = None
    after: Optional[str] = None
    before: Optional[str] = None
    labelIds: Optional[str] = None
