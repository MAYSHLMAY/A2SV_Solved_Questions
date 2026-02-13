class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        final = []
        my_line = ""
        b = False

        for line in source:

            i = 0
            while i < len(line):

                if not b:
                    slash_line = line.find("//", i)
                    block_start = line.find("/*", i)

                    if slash_line != -1 and (block_start == -1 or slash_line < block_start):
                        my_line += line[i:slash_line]
                        i = len(line)
                    elif block_start != -1:
                        my_line += line[i:block_start]
                        b = True
                        i = block_start + 2
                    else:
                        my_line += line[i:]
                        i = len(line)
                else:
                    end_block = line.find("*/", i)

                    if (end_block != -1):
                        b = False
                        i = end_block + 2
                    else:
                        i = len(line)
            if not b and my_line != "":
                final.append(my_line)
                my_line = ""
        return final


