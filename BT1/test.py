import geopandas as gpd
import folium
import matplotlib.pyplot as plt

df = gpd.read_file("CSL_HCMC/Data/GIS/Population/population_HCMC/population_shapefile/Population_Ward_Level.shp") 
print(df.head(10))
max_dict_name=df[df.Shape_Area>=max(df['Shape_Area'])]
print(max_dict_name['Com_Name'])