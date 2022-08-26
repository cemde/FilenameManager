#!/usr/bin/env python
"""Tests for `filename_manager` package."""

import pytest


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    del response


# fm = FileNameManager(parameters=[s,m,t,k,p,g,v,b], postfix='.csv')
# print(fm.decode(f's_02.345_m_00000abc_t_de_k_blob000000_p_54321_g_0012_v_1.1_b_False.csv'))
# print(fm.encode(s=2.345, m="abc", t="de", k="blob", p=54321, g=12, v=1.1, b=False))


# fm = FileNameManager({"sigma": "fp2.3", "method": "str", "phi": "int", "v": "fp1.1"}, postfix='.csv')
# print(fm.pattern)
# print(fm.encode(sigma=1.246, method="tata_ta", phi=15, v=1.0))
# print(fm.decode(f'sigma_01.200_method_tata_ta_phi_5_v_1.3.csv'))
