from __future__ import annotations

import os
import typing
from dataclasses import dataclass
from warnings import warn

import cv2
import numpy as np
from pyzbar.pyzbar import Decoded, ZBarSymbol
from pyzbar.pyzbar import decode as decodeQR
