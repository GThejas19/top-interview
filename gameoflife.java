class Solution {
    public void gameOfLife(int[][] board) {
        int rows = board.length;
        int cols = board[0].length;

        // Directions for 8 neighbors
        int[][] dirs = {
            {-1,-1}, {-1,0}, {-1,1},
            {0,-1},         {0,1},
            {1,-1},  {1,0}, {1,1}
        };

        // First pass: mark transitions
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int liveNeighbors = 0;

                for (int[] d : dirs) {
                    int r = i + d[0];
                    int c = j + d[1];

                    if (r >= 0 && r < rows && c >= 0 && c < cols) {
                        if (Math.abs(board[r][c]) == 1) {
                            liveNeighbors++;
                        }
                    }
                }

                // Apply rules with encoding
                if (board[i][j] == 1) {
                    if (liveNeighbors < 2 || liveNeighbors > 3) {
                        board[i][j] = -1; // live → dead
                    }
                } else {
                    if (liveNeighbors == 3) {
                        board[i][j] = 2; // dead → live
                    }
                }
            }
        }

        // Second pass: finalize states
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] > 0) {
                    board[i][j] = 1;
                } else {
                    board[i][j] = 0;
                }
            }
        }
    }
}