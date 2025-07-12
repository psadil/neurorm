import typing
from enum import Enum
from pathlib import Path

import pydantic
from pydantic import BaseModel, Field


class Hemisphere(Enum):
    LEFT = "lh"
    RIGHT = "rh"


class TransformFiles(BaseModel):
    """Transform files in mri/transforms"""

    talairach_lta: pydantic.FilePath = Field(..., description="Talairach transform")
    talairach_xfm: pydantic.FilePath = Field(
        ..., description="Talairach transform (FSL format)"
    )
    talairach_m3z: pydantic.FilePath = Field(
        ..., description="Talairach transform (compressed)"
    )
    talairach_auto_xfm: pydantic.FilePath = Field(
        ..., description="Automatic Talairach transform"
    )
    cc_up_lta: pydantic.FilePath = Field(..., description="Corpus callosum transform")

    @classmethod
    def from_path(cls, transforms_path) -> typing.Self:
        return cls(
            talairach_lta=transforms_path / "talairach.lta",
            talairach_xfm=transforms_path / "talairach.xfm",
            talairach_m3z=transforms_path / "talairach.m3z",
            talairach_auto_xfm=transforms_path / "talairach.auto.xfm",
            cc_up_lta=transforms_path / "cc_up.lta",
        )


class MRIFiles(BaseModel):
    """MRI volume files in the mri directory"""

    aparc_aseg: pydantic.FilePath = Field(
        ..., description="Parcellation + subcortical segmentation"
    )
    aparc_a2009s_aseg: pydantic.FilePath = Field(
        ..., description="Destrieux atlas parcellation + subcortical"
    )
    aseg: pydantic.FilePath = Field(..., description="Subcortical segmentation")
    brain: pydantic.FilePath = Field(..., description="Brain-extracted volume")
    brainmask: pydantic.FilePath = Field(..., description="Brain mask")
    filled: pydantic.FilePath = Field(..., description="Filled volume")
    norm: pydantic.FilePath = Field(..., description="Normalized volume")
    nu: pydantic.FilePath = Field(..., description="Non-uniformity corrected volume")
    orig: pydantic.FilePath = Field(..., description="Original input volume")
    orig_nu: pydantic.FilePath = Field(
        ..., description="Non-uniformity corrected original"
    )
    rawavg: pydantic.FilePath = Field(..., description="Raw average volume")
    ribbon: pydantic.FilePath
    T1: pydantic.FilePath = Field(..., description="T1-weighted volume")
    transforms: TransformFiles
    wm: pydantic.FilePath = Field(..., description="White matter volume")
    wmparc: pydantic.FilePath = Field(..., description="White matter parcellation")

    @classmethod
    def from_path(cls, path: Path) -> typing.Self:
        return cls(
            orig=path / "orig.mgz",
            rawavg=path / "rawavg.mgz",
            T1=path / "T1.mgz",
            brain=path / "brain.mgz",
            brainmask=path / "brainmask.mgz",
            filled=path / "filled.mgz",
            wm=path / "wm.mgz",
            aseg=path / "aseg.mgz",
            norm=path / "norm.mgz",
            orig_nu=path / "orig_nu.mgz",
            nu=path / "nu.mgz",
            aparc_aseg=path / "aparc+aseg.mgz",
            aparc_a2009s_aseg=path / "aparc.a2009s+aseg.mgz",
            wmparc=path / "wmparc.mgz",
            transforms=TransformFiles.from_path(path / "transforms"),
            ribbon=path / "ribbon.mgz",
        )


class SurfaceFiles(BaseModel):
    """Surface files for a hemisphere"""

    orig: pydantic.FilePath = Field(..., description="Original surface")
    smoothwm: pydantic.FilePath = Field(
        ..., description="Smoothed white matter surface"
    )
    inflated: pydantic.FilePath = Field(..., description="Inflated surface")
    sphere: pydantic.FilePath = Field(..., description="Spherical surface")
    sphere_reg: pydantic.FilePath = Field(
        ..., description="Registered spherical surface"
    )
    white: pydantic.FilePath = Field(..., description="White matter surface")
    pial: pydantic.FilePath = Field(..., description="Pial surface")
    curv: pydantic.FilePath = Field(..., description="Curvature file")
    sulc: pydantic.FilePath = Field(..., description="Sulcal depth")
    area: pydantic.FilePath = Field(..., description="Surface area")
    volume: pydantic.FilePath = Field(..., description="Volume file")
    thickness: pydantic.FilePath = Field(..., description="Cortical thickness")
    w_g_pct_mgh: pydantic.FilePath = Field(..., description="White/gray contrast")
    jacobian_white: pydantic.FilePath = Field(
        ..., description="Jacobian on white surface"
    )

    @classmethod
    def from_path(cls, surf_path: Path, hemi: Hemisphere) -> typing.Self:
        return cls(
            orig=surf_path / f"{hemi.value}.orig",
            smoothwm=surf_path / f"{hemi.value}.smoothwm",
            inflated=surf_path / f"{hemi.value}.inflated",
            sphere=surf_path / f"{hemi.value}.sphere",
            sphere_reg=surf_path / f"{hemi.value}.sphere.reg",
            white=surf_path / f"{hemi.value}.white",
            pial=surf_path / f"{hemi.value}.pial",
            curv=surf_path / f"{hemi.value}.curv",
            sulc=surf_path / f"{hemi.value}.sulc",
            area=surf_path / f"{hemi.value}.area",
            volume=surf_path / f"{hemi.value}.volume",
            thickness=surf_path / f"{hemi.value}.thickness",
            w_g_pct_mgh=surf_path / f"{hemi.value}.w-g.pct.mgh",
            jacobian_white=surf_path / f"{hemi.value}.jacobian_white",
        )


class LabelFiles(BaseModel):
    aparc_annot: pydantic.FilePath = Field(
        ..., description="Desikan-Killiany parcellation"
    )
    aparc_a2009s_annot: pydantic.FilePath = Field(
        ..., description="Destrieux parcellation"
    )
    aparc_DKTatlas_annot: pydantic.FilePath = Field(..., description="DKT parcellation")
    BA_exvivo_annot: pydantic.FilePath = Field(..., description="Brodmann areas")
    BA_exvivo_thresh_annot: pydantic.FilePath = Field(
        ..., description="Thresholded Brodmann areas"
    )

    @classmethod
    def from_path(cls, surf_path: Path, hemi: Hemisphere) -> typing.Self:
        return cls(
            aparc_annot=surf_path / f"{hemi.value}.aparc.annot",
            aparc_a2009s_annot=surf_path / f"{hemi.value}.aparc.a2009s.annot",
            aparc_DKTatlas_annot=surf_path / f"{hemi.value}.aparc.DKTatlas.annot",
            BA_exvivo_annot=surf_path / f"{hemi.value}.BA_exvivo.annot",
            BA_exvivo_thresh_annot=surf_path / f"{hemi.value}.BA_exvivo.thresh.annot",
        )


class StatsFiles(BaseModel):
    """Statistics files"""

    aseg_stats: pydantic.FilePath = Field(
        ..., description="Subcortical segmentation statistics"
    )
    lh_aparc_stats: pydantic.FilePath = Field(
        ..., description="Left hemisphere parcellation statistics"
    )
    rh_aparc_stats: pydantic.FilePath = Field(
        ..., description="Right hemisphere parcellation statistics"
    )
    lh_aparc_a2009s_stats: pydantic.FilePath = Field(
        ..., description="Left hemisphere Destrieux statistics"
    )
    rh_aparc_a2009s_stats: pydantic.FilePath = Field(
        ..., description="Right hemisphere Destrieux statistics"
    )
    lh_aparc_DKTatlas_stats: pydantic.FilePath = Field(
        ..., description="Left hemisphere DKT statistics"
    )
    rh_aparc_DKTatlas_stats: pydantic.FilePath = Field(
        ..., description="Right hemisphere DKT statistics"
    )
    lh_curv_stats: pydantic.FilePath = Field(
        ..., description="Left hemisphere curvature statistics"
    )
    rh_curv_stats: pydantic.FilePath = Field(
        ..., description="Right hemisphere curvature statistics"
    )
    lh_w_g_pct_stats: pydantic.FilePath = Field(
        ..., description="Left hemisphere white/gray contrast statistics"
    )
    rh_w_g_pct_stats: pydantic.FilePath = Field(
        ..., description="Right hemisphere white/gray contrast statistics"
    )
    wmparc_stats: pydantic.FilePath = Field(
        ..., description="White matter parcellation statistics"
    )

    @classmethod
    def from_path(cls, stats_path: Path) -> typing.Self:
        return cls(
            aseg_stats=stats_path / "aseg.stats",
            lh_aparc_stats=stats_path / "lh.aparc.stats",
            rh_aparc_stats=stats_path / "rh.aparc.stats",
            lh_aparc_a2009s_stats=stats_path / "lh.aparc.a2009s.stats",
            rh_aparc_a2009s_stats=stats_path / "rh.aparc.a2009s.stats",
            lh_aparc_DKTatlas_stats=stats_path / "lh.aparc.DKTatlas.stats",
            rh_aparc_DKTatlas_stats=stats_path / "rh.aparc.DKTatlas.stats",
            lh_curv_stats=stats_path / "lh.curv.stats",
            rh_curv_stats=stats_path / "rh.curv.stats",
            lh_w_g_pct_stats=stats_path / "lh.w-g.pct.stats",
            rh_w_g_pct_stats=stats_path / "rh.w-g.pct.stats",
            wmparc_stats=stats_path / "wmparc.stats",
        )


class ScriptFiles(BaseModel):
    """Log and script files"""

    recon_all_log: pydantic.FilePath = Field(..., description="Main recon-all log file")
    recon_all_status: pydantic.FilePath = Field(
        ..., description="Processing status file"
    )
    build_log: pydantic.FilePath = Field(..., description="Build log")

    @classmethod
    def from_path(cls, scripts_path: Path) -> typing.Self:
        return cls(
            recon_all_log=scripts_path / "recon-all.log",
            recon_all_status=scripts_path / "recon-all.done",
            build_log=scripts_path / "build-stamp.txt",
        )


class FreeSurferSubject(BaseModel):
    """Complete FreeSurfer subject directory structure"""

    subject_id: str = Field(..., description="Subject identifier")
    subject_path: pydantic.DirectoryPath = Field(..., description="Subject Folder")

    # MRI volumes
    mri: MRIFiles

    # Hemisphere data
    left_hemisphere: SurfaceFiles
    right_hemisphere: SurfaceFiles

    # Statistics
    stats: StatsFiles

    # Log files
    scripts: ScriptFiles

    # parcellation files
    left_label: LabelFiles
    right_label: LabelFiles

    @property
    def recon_all_done(self) -> bool:
        return (self.subject_path / "script" / "recon-all.done").exists()

    @classmethod
    def from_subjects_dir(cls, subjects_dir: Path, subject_id: str) -> typing.Self:
        """Create a FreeSurferSubject instance by scanning a subjects directory"""
        subject_path = subjects_dir / subject_id

        if not subject_path.exists():
            raise ValueError(f"Subject directory does not exist: {subject_path}")

        return cls(
            subject_id=subject_id,
            subject_path=subject_path,
            mri=MRIFiles.from_path(subject_path / "mri"),
            left_hemisphere=SurfaceFiles.from_path(
                subject_path / "surf", Hemisphere.LEFT
            ),
            right_hemisphere=SurfaceFiles.from_path(
                subject_path / "surf", Hemisphere.RIGHT
            ),
            stats=StatsFiles.from_path(subject_path / "stats"),
            scripts=ScriptFiles.from_path(subject_path / "scripts"),
            left_label=LabelFiles.from_path(subject_path / "label", Hemisphere.LEFT),
            right_label=LabelFiles.from_path(subject_path / "label", Hemisphere.RIGHT),
        )
