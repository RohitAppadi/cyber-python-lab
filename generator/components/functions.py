"""
Cybersecurity function component registry.

Aggregates category-specific function registries into the
FUNCTION_COMPONENTS collection consumed by the program composer.
"""

from generator.categories.cryptography import CRYPTOGRAPHY_FUNCTIONS
from generator.categories.forensics import FORENSICS_FUNCTIONS
from generator.categories.network import NETWORK_FUNCTIONS
from generator.categories.system_security import SYSTEM_SECURITY_FUNCTIONS
from generator.categories.web_security import WEB_SECURITY_FUNCTIONS


FUNCTION_COMPONENTS = (
    NETWORK_FUNCTIONS
    + CRYPTOGRAPHY_FUNCTIONS
    + FORENSICS_FUNCTIONS
    + WEB_SECURITY_FUNCTIONS
    + SYSTEM_SECURITY_FUNCTIONS
)