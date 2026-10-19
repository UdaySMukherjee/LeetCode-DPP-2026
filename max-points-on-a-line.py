class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) == 1:
            return 1

        mcount = 0

        for i in range(len(points)):
            freq = {}

            for j in range(i + 1, len(points)):
                y_slope = points[j][1] - points[i][1]
                x_slope = points[j][0] - points[i][0]

                if x_slope == 0:
                    slope = "V" + str(points[j][0])

                elif y_slope == 0:
                    slope = "H" + str(points[j][1])

                else:
                    slope = y_slope / x_slope

                if slope not in freq:
                    freq[slope] = 1

                freq[slope] += 1
                mcount = max(mcount, freq[slope])

        return mcount
