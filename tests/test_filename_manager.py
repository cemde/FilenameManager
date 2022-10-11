#!/usr/bin/env python
"""Tests for `filename_manager` package."""

from filename_manager import FilenameManager, Parameter
import pytest


def get_pars():
    return [
        Parameter("s", "fp2.3"),
        Parameter("m", "8str"),
        Parameter("t_t_q", "str"),
        Parameter("k", "str10"),
        Parameter("p_q_0", "int"),
        Parameter("g", "4int"),
        Parameter("v", "fp1.1"),
        Parameter("b", "bool"),
    ]


def test_with_parameter_list():
    fm = FilenameManager(parameters=get_pars(), postfix='.csv')
    assert (
        fm.encode(s=2.345, m="abc", t_t_q="de", k="blob", p_q_0=54321, g=12, v=1.1, b=False)
        == 's_02.345_m_00000abc_t_t_q_de_k_blob000000_p_q_0_54321_g_0012_v_1.1_b_False.csv'
    )
    assert fm.decode('s_02.345_m_00000abc_t_t_q_de_k_blob000000_p_q_0_54321_g_0012_v_1.1_b_False.csv') == {
        "s": 2.345,
        "m": "abc",
        "t_t_q": "de",
        "k": "blob",
        "p_q_0": 54321,
        "g": 12,
        "v": 1.1,
        "b": False,
    }


def test_with_str_dict():
    fm = FilenameManager({"sigma": "fp2.3", "method": "str", "phi": "int", "v": "fp1.1"}, postfix='.csv')
    assert fm.encode(sigma=1.246, method="tata_ta", phi=15, v=1.0) == 'sigma_01.246_method_tata_ta_phi_15_v_1.0.csv'
    assert fm.decode('sigma_01.200_method_tata_ta_phi_5_v_1.3.csv') == {
        'sigma': 1.2,
        'method': 'tata_ta',
        'phi': 5,
        'v': 1.3,
    }


@pytest.mark.xfail
def test_encode_missing_parameter():
    pass


@pytest.mark.xfail
def test_encode_too_many_parameters():
    pass


def test_more_decoding():
    fm = FilenameManager(
        {'n_data': '6int', 'n_bins': '3int', 'conf': 'fp1.2', 'c': 'fp1.2', 'n_sim': '9int'},
        prefix='pkls/',
        postfix='.pickle',
    )
    filename = "pkls/n_data_000100_n_bins_001_conf_-0.50_c_0.40_n_sim_001000000.pickle"
    pars = fm.decode(filename)
    assert pars["conf"] == -0.5
