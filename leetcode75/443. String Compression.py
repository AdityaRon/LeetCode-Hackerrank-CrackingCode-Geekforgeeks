class Solution:
    def compress(self, chars: List[str]) -> int:
        self.chars = chars
        if len(chars) == 1:
            return 1
        # temporary_string = chars[0]
        # compressed_string = ""
        # temp = chars[0]
        # count = 1
        # for char in chars[1:]:
        #     if temp == char:
        #         count += 1
        #     else:
        #         compressed_string += temporary_string
        #         count = 1
        #         temporary_string = ""
        #     if count > 1:
        #         temporary_string = char + str(count)
        #     else:
        #         temporary_string = char
        #     temp = char
        # if temporary_string:
        #     compressed_string += temporary_string
        # # print(compressed_string)
        # result = len(list(compressed_string))
        # return result
        index = 0
        result = 0
        while index < len(chars):
            group_length = 1
            while (index + group_length < len(chars) and chars[index + group_length] == chars[index]):
                group_length +=1
            chars[result] = chars[index]
            result += 1
            if group_length > 1:
                chars[result : result + len(str(group_length))] = list(str(group_length))
                result += len(str(group_length))
            index += group_length
        return result
