
#%%
import os
import calendar
import datacube
from odc.apps.dc_tools.stac_api_to_dc import stac_api_to_odc
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
#%%
bbox = [20.6455928891, 59.846373196, 31.5160921567, 70.1641930203]
STAC_API_URL = 'https://earth-search.aws.element84.com/v0/'
dc = datacube.Datacube()
#%%
for year in [2017]:
    for month in range(1,13):
        start_date = f'{year}-{month:02}-01'
        end_date = f'{year}-{month:02}-{calendar.monthrange(year, month)[1]}'

        collections = ['sentinel-s2-l2a-cogs']

        config = {
            'url': STAC_API_URL,
            'collections': collections,
            'bbox': bbox,
            'datetime': f"{start_date}/{end_date}"
        }

        #    dc: Datacube,    products: list,    limit: int,    update: bool,    allow_unsafe: bool,    config: dict,
        indexed, failed = stac_api_to_odc(dc, 's2_l2a', 10000, False, False, config)
        print(f"Indexed {indexed} items with {failed} failures.")