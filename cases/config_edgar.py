from emiproc.grids import COSMOGrid, EDGARGrid, ICONGrid
import os
import time

# inventory
inventory = 'EDGAR'

# model either "cosmo-art", "cosmo-ghg" or "icon" (affects the
# output units and handling of the output grid)
model = 'cosmo-ghg'

# path to input inventory
input_path = "/input/EDGAR/v432_FT_CHE/"

# Year of the inventory (required for finding the inventory files)
input_year = 2015

# input grid
input_grid = EDGARGrid(
    xmin=-130,
    xmax=65,
    ymin=15,
    ymax=80,
    dx=0.1,
    dy=0.1,
)

# input species
species = ["CO2"]

# input categories
categories = [
    "AGS",
    "CHE",
    "ENE",
    "FFF",
    "IND",
    "IRO",
    "NEU",
    "NFE",
    "NMM",
    "PRO",
    "PRU_SOL",
    "RCO",
    "REF_TRF",
    "SWD_INC",
    "TNR_Aviation_CDS",
    "TNR_Aviation_CRS",
    "TNR_Aviation_LTO",
    "TNR_Other",
    "TNR_Ship",
    "TRO",
]

# mapping from input to output species (input is used for missing keys)
in2out_species = {}

# mapping from input to output species (input is used for missing keys)
# All the categories will be summed. 
# There is no mapping between these catgories and GNFR yet
in2out_category = {}

# output variables are written in the following format using species
varname_format = '{species}_EDGAR'

# Domain
# CHE_Europe domain
cosmo_grid = COSMOGrid(
    nx=321,
    ny=121,
    dx=0.5,
    dy=0.5,
    xmin=-99.75,
    ymin=15.25,
    pollon=180,
    pollat=90,
)

# output path and filename
output_path = os.path.join('outputs', 'EDGAR','{online}')
output_name = "edgar.nc"


# resolution of shape file used for country mask
shpfile_resolution = "10m"

# number of processes computing the mapping inventory->COSMO-grid
nprocs = 18

# metadata added as global attributes to netCDF output file
nc_metadata = {
    "DESCRIPTION": "Gridded annual emissions",
    "DATAORIGIN": "TNO",
    "CREATOR": "Jean-Matthieu Haussaire",
    "EMAIL": "jean-matthieu.haussaire@empa.ch",
    "AFFILIATION": "Empa Duebendorf, Switzerland",
    "DATE CREATED": time.ctime(time.time()),
}
