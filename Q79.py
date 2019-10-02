from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(ix,iy,arr,s,path):
            le = len(path)
            retflag = False
            if s[0]!=arr[ix][iy]:
                return retflag
            else:
                s = s[1:]
                if len(s)<1:
                    return True
                if ix+1<m and (ix+1,iy) not in path:
                    path.append((ix+1,iy))
                    retflag = retflag or search(ix+1,iy,arr,s,path)
                if ix-1>-1 and (ix-1,iy) not in path[:le]:
                    path = path[:le]
                    path.append((ix-1,iy))
                    retflag = retflag or search(ix-1,iy,arr,s,path)
                if iy+1<n and (ix,iy+1) not in path[:le]:
                    path = path[:le]
                    path.append((ix,iy+1))
                    retflag = retflag or search(ix,iy+1,arr,s,path)
                if iy-1>-1 and (ix,iy-1) not in path[:le]:
                    path = path[:le]
                    path.append((ix,iy-1))
                    retflag = retflag or search(ix,iy-1,arr,s,path)
                return retflag

        m = len(board)
        n = len(board[0])
        if len(word)<1:
            return False
        flag = False

        for i in range(m):
            for j in range(n):
                path = []
                path.append((i,j))
                flag = flag or search(i,j,board,word,path)
        return flag

if __name__ == '__main__':
    board =[["a","b"]]
    print(Solution().exist(board,"ba"))