# fao_pastureland

create maps for the study of pasturelands in LMIC

## Data
- FAO's 2000 pasture occurrence map shared by Yelena
- LMIC countries in the FAO GAUL description
- TNC [terrestrial ecoregions](http://maps.tnc.org/gis_data.html) through the [WWF 14 biomes](https://www.worldwildlife.org/biome-categories/terrestrial-ecoregions)
- [ESA’s CCI-LC maps](https://climate.esa.int/en/projects/land-cover/data/#cci-lc-user-tool) for the years 2000 and 2015 

## output 
- pasture_masked.tif : The pasture fraction masked to LMICs
- wwf_biomes_masked.tif : The biome rasterized on the pasture_masked raster
- LCCS-[year]-[zone_index]-masked.tif: on the pasture_masked extent and crs, represent the cell's fraction in the [zone_index] ecozone for the [year] considered. 0% pixels are all masked.

## usage 

on an instance >= `m4`, pull the repository in your sepal environment:
```
git clone https://github.com/12rambau/fao_pastureland.git
```

Then add the data folder that I send you in the `fao_pastureland` folder

launch the `pastureland.ipynb` notebook and run all cells

The full process takes **4h** 

You could also consider using the pastureland.py file by runing :

```
cd ~
nohup python3 fao_pastureland/pasureland.py &
```
:warning this file has 0 printing output and give no insight to the user, but at least now you can close SEPAL and have a kitkat.


