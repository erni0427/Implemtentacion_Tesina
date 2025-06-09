
# Este módulo define las estructuras de parámetros del modelo digestivo en cerdos
# siguiendo literalmente el artículo de Strathe et al. (2008).
# Cada grupo de parámetros está organizado según el compartimento digestivo correspondiente.

from dataclasses import dataclass

# -------------------------------------------------------
# ESTÓMAGO (STO) – parámetros de vaciado y alimentación
# -------------------------------------------------------
@dataclass
class StomachParams:
    TFEED: float       # Duración de la fase de ingestión (h)
    FFEED: float       # Frecuencia de alimentación (eventos/día)
    DMI: float         # Ingesta total de materia seca (kg/día)
    CSTO_pa: float     # Tasa de vaciado gástrico (1/h)
    CSTO_EP_sc: float  # Secreción endógena de proteína por OM ingerida (mol N/kg OM)
    CSTO_NAPN_sc: float  # Secreción de nitrógeno no proteico endógeno (mol N/kg OM)

stomach_params = StomachParams(
    TFEED=0.25,
    FFEED=3.0,
    DMI=1.5,
    CSTO_pa=0.231,
    CSTO_EP_sc=0.013,
    CSTO_NAPN_sc=0.013
)

# -------------------------------------------------------
# INTESTINO DELGADO PROXIMAL (SI1)
# -------------------------------------------------------
@dataclass
class SI1Params:
    CSI1_pa: float           # Tasa de pasaje a SI2 (1/h)
    CSI1_EPp_sc: float       # Secreción de proteína pancreática (mol N/kg OM)
    CSI1_NAPNp_sc: float     # Secreción de N no proteico pancreático (mol N/kg OM)
    CSI1_EPb_sc: float       # Secreción de proteína biliar (mol N/kg DMI)
    CSI1_NAPNb_sc: float     # Secreción de N no proteico biliar (mol N/kg DMI)
    CSI1_LD_sc: float        # Secreción de lípidos endógenos (mol C/kg DMI)

    CSI1_DP_hyv: float       # Vmáx hidrólisis proteína dietaria (mol N/h)
    CSI1_EP_hyv: float       # Vmáx hidrólisis proteína endógena (mol N/h)
    CSI1_NAPN_hyv: float     # Vmáx hidrólisis N no proteico (mol N/h)
    CSI1_ST_hyv: float       # Vmáx hidrólisis almidón (mol C/h)
    CSI1_LD_hyv: float       # Vmáx hidrólisis lípidos (mol C/h)

    CSI1_DP_hyk: float       # Constante MM hidrólisis proteína dietaria (mol N)
    CSI1_EP_hyk: float       # Constante MM hidrólisis proteína endógena (mol N)
    CSI1_NAPN_hyk: float     # Constante MM hidrólisis NAPN (mol N)
    CSI1_ST_hyk: float       # Constante MM hidrólisis almidón (mol C)
    CSI1_LD_hyk: float       # Constante MM hidrólisis lípidos (mol C)

    CSI1_SU_abv: float       # Vmáx absorción de azúcares (mol C/h)
    CSI1_FA_abv: float       # Vmáx absorción de ácidos grasos (mol C/h)
    CSI1_AA_abv: float       # Vmáx absorción de aminoácidos (mol N/h)

    CSI1_SU_abk: float       # Constante absorción de azúcares (mol C)
    CSI1_FA_abk: float       # Constante absorción de ácidos grasos (mol C)
    CSI1_AA_abk: float       # Constante absorción de aminoácidos (mol N)

si1_params = SI1Params(
    CSI1_pa=1.670,
    CSI1_EPp_sc=0.070,
    CSI1_NAPNp_sc=0.030,
    CSI1_EPb_sc=0.077,
    CSI1_NAPNb_sc=0.042,
    CSI1_LD_sc=1.25,
    CSI1_DP_hyv=0.40,
    CSI1_EP_hyv=0.10,
    CSI1_NAPN_hyv=0.10,
    CSI1_ST_hyv=4.00,
    CSI1_LD_hyv=2.50,
    CSI1_DP_hyk=0.50,
    CSI1_EP_hyk=0.50,
    CSI1_NAPN_hyk=0.50,
    CSI1_ST_hyk=1.20,
    CSI1_LD_hyk=0.28,
    CSI1_SU_abv=3.92,
    CSI1_FA_abv=2.40,
    CSI1_AA_abv=0.75,
    CSI1_SU_abk=0.05,
    CSI1_FA_abk=0.25,
    CSI1_AA_abk=0.06
)

# -------------------------------------------------------
# INTESTINO DELGADO DISTAL (SI2)
# -------------------------------------------------------
@dataclass
class SI2Params:
    CSI2_pa: float
    CSI2_EP_sc: float
    CSI2_NAPN_sc: float

    CSI2_DP_hyv: float
    CSI2_EP_hyv: float
    CSI2_NAPN_hyv: float
    CSI2_ST_hyv: float
    CSI2_LD_hyv: float

    CSI2_DP_hyk: float
    CSI2_EP_hyk: float
    CSI2_NAPN_hyk: float
    CSI2_ST_hyk: float
    CSI2_LD_hyk: float

    CSI2_SU_abv: float
    CSI2_FA_abv: float
    CSI2_AA_abv: float

    CSI2_SU_abk: float
    CSI2_FA_abk: float
    CSI2_AA_abk: float

si2_params = SI2Params(
    CSI2_pa=0.294,
    CSI2_EP_sc=0.37,
    CSI2_NAPN_sc=0.246,
    CSI2_DP_hyv=0.38,
    CSI2_EP_hyv=0.15,
    CSI2_NAPN_hyv=0.16,
    CSI2_ST_hyv=5.40,
    CSI2_LD_hyv=1.70,
    CSI2_DP_hyk=0.50,
    CSI2_EP_hyk=0.18,
    CSI2_NAPN_hyk=0.40,
    CSI2_ST_hyk=2.00,
    CSI2_LD_hyk=2.50,
    CSI2_SU_abv=3.92,
    CSI2_FA_abv=2.40,
    CSI2_AA_abv=0.75,
    CSI2_SU_abk=0.05,
    CSI2_FA_abk=0.25,
    CSI2_AA_abk=0.06
)

# -------------------------------------------------------
# INTESTINO GRUESO (LI)
# -------------------------------------------------------
@dataclass
class LIParams:
    CLI_pa_0: float        # Tasa base de pasaje del contenido del LI (1/h)
    CLI_OM_0: float        # Referencia para nivel de OM en pasaje (kg OM)
    CLI_pa_kn: float       # Exponente no lineal del pasaje

    CLI_EP_sc: float       # Secreción endógena de proteína (mol N/kg OM)
    CLI_NAPN_sc: float     # Secreción endógena de NAPN (mol N/kg OM)

    CLI_DP_hyv: float      # Vmáx hidrólisis proteína dietaria (mol N/h)
    CLI_EP_hyv: float      # Vmáx hidrólisis de proteína endógena (mol N/h)
    CLI_NAPN_hyv: float    # Vmáx hidrólisis de NAPN (mol N/h)
    CLI_ST_hyv: float      # Vmáx hidrólisis de almidón (mol C/h)
    CLI_DDF_hyv: float     # Vmáx hidrólisis de fibra (mol C/h)
    CLI_LD_hyv: float      # Vmáx hidrólisis de lípidos (mol C/h)

    CLI_DP_hyk: float
    CLI_EP_hyk: float
    CLI_NAPN_hyk: float
    CLI_ST_hyk: float
    CLI_DDF_hyk: float
    CLI_LD_hyk: float

li_params = LIParams(
    CLI_pa_0=0.033,
    CLI_OM_0=0.250,
    CLI_pa_kn=1.0,
    CLI_EP_sc=0.15,
    CLI_NAPN_sc=0.15,
    CLI_DP_hyv=0.08,
    CLI_EP_hyv=0.0155,
    CLI_NAPN_hyv=0.0155,
    CLI_ST_hyv=1.20,
    CLI_DDF_hyv=0.0155,
    CLI_LD_hyv=0.01,
    CLI_DP_hyk=0.50,
    CLI_EP_hyk=0.50,
    CLI_NAPN_hyk=0.50,
    CLI_ST_hyk=0.50,
    CLI_DDF_hyk=0.50,
    CLI_LD_hyk=1.0
)

# -------------------------------------------------------
# PARÁMETROS MICROBIANOS
# -------------------------------------------------------
@dataclass
class MicrobialParams:
    CMM: float           # Eficiencia de crecimiento microbiano (kg MM/kg OM)
    CMM_P: float         # Contenido de proteína microbiana (mol N/kg MM)
    CMM_CHO: float       # Contenido de CHO microbianos (mol C/kg MM)
    CMM_LD: float        # Contenido de lípidos microbianos (mol C/kg MM)
    CMM_ACET_fr: float   # Fracción C a acetato
    CMM_PROP_fr: float   # Fracción C a propionato
    CMM_BUT_fr: float    # Fracción C a butirato
    CMM_CO2_fr: float    # Fracción C a CO₂
    CMM_CH4_fr: float    # Fracción C a CH₄

microbial_params = MicrobialParams(
    CMM=0.145,
    CMM_P=6.70,
    CMM_CHO=10.67,
    CMM_LD=7.80,
    CMM_ACET_fr=0.447,
    CMM_PROP_fr=0.225,
    CMM_BUT_fr=0.073,
    CMM_CO2_fr=0.153,
    CMM_CH4_fr=0.102
)
