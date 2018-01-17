# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..registration import BSplineDeformableRegistration


def test_BSplineDeformableRegistration_inputs():
    input_map = dict(
        FixedImageFileName=dict(
            argstr='%s',
            position=-2,
        ),
        MovingImageFileName=dict(
            argstr='%s',
            position=-1,
        ),
        args=dict(argstr='%s', ),
        constrain=dict(argstr='--constrain ', ),
        default=dict(argstr='--default %d', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        gridSize=dict(argstr='--gridSize %d', ),
        histogrambins=dict(argstr='--histogrambins %d', ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        initialtransform=dict(argstr='--initialtransform %s', ),
        iterations=dict(argstr='--iterations %d', ),
        maximumDeformation=dict(argstr='--maximumDeformation %f', ),
        outputtransform=dict(
            argstr='--outputtransform %s',
            hash_files=False,
        ),
        outputwarp=dict(
            argstr='--outputwarp %s',
            hash_files=False,
        ),
        resampledmovingfilename=dict(
            argstr='--resampledmovingfilename %s',
            hash_files=False,
        ),
        spatialsamples=dict(argstr='--spatialsamples %d', ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
    )
    inputs = BSplineDeformableRegistration.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_BSplineDeformableRegistration_outputs():
    output_map = dict(
        outputtransform=dict(),
        outputwarp=dict(),
        resampledmovingfilename=dict(),
    )
    outputs = BSplineDeformableRegistration.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
