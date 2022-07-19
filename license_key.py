class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        self.s = s
        self.k = k
        license = s.split('-')
        temp = ''.join(license)
        i = len(temp)
        j = len(temp) - k
        result = ''
        if len(s) == 1 and k > 1 and s != '-':
            return s
        else:
            while i >= k and j >= 0:
                print(j,i)
                result += '-' + temp[j:i]
                j -= k
                i -= k
            print(result, temp)
            if i == 0:
                updatedLicense = result[1:]
                temp = len(updatedLicense.upper().split('-'))
                updatedList = updatedLicense.upper().split('-')
                reformatLicense = ''
                while temp >= 1:
                    reformatLicense += updatedList[temp-1] + '-'
                    temp -=1
                return reformatLicense[:len(reformatLicense)-1]
            else:
                updatedLicense = result[1:] + '-' + temp[0:i]
                temp = len(updatedLicense.upper().split('-'))
                updatedList = updatedLicense.upper().split('-')
                reformatLicense = ''
                while temp >= 1:
                    reformatLicense += updatedList[temp-1] + '-'
                    temp -=1
                return reformatLicense[:len(reformatLicense)-1]
            
