def det(mat):
  if len(mat)==2:
    return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
  return sum(mat[j][0]*((-1)**j)*det([(mat[:j]+mat[j+1:])[x][1:] for x in range(len(mat)-1)]) for j in range(len(mat)))
