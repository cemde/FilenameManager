from filename_manager import Parameter, parameter


def test_attributes():
    par = Parameter("par1", "bool")
    assert par.name == "par1"
    assert par.format == "bool"


def test_float():
    par = Parameter("par", "fp2.3")
    p_e = par.encode(133.234113)
    assert p_e == "133.234", f"Encoded {p_e} != 133.234"
    p_e = par.encode(1)
    assert p_e == "01.000", f"Encoded {p_e} != 01.000"
    assert par.decode(par.encode(133.234113)) == 133.234
    assert par.decode(par.encode(1.0)) == 1.0

    par = Parameter("par", "fp1.1")
    p_e = par.encode(133.234113)
    assert p_e == "133.2", f"Encoded {p_e} != 133.2"
    p_e = par.encode(1)
    assert p_e == "1.0", f"Encoded {p_e} != 1.0"
    assert par.decode(par.encode(133.354113)) == 133.4
    assert par.decode(par.encode(1.0)) == 1.0

    par = Parameter("par", "fp2.3")
    par = par.decode("-00.900")
    assert par == -0.9


def test_int():
    par = Parameter("par", "int")
    assert par.encode(133) == "133"
    assert par.encode(-100) == "-100"

    assert par.decode("-100") == -100
    assert par.decode("133") == 133

    par = Parameter("par", "4int")
    assert par.encode(133) == "0133"
    assert par.encode(-1) == "-001"
    assert par.encode(123456) == "123456"

    assert par.decode("-0100") == -100
    assert par.decode("0133") == 133
    assert par.decode("123456") == 123456


def test_str():
    par = Parameter("par", "str")
    assert par.encode("Blub45") == "Blub45"
    assert par.decode("Blub45") == "Blub45"
    assert par.decode("45.3") == "45.3"

    par = Parameter("par", "8str")
    assert par.encode("Blub45") == "00Blub45"
    assert par.encode("Blub45Blub12") == "Blub45Blub12"
    assert par.decode("00Blub45") == "Blub45"
    assert par.decode("000045.3") == "45.3"
    assert par.decode("Blub45Blub12") == "Blub45Blub12"

    par = Parameter("par", "str8")
    assert par.encode("Blub45") == "Blub4500"
    assert par.encode("Blub45Blub12") == "Blub45Blub12"
    assert par.decode("Blub4500") == "Blub45"
    assert par.decode("45.30000") == "45.3"
    assert par.decode("Blub45Blub12") == "Blub45Blub12"


def test_bool():
    par = Parameter("par", "bool")
    assert par.encode(True) == "True"
    assert par.decode("True") == True
    assert par.encode(False) == "False"
    assert par.decode("False") == False
