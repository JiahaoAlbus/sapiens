# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from .base import BaseTransform
from .builder import TRANSFORMS
from .loading import LoadAnnotations, LoadImageFromFile
from .processing import (CenterCrop, MultiScaleFlipAug, Normalize, Pad,
                         RandomChoiceResize, RandomFlip, RandomGrayscale,
                         RandomResize, Resize, TestTimeAug)
from .wrappers import (Compose, KeyMapper, RandomApply, RandomChoice,
                       TransformBroadcaster)

try:
    import torch  # noqa: F401
except ImportError:
    __all__ = [
        'BaseTransform', 'TRANSFORMS', 'TransformBroadcaster', 'Compose',
        'RandomChoice', 'KeyMapper', 'LoadImageFromFile', 'LoadAnnotations',
        'Normalize', 'Resize', 'Pad', 'RandomFlip', 'RandomChoiceResize',
        'CenterCrop', 'RandomGrayscale', 'MultiScaleFlipAug', 'RandomResize',
        'RandomApply', 'TestTimeAug'
    ]
else:
    from .formatting import ImageToTensor, ToTensor, to_tensor

    __all__ = [
        'BaseTransform', 'TRANSFORMS', 'TransformBroadcaster', 'Compose',
        'RandomChoice', 'KeyMapper', 'LoadImageFromFile', 'LoadAnnotations',
        'Normalize', 'Resize', 'Pad', 'ToTensor', 'to_tensor', 'ImageToTensor',
        'RandomFlip', 'RandomChoiceResize', 'CenterCrop', 'RandomGrayscale',
        'MultiScaleFlipAug', 'RandomResize', 'RandomApply', 'TestTimeAug'
    ]