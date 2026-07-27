class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=''
        for s in strs:
            encoded_string=encoded_string+str(len(s))+"~"+s
        print(encoded_string)
        return encoded_string




    def decode(self, s: str) -> List[str]:
        decoded_string=[]
        i=0
        while i < len(s):
            if s[i].isdigit():
                j=i
                while s[j]!="~":
                    j=j+1
                length_s=int(s[i:j])
                print(length_s,i)
                decoded_string.append(s[j+1:(int(length_s)+j+1)])
                i=j+1+length_s
            else:
                i=i+1
        print(decoded_string)
        return decoded_string


    #  def decode(self, s: str) -> List[str]:

    #     decoded_string = []
    #     i = 0

    #     while i < len(s):

    #         if s[i].isdigit():

    #             j = i

    #             # Read all digits until '~'
    #             while s[j] != "~":
    #                 j += 1

    #             length_s = int(s[i:j])

    #             decoded_string.append(s[j+1 : j+1+length_s])

    #             # Jump to next encoded string
    #             i = j + 1 + length_s

    #         else:
    #             i += 1

    #     return decoded_string