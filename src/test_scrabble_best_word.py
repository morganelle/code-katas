"""

Below are the tests from CodeWars.

Test.assert_equals(get_best_word(points, ["WHO","IS","THE","BEST","OF","US"]), 0)
Test.assert_equals(get_best_word(points, ["AABCDEF", "WHO","IS","THE","BEST","OF","US"]), 1)
Test.assert_equals(get_best_word(points, ["NOQ","TXAY","S","OM","ESFT","CJUKQ","QL","QO","ASTK","Y"]), 5)
Test.assert_equals(get_best_word(points, ["N","AO","TQGZW","P","OBTP","CLWXB","Y","JQGFJ","Q","RP","OC","MRQCZ","ZWN","ZRT","OIRYH","GWPMSZP","LQRYUKQ","LBM","LFEI","VHUX","RTALLIC","JEMUPS","XUW","X","ZLXFMWS","LFAGR","HJ","RTUAI","JRBNG","ZUYSC","CIEYV","FUY","B","EJS","CINBTQS","JEAC","JX","LLILSEK","W","KLUV"]), 16)
Test.assert_equals(get_best_word(points, ["SVWLIDP","FCPKTHW","EREMN","NFEF","PQ","FSC","ZYPOSXJ","BOR","YCGG","RC","DVPE","VAOE","OIGK","OTQE","REJFUFD","FVBCSSB","VHJ","BEC","MWZQ","WX","L","ZPCB","JKLHE","RYFTY","NKP","ID","O","KA","VRXX","NTDB","OERKPC","YFLUI","SKQCJ","PXDSW","ITYWD","TC","LOIDQEJ","NE","YND","VJHOCEC","RPRANZ","BQ","STM","RGVBFW","SMWUYLW","KT","SXHY","XCE","T","SC","UDJU","CHDR","UGXNQ","CQOOBA","O","NWW","V","L","BAQ","AZN","LBTR","N","QSURR","KADPH","M","LCBEAKM","ZHEVXS","F","TVAIQCY","MF","KCI","YQ","RCG","AKYPCP","WJXG","RQXOI","SJI","TWXZ","J","HIKCGHV","EAAXGG","AETSH","EO","BUET","TDIQCO","TKL","FJCRY","ZHAJLK","OLMCVA","F"]), 6)
Test.assert_equals(get_best_word(points, ["RBBL","ZJ","ZOFXE","LMBFCFX","O","JG","SYRYE","VXG","EU","DAIFZR","BQUNZHH","WKO","TFPHPLX","SWLG","CY","JYQNDSM","ITPS","B","UVSDMWR","LCPS"]), 15)
Test.assert_equals(get_best_word(points, ['LGVMJDW', 'HSPASA', 'CFHMVZNGH', 'ESKSKB', 'JDO', 'BQJUECZ', 'BB', 'IVVLXBC', 'ZRENSWMG']), 5)


"""
import pytest

POINTS = (1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 10, 1, 2, 1, 1, 3, 8, 1, 1, 1, 1, 4, 10, 10, 10, 10)


SCRABBLE_TEST = [
    (POINTS, ["WHO", "IS", "THE", "BEST", "OF", "US"], 0),
    (POINTS, ["AABCDEF", "WHO", "IS", "THE", "BEST", "OF", "US"], 1),
    (POINTS, ["NOQ", "TXAY", "S", "OM", "ESFT", "CJUKQ", "QL", "QO", "ASTK", "Y"], 5),
    (POINTS, ["N", "AO", "TQGZW", "P", "OBTP", "CLWXB", "Y", "JQGFJ", "Q", "RP", "OC", "MRQCZ", "ZWN", "ZRT", "OIRYH", "GWPMSZP", "LQRYUKQ", "LBM", "LFEI", "VHUX", "RTALLIC", "JEMUPS", "XUW", "X", "ZLXFMWS", "LFAGR", "HJ", "RTUAI", "JRBNG", "ZUYSC", "CIEYV", "FUY", "B", "EJS", "CINBTQS", "JEAC", "JX", "LLILSEK", "W", "KLUV"], 16),
    (POINTS, ["SVWLIDP", "FCPKTHW", "EREMN", "NFEF", "PQ", "FSC", "ZYPOSXJ", "BOR", "YCGG", "RC", "DVPE", "VAOE", "OIGK", "OTQE", "REJFUFD", "FVBCSSB", "VHJ", "BEC", "MWZQ", "WX", "L", "ZPCB", "JKLHE", "RYFTY", "NKP", "ID", "O", "KA", "VRXX", "NTDB", "OERKPC", "YFLUI", "SKQCJ", "PXDSW", "ITYWD", "TC", "LOIDQEJ", "NE", "YND", "VJHOCEC", "RPRANZ", "BQ", "STM", "RGVBFW", "SMWUYLW", "KT", "SXHY", "XCE", "T", "SC", "UDJU", "CHDR", "UGXNQ", "CQOOBA", "O", "NWW", "V", "L", "BAQ", "AZN", "LBTR", "N", "QSURR", "KADPH", "M", "LCBEAKM", "ZHEVXS", "F", "TVAIQCY", "MF", "KCI", "YQ", "RCG", "AKYPCP", "WJXG", "RQXOI", "SJI", "TWXZ", "J", "HIKCGHV", "EAAXGG", "AETSH", "EO", "BUET", "TDIQCO", "TKL", "FJCRY", "ZHAJLK", "OLMCVA", "F"], 6),
    (POINTS, ["RBBL", "ZJ", "ZOFXE", "LMBFCFX", "O", "JG", "SYRYE", "VXG", "EU", "DAIFZR", "BQUNZHH", "WKO", "TFPHPLX", "SWLG", "CY", "JYQNDSM", "ITPS", "B", "UVSDMWR", "LCPS"], 15),
    (POINTS, ['LGVMJDW', 'HSPASA', 'CFHMVZNGH', 'ESKSKB', 'JDO', 'BQJUECZ', 'BB', 'IVVLXBC', 'ZRENSWMG'], 5),
    (POINTS, ["B", "C", "D"], 0),
    (POINTS, ["CAKE", "CAKE", "CAKE", "CAKES"], 3),
    (POINTS, ["CAKES", "CAKE", "CAKE"], 0),
    (POINTS, ["PYTHON", "PY", "PY"], 0)
]


@pytest.mark.parametrize('points, words, result', SCRABBLE_TEST)
def test_get_best_word(points, words, result):
    """Test the output from the anagrams function."""
    from scrabble_best_word import get_best_word
    assert get_best_word(points, words) == result
