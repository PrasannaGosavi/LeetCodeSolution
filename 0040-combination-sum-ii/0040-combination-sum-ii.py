class Solution:
    def combinationSum2(self, candidates, target):

        candidates.sort()          # Step 1

        answer = []

        def dfs(start, target, path):

            # Target found
            if target == 0:
                answer.append(path[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicate numbers
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                # Since array is sorted
                if candidates[i] > target:
                    break

                # Choose
                path.append(candidates[i])

                # Move to next index
                dfs(i + 1, target - candidates[i], path)

                # Undo choice
                path.pop()

        dfs(0, target, [])

        return answer