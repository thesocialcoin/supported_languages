from typing import Dict, List

from supported_languages.constants import COUNTRIES
from supported_languages.languages import get_supported_languages as get_supported_langs


def get_available_countries() -> List[str]:
    """
    Get available countries.

    Returns:
        List[str]: List of countries in ISO 3166 alpha-2 format
    """
    languages = get_supported_langs()
    return [k for k, v in COUNTRIES.items() if any(lang in languages for lang in v["languages"])]


def get_countries() -> List[str]:
    """
    Get all countries.

    Returns:
        List[str]: List of countries in ISO 3166 alpha-2 format
    """
    return COUNTRIES.keys()


def get_country(country_code: str) -> Dict:
    """
    Get information of a country.

    Args:
        country_code (str): Country code in ISO 3166 alpha-2 format

    Returns:
        Dict: Country's information
    """
    return COUNTRIES.get(country_code, {})


def get_languages(country_code: str) -> List[str]:
    """
    Get all languages from a country.

    Args:
        country_code (str): Country code in ISO 3166 alpha-2 format

    Returns:
        List[str]: List of languages in ISO 639-1 alpha-2 format
    """
    return COUNTRIES.get(country_code, {})["languages"]


def get_supported_languages(country_code: str) -> List[str]:
    """
    Get supported languages from a country.

    Args:
        country_code (str): Country code in ISO 3166 alpha-2 format

    Returns:
        List[str]: List of supported languages in ISO 639-1 alpha-2 format
    """
    languages = get_supported_langs()
    return [lang for lang in get_languages(country_code) if lang in languages]
