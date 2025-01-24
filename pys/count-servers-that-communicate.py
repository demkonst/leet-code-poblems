from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        servers = []
        rows = dict()
        columns = dict()

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    servers.append((i, j))
                    rows[i] = rows.get(i, 0) + 1
                    columns[j] = columns.get(j, 0) + 1

        result = 0

        for server in servers:
            if rows[server[0]] >= 2 or columns[server[1]] >= 2:
                result += 1

        # print(servers)
        # print(rows)
        # print(columns)

        return result


s = Solution()
print(s.countServers([[1, 0], [0, 1]]))
print(s.countServers([[1, 0], [1, 1]]))
print(s.countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
