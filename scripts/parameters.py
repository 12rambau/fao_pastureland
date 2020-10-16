import os
from pathlib import Path
import pandas as pd 

#######################
##      folders      ##
#######################
def get_result_dir():
    folder = Path(Path.home(), 'fao_pastureland_results')
    folder.mkdir(parents=True, exist_ok=True)
    return str(folder)

def get_tmp_dir():
    folder = Path(Path.home(), 'fao_pastureland_results','tmp')
    folder.mkdir(parents=True, exist_ok=True)
    return str(folder)

def get_data_dir():
    folder = os.path.join(os.path.dirname(__file__), '..', 'data')
    return folder

#####################
##    variables    ##
#####################
ecozones = {
    100: 'Mosaic tree and shrub (>50%) / herbaceous cover (<50%)',
    110: 'Mosaic herbaceous cover (>50%) / tree and shrub (<50%)',
    120: 'Shrubland',
    130: 'Grassland',
    150: 'Sparse vegetation (tree, shrub, herbaceous cover) (<15%)'
}
    
#####################
##   tmp file      ##
#####################
wwf_biomes = os.path.join(get_tmp_dir(), 'wwf_biomes.tif') 
llc_2000_map = os.path.join(get_tmp_dir(), 'LCCS-2000-{}.tif')

#####################
##   output file   ##
#####################
pasture_masked = os.path.join(get_result_dir(), 'pasture_masked.tif')
biomes_masked = os.path.join(get_result_dir(), 'wwf_biomes_masked.tif')
llc_2000_map_masked = os.path.join(get_result_dir(), 'LCCS-2000-{}_masked.tif')

#####################
##   input file    ##
#####################
pastureLand_raster = os.path.join(get_data_dir(),  'pasture.tif')
tnc_ecozone_shp = os.path.join(get_data_dir(), 'wwf',  'wwf_terr_ecos.shp')
llc_2000_raster = os.path.join(get_data_dir(), 'ESACCI-LC-L4-LCCS-Map-300m-P1Y-2000-v2.0.7.tif')

####################
##  dataframes    ##
####################
country_list = pd.read_csv(os.path.join(os.path.dirname(__file__), '..', 'data',  'countries.csv'), sep=',')