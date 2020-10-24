import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class test {
	private static final int[][] OFFSET = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };

	private static void solution(int sizeOfMatrix, int[][] matrix) {

		ArrayList<Integer> answer = new ArrayList<Integer>();
		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < sizeOfMatrix; i++) {
			for (int j = 0; j < sizeOfMatrix; j++) {
				if (matrix[i][j] == 1) {
					ArrayList<int[]> queue = new ArrayList<int[]>();
					matrix[i][j] = 0;
					queue.add(new int[] { i, j });
					int count = 1;

					while (!queue.isEmpty()) {
						int[] curr = queue.remove(0);
						int x = curr[0], y = curr[1];

						for (int dir = 0; dir < OFFSET.length; dir++) {
							int newX = x + OFFSET[dir][0];
							int newY = y + OFFSET[dir][1];
							if (newX < 0 || newY < 0 || newX >= sizeOfMatrix || newY >= sizeOfMatrix)
								continue;
							else if (matrix[newX][newY] == 0)
								continue;

							count += 1;
							matrix[newX][newY] = 0;
							queue.add(new int[] { newX, newY });
						}
					}

					answer.add(count);
				}
			}
		}

		Collections.sort(answer);
		for (int i : answer) {
			sb.append(i + " ");
		}
		if (sb.length() == 0) {
			sb.append(0);
		} else {
			sb.delete(sb.length() - 1, sb.length());
		}
		System.out.println(sb);
	}

	private static class InputData {
		int sizeOfMatrix;
		int[][] matrix;
	}

	private static InputData processStdin() {
		InputData inputData = new InputData();

		try (Scanner scanner = new Scanner(System.in)) {
			inputData.sizeOfMatrix = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

			inputData.matrix = new int[inputData.sizeOfMatrix][inputData.sizeOfMatrix];
			for (int i = 0; i < inputData.sizeOfMatrix; i++) {
				String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
				for (int j = 0; j < inputData.sizeOfMatrix; j++) {
					inputData.matrix[i][j] = Integer.parseInt(buf[j]);
				}
			}
		} catch (Exception e) {
			throw e;
		}

		return inputData;
	}

	public static void main(String[] args) throws Exception {
		InputData inputData = processStdin();

		solution(inputData.sizeOfMatrix, inputData.matrix);
	}
}