# Test cases
version_01 = "1.01"
version_02 = "1.001"
# Expected output: 0

version_11 = "1.0"
version_12 = "1.0.0"
# Expected output: 0

version_21 = "0.1"
version_22 = "1.1"
# Expected output: -1

version_31 = "1.1"
version_32 = "1.01.0"

version_41 = "1.0.1"
version_42 = "1"

class Solution:
    def compareVersion(version1: str, version2: str) -> int:
        version1_lst, version2_lst = version1.split("."), version2.split(".")
        equalizer = abs(len(version1_lst) - len(version2_lst)) 
        tail_of_zeros = [0] * equalizer
        #print(equalizer)
        if len(version1_lst) < len(version2_lst):
            version1_lst += tail_of_zeros
        elif len(version1_lst) > len(version2_lst): 
            version2_lst += tail_of_zeros
        #print(f"version1_lst: {version1_lst}    version2_lst: {version2_lst}")
        for index in range(len(version1_lst)):
            vone_number = int(version1_lst[index])
            vtwo_number = int(version2_lst[index])
            if vone_number > vtwo_number:
                return 1
            if vone_number < vtwo_number:
                return - 1
        return 0            
    
    print(compareVersion(version_01, version_02))
    print(compareVersion(version_11, version_12))
    print(compareVersion(version_21, version_22))
    print(compareVersion(version_31, version_32))
    print(compareVersion(version_41, version_42))
    