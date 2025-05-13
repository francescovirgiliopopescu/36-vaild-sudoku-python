import collections

class Solution:
  def isValidSudoku(self, board):
    rows, cols, triples = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
    for i, row in enumerate(board):
      for j, c in enumerate(row):
        if c != "." and c in rows[i] or c in cols[j] or c in triples[(i // 3, j // 3)]:
          return False
        elif c != ".":
          rows[i].add(c); cols[j].add(c); triples[(i // 3, j // 3)].add(c)
    return True
  
sol = Solution()

matrix = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(sol.isValidSudoku(matrix))