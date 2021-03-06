import re

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def FilterWeatherData(df):
    df_filtered = df.copy()
    df_filtered = df_filtered[df_filtered.temperature.notnull()]
    return df_filtered

def AddPostalCode(df):
    logger.info("Add postal codes")
    df_with_postal_code = df.copy()
    df_with_postal_code['postal_code'] = df_with_postal_code.address.apply(lambda x: re.findall('\d{5}', x)[0])
    return df_with_postal_code


def FilterPostalCode(df, postal_code_list):
    logger.info("Filter postal codes")
    df_filtered = df.copy()
    df_filtered = df_filtered[df_filtered.postal_code.isin(postal_code_list)]
    return df_filtered


def FilterPreviousVariables(df):
    df_filtered = df.copy()
    df_filtered = df_filtered[df_filtered.available_bikes_previous.notnull()]
    return df_filtered


def SplitFeaturesTarget(df, target_column):
    target = df[target_column]
    features = df.drop(target_column, 1)
    return features, target

